In Helidon 4.x we have made some major changes to Helidon. Reactive
engine has been removed. APIS and implementations are rewritten in
"blocking" paradigm. This guide will help you upgrade a Helidon SE 3.x
application to 4.x.

# Java 21 Runtime

Java 17 is no longer supported in Helidon 4. Java 21 or newer is
required. Java 25 or newer is highly recommended. Please follow the
instructions in
[Prerequisites](../../about/prerequisites.md)
for proper installation.

Helidon 4 no longer uses Netty. Helidon SE is now running on Helidon
WebServer which is based on virtual threads technology, available in
Java 21.

# Programming Paradigm

Helidon SE has changed from an asynchronous style API to an
imperative/blocking style API that is optimized for use with virtual
threads. Currently, there is no compatibility API available

# Server Initialization and Start Up

In Helidon 1.x-3.x you started a server like this:

<div class="formalpara">

<div class="title">

Start Helidon SE 3.x Server

</div>

``` java
static Single<WebServer> startServer() {
    Config config = Config.create();

    WebServer server = WebServer.builder(createRouting(config))
            .config(config.get("server"))
            .addMediaSupport(JsonpSupport.create())
            .build();

    Single<WebServer> webserver = server.start(); 

    webserver.thenAccept(ws -> { 
                System.out.println("WEB server is up! http://localhost:" + ws.port() + "/greet");
                ws.whenShutdown().thenRun(() -> System.out.println("WEB server is DOWN. Good bye!"));
            })
            .exceptionallyAccept(t -> { 
                System.err.println("Startup failed: " + t.getMessage());
                t.printStackTrace(System.err);
            });

    return webserver;
}
```

</div>

- Server is started in an asynchronous way. A `Single` object is
  returned.

- Wait for the Server to start and print the message in an asynchronous
  way.

- Gracefully handle exceptions if they occur during the initialization
  process.

Since Helidon SE in 3.x was reactive, during the start a `Single` object
is returned, the server has been started in asynchronous way. We have to
use reactive methods like `thenAccept` to wait for the server to start
and then to perform the desired action. The exception handling should
also be done in reactive way using the corresponding method.

In Helidon 4.x asynchronous programming is no longer required so the
server startup is much simpler:

<div class="formalpara">

<div class="title">

Start Helidon SE 4.x Server

</div>

``` java
public static void main(String[] args) {

    Config config = Config.global();

    WebServer server = WebServer.builder() 
            .config(config.get("server"))
            .routing(Main::routing)
            .build()
            .start(); 

    System.out.println("WEB server is up! http://localhost:" + server.port() + "/greet"); 
}
```

</div>

- Configure the Server.

- Start the Server. No reactive objects returned.

- Print a message when the Server is started.

Just create it, configure it, and wait for it to start. If any
exceptions happen, they are handled the traditional way using available
language constructions.

# Server Lifecycle

In Helidon 3.x you provided code to run after WebServer startup and
after WebServer shutdown using asynchronous constructs:

<div class="formalpara">

<div class="title">

Helidon 3.x server lifecycle

</div>

``` java
Single<WebServer> webserver = server.start();

webserver.thenAccept(ws -> {
            System.out.println("WEB server is up! http://localhost:" + ws.port() + "/greet");
            ws.whenShutdown().thenRun(() -> System.out.println("Helidon WebServer has stopped"));
        })
        .exceptionallyAccept(t -> {
            System.err.println("Startup failed: " + t.getMessage());
            t.printStackTrace(System.err);
        });
```

</div>

In Helidon 4 your `HttpService` can interpose on the server lifecycle by
overriding the `beforeStart` and `afterStop` methods:

<div class="formalpara">

<div class="title">

Helidon 4.x server lifecycle

</div>

``` java
static class MyService implements HttpService {
    @Override
    public void beforeStart() {
        System.out.println("MyService: Helidon WebServer is starting!");
    }

    @Override
    public void afterStop() {
        System.out.println("MyService: Helidon WebServer has stopped.");
    }
```

</div>

No special API is needed for after server starup since the server starts
sycnhronously as described in the previous section.

# Server Features and Media Support Discovery

In previous versions of Helidon you had to explicitly register WebServer
features (`register(MetricsSupport.create())`) and explicitly add media
support (`addMediaSupport(JsonpSupport.create())`). In Helidon 4 the
default behavior is to automatically discover these components from the
classpath. So all you need to do is add the dependencies to your pom.xml
and optionally add configuration to customize them.

If you want full control using the API, you still have that option.

For more information see:

- [Observability feature support](../observability.md)

- [Media types support](../webserver/webserver.xml#_media_types_support)

# Routing Configuration

In Helidon 1.x-3.x the routing config was done the following way:

<div class="formalpara">

<div class="title">

Routing in Helidon SE 3.x Server

</div>

``` java
private static Routing createRouting(Config config) {

    MetricsSupport metrics = MetricsSupport.create(); 
    HealthSupport health = HealthSupport.builder()
            .addLiveness(HealthChecks.healthChecks())
            .build();

    GreetService greetService = new GreetService(config); 

    return Routing.builder()
            .register(health) 
            .register(metrics)
            .register("/greet", greetService) 
            .build();
}
```

</div>

- Create and configure `Metrics` and `Heath` support.

- Create a regular Helidon Service.

- Register `Metrics` and `Heath` support as Helidon Services.

- Register the regular Greeting service.

Services are created and assigned to the desired path. Observability and
other features are being created as usual Helidon `services`, available
as part of the framework. User-defined services are also registered the
same way.

In Helidon 4, the routing is configured the following way:

<div class="formalpara">

<div class="title">

Start Helidon SE 4.x Server

</div>

``` java
static void routing(HttpRouting.Builder routing) {
    routing.register("/greet", new GreetService()); 
}
```

</div>

- Register Greeting service as in previous versions of Helidon.

As described previously, the Metrics and Health features will be
discovered automatically as long as you have added the dependencies for
them to your project.

If you wanted to add these features to the server programmatically you
would do so using `WebServer.builder().addFeature()` method.

`Feature` encapsulates a set of endpoints, services and/or filters. It
is similar to `HttpService` but gives more freedom in setup. Main
difference is that a feature can add `Filters` and it cannot be
registered on a path. Features are not registered immediately—each
feature can define a `Weight` or implement `Weighted` to order features
according to their weight. Higher-weighted features are registered
first. This is to allow ordering of features in a meaningful way (e.g.
Context should be first, Tracing second, Security third etc).

# Adding Additional Routing Criteria

In prior versions, the `RequestPredicate` class was used to specify more
routing criteria. This class has been removed from Helidon 4.

So, for example, if you used the following in Helidon 3:

<div class="formalpara">

<div class="title">

Helidon 3.x using `RequestPredicate`

</div>

``` java
public abstract class RoutingHandlerResource<I, R> implements HttpService {

        protected Handler requestHandler(HttpRules rules, Method method, Handler applyHandler) {
            switch (method) {
            case PUT:
                return RequestPredicate.create()
                    .accepts(MediaType.APPLICATION_JSON)
                    .containsHeader(HttpHeaderField.AUTHORIZATION.headerName())
                    .hasContentType(ContentHeader.TYPE_JSON)
                    .thenApply(applyHandler);
            }
        }
}
```

</div>

Then, you would use the following in Helidon 4:

<div class="formalpara">

<div class="title">

Helidon 4 `RequestPredicate` removed

</div>

``` java
public abstract class RoutingHandlerResource<I, R> implements HttpService {

    protected Handler requestHandler(HttpRules rules, Method method, Handler applyHandler) {
        return switch (method.text()) {
            case "PUT" -> (req, res) -> {
                ServerRequestHeaders headers = req.headers();
                if (headers.isAccepted(MediaTypes.APPLICATION_JSON)
                    && headers.contains(HeaderNames.AUTHORIZATION)
                    && headers.contentType()
                            .filter(HttpMediaTypes.JSON_PREDICATE)
                            .isPresent()) {
                    applyHandler.handle(req, res);
                } else {
                    res.next();
                }
            };
            default -> (req, res) -> res.next();
        };
    }
}
```

</div>

# Services

There are also significant changes in Helidon `Service`.

In prior versions, a service looks this way:

<div class="formalpara">

<div class="title">

Helidon SE 3.x Service

</div>

``` java
public class GreetService implements Service {

    @Override
    public void update(Routing.Rules rules) { 
        rules
                .get("/", this::getDefaultMessageHandler)
                .get("/{name}", this::getMessageHandler)
                .put("/greeting", this::updateGreetingHandler);
    }

    private void getDefaultMessageHandler(ServerRequest request, ServerResponse response) { 
        sendResponse(response, "World");
    }

    // other methods omitted
}
```

</div>

- Use `update()` method to set up routing.

- Handle a `Request` and return a `Responce`.

In Helidon 4, the same service:

<div class="formalpara">

<div class="title">

Helidon SE 4.x Service

</div>

``` java
public class GreetService implements HttpService { 

    @Override
    public void routing(HttpRules rules) { 
        rules.get("/", this::getDefaultMessageHandler)
                .get("/{name}", this::getMessageHandler)
                .put("/greeting", this::updateGreetingHandler);
    }

    private void getDefaultMessageHandler(ServerRequest request, ServerResponse response) { 
        sendResponse(response, "World");
    }

    private void getMessageHandler(ServerRequest request, ServerResponse response) {
        // ...
    }

    private void updateGreetingHandler(ServerRequest request, ServerResponse response) { 
        // ...
    }
}
```

</div>

- Implement `HttpService` for the `GreetingService`.

- Use `routing(HttpRules rules)` to set up routing.

- Handle a `Request` and return a `Responce`.

Helidon 4 introduced `HttpService` that should be implemented in order
to process HTTP requests. To set up routing, the method
`routing(HttpRules rules)` should now be used. It receives `HttpRules`
object with routes description.

`ServerRequest` and `ServerResponse` are now in the
`io.helidon.webserver.http` package;

`Http.Status` is now `io.helidon.http.Status`

> [!WARNING]
> These changes make Helidon 4 incompatible with previous versions.

Learn more about `HttpService` and `Routing` at [Helidon SE
WebServer](../webserver/webserver.md)

## Other Significant Changes

### Media Support

Media support has moved from the `io.helidon.media` Java package to
`io.helidon.http.media` and has new dependency coordinates. For example:

``` xml
<dependency>
    <groupId>io.helidon.http.media</groupId>
    <artifactId>helidon-http-media-jsonp</artifactId>
</dependency>

<dependency>
    <groupId>io.helidon.http.media</groupId>
    <artifactId>helidon-http-media-jsonb</artifactId>
</dependency>
```

In Helidon 4 media support is discovered by default, so you simply need
to add the dependency. You no longer need to explicitly add media
support using the `WebServer` builder.

Media support no long transitively brings the Jakarta API dependencies.
So you might need to add these explicitly. For example:

``` xml
<dependency>
    <groupId>jakarta.json</groupId>
    <artifactId>jakarta.json-api</artifactId>
</dependency>
```

### Testing

There is a new testing framework for Helidon SE.

``` xml
<dependency>
    <groupId>io.helidon.microprofile.testing</groupId>
    <artifactId>helidon-microprofile-testing-junit5</artifactId>
    <scope>test</scope>
</dependency>
```

Find more information, see [Helidon SE testing](../introduction.md)

### Observability

Observability features of Helidon have now moved to different package.
For `Health` and `Metrics` please use:

``` xml
<dependencies>
    <dependency>
        <groupId>io.helidon.webserver.observe</groupId>
        <artifactId>helidon-webserver-observe-health</artifactId>
    </dependency>
    <dependency>
        <groupId>io.helidon.webserver.observe</groupId>
        <artifactId>helidon-webserver-observe-metrics</artifactId>
    </dependency>
</dependencies>
```

Observability has new endpoints. See them [here](../observability.md).

For System Metrics, please use:

``` xml
<dependency>
    <groupId>io.helidon.metrics</groupId>
    <artifactId>helidon-metrics-system-meters</artifactId>
</dependency>
```

By default, Observability features are discovered automatically if you
add the above dependencies. If you choose to add them programmatically
(using `addFeature`) you will need to add the following dependency:

``` xml
<dependency>
    <groupId>io.helidon.webserver.observe</groupId>
    <artifactId>helidon-webserver-observe</artifactId>
</dependency>
```

Metrics has changed significantly in Helidon 4. See [Helidon SE
Metrics](../metrics/metrics.md) for more information.

### Security

- Changed modules:

  - `helidon-security-integration-jersey` moved to the module
    `helidon-microprofile-security`

  - `helidon-security-integration-jersey-client` moved to the module
    `helidon-microprofile-security`

  - `helidon-security-integration-grpc` was removed

  - `helidon-security-integration-webserver` moved to the module
    `helidon-webserver-security`

- Significant class name changes:

  - `OidcSupport` renamed to `OidcFeature`

  - `WebSecurity` renamed to `SecurityFeature`

- Other:

  - `SynchronousProvider removed` - `SynchronousProvider` usage is no
    longer needed, since all security providers are synchronous.

## Global Configuration

The global configuration represents a single instance of the `Config`
class, which is implicitly employed by certain Helidon components.
Furthermore, it offers a handy approach for your application to access
configuration information from any part of your code.

``` java
Config config = Config.global();
```

More information at [Helidon SE Config](../config/introduction.md).

## Logging

The class `LogConfig` has moved to the `io.helidon.logging.common` Java
package.

The Helidon console handler has changed from
`io.helidon.common.HelidonConsoleHandler` to
`io.helidon.logging.jul.HelidonConsoleHandler`.

If you use this handler in your `logging.properties` you will need to
update it and add the following dependency:

``` xml
<dependency>
    <groupId>io.helidon.logging</groupId>
    <artifactId>helidon-logging-jul</artifactId>
    <scope>runtime</scope>
</dependency>
```

# Conclusion

Please proceed to [Helidon SE Introduction](../introduction.md) to find
more information and documentation about each module.

Also, the [Helidon
examples](https://github.com/helidon-io/helidon-examples/tree/helidon-4.x/examples/)
are a good resource for seeing how things are done in Helidon 4.
