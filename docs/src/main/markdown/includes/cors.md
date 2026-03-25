# CORS Shared content

The [cross-origin resource sharing (CORS) protocol](https://www.w3.org/TR/cors) helps developers control if and how REST resources served by their applications can be shared across origins. Helidon {flavor-uc} includes an implementation of CORS that you can use to add CORS behavior to the services you develop. You can define your application’s CORS behavior programmatically using the Helidon CORS API alone or together with configuration.

## Before You Begin

### Planning Your Resource Sharing

Before you revise your application to add CORS support, you need to decide what type of cross-origin sharing you want to allow for each resource your application exposes. For example, suppose for a given resource you want to allow unrestricted sharing for GET, HEAD, and POST requests (what CORS refers to as "simple" requests), but permit other types of requests only from the two origins `foo.com` and `there.com`. Your application would implement two types of CORS sharing: more relaxed for the simple requests and stricter for others.

Once you know the type of sharing you want to allow for each of your resources—​including any from built-in services—​you can change your application accordingly.

The [Managing Dependencies](../about/managing-dependencies.md) page describes how you should declare dependency management for Helidon applications. For CORS support in Helidon {flavor-uc}, you must include the following dependency in your project:

### Understanding the CORS Configuration Formats

CORS configuration is done through [`CorsFeature`]({webserver-cors-javadoc-base-url}/io/helidon/webserver/cors/CorsFeature.md), a `WebServer` feature that configures CORS for the whole application. This configuration contains a list of protected `paths`, which use the Cross-Origin options and are mapped to the [`CorsPathConfig`]({webserver-cors-javadoc-base-url}/io/helidon/webserver/cors/CorsPathConfig.md).

### Cross-Origin Server Feature Configuration

### Configuration options

| Key | Kind | Type | Default Value | Description |
|----|----|----|----|----|
| <span id="ae53cb-add-defaults"></span> `add-defaults` | `VALUE` | `Boolean` | `true` | Whether to add a default path configuration, that matches all paths, `GET, HEAD, POST` methods, and allows all origins, methods, and headers |
| <span id="a6b476-enabled"></span> `enabled` | `VALUE` | `Boolean` |   | This feature can be disabled |
| <span id="a44bb0-paths"></span> [`paths`](../config/io_helidon_webserver_cors_CorsPathConfig.md) | `LIST` | `i.h.w.c.CorsPathConfig` |   | Per path configuration |
| <span id="a29c5b-paths-discover-services"></span> `paths-discover-services` | `VALUE` | `Boolean` | `true` | Whether to enable automatic service discovery for `paths` |
| <span id="a93acb-sockets"></span> `sockets` | `LIST` | `String` |   | List of sockets to register this feature on |
| <span id="a96481-weight"></span> `weight` | `VALUE` | `Double` | `850.0` | Weight of the CORS feature |

The following example only adds defaults (allow all origins and all methods):

``` yaml
cors:
  enabled: true 
```

- To only use defaults, enabled must be set to `true`, as otherwise the feature is enabled only if at least one path is configured under `paths`

The following example limits cross-origin resource sharing for `PUT` and `DELETE` operations to only `foo.com` and `there.com`, and allows all other methods and origins

``` yaml
cors:
  paths:
    path-pattern: "/*" 
    allow-origins: ["https://foo.com", "https://there.com"]
    allow-methods: ["PUT", "DELETE"]
```

- A path pattern that matches all paths on the server

### Cross-Origin Path Configuration

All configuration options that can be used for each `path` when configuring CORS.

### Configuration options

| Key | Kind | Type | Default Value | Description |
|----|----|----|----|----|
| <span id="a63978-allow-credentials"></span> `allow-credentials` | `VALUE` | `Boolean` | `false` | Whether to allow credentials |
| <span id="abc506-allow-headers"></span> `allow-headers` | `LIST` | `String` | `*` | Set of allowed headers, defaults to all |
| <span id="a7f636-allow-methods"></span> `allow-methods` | `LIST` | `String` | `*` | Set of allowed methods, defaults to all |
| <span id="a10bcf-allow-origins"></span> `allow-origins` | `LIST` | `String` | `*` | Set of allowed origins, defaults to all |
| <span id="aeefbd-enabled"></span> `enabled` | `VALUE` | `Boolean` | `true` | Whether this CORS configuration should be enabled or not |
| <span id="abb307-expose-headers"></span> `expose-headers` | `LIST` | `String` |   | Set of exposed headers, defaults to none |
| <span id="a1f548-max-age"></span> `max-age` | `VALUE` | `i.h.w.c.C.PathCustomMethods` | `PT1H` | Max age as a duration |
| <span id="afe1ca-path-pattern"></span> `path-pattern` | `VALUE` | `String` |   | Path pattern to apply this configuration for |

### Accessing the Shared Resources

If you have edited the Helidon {flavor-uc} QuickStart application as described in the previous topics and saved your changes, you can build and run the application. Once you do so you can execute `curl` commands to demonstrate the behavior changes in the metric and health services with the addition of the CORS functionality. Note the addition of the `Origin` header value in the `curl` commands, and the `Access-Control-Allow-Origin` in the successful responses.

#### Build and Run the Application

Build and run the QuickStart application as usual.

## CORS and the Requested URI Feature

The decisions the Helidon CORS feature makes depend on accurate information about each incoming request, particularly the host to which the request is sent. Conveyed as headers in the request, this information can be changed or overwritten by intermediate nodes—​such as load balancers—​between the origin of the request and your service.

Well-behaved intermediate nodes preserve this important data in other headers, such as `Forwarded`.

The CORS support in Helidon uses the requested URI feature to discover the correct information about each request, according to your configuration, so it can make accurate decisions about whether to permit cross-origin accesses.

## Configuring CORS for Built-in Services

Use configuration to control whether and how each of the built-in services works with CORS.

In the `cors` configuration section add a block for each built-in service using its path as described in the CORS configuration section. The following example restricts sharing of the `/observe/health` resource, provided by the health built-in service, to only the origin `https://there.com`.

``` yaml
cors:
  paths:
    - "path-pattern": "/observe/health"
      "allow-origins": ["https://there.com"]
    - "path-pattern": "/observe/metrics"
      "allow-origins": ["https://foo.com"]
```

### Retrieve Metrics

The metrics service rejects attempts to access metrics on behalf of a disallowed origin.

``` bash
curl -i -H "Origin: https://other.com" http://localhost:8080/observe/metrics
```

*Curl output*

``` listing
HTTP/1.1 403 Forbidden
Date: Mon, 11 May 2020 11:08:09 -0500
transfer-encoding: chunked
connection: keep-alive
```

But accesses from `foo.com` succeed.

``` bash
curl -i -H "Origin: https://foo.com" http://localhost:8080/observe/metrics
```

*Curl output*

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

#### Retrieve Health

The health service rejects requests from origins not specifically approved.

``` bash
curl -i -H "Origin: https://foo.com" http://localhost:8080/observe/health
```

``` listing
HTTP/1.1 403 Forbidden
Date: Mon, 11 May 2020 12:06:55 -0500
transfer-encoding: chunked
connection: keep-alive
```

And responds successfully only to cross-origin requests from `https://there.com`.

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
