# CORS Shared content

The [cross-origin resource sharing (CORS) protocol](https://www.w3.org/TR/cors) helps developers control if and how REST resources served by their applications can be shared across origins. Helidon {flavor-uc} includes an implementation of CORS that you can use to add CORS behavior to the services you develop. You can define your application’s CORS behavior programmatically using the Helidon CORS API alone or together with configuration.

### Before You Begin

#### Planning Your Resource Sharing

Before you revise your application to add CORS support, you need to decide what type of cross-origin sharing you want to allow for each resource your application exposes. For example, suppose for a given resource you want to allow unrestricted sharing for GET, HEAD, and POST requests (what CORS refers to as "simple" requests), but permit other types of requests only from the two origins `foo.com` and `there.com`. Your application would implement two types of CORS sharing: more relaxed for the simple requests and stricter for others.

Once you know the type of sharing you want to allow for each of your resources—​including any from built-in services—​you can change your application accordingly.

The [Managing Dependencies](../about/managing-dependencies.md) page describes how you should declare dependency management for Helidon applications. For CORS support in Helidon {flavor-uc}, you must include the following dependency in your project:

#### Understanding the CORS Configuration Formats

CORS configuration is done through [`CorsFeature`](%7Bwebserver-cors-javadoc-base-url%7D/io/helidon/webserver/cors/CorsFeature.md), a `WebServer` feature that configures CORS for the whole application. This configuration contains a list of protected `paths`, which use the Cross-Origin options and are mapped to the [`CorsPathConfig`](%7Bwebserver-cors-javadoc-base-url%7D/io/helidon/webserver/cors/CorsPathConfig.md).

#### Cross-Origin Server Feature Configuration

Type: [io.helidon.webserver.cors.CorsFeature](%7Bjavadoc-base-url%7D/io.helidon.webserver.cors/io/helidon/webserver/cors/CorsFeature.md)

This is a standalone configuration type, prefix from configuration root: `cors`

This type provides the following service implementations:

- `io.helidon.webserver.spi.ServerFeatureProvider`

#### Configuration options

| key | type | default value | description |
|----|----|----|----|
| `enabled` | boolean |   | This feature can be disabled. This feature is automatically enabled if there is at least one paths() defined. |

Table 1. Required configuration options {.tableblock .frame-all .grid-all .stretch}

| key | type | default value | description |
|----|----|----|----|
| `add-defaults` | boolean | `true` | Whether to add a default path configuration, that matches all paths, `GET, HEAD, POST` methods, and allows all origins, methods, and headers. This is always added as a last path. |
| `paths` | [CorsPathConfig\[\]](../includes/../config/io_helidon_webserver_cors_CorsPathConfig.md) |   | Per path configuration. Default path is added, unless addDefaults() is set to `false`. |
| `sockets` | string\[\] |   | List of sockets to register this feature on. If empty, it would get registered on all sockets. |
| `weight` | double | `850.0` | Weight of the CORS feature. As it is used by other features, the default is quite high: `850.0`. |

Table 2. Optional configuration options {.tableblock .frame-all .grid-all .stretch}

The following example only adds defaults (allow all origins and all methods):

``` highlight
cors:
  enabled: true (1)
```

1.  To only use defaults, enabled must be set to `true`, as otherwise the feature is enabled only if at least one path is configured under `paths`

The following example limits cross-origin resource sharing for `PUT` and `DELETE` operations to only `foo.com` and `there.com`, and allows all other methods and origins

``` highlight
cors:
  paths:
    path-pattern: "/*" (1)
    allow-origins: ["https://foo.com", "https://there.com"]
    allow-methods: ["PUT", "DELETE"]
```

1.  A path pattern that matches all paths on the server

#### Cross-Origin Path Configuration

All configuration options that can be used for each `path` when configuring CORS.

Type: [io.helidon.webserver.cors.CorsPathConfig](%7Bjavadoc-base-url%7D/io.helidon.webserver.cors/io/helidon/webserver/cors/CorsPathConfig.md)

#### Configuration options

<table class="tableblock frame-all grid-all stretch" style="width:100%;">
<caption>Table 3. Optional configuration options</caption>
<colgroup>
<col style="width: 23%" />
<col style="width: 23%" />
<col style="width: 15%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr>
<th class="tableblock halign-left valign-top">key</th>
<th class="tableblock halign-left valign-top">type</th>
<th class="tableblock halign-left valign-top">default value</th>
<th class="tableblock halign-left valign-top">description</th>
</tr>
</thead>
<tbody>
<tr>
<td class="tableblock halign-left valign-top"><p><code>allow-credentials</code></p></td>
<td class="tableblock halign-left valign-top"><p>boolean</p></td>
<td class="tableblock halign-left valign-top"><p><code>false</code></p></td>
<td class="tableblock halign-left valign-top"><p>Whether to allow credentials.</p>
<p>If enabled, this will be used in <code>Access-Control-Allow-Credentials</code> header.</p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p><code>allow-headers</code></p></td>
<td class="tableblock halign-left valign-top"><p>string[]</p></td>
<td class="tableblock halign-left valign-top"><p><code>*</code></p></td>
<td class="tableblock halign-left valign-top"><p>Set of allowed headers, defaults to all.</p>
<p>If not empty, this will be used in <code>Access-Control-Allow-Headers</code> header.</p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p><code>allow-methods</code></p></td>
<td class="tableblock halign-left valign-top"><p>string[]</p></td>
<td class="tableblock halign-left valign-top"><p><code>*</code></p></td>
<td class="tableblock halign-left valign-top"><p>Set of allowed methods, defaults to all.</p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p><code>allow-origins</code></p></td>
<td class="tableblock halign-left valign-top"><p>string[]</p></td>
<td class="tableblock halign-left valign-top"><p><code>*</code></p></td>
<td class="tableblock halign-left valign-top"><p>Set of allowed origins, defaults to all.</p>
If not empty, this will be used with <code>Access-Control-Allow-Origin</code> header. Note that allowed origins may be either a full origin, such as <a href="http://www.example.com" class="bare"><code>http://www.example.com</code></a>, or a regular expression. Any origin that contains (
`), or `
, or curly braces is considered a regular expression (i.e. <code>http://..example.com</code>).
<p>If you configure a regular expression, it would never be returned if all allowed origins are returned in a pre-flight request.</p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p><code>enabled</code></p></td>
<td class="tableblock halign-left valign-top"><p>boolean</p></td>
<td class="tableblock halign-left valign-top"><p><code>true</code></p></td>
<td class="tableblock halign-left valign-top"><p>Whether this CORS configuration should be enabled or not. If disabled, this configuration will be ignored, and the next path will be checked.</p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p><code>expose-headers</code></p></td>
<td class="tableblock halign-left valign-top"><p>string[]</p></td>
<td class="tableblock halign-left valign-top"><p> </p></td>
<td class="tableblock halign-left valign-top"><p>Set of exposed headers, defaults to none.</p>
<p>If not empty, this will be used in <code>Access-Control-Expose-Headers</code> header.</p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p><code>max-age</code></p></td>
<td class="tableblock halign-left valign-top"><p>Duration</p></td>
<td class="tableblock halign-left valign-top"><p><code>PT1H</code></p></td>
<td class="tableblock halign-left valign-top"><p>Max age as a duration.</p>
<p>This value will be used in <code>Access-Control-Max-Age</code> header (in seconds).</p>
<p>For backward compatibility, you can specify the following when used from configuration:</p>
<ul>
<li><p>integer (such as <code>3600</code>) - number of seconds as a number</p></li>
<li><p>integer ms (such as <code>10000 ms</code>) - number of milliseconds</p></li>
<li><p>duration format (such as <code>PT1H</code>) - format of java.time.Duration</p></li>
</ul></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p><code>path-pattern</code></p></td>
<td class="tableblock halign-left valign-top"><p>string</p></td>
<td class="tableblock halign-left valign-top"><p> </p></td>
<td class="tableblock halign-left valign-top"><p>Path pattern to apply this configuration for. Note that paths are checked in sequence, and the first path that matches the request will be used to configure CORS.</p>
<p>Always configure the most restrictive rules first.</p></td>
</tr>
</tbody>
</table>

#### Accessing the Shared Resources

If you have edited the Helidon {flavor-uc} QuickStart application as described in the previous topics and saved your changes, you can build and run the application. Once you do so you can execute `curl` commands to demonstrate the behavior changes in the metric and health services with the addition of the CORS functionality. Note the addition of the `Origin` header value in the `curl` commands, and the `Access-Control-Allow-Origin` in the successful responses.

##### Build and Run the Application

Build and run the QuickStart application as usual.

### CORS and the Requested URI Feature

The decisions the Helidon CORS feature makes depend on accurate information about each incoming request, particularly the host to which the request is sent. Conveyed as headers in the request, this information can be changed or overwritten by intermediate nodes—​such as load balancers—​between the origin of the request and your service.

Well-behaved intermediate nodes preserve this important data in other headers, such as `Forwarded`.

The CORS support in Helidon uses the requested URI feature to discover the correct information about each request, according to your configuration, so it can make accurate decisions about whether to permit cross-origin accesses.

### Configuring CORS for Built-in Services

Use configuration to control whether and how each of the built-in services works with CORS.

In the `cors` configuration section add a block for each built-in service using its path as described in the CORS configuration section. The following example restricts sharing of the `/observe/health` resource, provided by the health built-in service, to only the origin `https://there.com`.

``` highlight
cors:
  paths:
    - "path-pattern": "/observe/health"
      "allow-origins": ["https://there.com"]
    - "path-pattern": "/observe/metrics"
      "allow-origins": ["https://foo.com"]
```

#### Retrieve Metrics

The metrics service rejects attempts to access metrics on behalf of a disallowed origin.

``` highlight
curl -i -H "Origin: https://other.com" http://localhost:8080/observe/metrics
```

Curl output

``` highlight
HTTP/1.1 403 Forbidden
Date: Mon, 11 May 2020 11:08:09 -0500
transfer-encoding: chunked
connection: keep-alive
```

But accesses from `foo.com` succeed.

``` highlight
curl -i -H "Origin: https://foo.com" http://localhost:8080/observe/metrics
```

Curl output

``` highlight
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

##### Retrieve Health

The health service rejects requests from origins not specifically approved.

``` highlight
curl -i -H "Origin: https://foo.com" http://localhost:8080/observe/health
```

``` highlight
HTTP/1.1 403 Forbidden
Date: Mon, 11 May 2020 12:06:55 -0500
transfer-encoding: chunked
connection: keep-alive
```

And responds successfully only to cross-origin requests from `https://there.com`.

``` highlight
curl -i -H "Origin: https://there.com" http://localhost:8080/observe/health
```

``` highlight
HTTP/1.1 200 OK
Access-Control-Allow-Origin: https://there.com
Content-Type: application/json
Date: Mon, 11 May 2020 12:07:32 -0500
Vary: Origin
connection: keep-alive
content-length: 461

{"outcome":"UP",...}
```
