Type:
[io.helidon.webserver.ListenerConfig](/apidocs/io.helidon.webserver/io/helidon/webserver/ListenerConfig.html)

# Configuration options

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
<td
style="text-align: left;"><p><code>smart-async-writes</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>false</code></p></td>
<td style="text-align: left;"><p>If enabled and writeQueueLength() is
greater than 1, then start with async writes but possibly switch to sync
writes if async queue size is always below a certain threshold.</p></td>
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
