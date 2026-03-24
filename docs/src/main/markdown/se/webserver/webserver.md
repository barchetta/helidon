# WebServer Introduction

## Contents

- [Overview](#_overview)

- [Maven Coordinates](#maven-coordinates)

- [Configuration](#_configuration)

  - [Configuring the WebServer in Your Code](#_configuring_the_webserver_in_your_code)

  - [Configuring the WebServer in a Configuration File](#_configuring_the_webserver_in_a_configuration_file)

  - [Configuring TLS](#_configuring_tls)

  - [Configuration Options](#_configuration_options)

- [Routing](#_routing)

  - [Request Handling](#_request_handling)

  - [Error Handling](#_error_handling)

- [Server Features](#_server_features)

  - [Access Log](#_access_log)

  - [Context](#_context)

- [Supported Technologies](#_supported_technologies)

  - [HTTP/2 Support](#_http2_support)

  - [Static Content Support](#_static_content_support)

  - [Media Types Support](#_media_types_support)

  - [HTTP Content Encoding](#_http_content_encoding)

  - [Proxy Protocol Support](#_proxy_protocol_support)

- [Reference](#_reference)

- [Additional Information](#_additional_information)

## Overview

WebServer provides an API for creating HTTP servers. It uses virtual threads and can handle nearly unlimited concurrent requests.

## Maven Coordinates

To enable WebServer, add the following dependency to your project’s `pom.xml` (see [Managing Dependencies](../../about/managing-dependencies.md)).

``` xml
<dependency>
    <groupId>io.helidon.webserver</groupId>
    <artifactId>helidon-webserver</artifactId>
</dependency>
```

## Configuration

You can configure the WebServer either programmatically or by the Helidon configuration framework.

### Configuring the WebServer in Your Code

The easiest way to configure the WebServer is in your application code.

``` java
WebServer.builder()
        .port(8080)
        .build()
        .start();
```

### Configuring the WebServer in a Configuration File

You can also define the configuration in a file.

*WebServer configuration file `application.yaml`*

``` yaml
server:
  port: 8080
  host: "0.0.0.0"
```

Then, in your application code, load the configuration from that file.

*WebServer initialization using the `application.yaml` file located on the classpath*

``` java
Config config = Config.create(); 
WebServer.builder()
        .config(config.get("server")); 
```

- `application.yaml` is a default configuration source loaded when YAML support is on classpath, so we can just use `Config.create()`

- Server expects the configuration tree located on the node of `server`

### Configuring TLS

Configure TLS either programmatically, or by the Helidon configuration framework.

#### Configuring TLS in Your Code

To configure TLS in WebServer programmatically create your keystore configuration and pass it to the WebServer builder.

``` java
Tls tls = Tls.builder()
        .privateKey(pk -> pk
                .keystore(keys -> keys.keystore(it -> it.resourcePath("private-key.p12"))
                        .passphrase("password".toCharArray())))
        .trust(trust -> trust
                .keystore(keys -> keys.keystore(it -> it.resourcePath("trust.p12"))))
        .build();

WebServer.builder()
        .tls(tls);
```

#### Configuring TLS in the Config File

It is also possible to configure TLS via the config file.

*WebServer TLS configuration file `application.yaml`*

``` yaml
server:
  tls:
    #Truststore setup
    trust:
      keystore:
        passphrase: "password"
        trust-store: true
        resource:
          # load from classpath
          resource-path: "keystore.p12" 
    # Keystore with private key and server certificate
    private-key:
      keystore:
        passphrase: "password"
        resource:
          # load from file system
          path: "/path/to/keystore.p12" 
```

- File loaded from classpath.

- File loaded from file system.

Then, in your application code, load the configuration from that file.

*WebServer initialization using the `application.yaml` file located on the classpath*

``` java
Config config = Config.create(); 
WebServer.builder()
        .config(config.get("server")); 
```

- `application.yaml` is a default configuration source loaded when YAML support is on classpath, so we can just use `Config.create()`

- Server expects the configuration tree located on the node of `server`

Or you can only create WebServerTls instance based on the config file.

*WebServerTls instance based on `application.yaml` file located on the classpath*

``` java
Config config = Config.create();
WebServer.builder()
        .tls(it -> it.config(config.get("server.tls")));
```

This can alternatively be configured with paths to PKCS#8 PEM files rather than KeyStores:

*WebServer TLS configuration file `application.yaml`*

``` yaml
server:
  tls:
    #Truststore setup
    trust:
      pem:
        certificates:
          resource:
            resource-path: "ca-bundle.pem"
    private-key:
      pem:
        key:
          resource:
            resource-path: "key.pem"
        cert-chain:
          resource:
            resource-path: "chain.pem"
```

### Configuration Options

Type: [io.helidon.webserver.WebServer](/apidocs/io.helidon.webserver/io/helidon/webserver/WebServer.html)

This is a standalone configuration type, prefix from configuration root: `server`

#### Configuration options

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
<td style="text-align: left;"><p><code>backlog</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p><code>1024</code></p></td>
<td style="text-align: left;"><p>Accept backlog.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>bind-address</code></p></td>
<td style="text-align: left;"><p>SocketAddress</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>The address to bind to. This is to permit both Internet Address (<code>&lt;host&gt;:&lt;port&gt;</code>) and Unix Domain socket (<code>unix:/path/to/socket</code>). If this is set it will override host(), address() and port().</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>concurrency-limit</code></p></td>
<td style="text-align: left;"><p>io.helidon.common.concurrency.limits.Limit (service provider interface)</p>
<p>Such as:</p>
<ul>
<li><p><a href="../../se/webserver/../../config/io_helidon_common_concurrency_limits_ThroughputLimit.xml">throughput (ThroughputLimit)</a></p></li>
<li><p><a href="../../se/webserver/../../config/io_helidon_common_concurrency_limits_FixedLimit.xml">fixed (FixedLimit)</a></p></li>
<li><p><a href="../../se/webserver/../../config/io_helidon_common_concurrency_limits_AimdLimit.xml">aimd (AimdLimit)</a></p></li>
</ul></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Concurrency limit to use to limit concurrent execution of incoming requests. The default is to have unlimited concurrency.</p>
<p>Note that if maxConcurrentRequests() is configured, this is ignored.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><span class="line-through"><code>connection-config</code></span></p></td>
<td style="text-align: left;"><p><a href="../../se/webserver/../../config/io_helidon_webserver_ConnectionConfig.xml">ConnectionConfig</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p><strong>Deprecated</strong> Configuration of a connection (established from client against our server).</p>
<p>@deprecated use connectionOptions() instead</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>connection-options</code></p></td>
<td style="text-align: left;"><p><a href="../../se/webserver/../../config/io_helidon_common_socket_SocketOptions.xml">SocketOptions</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Options for connections accepted by this listener. This is not used to setup server connection.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>content-encoding</code></p></td>
<td style="text-align: left;"><p><a href="../../se/webserver/../../config/io_helidon_http_encoding_ContentEncodingContext.xml">ContentEncodingContext</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Configure the listener specific io.helidon.http.encoding.ContentEncodingContext. This method discards all previously registered ContentEncodingContext. If no content encoding context is registered, content encoding context of the webserver would be used.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>enable-proxy-protocol</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>false</code></p></td>
<td style="text-align: left;"><p>Enable proxy protocol support for this socket. This protocol is supported by some load balancers/reverse proxies as a means to convey client information that would otherwise be lost. If enabled, the proxy protocol header must be present on every new connection established with your server. For more information, see <a href="https://www.haproxy.org/download/1.8/doc/proxy-protocol.txt"> the specification</a>. Default is <code>false</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>error-handling</code></p></td>
<td style="text-align: left;"><p><a href="../../se/webserver/../../config/io_helidon_webserver_ErrorHandling.xml">ErrorHandling</a></p></td>
<td style="text-align: left;"><p><code>io.helidon.webserver.ListenerConfigBlueprint.create()</code></p></td>
<td style="text-align: left;"><p>Configuration for this listener’s error handling.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>features</code></p></td>
<td style="text-align: left;"><p>io.helidon.webserver.spi.ServerFeature[] (service provider interface)</p>
<p>Such as:</p>
<ul>
<li><p><a href="../../se/webserver/../../config/io_helidon_webserver_accesslog_AccessLogFeature.xml">access-log (AccessLogFeature)</a></p></li>
<li><p><a href="../../se/webserver/../../config/io_helidon_webserver_observe_ObserveFeature.xml">observe (ObserveFeature)</a></p></li>
<li><p><a href="../../se/webserver/../../config/io_helidon_webserver_context_ContextFeature.xml">context (ContextFeature)</a></p></li>
<li><p><a href="../../se/webserver/../../config/io_helidon_openapi_OpenApiFeature.xml">openapi (OpenApiFeature)</a></p></li>
<li><p><a href="../../se/webserver/../../config/io_helidon_webserver_grpc_GrpcReflectionFeature.xml">grpc-reflection (GrpcReflectionFeature)</a></p></li>
<li><p><a href="../../se/webserver/../../config/io_helidon_webserver_cors_CorsFeature.xml">cors (CorsFeature)</a></p></li>
<li><p><a href="../../se/webserver/../../config/io_helidon_webserver_concurrency_limits_LimitsFeature.xml">limits (LimitsFeature)</a></p></li>
<li><p><a href="../../se/webserver/../../config/io_helidon_webserver_staticcontent_StaticContentFeature.xml">static-content (StaticContentFeature)</a></p></li>
<li><p><a href="../../se/webserver/../../config/io_helidon_integrations_eureka_EurekaRegistrationServerFeature.xml">eureka (EurekaRegistrationServerFeature)</a></p></li>
<li><p><a href="../../se/webserver/../../config/io_helidon_webserver_security_SecurityFeature.xml">security (SecurityFeature)</a></p></li>
</ul></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Server features allow customization of the server, listeners, or routings.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>host</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p><code>0.0.0.0</code></p></td>
<td style="text-align: left;"><p>Host of the default socket. Defaults to all host addresses (<code>0.0.0.0</code>).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>idle-connection-period</code></p></td>
<td style="text-align: left;"><p>Duration</p></td>
<td style="text-align: left;"><p><code>PT2M</code></p></td>
<td style="text-align: left;"><p>How often should we check for idleConnectionTimeout(). Defaults to <code>PT2M</code> (2 minutes).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>idle-connection-timeout</code></p></td>
<td style="text-align: left;"><p>Duration</p></td>
<td style="text-align: left;"><p><code>PT5M</code></p></td>
<td style="text-align: left;"><p>How long should we wait before closing a connection that has no traffic on it. Defaults to <code>PT5M</code> (5 minutes). Note that the timestamp is refreshed max. once per second, so this setting would be useless if configured for shorter periods of time (also not a very good support for connection keep alive, if the connections are killed so soon anyway).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ignore-invalid-named-routing</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>If set to <code>true</code>, any named routing configured that does not have an associated named listener will NOT cause an exception to be thrown (default behavior is to throw an exception).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>max-concurrent-requests</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p><code>-1</code></p></td>
<td style="text-align: left;"><p>Limits the number of requests that can be executed at the same time (the number of active virtual threads of requests). Defaults to <code>-1</code>, meaning "unlimited" - what the system allows. Also make sure that this number is higher than the expected time it takes to handle a single request in your application, as otherwise you may stop in-progress requests.</p>
<p>Setting this option will always ignore concurrencyLimit() and will use the io.helidon.common.concurrency.limits.FixedLimit.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>max-in-memory-entity</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p><code>131072</code></p></td>
<td style="text-align: left;"><p>If the entity is expected to be smaller that this number of bytes, it would be buffered in memory to optimize performance when writing it. If bigger, streaming will be used.</p>
<p>Note that for some entity types we cannot use streaming, as they are already fully in memory (String, byte[]), for such cases, this option is ignored.</p>
<p>Default is 128Kb.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>max-payload-size</code></p></td>
<td style="text-align: left;"><p>long</p></td>
<td style="text-align: left;"><p><code>-1</code></p></td>
<td style="text-align: left;"><p>Maximal number of bytes an entity may have. If io.helidon.http.HeaderNames.CONTENT_LENGTH is used, this is checked immediately, if io.helidon.http.HeaderValues.TRANSFER_ENCODING_CHUNKED is used, we will fail when the number of bytes read would exceed the max payload size. Defaults to unlimited (<code>-1</code>).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>max-tcp-connections</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p><code>-1</code></p></td>
<td style="text-align: left;"><p>Limits the number of connections that can be opened at a single point in time. Defaults to <code>-1</code>, meaning "unlimited" - what the system allows.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>media-context</code></p></td>
<td style="text-align: left;"><p><a href="../../se/webserver/../../config/io_helidon_http_media_MediaContext.xml">MediaContext</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Configure the listener specific io.helidon.http.media.MediaContext. This method discards all previously registered MediaContext. If no media context is registered, media context of the webserver would be used.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p><code>@default</code></p></td>
<td style="text-align: left;"><p>Name of this socket. Defaults to <code>@default</code>. Must be defined if more than one socket is needed.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>port</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p><code>0</code></p></td>
<td style="text-align: left;"><p>Port of the default socket. If configured to <code>0</code> (the default), server starts on a random port.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>protocols</code></p></td>
<td style="text-align: left;"><p>io.helidon.webserver.spi.ProtocolConfig[] (service provider interface)</p>
<p>Such as:</p>
<ul>
<li><p><a href="../../se/webserver/../../config/io_helidon_webserver_http2_Http2Config.xml">http_2 (Http2Config)</a></p></li>
<li><p><a href="../../se/webserver/../../config/io_helidon_webserver_websocket_WsConfig.xml">websocket (WsConfig)</a></p></li>
<li><p><a href="../../se/webserver/../../config/io_helidon_webserver_http1_Http1Config.xml">http_1_1 (Http1Config)</a></p></li>
<li><p><a href="../../se/webserver/../../config/io_helidon_webserver_grpc_GrpcConfig.xml">grpc (GrpcConfig)</a></p></li>
</ul></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Configuration of protocols. This may be either protocol selectors, or protocol upgraders from HTTP/1.1. As the order is not important (providers are ordered by weight by default), we can use a configuration as an object, such as:</p>
<pre><code>protocols:
  providers:
    http_1_1:
      max-prologue-length: 8192
    http_2:
      max-frame-size: 4096
    websocket:
      ....</code></pre></td>
</tr>
<tr>
<td style="text-align: left;"><p><span class="line-through"><code>receive-buffer-size</code></span></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p><strong>Deprecated</strong> Listener receive buffer size.</p>
<p>@deprecated use SocketOptions.socketReceiveBufferSize() instead via connectionOptions().</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>requested-uri-discovery</code></p></td>
<td style="text-align: left;"><p><a href="../../se/webserver/../../config/io_helidon_http_RequestedUriDiscoveryContext.xml">RequestedUriDiscoveryContext</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Requested URI discovery context.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>restore-response-headers</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Copy and restore response headers before and after passing a request to Jersey for processing. If Jersey fails to handle the request, and the Webserver continues processing the request, it needs to make sure the original headers are restored. Turn off this flag to avoid the extra overhead of copying headers when no handler executes after Jersey returns.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>shutdown-grace-period</code></p></td>
<td style="text-align: left;"><p>Duration</p></td>
<td style="text-align: left;"><p><code>PT0.5S</code></p></td>
<td style="text-align: left;"><p>Grace period in ISO 8601 duration format to allow running tasks to complete before listener’s shutdown. Default is <code>500</code> milliseconds. Configuration file values example: <code>PT0.5S</code>, <code>PT2S</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>shutdown-hook</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>When true the webserver registers a shutdown hook with the JVM Runtime.</p>
<p>Defaults to true. Set this to false such that a shutdown hook is not registered.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>smart-async-writes</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>false</code></p></td>
<td style="text-align: left;"><p>If enabled and writeQueueLength() is greater than 1, then start with async writes but possibly switch to sync writes if async queue size is always below a certain threshold.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>sockets</code></p></td>
<td style="text-align: left;"><p><a href="../../se/webserver/../../config/io_helidon_webserver_ListenerConfig.xml">Map&lt;string, ListenerConfig&gt;</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Socket configurations. Note that socket named <code>@default</code> cannot be used, configure the values on the server directly.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>tls</code></p></td>
<td style="text-align: left;"><p><a href="../../se/webserver/../../config/io_helidon_common_tls_Tls.xml">Tls</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Listener TLS configuration.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>use-nio</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>If set to <code>true</code>, use NIO socket channel, instead of a socket. Listener will always be a channel.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>write-buffer-size</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p><code>4096</code></p></td>
<td style="text-align: left;"><p>Initial buffer size in bytes of java.io.BufferedOutputStream created internally to write data to a socket connection. Default is <code>4096</code>. Set buffer size to a value less than one to turn off buffering.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>write-queue-length</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p><code>0</code></p></td>
<td style="text-align: left;"><p>Number of buffers queued for write operations.</p></td>
</tr>
</tbody>
</table>

## Routing

Routing lets you use request matching criteria to bind requests to a `handler` that implements your custom business logic. Matching criteria include one or more **HTTP Method(s)** and, optionally, a request **path matcher**.

### Routing Basics

Routing also supports *Error Routing* which binds Java `Throwable` to the handling logic.

Configure HTTP request routing using `HttpRouting.Builder`.

*Using HttpRouting.Builder to specify how HTTP requests are handled*

``` java
WebServer.builder()
        .routing(it -> it
                .get("/hello", (req, res) -> res.send("Hello World!"))) 
        .build(); 
```

- Handle all GETs to `/hello` path. Send the `Hello World!` string.

- Create a server instance with the provided routing

### HTTP Method Routing

`HttpRouting.Builder` lets you specify how to handle each HTTP method. For example:

| HTTP Method | HttpRouting.Builder example |
|----|----|
| **GET** | `.get(handler)` |
| **PUT** | `.put(handler)` |
| **POST** | `.post(handler)` |
| **HEAD** | `.head(handler)` |
| **DELETE** | `.delete(handler)` |
| **TRACE** | `.trace(handler)` |
| **OPTIONS** | `.options(handler)` |
| *any method* | `.any(handler)` |
| *multiple methods* | `.route(Method.predicate(Method.GET, Method.POST), path, handler)` |
| *custom method* | `.route(Method.create("CUSTOM"), handler)` |

### Path Matcher Routing

You can combine HTTP method routing with request path matching.

``` java
routing.post("/some/path", (req, res) -> { /* handler */ });
```

You can use **path pattern** instead of *path* with the following syntax:

- `/foo/bar/baz` - Exact path match against resolved path even with non-usual characters

- `/foo/*` - convenience method to match `/foo` or any subpath (but not `/foobar`)

- `/foo/{}/baz` - `{}` Unnamed regular expression segment `([^/]+)`

- `/foo/{var}/baz` - Named regular expression segment `([^/]+)`

- `/foo/{var:\d+}` - Named regular expression segment with a specified expression

- `/foo/{:\d+}` - Unnamed regular expression segment with a specified expression

- `/foo/{+var}` - Convenience shortcut for `{var:.+}`

- `/foo/{+}` - Convenience shortcut for unnamed segment with regular expression `{:.+}`

- `/foo/{*}` - Convenience shortcut for unnamed segment with regular expression `{:.*}`

- `/foo[/bar]` - An optional block, which translates to the `/foo(/bar)?` regular expression

- `/*` or `/foo*` - `*` Wildcard character can be matched with any number of characters.

> [!IMPORTANT]
> Path (matcher) routing is **exact**. For example, a `/foo/bar` request is **not** routed to `.post('/foo', …​)`.

> [!TIP]
> Always start *path* and *path patterns* with the `/` character.

For more precise setup of path, you can use factory methods on `io.helidon.http.PathMatchers` and register using `HttpRouting.Builder.route(Predicate<Method>, PathMatcher, Handler)` method.

### Using full `HttpRoute`

To have more control over selecting which requests should be handled by a specific route, you can use the `io.helidon.webserver.http.HttpRoute` interface using its `Builder`.

``` java
routing.route(HttpRoute.builder()
                      .path("/hello")
                      .methods(Method.POST, Method.PUT) 
                      .handler((req, res) -> {
                          String requestEntity = req.content().as(String.class);
                          res.send(requestEntity); 
                      }));
```

- The route is specified for `GET` and `POST` requests

- The handler consumes the request payload and echoes it back

### Organizing Code into Services

By implementing the `io.helidon.webserver.http.HttpService` interface you can organize your code into one or more services, each with its own path prefix and set of handlers.

*Use `HttpRouting.Builder.register` to register your service*

``` java
routing.register("/hello", new HelloService());
```

*Service implementation*

``` java
class HelloService implements HttpService {
    @Override
    public void routing(HttpRules rules) {
        rules.get("/subpath", (req, res) -> {
            // Some logic
        });
    }
}
```

In this example, the `GET` handler matches requests to `/hello/subpath`.

### Server Lifecycle

In Helidon 4 your `HttpService` can interpose on the server lifecycle by overriding the `beforeStart` and `afterStop` methods:

*Helidon 4.x server lifecycle*

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

### Using `HttpFeature`

By implementing the `io.helidon.webserver.http.HttpFeature` interface, you can organize multiple routes and/or filters into a feature, that will be setup according to its defined `io.helidon.common.Weight` (or using `io.helidon.common.Weighted`).

Each service has access to the routing builder. HTTP Features are configured for each routing builder. If there is a need to configure a feature for multiple sockets, you can use [Server Feature](#_server_features) instead.

## Request Handling

Implement the logic to handle requests to WebServer in a `Handler`, which is a `FunctionalInterface`. Handlers:

- Process the request and [send](#anchor-sending-response) a response.

- Act as a filter and forward requests to downstream handlers using the `response.next()` method.

- Throw an exception to begin [error handling](#_error_handling).

### Process Request and Produce Response

Each `Handler` has two parameters. `ServerRequest` and `ServerResponse`.

- Request provides access to the request method, URI, path, query parameters, headers and entity.

- Response provides an ability to set response code, headers, and entity.

### Filtering

Filtering can be done either using a dedicated `Filter`, or through routes.

#### Filter

You can register a `io.helidon.webserver.http.Filter` with HTTP routing to handle filtering in interception style.

A simple filter example:

``` java
routing.addFilter((chain, req, res) -> {
    try {
        chain.proceed();
    } finally {
        // do something for any finished request
    }
});
```

#### Routes

The handler forwards the request to the downstream handlers by *nexting*. There are two options:

- call `res.next()`

  ``` java
  rules.any("/hello", (req, res) -> { 
      // filtering logic  
      res.next(); 
  });
  ```

  - handler for any HTTP method using the `/hello` path

  - business logic implementation

  - forward the current request to the downstream handler

- throw an exception to forward to [error handling](#_error_handling)

  ``` java
  rules.any("/hello", (req, res) -> { 
      // filtering logic (e.g., validating parameters) 
      if (userParametersOk()) {
          res.next(); 
      } else {
          throw new IllegalArgumentException("Invalid parameters."); 
      }
  });
  ```

  - handler for any HTTP method using the `/hello` path

  - custom logic

  - forward the current request to the downstream handler

  - forward the request to the error handler

### Sending a Response

To complete the request handling, you must send a response by calling the `res.send()` method.

> [!IMPORTANT]
> one of the variants of `send` method MUST be invoked in the same thread the request is started in; as we run in Virtual Threads, you can simply wait for any asynchronous tasks that must complete before sending a response

``` java
rules.get("/hello", (req, res) -> { 
    // terminating logic
    res.status(Status.ACCEPTED_202)
            .send("Saved!"); 
});
```

- handler that terminates the request handling for any HTTP method using the `/hello` path

- send the response

## Protocol-Specific Routing

Handling routes based on the protocol version is possible by registering specific routes on routing builder.

*Routing based on HTTP version*

``` java
rules.get("/any-version", (req, res) -> res.send("HTTP Version " + req.prologue().protocolVersion())) 
        .route(Http1Route.route(Method.GET, "/version-specific", (req, res) -> res.send("HTTP/1.1 route"))) 
        .route(Http2Route.route(Method.GET, "/version-specific", (req, res) -> res.send("HTTP/2 route"))); 
```

- An HTTP route registered on `/any-version` path that prints the version of HTTP protocol

- An HTTP/1.1 route registered on `/version-specific` path

- An HTTP/2 route registered on `/version-specific` path

While `Http1Route` for Http/1 is always available with Helidon webserver, other routes like `Http2Route` for [HTTP/2](#_http2_support) needs to be added as additional dependency.

## Requested URI Discovery

Proxies and reverse proxies between an HTTP client and your Helidon application mask important information (for example `Host` header, originating IP address, protocol) about the request the client sent. Fortunately, many of these intermediary network nodes set or update either the [standard HTTP `Forwarded` header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Forwarded) or the [non-standard `X-Forwarded-*` family of headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-For) to preserve information about the original client request.

Helidon’s requested URI discovery feature allows your application—​and Helidon itself—​to reconstruct information about the original request using the `Forwarded` header and the `X-Forwarded-*` family of headers.

When you prepare the connections in your server you can include the following optional requested URI discovery settings:

- enabled or disabled

- which type or types of requested URI discovery to use:

  - `FORWARDED` - uses the `Forwarded` header

  - `X_FORWARDED` - uses the `X-Forwarded-*` headers

  - `HOST` - uses the `Host` header

- what intermediate nodes to trust

When your application invokes `request.requestedUri()` Helidon iterates through the discovery types you set up for the receiving connection, gathering information from the corresponding header(s) for that type. If the request does not have the corresponding header(s), or your settings do not trust the intermediate nodes reflected in those headers, then Helidon tries the next discovery type you set up. Helidon uses the `HOST` discovery type if you do not set up discovery yourself or if, for a particular request, it cannot assemble the request information using any discovery type you did set up for the socket.

### Setting Up Requested URI Discovery Programmatically

To set up requested URI discovery on the default socket for your server, use the [`WebServerConfig.Builder`](/apidocs/io.helidon.webserver/io/helidon/webserver/WebServerConfig.Builder.html):

*Requested URI set-up for the default server socket*

``` java
import io.helidon.common.configurable.AllowList;
import jakarta.json.Json;
import jakarta.json.JsonBuilderFactory;
import jakarta.json.JsonObject;

import static io.helidon.http.RequestedUriDiscoveryContext.RequestedUriDiscoveryType.FORWARDED;
import static io.helidon.http.RequestedUriDiscoveryContext.RequestedUriDiscoveryType.X_FORWARDED;

AllowList trustedProxies = AllowList.builder()
        .addAllowedPattern(Pattern.compile("lb.+\\.mycorp\\.com"))
        .addDenied("lbtest.mycorp.com")
        .build(); 

WebServer.builder()
        .requestedUriDiscoveryContext(it -> it
                .addDiscoveryType(FORWARDED) 
                .addDiscoveryType(X_FORWARDED)
                .trustedProxies(trustedProxies)); 
```

- Create the `AllowList` describing the intermediate networks nodes to trust and not trust. Presumably the `lbxxx.mycorp.com` nodes are trusted load balancers except for the test load balancer `lbtest`, and no other nodes are trusted. `AllowList` accepts prefixes, suffixes, predicates, regex patterns, and exact matches. See the [`AllowList`](/apidocs/io.helidon.common.configurable/io/helidon/common/configurable/AllowList.html) JavaDoc for complete information.

- Use `Forwarded` first, then try `X-Forwarded-*` on each request.

- Set the `AllowList` for trusted intermediaries.

If you build your server with additional sockets, you can control requested URI discovery separately for each.

### Setting Up Requested URI Discovery using Configuration

You can also use configuration to set up the requested URI discovery behavior. The following example replicates the settings assigned programmatically in the earlier code example:

*Configuring requested URI behavior*

``` yaml
server:
  port: 0
  requested-uri-discovery:
    types: FORWARDED,X_FORWARDED
    trusted-proxies:
      allow:
        pattern: "lb.*\\.mycorp\\.com"
      deny:
        exact: "lbtest.mycorp.com""
```

### Obtaining the Requested URI Information

Your code obtains the requested URI information from the Helidon server request object:

*Retrieving Requested URI Information*

``` java
import io.helidon.common.tls.Tls;
import io.helidon.common.uri.UriInfo;

rules.get((req, res) -> {
    UriInfo uriInfo = req.requestedUri();
    // ...
});
```

See the [`UriInfo`](/apidocs/io.helidon.common.uri/io/helidon/common/uri/UriInfo.html) JavaDoc for more information.

## Error Handling

### Error Routing

You may register an error handler for a specific `Throwable` in a `HttpRouting.Builder` method.

``` java
routing.error(MyException.class, (req, res, ex) -> { 
    // handle the error, set the HTTP status code
    res.send(errorDescriptionObject); 
});
```

- Registers an error handler that handles `MyException` that are thrown from the upstream handlers

- Finishes the request handling by sending a response

Error handlers are called when

- an exception is thrown from a handler

As with the standard handlers, the error handler must either

- send a response

  ``` java
  routing.error(MyException.class, (req, res, ex) -> {
      res.status(Status.BAD_REQUEST_400);
      res.send("Unable to parse request. Message: " + ex.getMessage());
  });
  ```

- or throw an exception

  ``` java
  routing.error(MyException.class, (req, res, ex) -> {
      // some logic
      throw ex;
  });
  ```

Exceptions thrown from error handlers are not error handled, and will end up in an `InternalServerError`.

### Default Error Handling

If no user-defined error handler is matched, or if the error handler of the exception threw an exception, then the exception is translated to an HTTP response as follows:

- Subtypes of `HttpException` are translated to their associated HTTP error codes.

  *Reply with the `406` HTTP error code by throwing an exception*

``` java
  rules.get((req, res) -> {
      throw new HttpException(
              "Amount of money must be greater than 0.",
              Status.NOT_ACCEPTABLE_406); 
  });
  ```

- Otherwise, the exceptions are translated to an Internal Server Error HTTP error code `500`.

## Direct Error Handling

There are a number of scenarios where errors can be detected before the request routing phase is initiated, some of these include: error validating requests (e.g. a bad URI), CORS rejections, invalid payloads, unsupported HTTP versions, etc. For all these type of events, Helidon provides the so-called *direct handlers*. The complete list of events that are handled in this way is defined by the enum [EventType](/apidocs/io.helidon.http/io/helidon/http/DirectHandler.EventType.html).

Direct handlers can be configured independently for each port exposed by the Webserver; similar to other config, if configured directly on the Webserver they will only apply to the default port. For more information see [directHandlers](/apidocs/io.helidon.webserver/io/helidon/webserver/ListenerConfig.BuilderBase.html#directHandlers(io.helidon.webserver.http.DirectHandlers)) method in `ListenerConfig`.

The following example shows how to register a custom handler for a request that is deemed invalid before the routing phase stars. The custom handler in this example simply returns a status code of 400 and a message that references the server log.

*Register a direct handler for bad requests in the Webserver*

``` java
public static void main(String[] args) {
    WebServer server = WebServer.builder()
            .directHandlers(DirectHandlers.builder()
                    .addHandler(EventType.BAD_REQUEST, new MyDirectHandler())
                    .build())
            .build()
            .start();
}

static class MyDirectHandler implements DirectHandler {

    @Override
    public TransportResponse handle(TransportRequest transportRequest,
                                    EventType eventType,
                                    Status status,
                                    ServerResponseHeaders serverResponseHeaders,
                                    String s) {
        return DirectHandler.TransportResponse.builder()
                .status(Status.BAD_REQUEST_400)
                .entity("Bad request, see server log")
                .build();
    }
}
```

### Default Direct Error Handler

Helidon includes a *default* direct handler that offers basic support for all these events out of the box. This default handler supports a couple of config properties that control logging and error reporting: these are `includeEntity` and `logAllMessages`. The former controls how data reflection from the request is handled, while the latter controls logging of potentially sensitive information. Both of these flags are set to `false` by default to prevent any data leak either in the response or in the server log.

The default direct handler’s settings in the Webserver can be controlled via config:

*Configuring error handling on default port*

``` yaml
server:
  error-handling:
    include-entity: true
    log-all-messages: true
```

With these settings, the default error handler—​on the default Webserver port—​will log all messages and may include reflected user data in error response entities.

Note: Even though some request data can be reflected back in responses when `include-entity` is set to `true`, Helidon will always ensure that it is properly encoded to prevent common HTML attacks.

Any other port defined in your application may include an `error-handling` section to configure the default handler behavior on that port.

## Configuration Options

Type: [io.helidon.common.tls.Tls](/apidocs/io.helidon.common.tls/io/helidon/common/tls/Tls.html)

### Configuration options

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
<td style="text-align: left;"><p><code>cipher-suite</code></p></td>
<td style="text-align: left;"><p>string[]</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Enabled cipher suites for TLS communication.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>client-auth</code></p></td>
<td style="text-align: left;"><p>TlsClientAuth (REQUIRED, OPTIONAL, NONE)</p></td>
<td style="text-align: left;"><p><code>TlsClientAuth.NONE</code></p></td>
<td style="text-align: left;"><p>Configure requirement for mutual TLS.</p>
<p>Allowed values:</p>
<ul>
<li><p><code>REQUIRED</code>: Mutual TLS is required. Server MUST present a certificate trusted by the client, client MUST present a certificate trusted by the server. This implies private key and trust configuration for both server and client.</p></li>
<li><p><code>OPTIONAL</code>: Mutual TLS is optional. Server MUST present a certificate trusted by the client, client MAY present a certificate trusted by the server. This implies private key configuration at least for server, trust configuration for at least client.</p></li>
<li><p><code>NONE</code>: Mutual TLS is disabled. Server MUST present a certificate trusted by the client, client does not present a certificate. This implies private key configuration for server, trust configuration for client.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>enabled</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Flag indicating whether Tls is enabled.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>endpoint-identification-algorithm</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p><code>HTTPS</code></p></td>
<td style="text-align: left;"><p>Identification algorithm for SSL endpoints.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>internal-keystore-provider</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Provider of the key stores used internally to create a key and trust manager factories.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>internal-keystore-type</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Type of the key stores used internally to create a key and trust manager factories.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>key-manager-factory-algorithm</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Algorithm of the key manager factory used when private key is defined. Defaults to javax.net.ssl.KeyManagerFactory.getDefaultAlgorithm().</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>manager</code></p></td>
<td style="text-align: left;"><p>io.helidon.common.tls.TlsManager (service provider interface)</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>The Tls manager. If one is not explicitly defined in the config then a default manager will be created.</p>
<p>See ConfiguredTlsManager</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>private-key</code></p></td>
<td style="text-align: left;"><p>PrivateKey</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Private key to use. For server side TLS, this is required. For client side TLS, this is optional (used when mutual TLS is enabled).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>protocol</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p><code>TLS</code></p></td>
<td style="text-align: left;"><p>Configure the protocol used to obtain an instance of javax.net.ssl.SSLContext.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>protocols</code></p></td>
<td style="text-align: left;"><p>string[]</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Enabled protocols for TLS communication. Example of valid values for <code>TLS</code> protocol: <code>TLSv1.3</code>, <code>TLSv1.2</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>provider</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Use explicit provider to obtain an instance of javax.net.ssl.SSLContext.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>revocation</code></p></td>
<td style="text-align: left;"><p><a href="../../se/webserver/../../config/io_helidon_common_tls_RevocationConfig.xml">RevocationConfig</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Certificate revocation check configuration.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>secure-random-algorithm</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Algorithm to use when creating a new secure random.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>secure-random-provider</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Provider to use when creating a new secure random. When defined, secureRandomAlgorithm() must be defined as well.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>session-cache-size</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p><code>20480</code></p></td>
<td style="text-align: left;"><p>SSL session cache size.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>session-timeout</code></p></td>
<td style="text-align: left;"><p>Duration</p></td>
<td style="text-align: left;"><p><code>PT24H</code></p></td>
<td style="text-align: left;"><p>SSL session timeout.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>trust</code></p></td>
<td style="text-align: left;"><p>X509Certificate[]</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>List of certificates that form the trust manager.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>trust-all</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>false</code></p></td>
<td style="text-align: left;"><p>Trust any certificate provided by the other side of communication.</p>
<p><strong>This is a dangerous setting:</strong> if set to <code>true</code>, any certificate will be accepted, throwing away most of the security advantages of TLS. <strong>NEVER</strong> do this in production.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>trust-manager-factory-algorithm</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Trust manager factory algorithm.</p></td>
</tr>
</tbody>
</table>

# Server Features

Server features provide additional functionality to the WebServer, through modification of the server configuration, listener configuration, or routing.

A server feature can be added by implementing `io.helidon.webserver.spi.ServerFeature`. Server features support automated discovery, as long as the implementation is available through Java `ServiceLoader`. Server features can also be added through configuration, as can be seen above in [Configuration Options](#_configuration_options), configuration key `features`.

All features (both `ServerFeature` and [HttpFeature](#anchor-http-feature)) honor weight of the feature (defined either through `@Weight` annotation, or by implementing `Weighted` interface) when registering routes, `HttpService`, or `Filter` to the routing.

The following table shows available server features and their weight. The highest weight is always registered (and invoked) first.

| Feature | Weight |
|----|----|
| [Context](#_context) | 1100 |
| [Access Log](#_access_log) | 1000 |
| [Tracing](../../se/tracing.md) | 900 |
| [CORS](../../se/cors.md) | 850 |
| [Security](../../se/security/introduction.md) | 800 |
| Routing (all handlers and filters) | 100 |
| [OpenAPI](../../se/openapi/openapi.md) | 90 |
| [Observability](../../se/observability.md) | 80 |

## Context

Context feature adds a filter that executes all requests within the context of `io.helidon.common.context.Context`. A `Context` instance is available on `ServerRequest` even if this feature is not added. This feature adds support for obtaining request context through `io.helidon.common.context.Contexts.context()`.

This feature will provide the same behavior as previous versions of Helidon. Since Helidon 4.0.0, this feature is not automatically added.

To enable execution of routes within Context, add the following dependency to project’s `pom.xml`:

``` xml
<dependency>
    <groupId>io.helidon.webserver</groupId>
    <artifactId>helidon-webserver-context</artifactId>
</dependency>
```

Context feature can be configured, all options shown below are also available both in config, and programmatically when using builder.

# ContextFeature (webserver.context) Configuration

Type: [io.helidon.webserver.context.ContextFeature](/apidocs/io.helidon.webserver.context/io/helidon/webserver/context/ContextFeature.html)

*Config key*

``` text
context
```

This type provides the following service implementations:

- `io.helidon.webserver.spi.ServerFeatureProvider`

## Configuration options

| key | type | default value | description |
|----|----|----|----|
| `records` | [ContextRecordConfig\[\]](../../se/webserver/../../config/io_helidon_common_context_http_ContextRecordConfig.md) |   | List of propagation records. |
| `sockets` | string\[\] |   | List of sockets to register this feature on. If empty, it would get registered on all sockets. |
| `weight` | double | `1100.0` | Weight of the context feature. As it is used by other features, the default is quite high: `1100.0`. |

Optional configuration options

## Access Log

Access logging in Helidon is done by a dedicated module that can be added to WebServer and configured.

Access logging is a Helidon WebServer `ServerFeature`. Access Log feature has a very high weight, so it is registered before other features (such as security) that may terminate a request. This is to ensure the log contains all requests with appropriate status codes.

To enable Access logging add the following dependency to project’s `pom.xml`:

``` xml
<dependency>
    <groupId>io.helidon.webserver</groupId>
    <artifactId>helidon-webserver-access-log</artifactId>
</dependency>
```

### Configuring Access Log in Your Code

`AccessLogFeature` is discovered automatically by default, and configured through `server.features.access-log`. You can also configure this feature in code by registering it with WebServer (which will replace the discovered feature).

``` java
WebServer.builder()
        .addFeature(AccessLogFeature.builder()
                            .commonLogFormat()
                            .build());
```

### Configuring Access Log in a Configuration File

Access log can be configured as follows:

*Access Log configuration file*

``` yaml
server:
  port: 8080
  features:
    access-log:
      format: "%h %l %u %t %r %s %b %{Referer}i"
```

All options shown below are also available programmatically when using builder.

# AccessLogFeature (webserver.accesslog) Configuration

Type: [io.helidon.webserver.accesslog.AccessLogFeature](/apidocs/io.helidon.webserver.accesslog/io/helidon/webserver/accesslog/AccessLogFeature.html)

*Config key*

``` text
access-log
```

This type provides the following service implementations:

- `io.helidon.webserver.spi.ServerFeatureProvider`

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
<td style="text-align: left;"><p><code>enabled</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Whether this feature will be enabled.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>format</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>The format for log entries (similar to the Apache <code>LogFormat</code>).</p>
<table class="config">
<caption>Log format elements</caption>
<tbody>
<tr>
<td>%h</td>
<td>IP address of the remote host</td>
<td>HostLogEntry</td>
</tr>
<tr>
<td>%l</td>
<td>The client identity. This is always undefined in Helidon.</td>
<td>UserIdLogEntry</td>
</tr>
<tr>
<td>%u</td>
<td>User ID as asserted by Helidon Security.</td>
<td>UserLogEntry</td>
</tr>
<tr>
<td>%t</td>
<td>The timestamp</td>
<td>TimestampLogEntry</td>
</tr>
<tr>
<td>%r</td>
<td>The request line (`"GET /favicon.ico HTTP/1.0"`)</td>
<td>RequestLineLogEntry</td>
</tr>
<tr>
<td>%s</td>
<td>The status code returned to the client</td>
<td>StatusLogEntry</td>
</tr>
<tr>
<td>%b</td>
<td>The entity size in bytes</td>
<td>SizeLogEntry</td>
</tr>
<tr>
<td>%D</td>
<td>The time taken in microseconds (start of request until last byte written)</td>
<td>TimeTakenLogEntry</td>
</tr>
<tr>
<td>%T</td>
<td>The time taken in seconds (start of request until last byte written), integer</td>
<td>TimeTakenLogEntry</td>
</tr>
<tr>
<td>%{header-name}i</td>
<td>Value of header `header-name`</td>
<td>HeaderLogEntry</td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>logger-name</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p><code>io.helidon.webserver.AccessLog</code></p></td>
<td style="text-align: left;"><p>Name of the logger used to obtain access log logger from System.getLogger(String). Defaults to <code>io.helidon.webserver.AccessLog</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>sockets</code></p></td>
<td style="text-align: left;"><p>string[]</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>List of sockets to register this feature on. If empty, it would get registered on all sockets. The logger used will have the expected logger with a suffix of the socket name.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>weight</code></p></td>
<td style="text-align: left;"><p>double</p></td>
<td style="text-align: left;"><p><code>1000.0</code></p></td>
<td style="text-align: left;"><p>Weight of the access log feature. We need to log access for anything happening on the server, so weight is high: <code>1000.0</code>.</p></td>
</tr>
</tbody>
</table>

# Supported Technologies

# HTTP/2 Support

Helidon supports HTTP/2 upgrade from HTTP/1, HTTP/2 without prior knowledge, HTTP/2 with prior knowledge, and HTTP/2 with ALPN over TLS. HTTP/2 support is enabled in WebServer by default when it’s artifact is available on classpath.

> [!WARNING]
> For HTTP/2 `request.content().hasEntity()` returns `true` by default. It returns `false` only if the request’s header frame includes the `END_STREAM` flag or the `Content‑Length` header is present with a value of `0`.

## Maven Coordinates

To enable HTTP/2 support add the following dependency to your project’s `pom.xml`.

``` xml
<dependency>
    <groupId>io.helidon.webserver</groupId>
    <artifactId>helidon-webserver-http2</artifactId>
</dependency>
```

# Static Content Support

Static content is served through a `StaticContentFeature`. As with other server features, it can be configured through config, or registered with server config builder.

Static content supports serving of files from classpath, or from any readable directory on the file system. Each content handler must include a location, and can provide a context that will be registered with the WebServer (defaults to `/`).

## Maven Coordinates

To enable Static Content Support add the following dependency to your project’s `pom.xml`.

``` xml
<dependency>
    <groupId>io.helidon.webserver</groupId>
    <artifactId>helidon-webserver-static-content</artifactId>
</dependency>
```

## Registering Static Content

To register static content based on a file system (`/pictures`), and classpath (`/`):

*server feature using `WebServerConfig.Builder`*

``` java
builder.addFeature(StaticContentFeature.builder() 
                           .addPath(p -> p.location(Paths.get("/some/WEB/pics")) 
                                   .context("/pictures")) 
                           .addClasspath(cl -> cl.location("/static-content") 
                                   .welcome("index.html") 
                                   .context("/")) 
                           .build());
```

- Create a new `StaticContentFeature` to register with the web server (will be served on all sockets by default)

- Add path location served from `/some/WEB/pics` absolute path

- Associate the path location with server context `/pictures`

- Add classpath location to serve resources from the contextual `ClassLoader` from location `/static-content`

- `index.html` is the file that is returned if a directory is requested

- serve the classpath content on root context `/`

Static content can also be registered using the configuration of server feature.

If you use `Config` with your webserver setup, you can register the same static content using configuration:

*application.yaml*

``` yaml
server:
  features:
    static-content:
      path:
        - context: "/pictures"
          location: "/some/WEB/pics"
      classpath:
        - context: "/"
          welcome: "index.html"
          location: "/static-content"
```

See [Static Content Feature Configuration Reference](../../config/io_helidon_webserver_staticcontent_StaticContentFeature.md) for details of configuration options.

# Media types support

WebServer and WebClient share the HTTP media support of Helidon, and any supported media type can be used in both. The media type support is automatically discovered from classpath. Programmatic support is of course enabled as well through `MediaContext`.

Customized media support for WebServer

``` java
WebServer.builder()
        .mediaContext(it -> it
                .mediaSupportsDiscoverServices(false)
                .addMediaSupport(JsonpSupport.create())
                .build());
```

Each registered (or discovered) media support adds support for writing and reading entities of a specific type.

The following table lists JSON media supports:

| Media type | TypeName | Maven groupId:artifactId | Supported Java type(s) |
|----|----|----|----|
| **[JSON-P](#_json_p_support)** | JsonpSupport | `io.helidon.http.media:helidon-http-media-jsonp` | `JsonObject, JsonArray` |
| **[JSON-B](#_json_b_support)** | JsonbSupport | `io.helidon.http.media:helidon-http-media-jsonb` | Any \* |
| **[Jackson](#_jackson_support)** | JacksonSupport | `io.helidon.http.media:helidon-http-media-jackson` | Any \* |
| **[Gson](#_gson_support)** | GsonSupport | `io.helidon.http.media:helidon-http-media-gson` | Any \* |

- JSON-B and Jackson have lower weight, so they are used only when no other media type matched the object being written or read

## JSON-P Support

The WebServer supports JSON-P. When enabled, you can send and receive JSON-P objects transparently.

### Maven Coordinates

To enable JSON Support add the following dependency to your project’s `pom.xml`.

``` xml
<dependency>
    <groupId>io.helidon.http.media</groupId>
    <artifactId>helidon-http-media-jsonp</artifactId>
</dependency>
```

### Usage

*Handler that receives and returns JSON objects*

``` java
static final JsonBuilderFactory JSON_FACTORY = Json.createBuilderFactory(Map.of()); 

rules.post("/hello", (req, res) -> {
    JsonObject requestEntity = req.content().as(JsonObject.class); 
    JsonObject responseEntity = JSON_FACTORY.createObjectBuilder() 
            .add("message", "Hello " + requestEntity.getString("name"))
            .build();
    res.send(responseEntity); 
});
```

- Using a `JsonBuilderFactory` is more efficient than `Json.createObjectBuilder()`

- Get the request entity as `JsonObject`

- Create a new `JsonObject` for the response entity

- Send `JsonObject` in response

*Example of posting JSON to sayHello endpoint*

``` bash
curl --noproxy '*' -X POST -H "Content-Type: application/json" \
    http://localhost:8080/sayhello -d '{"name":"Joe"}'
```

*Response body*

``` json
{"message":"Hello Joe"}
```

## JSON-B Support

The WebServer supports the [JSON-B specification](http://json-b.net/). When this support is enabled, Java objects will be serialized to and deserialized from JSON automatically using [Yasson](https://github.com/eclipse-ee4j/yasson), an implementation of the [JSON-B specification](https://jakarta.ee/specifications/jsonb/3.0/jakarta-jsonb-spec-3.0.html).

### Maven Coordinates

To enable JSON-B Support add the following dependency to your project’s `pom.xml`.

``` xml
<dependency>
    <groupId>io.helidon.http.media</groupId>
    <artifactId>helidon-http-media-jsonb</artifactId>
</dependency>
```

### Configuration

It is possible to configure the Jsonb instance via programmatic or configuration-based approach. When configured over the configuration, all the configured value types need to be selected correctly according to the JSON-B spec and placed to the right section.

Type: [io.helidon.http.media.jsonb.JsonbSupport](/apidocs/io.helidon.http.media.jsonb/io/helidon/http/media/jsonb/JsonbSupport.html)

*Config key*

``` text
jsonb
```

This type provides the following service implementations:

- `io.helidon.http.media.spi.MediaSupportProvider`

#### Configuration options

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
<td style="text-align: left;"><p><code>accepted-media-types</code></p></td>
<td style="text-align: left;"><p>MediaType[]</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Types accepted by this media support. When server processes the response, it checks the <code>Accept</code> header, to choose the right media support, if there are more supports available for the provided entity object.</p>
<p>NOTE Make sure that you accept the type returned by contentType().</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>boolean-properties</code></p></td>
<td style="text-align: left;"><p>Map&lt;string, boolean&gt;</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Jsonb <code>boolean</code> configuration properties. Properties are being ignored if specific Jsonb is set.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>class-properties</code></p></td>
<td style="text-align: left;"><p>Map&lt;string, Class&gt;</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Jsonb Class configuration properties. Properties are being ignored if specific Jsonb is set.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>content-type</code></p></td>
<td style="text-align: left;"><p>HttpMediaType</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Content type to use if not configured (in response headers for server, and in request headers for client).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Name of the support. Each extension should provide its own default. This is to enable multiple instance of the same type.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>properties</code></p></td>
<td style="text-align: left;"><p>Map&lt;string, string&gt;</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Jsonb String configuration properties. Properties are being ignored if specific Jsonb is set.</p></td>
</tr>
</tbody>
</table>

#### Example

*Example JSON-B configuration*

``` yaml
jsonb:
  boolean-properties:
    jsonb.null-values: true
  properties:
    jsonb.property-naming-strategy: "LOWER_CASE_WITH_DASHES"
```

### Usage

Now that automatic JSON serialization and deserialization facilities have been set up, you can register a `Handler` that works with Java objects instead of raw JSON. Deserialization from and serialization to JSON will be handled according to the [JSON-B specification](https://jcp.org/en/jsr/detail?id=367).

Suppose you have a `Person` class that looks like this:

*Hypothetical `Person` class*

``` java
public class Person {

    private String name;

    public Person() {
        super();
    }

    public String getName() {
        return this.name;
    }

    public void setName(String name) {
        this.name = name;
    }
}
```

Then you can set up a `Handler` like this:

*A `Handler` that works with Java objects instead of raw JSON*

``` java
rules.post("/echo", (req, res) -> {
    res.send(req.content().as(Person.class)); 
});
```

- This handler consumes a `Person` instance and simply echoes it back. Note that there is not working with raw JSON here.

*Example of posting JSON to the `/echo` endpoint*

``` bash
curl --noproxy '*' -X POST -H "Content-Type: application/json" \
    http://localhost:8080/echo -d '{"name":"Joe"}'
{"name":"Joe"}
```

## Jackson Support

The WebServer supports [Jackson](https://github.com/FasterXML/jackson#jackson-project-home-github). When this support is enabled, Java objects will be serialized to and deserialized from JSON automatically using Jackson.

### Maven Coordinates

To enable Jackson Support add the following dependency to your project’s `pom.xml`.

``` xml
<dependency>
    <groupId>io.helidon.http.media</groupId>
    <artifactId>helidon-http-media-jackson</artifactId>
</dependency>
```

### Configuration

It is possible to configure the Jackson ObjectMapper instance via programmatic or configuration-based approach.

Type: [io.helidon.http.media.jackson.JacksonSupport](/apidocs/io.helidon.http.media.jackson/io/helidon/http/media/jackson/JacksonSupport.html)

*Config key*

``` text
jackson
```

This type provides the following service implementations:

- `io.helidon.http.media.spi.MediaSupportProvider`

#### Configuration options

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
<td style="text-align: left;"><p><code>accepted-media-types</code></p></td>
<td style="text-align: left;"><p>MediaType[]</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Types accepted by this media support. When server processes the response, it checks the <code>Accept</code> header, to choose the right media support, if there are more supports available for the provided entity object.</p>
<p>NOTE Make sure that you accept the type returned by contentType().</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>content-type</code></p></td>
<td style="text-align: left;"><p>HttpMediaType</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Content type to use if not configured (in response headers for server, and in request headers for client).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Name of the support. Each extension should provide its own default. This is to enable multiple instance of the same type.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>properties</code></p></td>
<td style="text-align: left;"><p>Map&lt;string, boolean&gt;</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Jackson configuration properties. Properties are being ignored if specific JacksonSupport is set. Only <code>boolean</code> configuration values are supported.</p></td>
</tr>
</tbody>
</table>

#### Example

*Example Jackson configuration*

``` yaml
jackson:
  properties:
    FAIL_ON_UNKNOWN_PROPERTIES: false
```

### Usage

Now that automatic JSON serialization and deserialization facilities have been set up, you can register a `Handler` that works with Java objects instead of raw JSON. Deserialization from and serialization to JSON will be handled by [Jackson](https://github.com/FasterXML/jackson#jackson-project-home-github).

Suppose you have a `Person` class that looks like this:

*Hypothetical `Person` class*

``` java
public class Person {

    private String name;

    public Person() {
        super();
    }

    public String getName() {
        return this.name;
    }

    public void setName(String name) {
        this.name = name;
    }
}
```

Then you can set up a `Handler` like this:

*A `Handler` that works with Java objects instead of raw JSON*

``` java
rules.post("/echo", (req, res) -> {
    res.send(req.content().as(Person.class)); 
});
```

- This handler consumes a `Person` instance and simply echoes it back. Note that there is no working with raw JSON here.

*Example of posting JSON to the `/echo` endpoint*

``` bash
curl --noproxy '*' -X POST -H "Content-Type: application/json" \
    http://localhost:8080/echo -d '{"name":"Joe"}'
```

*Response body*

``` json
{"name":"Joe"}
```

## Gson Support

The WebServer supports [Gson](https://github.com/google/gson#gson). When this support is enabled, Java objects will be serialized to and deserialized from JSON automatically using Gson.

### Maven Coordinates

To enable Gson Support add the following dependency to your project’s `pom.xml`.

``` xml
<dependency>
    <groupId>io.helidon.http.media</groupId>
    <artifactId>helidon-http-media-gson</artifactId>
</dependency>
```

### Configuration

It is possible to configure the Gson instance via programmatic or configuration-based approach.

Type: [io.helidon.http.media.gson.GsonSupport](/apidocs/io.helidon.http.media.gson/io/helidon/http/media/gson/GsonSupport.html)

*Config key*

``` text
gson
```

This type provides the following service implementations:

- `io.helidon.http.media.spi.MediaSupportProvider`

#### Configuration options

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
<td style="text-align: left;"><p><code>accepted-media-types</code></p></td>
<td style="text-align: left;"><p>MediaType[]</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Types accepted by this media support. When server processes the response, it checks the <code>Accept</code> header, to choose the right media support, if there are more supports available for the provided entity object.</p>
<p>NOTE Make sure that you accept the type returned by contentType().</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>content-type</code></p></td>
<td style="text-align: left;"><p>HttpMediaType</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Content type to use if not configured (in response headers for server, and in request headers for client).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Name of the support. Each extension should provide its own default. This is to enable multiple instance of the same type.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>properties</code></p></td>
<td style="text-align: left;"><p>Map&lt;string, boolean&gt;</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Gson configuration properties. Properties are being ignored if specific Gson is set. Only <code>boolean</code> configuration values are supported.</p></td>
</tr>
</tbody>
</table>

#### Example

*Example Gson configuration*

``` yaml
gson:
  properties:
    serialize-nulls: false
```

### Usage

Now that automatic JSON serialization and deserialization facilities have been set up, you can register a `Handler` that works with Java objects instead of raw JSON. Deserialization from and serialization to JSON will be handled by [Gson](++https://github.com/google/gson#gson).

Suppose you have a `Person` class that looks like this:

*Hypothetical `Person` class*

``` java
public class Person {

    private String name;

    public Person() {
        super();
    }

    public String getName() {
        return this.name;
    }

    public void setName(String name) {
        this.name = name;
    }
}
```

Then you can set up a `Handler` like this:

*A `Handler` that works with Java objects instead of raw JSON*

``` java
rules.post("/echo", (req, res) -> {
    res.send(req.content().as(Person.class)); 
});
```

- This handler consumes a `Person` instance and simply echoes it back. Note that there is no working with raw JSON here.

*Example of posting JSON to the `/echo` endpoint*

``` bash
curl --noproxy '*' -X POST -H "Content-Type: application/json" \
    http://localhost:8080/echo -d '{"name":"Joe"}'
```

*Response body*

``` json
{"name":"Joe"}
```

# HTTP Content Encoding

HTTP encoding can improve bandwidth utilization and transfer speeds in certain scenarios. It requires a few extra CPU cycles for compressing and uncompressing, but these can be offset if data is transferred over low-bandwidth network links.

A client advertises the compression encodings it supports at request time, and the WebServer responds by selecting an encoding it supports and setting it in a header, effectively *negotiating* the content encoding of the response. If none of the advertised encodings is supported by the WebServer, the response is returned uncompressed.

Handlers can encode the response and set the appropriate header to preempt encoding by the WebServer. For instance, if a Handler sets the `Content-Encoding: gzip` header then the response will not be additionally compressed.

## Configuring HTTP Encoding

HTTP encoding support is discovered automatically by WebServer from the classpath, or it can be customized programmatically.

Encoding can be configured per socket.

Disabling discovery and registering a Gzip encoding support:

``` java
WebServer.builder()
        .contentEncoding(it -> it
        .contentEncodingsDiscoverServices(false)
        .addContentEncoding(GzipEncoding.create()));
```

Or use a config file using the following options:

Type: [io.helidon.http.encoding.ContentEncodingContext](/apidocs/io.helidon.http.encoding/io/helidon/http/encoding/ContentEncodingContext.html)

### Configuration options

| key | type | default value | description |
|----|----|----|----|
| `content-encodings` | io.helidon.http.encoding.ContentEncoding\[\] (service provider interface) |   | List of content encodings that should be used. Encodings configured here have priority over encodings discovered through service loader. |

Optional configuration options

The following providers are currently available (simply add the library on the classpath):

| Encoding type | TypeName | Maven groupId:artifactId |
|----|----|----|
| **gzip** | GzipEncoding | `io.helidon.http.encoding:helidon-http-encoding-gzip` |
| **deflate** | DeflateSupport | `io.helidon.http.encoding:helidon-http-encoding-deflate` |

## HTTP Compression Negotiation

HTTP compression negotiation is controlled by clients using the `Accept-Encoding` header. The value of this header is a comma-separated list of encodings. The WebServer will select one of these encodings for compression purposes; it currently supports `gzip` and `deflate`.

For example, if the request includes `Accept-Encoding: gzip, deflate`, and HTTP compression has been enabled as shown above, the response shall include the header `Content-Encoding: gzip` and a compressed payload.

# Proxy Protocol Support

The [Proxy Protocol](https://www.haproxy.org/download/1.8/doc/proxy-protocol.txt) provides a way to convey client information across reverse proxies or load balancers which would otherwise be lost given that new connections are established for each network hop. Often times, this information can be carried in HTTP headers, but not all proxies support this feature. Helidon is capable of parsing a proxy protocol header (i.e., a network preamble) that is based on either V1 or V2 of the protocol, thus making client information available to service developers.

Proxy Protocol support is enabled via configuration, and can be done either declaratively or programmatically. Once enabled, every new connection on the corresponding port **MUST** be preambled by a proxy header for the connection not to be rejected as invalid --that is, proxy headers are never optional.

Programmatically, support for the Proxy Protocol is enabled as follows:

``` java
WebServer.builder()
        .enableProxyProtocol(true);
```

Declaratively, support for the Proxy Protocol is enabled as follows:

``` yaml
server:
  port: 8080
  host: 0.0.0.0
  enable-proxy-protocol: true
```

## Accessing Proxy Protocol Data

There are two ways in which the header data can be accessed in your application. One way is by obtaining the protocol data directly from a request as shown next:

``` java
rules.get("/", (req, res) -> {
    ProxyProtocolData data = req.proxyProtocolData().orElse(null);
    if (data != null
        && data.family() == ProxyProtocolData.Family.IPv4
        && data.protocol() == ProxyProtocolData.Protocol.TCP
        && data.sourceAddress().equals("192.168.0.1")
        && data.destAddress().equals("192.168.0.11")
        && data.sourcePort() == 56324
        && data.destPort() == 443) {
        // ...
    }
});
```

> [!NOTE]
> Every request associated with a certain connection shall have access to the Proxy Protocol data received when the connection was opened.

Alternatively, the WebServer also makes the original client source address and source port available in the HTTP headers `X-Forwarded-For` and `X-Forwarded-Port`, respectively. In some cases, it is just simpler to inspect these headers instead of getting the complete `ProxyProtocolData` instance as shown above.

## Accessing Proxy Protocol V2 Data

The binary (V2) version of the Proxy Protocol includes additional information beyond that found in the text (V1) protocol version. The V2 version exposes a proxy command type (LOCAL or PROXY), allows source and destination addresses to be Unix domain sockets, and supports structured metadata using Tag-Length-Value (TLV) encoded structures. Helidon makes this additional information available through the `ProxyProtocolV2Data` interface, which extends `ProxyProtocolData`.

To access the V2 data, check whether the `ProxyProtocolData` object obtained from the request implements the `ProxyProtocolV2Data` interface:

``` java
rules.get("/", (req, res) -> {
    ProxyProtocolData data = req.proxyProtocolData().orElse(null);
    // The data object will be an instance of ProxyProtocolV2Data if V2 of the Proxy Protocol
    // was used by the upstream proxy.
    if (data instanceof ProxyProtocolV2Data v2Data) {
        // PROXY or LOCAL?
        ProxyProtocolV2Data.Command command = v2Data.command();

        // Will be either an InetSocketAddress (for IPv4 or IPv6) or a UnixDomainSocketAddress.
        SocketAddress sourceSocketAddress = v2Data.sourceSocketAddress();
        SocketAddress destSocketAddress = v2Data.destSocketAddress();

        // Contains all of the Tag-Length-Value objects from the Proxy Protocol header.
        List<ProxyProtocolV2Data.Tlv> tlvData = v2Data.tlvs();
    }
});
```

# Additional Information

Here is the code for a minimalist web application that runs on a random free port:

``` java
public static void main(String[] args) {
    WebServer webServer = WebServer.builder()
            .routing(it -> it.any((req, res) -> res.send("It works!"))) 
            .build() 
            .start(); 

    System.out.println("Server started at: http://localhost:" + webServer.port()); 
}
```

- For any kind of request, at any path, respond with `It works!`.

- Build the server with the provided configuration

- Start the server (and wait for it to open the port).

- The server is bound to a random free port.

# Reference

- [Helidon WebServer JavaDoc](/apidocs/io.helidon.webserver/module-summary.html)

- [Helidon WebServer Static Content JavaDoc](/apidocs/io.helidon.webserver.staticcontent/module-summary.html)

- [Helidon JSON-B Support JavaDoc](/apidocs/io.helidon.http.media.jsonp/module-summary.html)

- [Helidon JSON-P Support JavaDoc](/apidocs/io.helidon.http.media.jsonb/module-summary.html)

- [Helidon Jackson Support JavaDoc](/apidocs/io.helidon.http.media.jackson/module-summary.html)

- [Proxy Protocol Specification](https://www.haproxy.org/download/1.8/doc/proxy-protocol.txt)
