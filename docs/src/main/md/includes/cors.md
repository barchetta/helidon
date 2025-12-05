The [cross-origin resource sharing (CORS)
protocol](https://www.w3.org/TR/cors) helps developers control if and
how REST resources served by their applications can be shared across
origins. Helidon {flavor-uc} includes an implementation of CORS that you
can use to add CORS behavior to the services you develop. You can define
your application’s CORS behavior programmatically using the Helidon CORS
API alone or together with configuration.

Helidon also provides three built-in services that add their own
endpoints to your application—​health, metrics, and OpenAPI—​that have
integrated CORS support. By adding very little code to your application,
you control how all the resources in your application—​the ones you write
and the ones provided by the Helidon built-in services—​can be shared
across origins.

# Before You Begin

## Planning Your Resource Sharing

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

The [Managing
Dependencies](../about/managing-dependencies.md)
page describes how you should declare dependency management for Helidon
applications. For CORS support in Helidon {flavor-uc}, you must include
the following dependency in your project:

# Understanding the CORS Configuration Formats

Support in Helidon for CORS configuration uses two closely-related
cross-origin configuration formats: basic and mapped. Each format
corresponds to a class in the Helidon CORS library. The basic format
corresponds to the
[`CrossOriginConfig`]({cors-javadoc-base-url}/io/helidon/cors/CrossOriginConfig.html)
class, and the mapped format corresponds to the
[`MappedCrossOriginConfig`]({cors-javadoc-base-url}/io/helidon/cors/MappedCrossOriginConfig.html)
class.

# Basic Cross-Origin Configuration

In configuration, Helidon represents basic CORS information as a section
that contains one or more key/value pairs. Each key-value pair assigns
one characteristic of CORS behavior.

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
{mapped-config-top-key}: 
  paths: 
    - path-pattern: /greeting 
      allow-origins: ["https://foo.com", "https://there.com", "https://other.com"] 
      allow-methods: ["PUT", "DELETE"]
    - path-pattern: / 
      allow-methods: ["GET", "HEAD", "OPTIONS", "POST"] 
```

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
[`PathMatcher`]({http-javadoc-base-url}/io/helidon/http/PathMatcher.html)
class.

> [!NOTE]
> Be sure to arrange the entries in the order that you want Helidon to
> check them. Helidon CORS support searches the cross-origin entries in
> the order you define them until it finds an entry that matches an
> incoming request’s path pattern and HTTP method.

# CORS and the Requested URI Feature

The decisions the Helidon CORS feature makes depend on accurate
information about each incoming request, particularly the host to which
the request is sent. Conveyed as headers in the request, this
information can be changed or overwritten by intermediate nodes—​such as
load balancers—​between the origin of the request and your service.

Well-behaved intermediate nodes preserve this important data in other
headers, such as `Forwarded`.

The CORS support in Helidon uses the requested URI feature to discover
the correct information about each request, according to your
configuration, so it can make accurate decisions about whether to permit
cross-origin accesses.

# Using CORS Support in Built-in Helidon Services

Several built-in Helidon services—​[health](#{health-page}),
[metrics](#{metrics-page}), and [OpenAPI](#{openapi-page})--have
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

## Built-in Services with CORS

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

## Configuring CORS for Built-in Services

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

## Accessing the Shared Resources

If you have edited the Helidon {flavor-uc} QuickStart application as
described in the previous topics and saved your changes, you can build
and run the application. Once you do so you can execute `curl` commands
to demonstrate the behavior changes in the metric and health services
with the addition of the CORS functionality. Note the addition of the
`Origin` header value in the `curl` commands, and the
`Access-Control-Allow-Origin` in the successful responses.

### Build and Run the Application

Build and run the QuickStart application as usual.

### Retrieve Metrics

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

### Retrieve Health

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
