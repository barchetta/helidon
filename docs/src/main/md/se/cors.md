# Overview

The [cross-origin resource sharing (CORS)
protocol](https://www.w3.org/TR/cors) helps developers control if and
how REST resources served by their applications can be shared across
origins. Helidon SE includes an implementation of CORS that you can use
to add CORS behavior to the services you develop. You can define your
application’s CORS behavior programmatically using the Helidon CORS API
alone or together with configuration.

Helidon also provides three built-in services that add their own
endpoints to your application—​health, metrics, and OpenAPI—​that have
integrated CORS support. By adding very little code to your application,
you control how all the resources in your application—​the ones you write
and the ones provided by the Helidon built-in services—​can be shared
across origins.

## Before You Begin

### Planning Your Resource Sharing

Before you revise your application to add CORS support, you need to
decide what type of cross-origin sharing you want to allow for each
resource your application exposes. For example, suppose for a given
resource you want to allow unrestricted sharing for GET, HEAD, and POST
requests (what CORS refers to as "simple" requests), but permit other
types of requests only from the two origins `foo.com` and `there.com`.
Your application would implement two types of CORS sharing: more relaxed
for the simple requests and stricter for others.

Once you know the type of sharing you want to allow for each of your
resources—​including any from built-in services—​you can change your
application accordingly.

### Choosing How To Implement CORS

You can add CORS support to your application in either or both of the
following ways, depending on your specific requirements:

- Use configuration and automatic feature detection: **recommended**.

  If you add the Helidon CORS Maven artifact to your project, at runtime
  Helidon automatically discovers it and activates it according to
  configuration. You do not need to change your Java code. Instead, you
  control your application’s CORS behavior entirely using configuration
  linked to the resource paths your application exposes.

  This is the simplest way to set up CORS for your service, and we
  recommend you use this approach.

- Use the Helidon CORS API to add CORS processing to the routing for
  specific services or endpoints in your application.

  Your code creates one or more
  [`CorsSupport`](/apidocs/io.helidon.webserver.cors/io/helidon/webserver/cors/CorsSupport.html)
  instances and adds them to routing rules.

The following sections briefly illustrate each approach.

# Maven Coordinates

To enable CORS, add the following dependency to your project’s `pom.xml`
(see [Managing
Dependencies](../about/managing-dependencies.md)).

``` xml
<dependency>
    <groupId>io.helidon.webserver</groupId>
    <artifactId>helidon-webserver-cors</artifactId>
</dependency>
```

If you also choose to write Java code to add CORS behavior explicitly to
your application also add the following dependency as well:

``` xml
<dependency>
    <groupId>io.helidon.cors</groupId>
    <artifactId>helidon-cors</artifactId>
</dependency>
```

# API

## Using the Config-only Approach

If you add the `io.helidon.webserver:helidon-webserver-cors` Maven
artifact to your project you do not have to add any CORS-specific code
to your application to implement CORS. Express the CORS behavior you
want in configuration, associating path patterns with the CORS settings
you want to apply to the matching paths.

See the [configuration](#_configuration) section below for more
information.

## Adding Code to Include CORS in Routing Rules

Every Helidon SE application explicitly creates routing rules that
govern how Helidon delivers each incoming request to the code that needs
to respond. You can add CORS behavior to specific endpoints with only
minimal changes to how you set up the routing for those endpoints. Using
the Helidon SE CORS API, you define the CORS behavior that you want and
then include that behavior as you build the routing rules for the
services in your application.

The Helidon SE CORS API provides two key classes that you use in your
application:

- [`CorsSupport`](/apidocs/io.helidon.webserver.cors/io/helidon/webserver/cors/CorsSupport.html) -
  Represents information about resource sharing for a single resource.
  Typically, you create one `CorsSupport` instance for each distinct
  resource in your application (such as the `/greet` resource in the
  QuickStart greeting application) that should participate in CORS.

- [`CrossOriginConfig`](/apidocs/io.helidon.cors/io/helidon/cors/CrossOriginConfig.html) -
  Represents the details for a particular type of sharing, such as which
  origins are allowed to have access using which HTTP methods, etc.
  Create one instance of `CrossOriginConfig` for each different type of
  sharing you need.

You associate one or more `CrossOriginConfig` objects with each
`CorsSupport` object. You use the `CorsSupport` object when you
construct the routing rules for the service. When your application is
running and requests arrive, the Helidon CORS implementation enforces
the CORS behavior represented by the `CorsSupport` object before routing
the request to your endpoint code for the resource.

Because Helidon SE does not use annotation processing to identify
endpoints, you need to provide the CORS information for your application
another way — by including CORS into the routing you construct for your
application.

For each distinct resource or subresource your application exposes:

1.  Create a
    [`CorsSupport`](/apidocs/io.helidon.webserver.cors/io/helidon/webserver/cors/CorsSupport.html)
    instance corresponding to the resource.

2.  For each different type of sharing you want to provide for that
    resource:

    1.  Create a
        [`CrossOriginConfig`](/apidocs/io.helidon.cors/io/helidon/cors/CrossOriginConfig.html)
        instance. The `CrossOriginConfig` Java class represents the
        details for a particular type of sharing, such as which origins
        are allowed to share via which HTTP methods, etc.

    2.  Add the `CrossOriginConfig` to the `CorsSupport` instance for
        this resource.

3.  Use the resource’s `CorsSupport` object in setting up the routing
    rules for that resource.

Each of these classes has an associated builder that you use in
constructing instances of the class.

The table below describes the methods on the `CrossOriginConfig.Builder`
class and the configuration keys that map to the headers defined in the
CORS protocol. (A later section discusses
[configuration](#_configuration).)

| builder method | config key | type | default | description | CORS header name |
|----|----|----|----|----|----|
| `allowCredentials` | `allow-credentials` | boolean | `false` | Sets the allow credentials flag. | `Access-Control-Allow-Credentials` |
| `allowHeaders` | `allow-headers` | string\[\] | `*` | Sets the allowed headers. | `Access-Control-Allow-Headers` |
| `allowMethods` | `allow-methods` | string\[\] | `*` | Sets the allowed methods. | `Access-Control-Allow-Methods` |
| `allowOrigins` | `allow-origins` | string\[\] | `*` | Sets the allowed origins. | `Access-Control-Allow-Origins` |
| `exposeHeaders` | `expose-headers` | string\[\] |   | Sets the expose headers. | `Access-Control-Expose-Headers` |
| `maxAgeSeconds` | `max-age-seconds` | long | `3600` | Sets the maximum age. | `Access-Control-Max-Age` |
| `enabled` | `enabled` | boolean | `true` | Sets whether this config should be enabled or not. | n/a |

If the cross-origin configuration is disabled (`enabled` = false), then
the Helidon CORS implementation ignores the cross-origin configuration
entry.

## Sample Routing Setup Using the `CrossOriginConfig` API

The [Helidon SE Quickstart
application](https://github.com/helidon-io/helidon-examples/tree/helidon-4.x/examples/quickstarts/helidon-quickstart-se)
lets you change the greeting by sending a `PUT` request to the
`/greet/greeting` resource.

This example, based on the QuickStart greeting app, uses the low-level
`CrossOriginConfig` API and the `CorsSupport` API to influence the
[routing](../se/webserver/webserver.xml#routing),
thereby determining how that resource is shared. (If desired, you can
use [configuration](#_configuration) instead of the low-level API.)

The following code shows one way to prepare your application’s routing
to support CORS.

``` java
CorsSupport corsSupport = CorsSupport.builder()  
        .addCrossOrigin(CrossOriginConfig.builder() 
                                .allowOrigins("http://foo.com", "http://there.com") 
                                .allowMethods("PUT", "DELETE") 
                                .build()) 
        .addCrossOrigin(CrossOriginConfig.create()) 
        .build(); 
routing.register("/greet", corsSupport, new GreetService()); 
```

- Create a `CorsSupport.Builder` instance.

- Add a `CrossOriginConfig` instance (using *its* builder) to constrain
  resource sharing.

- List the origins (sites) allowed to share resources from this app.

- List the HTTP methods the constraint applies to.

- Build the `CrossOriginConfig` instance.

- Add a `CrossOriginConfig` instance that permits all sharing (the
  default).

- Build the `CorsSupport` instance.

- Register the new `CorsSupport` instance with — but in front of — the
  service which implements the business logic.

The order of steps 2 and 6 above is important. When processing an
incoming request, the Helidon CORS implementation scans the
`CrossOriginConfig` instances in the order they were added to the
`CorsSupport` object, stopping as soon as it finds a `CrossOriginConfig`
instance for which `allowMethods` matches the HTTP method of the
request.

By adding the few additional lines described above you allow the
greeting application to participate in CORS.

# Configuration

You can use configuration instead of or in combination with the Helidon
CORS SE API to add CORS support to your resources by replacing some Java
code with declarative configuration.

## Configuration for Automatic CORS Processing

Recall that simply by adding the
`io.helidon.webserver:helidon-webserver-cors` artifact to your project
you allow Helidon to automatically use configuration to set up CORS
behavior throughout your application.

To use this automatic support, make sure your configuration contains a
`cors` section which contains mapped CORS configuration as described
below and as shown in the following example.

``` yaml
cors:
  paths:
    - path-pattern: /greeting
      allow-origins: ["https://foo.com", "https://there.com", "https://other.com"]
      allow-methods: ["PUT", "DELETE"]
    - path-pattern: /
      allow-methods: ["GET", "HEAD", "OPTIONS", "POST"]
```

## Understanding the CORS Configuration Formats

Support in Helidon for CORS configuration uses two closely-related
cross-origin configuration formats: basic and mapped. Each format
corresponds to a class in the Helidon CORS library. The basic format
corresponds to the
[`CrossOriginConfig`](/apidocs/io.helidon.cors/io/helidon/cors/CrossOriginConfig.html)
class, and the mapped format corresponds to the
[`MappedCrossOriginConfig`](/apidocs/io.helidon.cors/io/helidon/cors/MappedCrossOriginConfig.html)
class.

## Basic Cross-Origin Configuration

In configuration, Helidon represents basic CORS information as a
section, identified by a configuration key of your choosing, that
contains one or more key/value pairs. Each key-value pair assigns one
characteristic of CORS behavior.

The table below lists the configuration keys that identify the CORS
characteristics.

| builder method | config key | type | default | description | CORS header name |
|----|----|----|----|----|----|
| `allowCredentials` | `allow-credentials` | boolean | `false` | Sets the allow credentials flag. | `Access-Control-Allow-Credentials` |
| `allowHeaders` | `allow-headers` | string\[\] | `*` | Sets the allowed headers. | `Access-Control-Allow-Headers` |
| `allowMethods` | `allow-methods` | string\[\] | `*` | Sets the allowed methods. | `Access-Control-Allow-Methods` |
| `allowOrigins` | `allow-origins` | string\[\] | `*` | Sets the allowed origins. | `Access-Control-Allow-Origins` |
| `exposeHeaders` | `expose-headers` | string\[\] |   | Sets the expose headers. | `Access-Control-Expose-Headers` |
| `maxAgeSeconds` | `max-age-seconds` | long | `3600` | Sets the maximum age. | `Access-Control-Max-Age` |
| `enabled` | `enabled` | boolean | `true` | Sets whether this config should be enabled or not. | n/a |

If the cross-origin configuration is disabled (`enabled` = false), then
the Helidon CORS implementation ignores the cross-origin configuration
entry.

The following example of basic cross-origin configuration, when
explicitly loaded and used by your application code, limits cross-origin
resource sharing for `PUT` and `DELETE` operations to only `foo.com` and
`there.com`:

``` yaml
restrictive-cors:
  allow-origins: ["https://foo.com", "https://there.com"]
  allow-methods: ["PUT", "DELETE"]
```

## Mapped Cross-Origin Configuration

In some cases, you or your users might want to configure CORS behavior
based on URL path matching.

Helidon represents mapped CORS information as a config section that
contains:

- An optional `enabled` setting which defaults to `true` and applies to
  the whole mapped CORS config section, and

- An optional `paths` subsection containing zero or more entries, each
  of which contains:

  - a basic CORS config section, and

  - a `path-pattern` path pattern that maps that basic CORS config
    section to the resource(s) it affects.

You can use mapped configuration to your advantage if you want to
specify all CORS behavior using configuration (with no explicit coding
changes) or to allow your users to override the CORS behavior that your
code explicitly sets up.

The following example illustrates the mapped cross-origin configuration
format.

``` yaml
my-cors: 
  paths: 
    - path-pattern: /greeting 
      allow-origins: ["https://foo.com", "https://there.com", "https://other.com"] 
      allow-methods: ["PUT", "DELETE"]
    - path-pattern: / 
      allow-methods: ["GET", "HEAD", "OPTIONS", "POST"] 
```

- Assigns a unique identifier for this mapped CORS config section.

- Collects the sequence of entries, each of which maps a basic CORS
  config to a path pattern.

- Marks the beginning of an entry (the `-` character) and maps the
  associated basic CORS config to the `/greeting` subresource (the
  `path-pattern` key and value).

- Begins the basic CORS config section for `/greeting`; it restricts
  sharing via `PUT` and `DELETE` to the listed origins.

- Marks the beginning of the next entry (the `-` character) and maps the
  associated basic CORS config to the top-level resource in the app (the
  `path-pattern` key and value).

- Begins the basic CORS config section for `/`; it permits sharing of
  resources at the top-level path with all origins for the indicated
  HTTP methods.

Path patterns can be any expression accepted by the
[`PathMatcher`](/apidocs/io.helidon.http/io/helidon/http/PathMatcher.html)
class.

> [!NOTE]
> Be sure to arrange the entries in the order that you want Helidon to
> check them. Helidon CORS support searches the cross-origin entries in
> the order you define them until it finds an entry that matches an
> incoming request’s path pattern and HTTP method.

## Using CORS Configuration in the Application

You use configuration in combination with the Helidon CORS SE API to add
CORS support to your resources. The example in [Sample Routing Setup
Using the `CrossOriginConfig` API](#se-api-routing-example) uses the
low-level Helidon CORS SE API to create a `CrossOriginConfig` instance
that is then used as part of a `CorsSupport` instance to create the
routing rules. As an alternative to using the low-level API, this
example uses config to create the `CrossOriginConfig` instance instead.

``` java
CorsSupport corsSupport = CorsSupport.builder()
        .update(builder -> {
            config.get("my-cors").ifExists(builder::mappedConfig); 
            config.get("restrictive-cors").ifExists(builder::config); 
            builder.addCrossOrigin(CrossOriginConfig.create()); 
        }).build();

routing.register("/greet", corsSupport, new GreetService()); 
```

- If `my-cors` exists in the configuration, use it to add mapped CORS
  config to the `CorsSupport` builder.

- If `restrictive-cors` exists in the configuration, use it to add basic
  (not mapped) config to the builder.

- Provide default CORS handling for requests that do not match earlier
  entries.

- Add the CORS routing **before** registering the GreetService routing.

As each request arrives, Helidon checks it against the cross-origin
config instances in the order that your application added them to the
`CorsSupport.Builder`. The `my-cors` mapped configuration acts as an
override because the application added it to the builder first.

If the `my-cors` config key does not appear in the configuration, then
the code skips creating a `CrossOriginConfig` instance based on that
configuration, and no overriding occurs. The CORS behavior that is
established by the other `CrossOriginConfig` instance based on the
`restrictive-cors` config (if present) prevails.

> [!NOTE]
> Remember that if you set configuration in a file that you include as
> part of your application JAR file, then you need to rebuild and
> restart your application for any changes to take effect.

# Examples

For a complete example, see [Helidon SE CORS
Example](https://github.com/helidon-io/helidon-examples/tree/helidon-4.x/examples/cors).

# Additional Information

## CORS and the Requested URI Feature

The decisions the Helidon CORS feature makes depend on accurate
information about each incoming request, particularly the host to which
the request is sent. Conveyed as headers in the request, this
information can be changed or overwritten by intermediate nodes—​such as
load balancers—​between the origin of the request and your service.

Well-behaved intermediate nodes preserve this important data in other
headers, such as `Forwarded`. You can configure how the Helidon server
handles these headers as described in the documentation for [requested
URI
discovery](../se/webserver/webserver.xml#_requested_uri_discovery).

The CORS support in Helidon uses the requested URI feature to discover
the correct information about each request, according to your
configuration, so it can make accurate decisions about whether to permit
cross-origin accesses.

## Using CORS Support in Built-in Helidon Services

Several built-in Helidon
services—​[health](../se/health.md),
[metrics](../se/metrics/metrics.md),
and
[OpenAPI](../se/openapi/openapi.md)--have
integrated CORS support. You can include these services in your
application and control how those resources can be shared across
origins.

For example, several websites related to OpenAPI run a web application
in your browser. You provide the URL for your application to the browser
application. The browser application uses the URL to retrieve the
OpenAPI document that describes the application’s endpoints directly
from your application. The browser application then displays a user
interface that you use to "drive" your application. That is, you provide
input, have the web application send requests to your application
endpoints, and then view the responses. This scenario is exactly the
situation CORS addresses: an application in the browser from one
origin — the user interface downloaded from the website — requests a
resource from another origin — the `/openapi` endpoint which Helidon’s
OpenAPI built-in service automatically adds to your application.

Integrating CORS support into these built-in services allows such
third-party web sites and their browser applications — or more
generally, apps from any other origin — to work with your Helidon
application.

Because all three of these built-in Helidon services serve primarily
`GET` endpoints, by default the integrated CORS support in all three
services permits any origin to share their resources using `GET`,
`HEAD`, and `OPTIONS` HTTP requests. You can customize the CORS set-up
for these built-in services independently from each other using either
the Helidon API, configuration, or both. You can use this override
feature to control the CORS behavior of the built-in services even if
you do not add CORS behavior to your own endpoints.

### Built-in Services with CORS

To use built-in services with CORS support and customize the CORS
behavior:

1.  Add the built-in service or services to your application.

2.  Add a dependency on the
    `io.helidon.webserver:helidon-webserver-cors` CORS artifact to your
    Maven `pom.xml` file.

    > [!NOTE]
    > If you want the built-in services to support CORS, then you need
    > to add the CORS dependency even if your own endpoints do not use
    > CORS.

3.  Use configuration to set up the CORS behavior by path as needed.

The documentation for the individual built-in services describes how to
add each service to your application, including adding a Maven
dependency for the built-in feature.

#### Configuring CORS for Built-in Services

Use configuration to control whether and how each of the built-in
services works with CORS.

In the `cors` configuration section add a block for each built-in
service using its path as described in the [mapped
](#mapped-config-descr) CORS configuration section. The following
example restricts sharing of the `/observe/health` resource, provided by
the health built-in service, to only the origin `https://there.com`.

``` hocon
cors:
  paths:
    - path-pattern: "/observe/health"
      allow-origins: [https://there.com]
    - path-pattern: "/observe/metrics"
      allow-origins: [https://foo.com]
```

### Accessing the Shared Resources

If you have edited the Helidon SE QuickStart application as described in
the previous topics and saved your changes, you can build and run the
application. Once you do so you can execute `curl` commands to
demonstrate the behavior changes in the metric and health services with
the addition of the CORS functionality. Note the addition of the
`Origin` header value in the `curl` commands, and the
`Access-Control-Allow-Origin` in the successful responses.

#### Build and Run the Application

Build and run the QuickStart application as usual.

``` bash
mvn package
java -jar target/helidon-quickstart-se.jar
```

``` listing
WEB server is up! http://localhost:8080/greet
```

#### Retrieve Metrics

The metrics service rejects attempts to access metrics on behalf of a
disallowed origin.

``` bash
curl -i -H "Origin: https://other.com" http://localhost:8080/observe/metrics
```

<div class="formalpara">

<div class="title">

Curl output

</div>

``` listing
HTTP/1.1 403 Forbidden
Date: Mon, 11 May 2020 11:08:09 -0500
transfer-encoding: chunked
connection: keep-alive
```

</div>

But accesses from `foo.com` succeed.

``` bash
curl -i -H "Origin: https://foo.com" http://localhost:8080/observe/metrics
```

<div class="formalpara">

<div class="title">

Curl output

</div>

``` listing
HTTP/1.1 200 OK
Access-Control-Allow-Origin: https://foo.com
Content-Type: text/plain
Date: Mon, 11 May 2020 11:08:16 -0500
Vary: Origin
connection: keep-alive
content-length: 6065

# TYPE base_classloader_loadedClasses_count gauge
# HELP base_classloader_loadedClasses_count Displays the number of classes that are currently loaded in the Java virtual machine.
base_classloader_loadedClasses_count 3568
```

</div>

#### Retrieve Health

The health service rejects requests from origins not specifically
approved.

``` bash
curl -i -H "Origin: https://foo.com" http://localhost:8080/observe/health
```

``` listing
HTTP/1.1 403 Forbidden
Date: Mon, 11 May 2020 12:06:55 -0500
transfer-encoding: chunked
connection: keep-alive
```

And responds successfully only to cross-origin requests from
`https://there.com`.

``` bash
curl -i -H "Origin: https://there.com" http://localhost:8080/observe/health
```

``` listing
HTTP/1.1 200 OK
Access-Control-Allow-Origin: https://there.com
Content-Type: application/json
Date: Mon, 11 May 2020 12:07:32 -0500
Vary: Origin
connection: keep-alive
content-length: 461

{"outcome":"UP",...}
```
