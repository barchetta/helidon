# Tracing

## Contents

- [Overview](#_overview)

- [Maven Coordinates](#maven-coordinates)

- [Usage](#_usage)

- [Configuration](#_configuration)

- [Examples](#_examples)

- [Additional Information](#_additional_information)

  - [Jaeger Tracing](#jaeger-tracing)

  - [Zipkin Tracing](#zipkin-tracing)

  - [OpenTelemetry Tracing](#opentelemetry-tracing)

  - [Responding to Span Life Cycle Events](#Tracing-callbacks)

- [Reference](#_reference)

## Overview

> [!WARNING]
> This feature is marked as `@Deprecated` in Helidon. Please use the [Telemetry](../mp/telemetry.md) feature instead. The OpenTracing Specification that MP OpenTracing is based on is no longer maintained. The MP OpenTracing specification is no longer required by MicroProfile. The specification is superseded by the [MicroProfile Telemetry specification](https://github.com/eclipse/microprofile-telemetry).

Distributed tracing is a critical feature of micro-service based applications, since it traces workflow both within a service and across multiple services. This provides insight to sequence and timing data for specific blocks of work, which helps you identify performance and operational issues. Helidon MP includes support for distributed tracing through the [OpenTracing API](https://opentracing.io). Tracing is integrated with WebServer and Security.

## Maven Coordinates

To enable MicroProfile Tracing, either add a dependency on the [helidon-microprofile bundle](../mp/introduction/microprofile.md) or add the following dependency to your project’s `pom.xml` (see [Managing Dependencies](../about/managing-dependencies.md)).

``` xml
<dependency>
    <groupId>io.helidon.microprofile.tracing</groupId>
    <artifactId>helidon-microprofile-tracing</artifactId>
</dependency>
```

## Usage

This section explains a few concepts that you need to understand before you get started with tracing.

- In the context of this document, a *service* is synonymous with an application.

- A *span* is the basic unit of work done within a single service, on a single host. Every span has a name, starting timestamp, and duration. For example, the work done by a REST endpoint is a span. A span is associated to a single service, but its descendants can belong to different services and hosts.

- A *trace* contains a collection of spans from one or more services, running on one or more hosts. For example, if you trace a service endpoint that calls another service, then the trace would contain spans from both services. Within a trace, spans are organized as a directed acyclic graph (DAG) and can belong to multiple services, running on multiple hosts. The *OpenTracing Data Model* describes the details at [The OpenTracing Semantic Specification](https://opentracing.io/specification). Spans are automatically created by Helidon as needed during execution of the REST request. Additional spans can be added through MP annotation `@Traced` or through OpenTracing APIs.

## Traced spans

The following table lists all spans traced by Helidon components:

| component | span name | description |
|----|----|----|
| `web-server` | `HTTP Request` | The overall span of the Web Server from request initiation until response Note that in `Zipkin` the name is replaced with `jax-rs` span name if `jax-rs` tracing is used. |
| `web-server` | `content-read` | Span for reading the request entity |
| `web-server` | `content-write` | Span for writing the response entity |
| `security` | `security` | Processing of request security |
| `security` | `security:atn` | Span for request authentication |
| `security` | `security:atz` | Span for request authorization |
| `security` | `security:response` | Processing of response security |
| `security` | `security:outbound` | Processing of outbound security |
| `jax-rs` | A generated name | Span for the resource method invocation, name is generated from class and method name |
| `jax-rs` | `jersey-client-call` | Span for outbound client call |

Some of these spans `log` to the span. These log events can be (in most cases) configured:

| span name | log name | configurable | enabled by default | description |
|----|----|----|----|----|
| `HTTP Request` | `handler.class` | YES | YES | Each handler has its class and event logged |
| `security` | `status` | YES | YES | Logs either "status: PROCEED" or "status: DENY" |
| `security:atn` | `security.user` | YES | NO | The username of the user if logged in |
| `security:atn` | `security.service` | YES | NO | The name of the service if logged in |
| `security:atn` | `status` | YES | YES | Logs the status of security response (such as `SUCCESS`) |
| `security:atz` | `status` | YES | YES | Logs the status of security response (such as `SUCCESS`) |
| `security:outbound` | `status` | YES | YES | Logs the status of security response (such as `SUCCESS`) |

There are also tags that are set by Helidon components. These are not configurable.

| span name | tag name | description |
|----|----|----|
| `HTTP Request` | `component` | name of the component - `helidon-webserver`, or `jaxrs` when using MP |
| `HTTP Request` | `http.method` | HTTP method of the request, such as `GET`, `POST` |
| `HTTP Request` | `http.status_code` | HTTP status code of the response |
| `HTTP Request` | `http.url` | The path of the request (for SE without protocol, host and port) |
| `HTTP Request` | `error` | If the request ends in error, this tag is set to `true`, usually accompanied by logs with details |
| `security` | `security.id` | ID of the security context created for this request (if security is used) |
| `jersey-client-call` | `http.method` | HTTP method of the client request |
| `jersey-client-call` | `http.status_code` | HTTP status code of client response |
| `jersey-client-call` | `http.url` | Full URL of the request (such as `http://localhost:8080/greet`) |

## Configuration

### Enabling and Disabling Tracing

You can configure a custom service name using the `tracing.service` configuration property. If this property is undefined, name is created from JAX-RS Application name, or `Helidon MP` is used if no application is defined.

Jaeger tracer configuration.

Type: [io.helidon.tracing.Tracer](/apidocs/io.helidon.tracing/io/helidon/tracing/Tracer.html)

This is a standalone configuration type, prefix from configuration root: `tracing`

## Configuration options

<table style="width:100%;">
<caption>Optional configuration options</caption>
<colgroup>
<col style="width: 23%" />
<col style="width: 23%" />
<col style="width: 15%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">key</th>
<th style="text-align: left;">type</th>
<th style="text-align: left;">default value</th>
<th style="text-align: left;">description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>client-cert-pem</code></p></td>
<td style="text-align: left;"><p><a href="../mp/../config/io_helidon_common_configurable_Resource.xml">Resource</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Certificate of client in PEM format.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>exporter-timeout</code></p></td>
<td style="text-align: left;"><p>Duration</p></td>
<td style="text-align: left;"><p><code>PT10S</code></p></td>
<td style="text-align: left;"><p>Timeout of exporter requests.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>max-export-batch-size</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p><code>512</code></p></td>
<td style="text-align: left;"><p>Maximum Export Batch Size of exporter requests.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>max-queue-size</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p><code>2048</code></p></td>
<td style="text-align: left;"><p>Maximum Queue Size of exporter requests.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>private-key-pem</code></p></td>
<td style="text-align: left;"><p><a href="../mp/../config/io_helidon_common_configurable_Resource.xml">Resource</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Private key in PEM format.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>propagation</code></p></td>
<td style="text-align: left;"><p>JaegerTracerBuilder.PropagationFormat[] (B3, B3_SINGLE, JAEGER, W3C)</p></td>
<td style="text-align: left;"><p><code>JAEGER</code></p></td>
<td style="text-align: left;"><p>Add propagation format to use.</p>
<p>Allowed values:</p>
<ul>
<li><p><code>B3</code>: The Zipkin B3 trace context propagation format using multiple headers.</p></li>
<li><p><code>B3_SINGLE</code>: B3 trace context propagation using a single header.</p></li>
<li><p><code>JAEGER</code>: The Jaeger trace context propagation format.</p></li>
<li><p><code>W3C</code>: The W3C trace context propagation format.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>sampler-param</code></p></td>
<td style="text-align: left;"><p>Number</p></td>
<td style="text-align: left;"><p><code>1</code></p></td>
<td style="text-align: left;"><p>The sampler parameter (number).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>sampler-type</code></p></td>
<td style="text-align: left;"><p>JaegerTracerBuilder.SamplerType (CONSTANT, RATIO)</p></td>
<td style="text-align: left;"><p><code>CONSTANT</code></p></td>
<td style="text-align: left;"><p>Sampler type.</p>
<p>See <a href="https://www.jaegertracing.io/docs/latest/sampling/#client-sampling-configuration">Sampler types</a>.</p>
<p>Allowed values:</p>
<ul>
<li><p><code>CONSTANT</code>: Constant sampler always makes the same decision for all traces. It either samples all traces <code>1</code> or none of them <code>0</code>.</p></li>
<li><p><code>RATIO</code>: Ratio of the requests to sample, double value.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>schedule-delay</code></p></td>
<td style="text-align: left;"><p>Duration</p></td>
<td style="text-align: left;"><p><code>PT5S</code></p></td>
<td style="text-align: left;"><p>Schedule Delay of exporter requests.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>span-processor-type</code></p></td>
<td style="text-align: left;"><p>JaegerTracerBuilder.SpanProcessorType (SIMPLE, BATCH)</p></td>
<td style="text-align: left;"><p><code>batch</code></p></td>
<td style="text-align: left;"><p>Span Processor type used.</p>
<p>Allowed values:</p>
<ul>
<li><p><code>SIMPLE</code>: Simple Span Processor.</p></li>
<li><p><code>BATCH</code>: Batch Span Processor.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>trusted-cert-pem</code></p></td>
<td style="text-align: left;"><p><a href="../mp/../config/io_helidon_common_configurable_Resource.xml">Resource</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Trusted certificates in PEM format.</p></td>
</tr>
</tbody>
</table>

To disable Helidon tracing for web server and security:

``` properties
tracing.components.web-server.enabled=false
tracing.components.security.enabled=false
```

To disables MP Tracing as by specification:

``` properties
mp.opentracing.server.skip-pattern=.*
```

Tracing configuration can be defined in `application.yaml` file.

*Tracing configuration example*

``` yaml
tracing:
  paths:
    - path: "/favicon.ico"
      enabled: false
    - path: "/metrics"
      enabled: false
    - path: "/health"
      enabled: false
  components:
    web-server:
      spans:
        - name: "HTTP Request"
          logs:
            - name: "content-write"
              enabled: false
```

### Controlling Tracing Output

For Web Server we have a path based support for configuring tracing, in addition to the configuration described above.

Configuration of path can use any path string supported by the Web Server. The configuration itself has the same possibilities as traced configuration described above. The path specific configuration will be merged with global configuration (path is the "newer" configuration, global is the "older")

#### Renaming top level span using request properties

To have a nicer overview in search pane of a tracer, you can customize the top-level span name using configuration.

Example:

*Configuration properties*

``` properties
tracing.components.web-server.spans.0.name="HTTP Request"
tracing.components.web-server.spans.0.new-name: "HTTP %1$s %2$s"
```

This is supported ONLY for the span named "HTTP Request" on component "web-server".

Parameters provided:

1.  Method - HTTP method

2.  Path - path of the request (such as '/greet')

3.  Query - query of the request (may be null)

## Examples

The examples in this guide demonstrate how to integrate tracing with Helidon, how to view traces, how to trace across multiple services, and how to integrate tracing with Kubernetes. All examples use Jaeger and traces will be viewed using both the Jaeger UI.

### Set up Jaeger

First, you need to run the Jaeger tracer. Helidon will communicate with this tracer at runtime.

*Run Jaeger within a docker container, then check the Jaeger server working:*

``` bash
docker run -d --name jaeger \                  
  -e COLLECTOR_OTLP_ENABLED=true \
  -p 6831:6831/udp \
  -p 6832:6832/udp \
  -p 5778:5778 \
  -p 16686:16686 \
  -p 4317:4317 \
  -p 4318:4318 \
  -p 14250:14250 \
  -p 14268:14268 \
  -p 14269:14269 \
  -p 9411:9411 \
  jaegertracing/all-in-one:1.50
```

- Run the Jaeger docker image.

*Check the Jaeger server by opening in browser:*

``` bash
http://localhost:16686/search
```

### Trace Across Services

Helidon automatically traces across services as long as the services use the same tracer, for example, the same instance of Jaeger. This means a single trace can include spans from multiple services and hosts. OpenTracing uses a `SpanContext` to propagate tracing information across process boundaries. When you make client API calls, Helidon will internally call OpenTracing APIs to propagate the `SpanContext`. There is nothing you need to do in your application to make this work.

To demonstrate distributed tracing, you will need to create a second project, where the server listens on port 8081. Create a new root directory to hold this new project, then do the following steps, similar to what you did at the start of this guide:

#### Create a second service

*Run the Maven archetype:*

``` bash
mvn -U archetype:generate -DinteractiveMode=false \
    -DarchetypeGroupId=io.helidon.archetypes \
    -DarchetypeArtifactId=helidon-quickstart-mp \
    -DarchetypeVersion=4.4.0-SNAPSHOT \
    -DgroupId=io.helidon.examples \
    -DartifactId=helidon-quickstart-mp-2 \
    -Dpackage=io.helidon.examples.quickstart.mp
```

*The project will be built and run from the `helidon-quickstart-mp` directory:*

``` bash
cd helidon-quickstart-mp-2
```

*Add the following dependency to `pom.xml`:*

``` xml
<dependency>
    <groupId>io.helidon.tracing.providers</groupId>
    <artifactId>helidon-tracing-providers-jaeger</artifactId>
</dependency>
```

*Replace `META-INF/microprofile-config.properties` with the following:*

``` bash
app.greeting=Hello From MP-2
tracing.service=helidon-mp-2

# Microprofile server properties
server.port=8081
```

*Build the application, skipping unit tests, then run it:*

``` bash
mvn package -DskipTests=true
java -jar target/helidon-quickstart-mp-2.jar
```

*Run the curl command in a new terminal window and check the response (**notice the port is 8081**) :*

``` bash
curl http://localhost:8081/greet
```

*Response body*

``` json
{
  "message": "Hello From MP-2 World!"
}
```

#### Modify the first service

Once you have validated that the second service is running correctly, you need to modify the original application to call it.

*Replace the `GreetResource` class with the following code:*

``` java
@Path("/greet")
@RequestScoped
public class GreetResource {

    @Uri("http://localhost:8081/greet")
    private WebTarget target; 

    private static final JsonBuilderFactory JSON = Json.createBuilderFactory(Map.of());
    private final GreetingProvider greetingProvider;

    @Inject
    public GreetResource(GreetingProvider greetingConfig) {
        this.greetingProvider = greetingConfig;
    }

    @GET
    @Produces(MediaType.APPLICATION_JSON)
    public JsonObject getDefaultMessage() {
        return createResponse("World");
    }

    @GET
    @Path("/outbound") 
    public JsonObject outbound() {
        return target.request().accept(MediaType.APPLICATION_JSON_TYPE).get(JsonObject.class);
    }

    private JsonObject createResponse(String who) {
        String msg = String.format("%s %s!", greetingProvider.getMessage(), who);

        return JSON.createObjectBuilder().add("message", msg).build();
    }
}
```

- This is the `WebTarget` needed to send a request to the second service at port `8081`.

- This is the new endpoint that will call the second service.

*Build and run the application, then invoke the endpoint and check the response:*

``` bash
curl -i http://localhost:8080/greet/outbound 
```

- The request went to the service on `8080`, which then invoked the service at `8081` to get the greeting.

*Response body*

``` hocon
{
  "message": "Hello From MP-2 World!" 
}
```

- Notice the greeting came from the second service.

Refresh the Jaeger UI trace listing page and notice that there is a trace across two services.

<figure>
<img src="../images/guides/12_tracing_detail_2_services.png" alt="Traces" />
<figcaption>Tracing across multiple services detail view</figcaption>
</figure>

In the image above, you can see that the trace includes spans from two services. You will notice there is a gap before the sixth span, which is a `get` operation. This is a one-time client initialization delay. Run the `/outbound` curl command again and look at the new trace to see that the delay no longer exists.

You can now stop your second service, it is no longer used in this guide.

## Integration with Kubernetes

The following example demonstrates how to use Jaeger from a Helidon application running in Kubernetes.

*Update `application.yaml`:*

``` bash
tracing:
  host: "jaeger"
```

*Stop the application and build the docker image for your application:*

``` bash
docker build -t helidon-tracing-mp .
```

### Deploy Jaeger into Kubernetes

*Create the Kubernetes YAML specification, named `jaeger.yaml`, with the following contents:*

``` yaml
apiVersion: v1
kind: Service
metadata:
  name: jaeger
spec:
  ports:
    - port: 16686
      protocol: TCP
  selector:
    app: jaeger
---
kind: Pod
apiVersion: v1
metadata:
  name: jaeger
  labels:
    app: jaeger
spec:
  containers:
    - name: jaeger
      image: jaegertracing/all-in-one
      imagePullPolicy: IfNotPresent
      ports:
        - containerPort: 16686
```

*Create the Jaeger pod and ClusterIP service:*

``` bash
kubectl apply -f ./jaeger.yaml
```

*Create a Jaeger external server and expose it on port 9142:*

``` bash
kubectl expose pod jaeger --name=jaeger-external --port=16687 --target-port=16686 --type=LoadBalancer 
```

- Create a service so that you can access the Jaeger UI.

Navigate to <http://localhost:16687/search> to validate that you can access Jaeger running in Kubernetes. It may take a few seconds before it is ready.

### Deploy Your Helidon Application into Kubernetes

*Create the Kubernetes YAML specification, named `tracing.yaml`, with the following contents:*

``` yaml
kind: Service
apiVersion: v1
metadata:
  name: helidon-tracing 
  labels:
    app: helidon-tracing
spec:
  type: NodePort
  selector:
    app: helidon-tracing
  ports:
    - port: 8080
      targetPort: 8080
      name: http
---
kind: Deployment
apiVersion: apps/v1
metadata:
  name: helidon-tracing
spec:
  replicas: 1 
  selector:
    matchLabels:
      app: helidon-tracing
  template:
    metadata:
      labels:
        app: helidon-tracing
        version: v1
    spec:
      containers:
        - name: helidon-tracing
          image: helidon-tracing-mp
          imagePullPolicy: IfNotPresent
          ports:
            - containerPort: 8080
```

- A service of type `NodePort` that serves the default routes on port `8080`.

- A deployment with one replica of a pod.

*Create and deploy the application into Kubernetes:*

``` bash
kubectl apply -f ./tracing.yaml
```

### Access Your Application and the Jaeger Trace

*Get the application service information:*

``` bash
kubectl get service/helidon-tracing
```

``` bash
NAME             TYPE       CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
helidon-tracing   NodePort   10.99.159.2   <none>        8080:31143/TCP   8s 
```

- A service of type `NodePort` that serves the default routes on port `31143`.

*Verify the tracing endpoint using port `31143`, your port will likely be different:*

``` bash
curl http://localhost:31143/greet
```

``` json
{
  "message": "Hello World!"
}
```

Access the Jaeger UI at <http://localhost:16687/search> and click on the refresh icon to see the trace that was just created.

### Cleanup

You can now delete the Kubernetes resources that were just created during this example.

*Delete the Kubernetes resources:*

``` bash
kubectl delete -f ./jaeger.yaml
kubectl delete -f ./tracing.yaml
kubectl delete service jaeger-external
docker rm -f jaeger
```

## Creating custom spans

Helidon MP fully supports MicroProfile OpenTracing. You can add custom spans using `@Traced` annotation on methods of CDI beans.

**Note for invoking methods on same class:** *If you invoke a method on the same class, `@Traced` annotation would be ignored, as it is not invoked through a CDI proxy and as such cannot be intercepted. To make sure `@Traced` is honored, use it on JAX-RS resource methods and on CDI bean methods used from other beans.*

## Trace propagation across services

Automated trace propagation is supported currently only with Jersey client.

Tracing propagation works automatically as long as you run within the scope of Helidon MP and use Helidon components to invoke external services.

### Manual handling of traces in Jersey Client

There is an option to provide `SpanContext` programmatically (such as when writing a command line application that starts the span manually).

You can either configure the span context as the active span, or explicitly define it as client property.

*Tracing propagation with Jersey client*

``` java
Response response = client.target(serviceEndpoint)
        .request()
        // tracer should be provided unless available as GlobalTracer
        .property(TRACER_PROPERTY_NAME, tracer)
        .property(CURRENT_SPAN_CONTEXT_PROPERTY_NAME, spanContext)
        .get();
```

## Additional Information

### Jaeger Tracing

``` xml
<dependency>
    <groupId>io.helidon.tracing</groupId>
    <artifactId>helidon-tracing-providers-jaeger</artifactId>
</dependency>
```

## Configuring Jaeger

Jaeger tracer configuration.

Type: [io.helidon.tracing.Tracer](/apidocs/io.helidon.tracing/io/helidon/tracing/Tracer.html)

This is a standalone configuration type, prefix from configuration root: `tracing`

## Configuration options

<table style="width:100%;">
<caption>Optional configuration options</caption>
<colgroup>
<col style="width: 23%" />
<col style="width: 23%" />
<col style="width: 15%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">key</th>
<th style="text-align: left;">type</th>
<th style="text-align: left;">default value</th>
<th style="text-align: left;">description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>client-cert-pem</code></p></td>
<td style="text-align: left;"><p><a href="../mp/../config/io_helidon_common_configurable_Resource.xml">Resource</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Certificate of client in PEM format.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>exporter-timeout</code></p></td>
<td style="text-align: left;"><p>Duration</p></td>
<td style="text-align: left;"><p><code>PT10S</code></p></td>
<td style="text-align: left;"><p>Timeout of exporter requests.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>max-export-batch-size</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p><code>512</code></p></td>
<td style="text-align: left;"><p>Maximum Export Batch Size of exporter requests.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>max-queue-size</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p><code>2048</code></p></td>
<td style="text-align: left;"><p>Maximum Queue Size of exporter requests.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>private-key-pem</code></p></td>
<td style="text-align: left;"><p><a href="../mp/../config/io_helidon_common_configurable_Resource.xml">Resource</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Private key in PEM format.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>propagation</code></p></td>
<td style="text-align: left;"><p>JaegerTracerBuilder.PropagationFormat[] (B3, B3_SINGLE, JAEGER, W3C)</p></td>
<td style="text-align: left;"><p><code>JAEGER</code></p></td>
<td style="text-align: left;"><p>Add propagation format to use.</p>
<p>Allowed values:</p>
<ul>
<li><p><code>B3</code>: The Zipkin B3 trace context propagation format using multiple headers.</p></li>
<li><p><code>B3_SINGLE</code>: B3 trace context propagation using a single header.</p></li>
<li><p><code>JAEGER</code>: The Jaeger trace context propagation format.</p></li>
<li><p><code>W3C</code>: The W3C trace context propagation format.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>sampler-param</code></p></td>
<td style="text-align: left;"><p>Number</p></td>
<td style="text-align: left;"><p><code>1</code></p></td>
<td style="text-align: left;"><p>The sampler parameter (number).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>sampler-type</code></p></td>
<td style="text-align: left;"><p>JaegerTracerBuilder.SamplerType (CONSTANT, RATIO)</p></td>
<td style="text-align: left;"><p><code>CONSTANT</code></p></td>
<td style="text-align: left;"><p>Sampler type.</p>
<p>See <a href="https://www.jaegertracing.io/docs/latest/sampling/#client-sampling-configuration">Sampler types</a>.</p>
<p>Allowed values:</p>
<ul>
<li><p><code>CONSTANT</code>: Constant sampler always makes the same decision for all traces. It either samples all traces <code>1</code> or none of them <code>0</code>.</p></li>
<li><p><code>RATIO</code>: Ratio of the requests to sample, double value.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>schedule-delay</code></p></td>
<td style="text-align: left;"><p>Duration</p></td>
<td style="text-align: left;"><p><code>PT5S</code></p></td>
<td style="text-align: left;"><p>Schedule Delay of exporter requests.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>span-processor-type</code></p></td>
<td style="text-align: left;"><p>JaegerTracerBuilder.SpanProcessorType (SIMPLE, BATCH)</p></td>
<td style="text-align: left;"><p><code>batch</code></p></td>
<td style="text-align: left;"><p>Span Processor type used.</p>
<p>Allowed values:</p>
<ul>
<li><p><code>SIMPLE</code>: Simple Span Processor.</p></li>
<li><p><code>BATCH</code>: Batch Span Processor.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>trusted-cert-pem</code></p></td>
<td style="text-align: left;"><p><a href="../mp/../config/io_helidon_common_configurable_Resource.xml">Resource</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Trusted certificates in PEM format.</p></td>
</tr>
</tbody>
</table>

The following is an example of a Jaeger configuration, specified in the YAML format.

``` yaml
tracing:
    service: "helidon-full-http"
    protocol: "https"
    host: "jaeger"
    port: 14240
```

### Jaeger Tracing Metrics

As the [Jaeger Tracing](#jaeger-tracing) section describes, you can use Jaeger tracing in your Helidon application.

### Zipkin Tracing

``` xml
<dependency>
    <groupId>io.helidon.tracing.providers</groupId>
    <artifactId>helidon-tracing-providers-zipkin</artifactId>
</dependency>
```

## Configuring Zipkin

Zipkin tracer configuration

Type: io.opentracing.Tracer

This is a standalone configuration type, prefix from configuration root: `tracing`

## Configuration options

<table style="width:100%;">
<caption>Optional configuration options</caption>
<colgroup>
<col style="width: 23%" />
<col style="width: 23%" />
<col style="width: 15%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">key</th>
<th style="text-align: left;">type</th>
<th style="text-align: left;">default value</th>
<th style="text-align: left;">description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>api-version</code></p></td>
<td style="text-align: left;"><p>ZipkinTracerBuilder.Version (V1, V2)</p></td>
<td style="text-align: left;"><p><code>V2</code></p></td>
<td style="text-align: left;"><p>Version of Zipkin API to use. Defaults to Version.V2.</p>
<p>Allowed values:</p>
<ul>
<li><p><code>V1</code>: Version 1.</p></li>
<li><p><code>V2</code>: Version 2.</p></li>
</ul></td>
</tr>
</tbody>
</table>

The following is an example of a Zipkin configuration, specified in the YAML format.

``` yaml
tracing:
  zipkin:
    service: "helidon-service"
    protocol: "https"
    host: "zipkin"
    port: 9987
    api-version: 1
    # this is the default path for API version 2
    path: "/api/v2/spans"
    tags:
      tag1: "tag1-value"
      tag2: "tag2-value"
    boolean-tags:
      tag3: true
      tag4: false
    int-tags:
      tag5: 145
      tag6: 741
```

Example of Zipkin trace:

<figure>
<img src="../images/webserver/zipkin.png" alt="Zipkin example" />
</figure>

### OpenTelemetry Tracing

Helidon supports configuration of OpenTelemetry and OpenTelemetry tracing in two primary ways: using tracing or using telemetry. The [Helidon MP Telemetry doc page](../mp/telemetry.md) describes how to use Helidon’s support for MicroProfile Telemetry to control OpenTelemetry.

Avoid using both the OpenTelemetry tracing support described here and support for MicroProfile Telemetry as the results are unpredictable.

> [!NOTE]
> If you provide settings under both `telemetry` and `tracing`, Helidon uses the `telemetry` settings. Specifying both does not confuse Helidon but it might confuse users.

*Dependency for OpenTelemetry support using tracing*

``` xml
<dependency>
    <groupId>io.helidon.tracing.providers</groupId>
    <artifactId>helidon-tracing-providers-opentelemetry</artifactId>
</dependency>
```

## Configuring OpenTelemetry Tracing

Type: [io.helidon.tracing.providers.opentelemetry.OpenTelemetryTracer](/apidocs/io.helidon.tracing.providers.opentelemetry/io/helidon/tracing/providers/opentelemetry/OpenTelemetryTracer.html)

This is a standalone configuration type, prefix from configuration root: `tracing`

## Configuration options

<table style="width:100%;">
<caption>Optional configuration options</caption>
<colgroup>
<col style="width: 23%" />
<col style="width: 23%" />
<col style="width: 15%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">key</th>
<th style="text-align: left;">type</th>
<th style="text-align: left;">default value</th>
<th style="text-align: left;">description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>boolean-tags</code></p></td>
<td style="text-align: left;"><p>Map&lt;string, boolean&gt;</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Tracer-level tags with boolean values added to all reported spans.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>client-cert-pem</code></p></td>
<td style="text-align: left;"><p><a href="../mp/../config/io_helidon_common_configurable_Resource.xml">Resource</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Client certificate for connecting securely to the tracing collector.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>enabled</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Whether to enable tracing. That is, whether to use a fully-featured tracing implementation on the path vs. a no-op implementation.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>export-timeout</code></p></td>
<td style="text-align: left;"><p>Duration</p></td>
<td style="text-align: left;"><p><code>PT10S</code></p></td>
<td style="text-align: left;"><p>Maximum time a transmission can be in progress before being cancelled.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>exporter-type</code></p></td>
<td style="text-align: left;"><p>OtlpExporterProtocolType (HTTP_PROTO, GRPC)</p></td>
<td style="text-align: left;"><p><code>OtlpExporterProtocolType.GRPC</code></p></td>
<td style="text-align: left;"><p>Type of OTLP exporter to use for pushing span data.</p>
<p>Allowed values:</p>
<ul>
<li><p><code>HTTP_PROTO</code>: http/proto protocol type.</p></li>
<li><p><code>GRPC</code>: grpc protocol type.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>global</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Whether to create and register a tracer as the global tracer.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>host</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Host used in connecting to the tracing collector.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>int-tags</code></p></td>
<td style="text-align: left;"><p>Map&lt;string, int&gt;</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Tracer level tags with integer values added to all reported spans.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>max-export-batch-size</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p><code>512</code></p></td>
<td style="text-align: left;"><p>Maximum number of spans grouped for transmission together; typically does not exceed maxQueueSize() (batch processing).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>max-queue-size</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p><code>2048</code></p></td>
<td style="text-align: left;"><p>Maximum number of spans retained before discarding any not sent to the tracing collector (batch processing).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>path</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Path at the collector host and port used when sending trace data to the collector.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>port</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Port used in connecting to the tracing collector.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>private-key-pem</code></p></td>
<td style="text-align: left;"><p><a href="../mp/../config/io_helidon_common_configurable_Resource.xml">Resource</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Private key for connecting securely to the tracing collector.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>propagators</code></p></td>
<td style="text-align: left;"><p>TextMapPropagator[]</p></td>
<td style="text-align: left;"><p><code>new java.util.ArrayList&lt;&gt;(io.helidon.tracing.providers.opentelemetry.ContextPropagationType.DEFAULT_PROPAGATORS)</code></p></td>
<td style="text-align: left;"><p>Context propagators.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>protocol</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Protocol (such as <code>http</code> or <code>https</code>) used in connecting to the tracing collector.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>sampler-param</code></p></td>
<td style="text-align: left;"><p>double</p></td>
<td style="text-align: left;"><p><code>1.0</code></p></td>
<td style="text-align: left;"><p>Parameter value used by the selected sampler; interpretation depends on the sampler type..</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>sampler-type</code></p></td>
<td style="text-align: left;"><p>SamplerType (CONSTANT, RATIO)</p></td>
<td style="text-align: left;"><p><code>SamplerType.CONSTANT</code></p></td>
<td style="text-align: left;"><p>Type of sampler for collecting spans.</p>
<p>Allowed values:</p>
<ul>
<li><p><code>CONSTANT</code>: Sampling of every span.</p></li>
<li><p><code>RATIO</code>: Sampling of a proportion [0.0, 1.0] of spans.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>schedule-delay</code></p></td>
<td style="text-align: left;"><p>Duration</p></td>
<td style="text-align: left;"><p><code>PT5S</code></p></td>
<td style="text-align: left;"><p>Delay between consecutive transmissions to the tracing collector (batch processing).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>service</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Service name of the traced service.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>span-processor-type</code></p></td>
<td style="text-align: left;"><p>SpanProcessorType (SIMPLE, BATCH)</p></td>
<td style="text-align: left;"><p><code>SpanProcessorType.BATCH</code></p></td>
<td style="text-align: left;"><p>Type of span processor for accumulating spans before transmission to the tracing collector.</p>
<p>Allowed values:</p>
<ul>
<li><p><code>SIMPLE</code>: Simple Span Processor.</p></li>
<li><p><code>BATCH</code>: Batch Span Processor.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>tags</code></p></td>
<td style="text-align: left;"><p>Map&lt;string, string&gt;</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Tracer-level tags with <code>String</code> values added to all reported spans.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>trusted-cert-pem</code></p></td>
<td style="text-align: left;"><p><a href="../mp/../config/io_helidon_common_configurable_Resource.xml">Resource</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Trusted certificates for connecting to the tracing collector.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>uri</code></p></td>
<td style="text-align: left;"><p>URI</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>URI for the collector to which to send tracing data.</p></td>
</tr>
</tbody>
</table>

*Example Helidon configuration for OpenTelemetry tracing*

tracing.service=helidon-otel-tracing-example 
    tracing.global=false                         
    tracing.int-tags.0.example=1                 
    tracing.tags.0.direction=north

- Specifies the OpenTelemetry service name.

- Indicates the configured tracer *should not* be made the global tracer (defaults to `true`).

- Assigns an integer-valued tag `example` the value `1`.

- Assigns a string-valued tag `direction` the value `north`.

By default, Helidon tracing support for OpenTelemetry uses OpenTelemetry’s OTLP gRPC exporter. Alternatively, you can choose to use OpenTelemetry’s HTTP exporter using protobuf by setting `exporter-type` to `http/proto`. To use other exporters OpenTelemetry offers, use the Helidon `telemetry` configuration instead of `tracing`.

### Responding to Span Lifecycle Events

Applications and libraries can register listeners to be notified at several moments during the lifecycle of every Helidon span:

- Before a new span starts

- After a new span has started

- After a span ends

- After a span is activated (creating a new scope)

- After a scope is closed

The next sections explain how you can write and add a listener and what it can do. See the [`SpanListener`](/apidocs/io.helidon.tracing/io/helidon/tracing/SpanListener.html) Javadoc for more information.

#### Understanding What Listeners Do

A listener cannot affect the lifecycle of a span or scope it is notified about, but it can add tags and events and update the baggage associated with a span. Often a listener does additional work that does not change the span or scope such as logging a message.

When Helidon invokes the listener’s methods it passes proxies for the `Span.Builder`, `Span`, and `Scope` arguments. These proxies limit the access the listener has to the span builder, span, or scope, as summarized in the following table. If a listener method tries to invoke a forbidden operation, the proxy throws a [`SpanListener.ForbiddenOperationException`](/apidocs/io.helidon.tracing/io/helidon/tracing/SpanListener.ForbiddenOperationException.html) and Helidon then logs a `WARNING` message describing the invalid operation invocation.

| Tracing type | Changes allowed |
|----|----|
| [`Span.Builder`](/apidocs/io.helidon.tracing/io/helidon/tracing/Span.Builder.html) | Add tags |
| [`Span`](/apidocs/io.helidon.tracing/io/helidon/tracing/Span.html) | Retrieve and update baggage, add events, add tags |
| [`Scope`](/apidocs/io.helidon.tracing/io/helidon/tracing/Scope.html) | none |

Summary of Permitted Operations on Proxies Passed to Listeners

The following tables list specifically what operations the proxies permit.

| Method | Purpose | OK? |
|----|----|----|
| `build()` | Starts the span. | \- |
| `end` methods | Ends the span. | \- |
| `get()` | Starts the span. | \- |
| `kind(Kind)` | Sets the "kind" of span (server, client, internal, etc.) | \- |
| `parent(SpanContext)` | Sets the parent of the span to be created from the builder. | \- |
| `start()` | Starts the span. | \- |
| `start(Instant)` | Starts the span. | \- |
| `tag` methods | Add a tag to the builder before the span is built. | ✓ |
| `unwrap(Class)` | Cast the builder to the specified implementation type. † | ✓ |

[`io.helidon.tracing.Span.Builder`](/apidocs/io.helidon.tracing/io/helidon/tracing/Span.Builder.html) Operations

† Helidon returns the unwrapped object, not a proxy for it.

| Method | Purpose | OK? |
|----|----|----|
| `activate()` | Makes the span "current", returning a `Scope`. | \- |
| `addEvent` methods | Associate a string (and optionally other info) with a span. | ✓ |
| `baggage()` | Returns the `Baggage` instance associated with the span. | ✓ |
| `context()` | Returns the `SpanContext` associated with the span. | ✓ |
| `status(Status)` | Sets the status of the span. | \- |
| any `tag` method | Add a tag to the span. | ✓ |
| `unwrap(Class)` | Cast the span to the specified implementation type. † | ✓ |

[`io.helidon.tracing.Span`](/apidocs/io.helidon.tracing/io/helidon/tracing/Span.html) Operations

† Helidon returns the unwrapped object, not a proxy to it.

| Method       | Purpose                              | OK? |
|--------------|--------------------------------------|-----|
| `close()`    | Close the scope.                     | \-  |
| `isClosed()` | Reports whether the scope is closed. | ✓   |

[`io.helidon.tracing.Scope`](/apidocs/io.helidon.tracing/io/helidon/tracing/Scope.html) Operations

| Method | Purpose | OK? |
|----|----|----|
| `asParent(Span.Builder)` | Sets this context as the parent of a new span builder. | ✓ |
| `baggage()` | Returns `Baggage` instance associated with the span context. | ✓ |
| `spanId()` | Returns the span ID. | ✓ |
| `traceId()` | Returns the trace ID. | ✓ |

[`io.helidon.tracing.SpanContext`](/apidocs/io.helidon.tracing/io/helidon/tracing/SpanContext.html) Operations

#### Adding a Listener

##### Explicitly Registering a Listener on a [`Tracer`](/apidocs/io.helidon.tracing/io/helidon/tracing/Tracer.html)

Create a `SpanListener` instance and invoke the `Tracer#register(SpanListener)` method to make the listener known to that tracer.

##### Automatically Registering a Listener on all `Tracer` Instances

Helidon also uses Java service loading to locate listeners and register them automatically on all `Tracer` objects. Follow these steps to add a listener service provider.

1.  Implement the [`SpanListener`](/apidocs/io.helidon.tracing/io/helidon/tracing/SpanListener.html) interface.

2.  Declare your implementation as a service provider:

    1.  Create the file `META-INF/services/io.helidon.tracing.SpanListener` containing a line with the fully-qualified name of your class which implements `SpanListener`.

    2.  If your service has a `module-info.java` file add the following line to it:

        ``` java
        provides io.helidon.tracing.SpanListener with <your-implementation-class>;
        ```

The `SpanListener` interface declares default no-op implementations for all the methods, so your listener can implement only the methods it needs to.

Helidon invokes each listener’s methods in the following order:

| Method | When invoked |
|----|----|
| `starting(Span.Builder<?> spanBuilder)` | Just before a span is started from its builder. |
| `started(Span span)` | Just after a span has started. |
| `activated(Span span, Scope scope)` | After a span has been activated, creating a new scope. A given span might never be activated; it depends on the code. |
| `closed(Span span, Scope scope)` | After a scope has been closed. |
| `ended(Span span)` | After a span has ended successfully. |
| `ended(Span span, Throwable t)` | After a span has ended unsuccessfully. |

Order in which Helidon Invokes Listener Methods

## Reference

- [MicroProfile Opentracing Specification](https://download.eclipse.org/microprofile/microprofile-opentracing-3.0/microprofile-opentracing-spec-3.0.html)

- [Opentracing Project](https://opentracing.io/)
