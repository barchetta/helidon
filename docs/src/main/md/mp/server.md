# Content

- [Overview](#_overview)

- [Maven Coordinates](#_maven_coordinates)

- [Usage](#_usage)

- [API](#_api)

- [Configuration](#_configuration)

- [Examples](#_examples)

- [Reference](#_reference)

# Overview

Helidon provides a MicroProfile server implementation
(`io.helidon.microprofile.server.Server`) that encapsulates the Helidon
WebServer.

# Maven-Coordinates

To enable MicroProfile Server add the helidon-microprofile-core bundle
dependency to your project’s `pom.xml` (see [Managing
Dependencies](../about/managing-dependencies.md)).

``` xml
<dependency>
    <groupId>io.helidon.microprofile.bundles</groupId>
    <artifactId>helidon-microprofile-core</artifactId>
</dependency>
```

MicroProfile Server is already included in the bundle.

If full control over the dependencies is required, and you want to
minimize the quantity of the dependencies -
`Helidon MicroProfile Server` should be used. In this case the following
dependencies should be included in your project’s `pom.xml`:

``` xml
<dependency>
    <groupId>io.helidon.microprofile.server</groupId>
    <artifactId>helidon-microprofile-server</artifactId>
</dependency>
```

# Usage

Helidon Microprofile Server is used to collect and deploy JAX-RS
application(s). When starting Helidon MP, it is recommended to use the
`io.helidon.Main` main class, which will take care of starting Helidon.
CDI will then discover all extensions, including the Server extension
and start it.

See the [Helidon MP Quickstart example](guides/quickstart.md). Note
that the server lifecycle is bound to CDI.

Usage of the `io.helidon.microprofile.server.Server` API is discouraged,
as Helidon MP uses convention to discover and configure features, which
makes the applications easier to understand and maintain.

# API

The following table provides a brief description of routing annotations,
including its parameters. More information in
`Configuring a WebServer route` section.

<table>
<colgroup>
<col style="width: 37%" />
<col style="width: 62%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Annotation</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><pre><code>@RoutingName(
    value = &quot;&quot;
    required = false
)</code></pre></td>
<td style="text-align: left;"><p>Binds a JAX-RS Application or Helidon
Service to a specific (named) routing on <code>WebServer</code>.The
routing should have a corresponding named socket configured on the
WebServer to run the routing on.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>@RoutingPath(&quot;/path&quot;)</code></pre></td>
<td style="text-align: left;"><p>Path of a Helidon Service to register
with routing.</p></td>
</tr>
</tbody>
</table>

# Configuration

By default, the server uses the MicroProfile Config, but you may also
want to use [Helidon configuration](config/introduction.md).

In this example, the configuration is in a file, and it includes Helidon
configuration options.

Configuration reference:

Type:
[io.helidon.webserver.WebServer](/apidocs/io.helidon.webserver/io/helidon/webserver/WebServer.html)

This is a standalone configuration type, prefix from configuration root:
`server`

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
<td style="text-align: left;"><p><code>backlog</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p><code>1024</code></p></td>
<td style="text-align: left;"><p>Accept backlog.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>concurrency-limit</code></p></td>
<td
style="text-align: left;"><p>io.helidon.common.concurrency.limits.Limit
(service provider interface)</p>
<p>Such as:</p>
<ul>
<li><p><a
href="../config/io_helidon_common_concurrency_limits_AimdLimit.xml">aimd
(AimdLimit)</a></p></li>
<li><p><a
href="../config/io_helidon_common_concurrency_limits_FixedLimit.xml">fixed
(FixedLimit)</a></p></li>
</ul></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Concurrency limit to use to limit
concurrent execution of incoming requests. The default is to have
unlimited concurrency.</p>
<p>Note that if maxConcurrentRequests() is configured, this is
ignored.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><span
class="line-through"><code>connection-config</code></span></p></td>
<td style="text-align: left;"><p><a
href="../config/io_helidon_webserver_ConnectionConfig.xml">ConnectionConfig</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p><strong>Deprecated</strong>
Configuration of a connection (established from client against our
server).</p>
<p>@deprecated use connectionOptions() instead</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>connection-options</code></p></td>
<td style="text-align: left;"><p><a
href="../config/io_helidon_common_socket_SocketOptions.xml">SocketOptions</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Options for connections accepted by
this listener. This is not used to setup server connection.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>content-encoding</code></p></td>
<td style="text-align: left;"><p><a
href="../config/io_helidon_http_encoding_ContentEncodingContext.xml">ContentEncodingContext</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Configure the listener specific
io.helidon.http.encoding.ContentEncodingContext. This method discards
all previously registered ContentEncodingContext. If no content encoding
context is registered, content encoding context of the webserver would
be used.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>enable-proxy-protocol</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>false</code></p></td>
<td style="text-align: left;"><p>Enable proxy protocol support for this
socket. This protocol is supported by some load balancers/reverse
proxies as a means to convey client information that would otherwise be
lost. If enabled, the proxy protocol header must be present on every new
connection established with your server. For more information, see <a
href="https://www.haproxy.org/download/1.8/doc/proxy-protocol.txt"> the
specification</a>. Default is <code>false</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>error-handling</code></p></td>
<td style="text-align: left;"><p><a
href="../config/io_helidon_webserver_ErrorHandling.xml">ErrorHandling</a></p></td>
<td
style="text-align: left;"><p><code>io.helidon.webserver.ListenerConfigBlueprint.create()</code></p></td>
<td style="text-align: left;"><p>Configuration for this listener’s error
handling.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>features</code></p></td>
<td
style="text-align: left;"><p>io.helidon.webserver.spi.ServerFeature[]
(service provider interface)</p>
<p>Such as:</p>
<ul>
<li><p><a
href="../config/io_helidon_webserver_observe_ObserveFeature.xml">observe
(ObserveFeature)</a></p></li>
<li><p><a
href="../config/io_helidon_webserver_context_ContextFeature.xml">context
(ContextFeature)</a></p></li>
<li><p><a
href="../config/io_helidon_openapi_OpenApiFeature.xml">openapi
(OpenApiFeature)</a></p></li>
<li><p><a
href="../config/io_helidon_webserver_grpc_GrpcReflectionFeature.xml">grpc-reflection
(GrpcReflectionFeature)</a></p></li>
<li><p><a
href="../config/io_helidon_webserver_cors_CorsFeature.xml">cors
(CorsFeature)</a></p></li>
<li><p><a
href="../config/io_helidon_webserver_concurrency_limits_LimitsFeature.xml">limits
(LimitsFeature)</a></p></li>
<li><p><a
href="../config/io_helidon_webserver_staticcontent_StaticContentFeature.xml">static-content
(StaticContentFeature)</a></p></li>
<li><p><a
href="../config/io_helidon_integrations_eureka_EurekaRegistrationServerFeature.xml">eureka
(EurekaRegistrationServerFeature)</a></p></li>
<li><p><a
href="../config/io_helidon_webserver_security_SecurityFeature.xml">security
(SecurityFeature)</a></p></li>
<li><p><a
href="../config/io_helidon_webserver_accesslog_AccessLogFeature.xml">access-log
(AccessLogFeature)</a></p></li>
</ul></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Server features allow customization of
the server, listeners, or routings.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>host</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p><code>0.0.0.0</code></p></td>
<td style="text-align: left;"><p>Host of the default socket. Defaults to
all host addresses (<code>0.0.0.0</code>).</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>idle-connection-period</code></p></td>
<td style="text-align: left;"><p>Duration</p></td>
<td style="text-align: left;"><p><code>PT2M</code></p></td>
<td style="text-align: left;"><p>How often should we check for
idleConnectionTimeout(). Defaults to <code>PT2M</code> (2
minutes).</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>idle-connection-timeout</code></p></td>
<td style="text-align: left;"><p>Duration</p></td>
<td style="text-align: left;"><p><code>PT5M</code></p></td>
<td style="text-align: left;"><p>How long should we wait before closing
a connection that has no traffic on it. Defaults to <code>PT5M</code> (5
minutes). Note that the timestamp is refreshed max. once per second, so
this setting would be useless if configured for shorter periods of time
(also not a very good support for connection keep alive, if the
connections are killed so soon anyway).</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>ignore-invalid-named-routing</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>If set to <code>true</code>, any named
routing configured that does not have an associated named listener will
NOT cause an exception to be thrown (default behavior is to throw an
exception).</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>max-concurrent-requests</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p><code>-1</code></p></td>
<td style="text-align: left;"><p>Limits the number of requests that can
be executed at the same time (the number of active virtual threads of
requests). Defaults to <code>-1</code>, meaning "unlimited" - what the
system allows. Also make sure that this number is higher than the
expected time it takes to handle a single request in your application,
as otherwise you may stop in-progress requests.</p>
<p>Setting this option will always ignore concurrencyLimit() and will
use the io.helidon.common.concurrency.limits.FixedLimit.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>max-in-memory-entity</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p><code>131072</code></p></td>
<td style="text-align: left;"><p>If the entity is expected to be smaller
that this number of bytes, it would be buffered in memory to optimize
performance when writing it. If bigger, streaming will be used.</p>
<p>Note that for some entity types we cannot use streaming, as they are
already fully in memory (String, byte[]), for such cases, this option is
ignored.</p>
<p>Default is 128Kb.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>max-payload-size</code></p></td>
<td style="text-align: left;"><p>long</p></td>
<td style="text-align: left;"><p><code>-1</code></p></td>
<td style="text-align: left;"><p>Maximal number of bytes an entity may
have. If io.helidon.http.HeaderNames.CONTENT_LENGTH is used, this is
checked immediately, if
io.helidon.http.HeaderValues.TRANSFER_ENCODING_CHUNKED is used, we will
fail when the number of bytes read would exceed the max payload size.
Defaults to unlimited (<code>-1</code>).</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>max-tcp-connections</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p><code>-1</code></p></td>
<td style="text-align: left;"><p>Limits the number of connections that
can be opened at a single point in time. Defaults to <code>-1</code>,
meaning "unlimited" - what the system allows.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>media-context</code></p></td>
<td style="text-align: left;"><p><a
href="../config/io_helidon_http_media_MediaContext.xml">MediaContext</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Configure the listener specific
io.helidon.http.media.MediaContext. This method discards all previously
registered MediaContext. If no media context is registered, media
context of the webserver would be used.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p><code>@default</code></p></td>
<td style="text-align: left;"><p>Name of this socket. Defaults to
<code>@default</code>. Must be defined if more than one socket is
needed.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>port</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p><code>0</code></p></td>
<td style="text-align: left;"><p>Port of the default socket. If
configured to <code>0</code> (the default), server starts on a random
port.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>protocols</code></p></td>
<td
style="text-align: left;"><p>io.helidon.webserver.spi.ProtocolConfig[]
(service provider interface)</p>
<p>Such as:</p>
<ul>
<li><p><a
href="../config/io_helidon_webserver_http2_Http2Config.xml">http_2
(Http2Config)</a></p></li>
<li><p><a
href="../config/io_helidon_webserver_grpc_GrpcConfig.xml">grpc
(GrpcConfig)</a></p></li>
<li><p><a
href="../config/io_helidon_webserver_websocket_WsConfig.xml">websocket
(WsConfig)</a></p></li>
<li><p><a
href="../config/io_helidon_webserver_http1_Http1Config.xml">http_1_1
(Http1Config)</a></p></li>
</ul></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Configuration of protocols. This may be
either protocol selectors, or protocol upgraders from HTTP/1.1. As the
order is not important (providers are ordered by weight by default), we
can use a configuration as an object, such as:</p>
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
<td style="text-align: left;"><p><span
class="line-through"><code>receive-buffer-size</code></span></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p><strong>Deprecated</strong> Listener
receive buffer size.</p>
<p>@deprecated use SocketOptions.socketReceiveBufferSize() instead via
connectionOptions().</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>requested-uri-discovery</code></p></td>
<td style="text-align: left;"><p><a
href="../config/io_helidon_http_RequestedUriDiscoveryContext.xml">RequestedUriDiscoveryContext</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Requested URI discovery
context.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>restore-response-headers</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Copy and restore response headers
before and after passing a request to Jersey for processing. If Jersey
fails to handle the request, and the Webserver continues processing the
request, it needs to make sure the original headers are restored. Turn
off this flag to avoid the extra overhead of copying headers when no
handler executes after Jersey returns.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>shutdown-grace-period</code></p></td>
<td style="text-align: left;"><p>Duration</p></td>
<td style="text-align: left;"><p><code>PT0.5S</code></p></td>
<td style="text-align: left;"><p>Grace period in ISO 8601 duration
format to allow running tasks to complete before listener’s shutdown.
Default is <code>500</code> milliseconds. Configuration file values
example: <code>PT0.5S</code>, <code>PT2S</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>shutdown-hook</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>When true the webserver registers a
shutdown hook with the JVM Runtime.</p>
<p>Defaults to true. Set this to false such that a shutdown hook is not
registered.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>smart-async-writes</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>false</code></p></td>
<td style="text-align: left;"><p>If enabled and writeQueueLength() is
greater than 1, then start with async writes but possibly switch to sync
writes if async queue size is always below a certain threshold.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>sockets</code></p></td>
<td style="text-align: left;"><p><a
href="../config/io_helidon_webserver_ListenerConfig.xml">Map&lt;string,
ListenerConfig&gt;</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Socket configurations. Note that socket
named WebServer.DEFAULT_SOCKET_NAME cannot be used, configure the values
on the server directly.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>tls</code></p></td>
<td style="text-align: left;"><p><a
href="../config/io_helidon_common_tls_Tls.xml">Tls</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Listener TLS configuration.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>write-buffer-size</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p><code>4096</code></p></td>
<td style="text-align: left;"><p>Initial buffer size in bytes of
java.io.BufferedOutputStream created internally to write data to a
socket connection. Default is <code>4096</code>. Set buffer size to a
value less than one to turn off buffering.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>write-queue-length</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p><code>0</code></p></td>
<td style="text-align: left;"><p>Number of buffers queued for write
operations.</p></td>
</tr>
</tbody>
</table>

# Examples

## Access Log

Access logging in Helidon is done by a dedicated module that can be
added to Maven and configured.

To enable Access logging add the following dependency to project’s
`pom.xml`:

``` xml
<dependency>
    <groupId>io.helidon.microprofile</groupId>
    <artifactId>helidon-microprofile-access-log</artifactId>
</dependency>
```

## Configuring Access Log in a configuration file

Access log can be configured as follows:

<div class="formalpara">

<div class="title">

Access Log configuration file

</div>

``` properties
server.port=8080
server.host=0.0.0.0
server.features.access-log.format=helidon
```

</div>

# AccessLogFeature (webserver.accesslog) Configuration

Type:
[io.helidon.webserver.accesslog.AccessLogFeature](/apidocs/io.helidon.webserver.accesslog/io/helidon/webserver/accesslog/AccessLogFeature.html)

<div class="formalpara">

<div class="title">

Config key

</div>

``` text
access-log
```

</div>

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
<td style="text-align: left;"><p>Whether this feature will be
enabled.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>format</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>The format for log entries (similar to
the Apache <code>LogFormat</code>).</p>
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
<td>The time taken in microseconds (start of request until last byte
written)</td>
<td>TimeTakenLogEntry</td>
</tr>
<tr>
<td>%T</td>
<td>The time taken in seconds (start of request until last byte
written), integer</td>
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
<td
style="text-align: left;"><p><code>io.helidon.webserver.AccessLog</code></p></td>
<td style="text-align: left;"><p>Name of the logger used to obtain
access log logger from System.getLogger(String). Defaults to
AccessLogFeature.DEFAULT_LOGGER_NAME.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>sockets</code></p></td>
<td style="text-align: left;"><p>string[]</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>List of sockets to register this
feature on. If empty, it would get registered on all sockets. The logger
used will have the expected logger with a suffix of the socket
name.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>weight</code></p></td>
<td style="text-align: left;"><p>double</p></td>
<td style="text-align: left;"><p><code>1000.0</code></p></td>
<td style="text-align: left;"><p>Weight of the access log feature. We
need to log access for anything happening on the server, so weight is
high: io.helidon.webserver.accesslog.AccessLogFeature.WEIGHT.</p></td>
</tr>
</tbody>
</table>

## Configuring TLS

Helidon MP also supports custom TLS configuration.

You can set the following properties:

- Server truststore

  - Keystore with trusted certificates

- Private key and certificate

  - Server certificate which will be used in TLS handshake

<div class="formalpara">

<div class="title">

META-INF/microprofile-config.properties - Server configuration

</div>

``` properties
#Truststore setup
server.tls.trust.keystore.resource.resource-path=server.p12
server.tls.trust.keystore.passphrase=password
server.tls.trust.keystore.trust-store=true

#Keystore with private key and server certificate
server.tls.private-key.keystore.resource.resource-path=server.p12
server.tls.private-key.keystore.passphrase=password
```

</div>

Or the same configuration done in application.yaml file.

<div class="formalpara">

<div class="title">

application.yaml - Server configuration

</div>

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
    #Keystore with private key and server certificate
    private-key:
      keystore:
        passphrase: "password"
        resource:
          # load from file system
          path: "/path/to/keystore.p12" 
```

</div>

- File loaded from the classpath.

- File loaded from the file system.

## Configuring additional ports

Helidon MP can expose multiple ports, with the following limitations:

- The default port is the port that serves your application (JAX-RS
  applications and resources)

- Other ports (in this example we configure one "admin" port) can be
  assigned endpoints that are exposed by Helidon components, currently
  supported by MP Health and MP Metrics

You can set the configuration in either `application.yaml` or
`META-INF/microprofile-config.properties`:

- The port `7011` is the default port and will serve your application

- The port `8011` is named "admin" (this is an arbitrary name)

- Observability endpoints, such as metrics and health, use the "admin"
  port through the `features.observe.sockets` setting.

<div class="formalpara">

<div class="title">

Server configuration using `application.yaml`

</div>

``` yaml
server:
  port: 7011
  host: "localhost"
  sockets:
    admin:
      port: 8011
      bind-address: "localhost"
  features:
    observe:
      sockets: "admin"
```

</div>

<div class="formalpara">

<div class="title">

Server configuration using `META-INF/microprofile-config.properties`

</div>

``` properties
server.port=7011
server.host=localhost
server.sockets.0.name=admin
server.sockets.0.port=8011
server.sockets.0.bind-address=localhost
server.features.observe.sockets=admin
```

</div>

## Configuring A WebServer Route

Helidon MP Server will pick up CDI beans that implement the
`io.helidon.webserver.HttpService` interface and configure them with the
underlying WebServer.

This allows configuration of WebServer routes to run alongside a JAX-RS
application.

The bean is expected to be either `ApplicationScoped` or `Dependent` and
will be requested only once during the boot of the `Server`.

The bean will support injection of `ApplicationScoped` and `Dependent`
scoped beans. You cannot inject `RequestScoped` beans. Please use
WebServer features to handle request related objects.

### Customizing the HTTP service

The service can be customized using annotations and/or configuration to
be

- registered on a specific path

- registered with a named routing

### Assigning an HTTP service to named ports

Helidon has the concept of named routing. These correspond to the named
ports configured with WebServer.

You can assign an HTTP service to a named routing (and as a result to a
named port) using either an annotation or configuration (or both to
override the value from annotation).

#### Annotation `@RoutingName`

You can annotate a service bean with this annotation to assign it to a
specific named routing, that is (most likely) going to be bound to a
specific port.

The annotation has two attributes: - `value` that defines the routing
name - `required` to mark that the routing name MUST be configured in
Helidon server

<div class="formalpara">

<div class="title">

`@RoutingName` example

</div>

``` java
@ApplicationScoped
@RoutingName(value = "admin", required = true)
@RoutingPath("/admin")
public class AdminService implements HttpService {
    @Override
    public void routing(HttpRules rules) {
        // ...
    }
}
```

</div>

The example above will be bound to `admin` routing (and port) and will
fail if such a port is not configured.

#### Configuration override of routing name

For each service bean you can define the routing name and its required
flag by specifying a configuration option
`bean-class-name.routing-name.name` and
`bean-class-name.routing-name.required`. For service beans produced with
producer method replace `bean-class-name` with
`class-name.producer-method-name`.

Example (YAML) configuration for a service bean
`io.helidon.examples.AdminService` that changes the routing name to
`management` and its required flag to `false`:

``` yaml
io.helidon.examples.AdminService:
  routing-name:
    name: "management"
    required: false
```

### Configuring an HTTP service path

Each service is registered on a path. If none is configured, then the
service would be configured on the root path.

You can configure service path using an annotation or configuration (or
both to override value from annotation)

#### Annotation `@RoutingPath`

You can configure `@RoutingPath` to define the path a service is
registered on.

#### Configuration override of routing path

For each HTTP service class you can define the routing path by
specifying a configuration option `class-name.routing-path.path`. The
`routing-path` configuration can be applied to Jax-RS application. See
[Jakarta REST Application](jaxrs/jaxrs-applications.md) for more
information.

Example (YAML) configuration for a class
`io.helidon.example.AdminService` that changes the routing path to
`/management`:

``` yaml
io.helidon.examples.AdminService:
  routing-path:
    path: "/management"
```

## Serving Static Content

<div class="formalpara">

<div class="title">

META-INF/microprofile-config.properties - File system static content

</div>

``` properties
# Location of content on file system
server.features.static-content.path.0.location=/var/www/html
# default is index.html (only in Helidon MicroProfile)
server.features.static-content.path.0.welcome=resource.html
# static content context on webserver - default is "/"
# server.features.static-content.path.0.context=/static-file
```

</div>

<div class="formalpara">

<div class="title">

META-INF/microprofile-config.properties - Classpath static content

</div>

``` properties
# src/main/resources/WEB in your source tree
server.features.static-content.classpath.0.location=/WEB
# default is index.html
server.features.static-content.classpath.0.welcome=resource.html
# static content path - default is "/"
# server.features.static-content.classpath.0.context=/static-cp
```

</div>

It is usually easier to configure list-based options using
`application.yaml` instead, such as:

<div class="formalpara">

<div class="title">

application.yaml - Static content

</div>

``` yaml
server:
  features:
    static-content:
      welcome: "welcome.html"
      classpath:
        - context: "/static"
          location: "/WEB"
      path:
        - context: "/static-file"
          location: "./static-content"
```

</div>

See [Static Content Feature Configuration
Reference](../config/io_helidon_webserver_staticcontent_StaticContentFeature.md)
for details. The only difference is that we set welcome file to
`index.html` by default.

## Re-direct root using `server.base-path`

To redirect requests for the root path (`/`) to another path you can use
the `server.base-path` property:

``` yaml
server:
  base-path: /static/index.html
```

For any HTTP request for `/` this will return a 301 with the `Location:`
header set to the value of `server.base-path`. This is often used with
Static Content Support to serve a specific `index.html` when `/` is
requested.

Note that this feature is not for setting a context root for
applications. To configure alternate context roots see see [Setting
Application
Path](jaxrs/jaxrs-applications.xml#_setting_application_path).

## Example configuration of routing

A full configuration example (YAML):

``` yaml
server:
  port: 8080
  sockets:
   management:
   port: 8090

io.helidon.examples.AdminApplication:
  routing-name:
    name: "management"
    required: true
  routing-path:
    path: "/management"
```

## Using Requested URI Discovery

Proxies and reverse proxies between an HTTP client and your Helidon
application mask important information (for example `Host` header,
originating IP address, protocol) about the request the client sent.
Fortunately, many of these intermediary network nodes set or update
either the [standard HTTP `Forwarded`
header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Forwarded)
or the [non-standard `X-Forwarded-*` family of
headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-For)
to preserve information about the original client request.

Helidon’s requested URI discovery feature allows your application—​and
Helidon itself—​to reconstruct information about the original request
using the `Forwarded` header and the `X-Forwarded-*` family of headers.

When you prepare the connections in your server you can include the
following optional requested URI discovery settings:

- enabled or disabled

- which type or types of requested URI discovery to use:

  - `FORWARDED` - uses the `Forwarded` header

  - `X_FORWARDED` - uses the `X-Forwarded-*` headers

  - `HOST` - uses the `Host` header

- what intermediate nodes to trust

When your application receives a request Helidon iterates through the
discovery types you set up for the receiving connection, gathering
information from the corresponding header(s) for that type. If the
request does not have the corresponding header(s), or your settings do
not trust the intermediate nodes reflected in those headers, then
Helidon tries the next discovery type you set up. Helidon uses the
`HOST` discovery type if you do not set up discovery yourself or if, for
a particular request, it cannot assemble the request information using
any discovery type you did set up for the socket.

### Setting Up Requested URI Discovery

You can use configuration to set up the requested URI discovery
behavior.

<div class="formalpara">

<div class="title">

Configuring Request URI Discovery (properties format)

</div>

``` properties
server.port=8080
server.requested-uri-discovery.types=FORWARDED,X_FORWARDED
server.requested-uri-discovery.trusted-proxies.allow.pattern=lb.*\\.mycorp\\.com
server.requested-uri-discovery.trusted-proxies.deny.exact=lbtest.mycorp.com
```

</div>

This example might apply if `mycorp.com` had trusted load balancers
named `lbxxx.mycorp.com` except for an untrusted test load balancer
`lbtest.mycorp.com`.

### Obtaining the Requested URI Information

Helidon makes the requested URI information available as a property in
the request context:

<div class="formalpara">

<div class="title">

Retrieving Requested URI Information

</div>

``` java
public class MyFilter implements ContainerRequestFilter {

    @Override
    public void filter(ContainerRequestContext requestContext) {
        UriInfo uriInfo = (UriInfo) requestContext.getProperty("io.helidon.jaxrs.requested-uri");
        // ...
    }
}
```

</div>

See the
[`UriInfo`](/apidocs/io.helidon.common.uri/io/helidon/common/uri/UriInfo.html)
JavaDoc for more information.

> [!NOTE]
> The `requestContext.getUriInfo()` method returns the Jakarta RESTful
> web services `UriInfo` object, *not* the Helidon-provided requested
> URI information `UriInfo` record.

# Reference

- [Helidon MicroProfile Server
  Javadoc](/apidocs/io.helidon.microprofile.server/module-summary.html)

- [Helidon MicroProfile Server on
  GitHub](https://github.com/oracle/helidon/tree/main/microprofile/server)
