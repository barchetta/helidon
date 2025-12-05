# Overview

WebClient is an HTTP client for Helidon SE. It can be used to send
requests and retrieve corresponding responses in a programmatic way.

Helidon WebClient provides the following features:

- **Blocking approach**  
  The Webclient uses the blocking approach to synchronously process a
  request and its correspond response. Both `HTTP/1.1` and `HTTP/2`
  request and response will run in the thread of the user. Additionally,
  for `HTTP/2`, virtual thread is employed to manage the connection.

- **Builder-like setup and execution**  
  Creates every client and request as a builder pattern. This improves
  readability and code maintenance.

- **Redirect chain**  
  Follows the redirect chain and perform requests on the correct
  endpoint by itself.

- **Tracing and security propagation**  
  Automatically propagates the configured tracing and security settings
  of the Helidon WebServer to the WebClient and uses them during request
  and response.

# Maven Coordinates

To enable WebClient, add the following dependency to your project’s
`pom.xml` (see [Managing
Dependencies](../about/managing-dependencies.md)).

``` xml
<dependency>
    <groupId>io.helidon.webclient</groupId>
    <artifactId>helidon-webclient</artifactId>
</dependency>
```

The `helidon-webclient` dependency has built-in support for `HTTP/1.1`.

If support for `HTTP/2` is a requirement, below dependency needs to be
added:

``` xml
<dependency>
    <groupId>io.helidon.webclient</groupId>
    <artifactId>helidon-webclient-http2</artifactId>
</dependency>
```

# Usage

## Instantiating the WebClient

You can create an instance of a WebClient by executing
`WebClient.create()` which will have default settings and without a base
uri set.

To change the default settings and register additional services, you can
use simple builder that allows you to customize the client behavior.

<div class="formalpara">

<div class="title">

Create a WebClient with simple builder:

</div>

``` java
WebClient client = WebClient.builder()
        .baseUri("http://localhost")
        .build();
```

</div>

## Creating the Request

WebClient offers a set of request methods that are used to specify the
type of action to be performed on a given resource. Below are some
examples of request methods:

- `get()`

- `post()`

- `put()`

- `method(Method method)`

Check out
[HttpClient](/apidocs/io.helidon.webclient.api/io/helidon/webclient/api/HttpClient.html)
API to learn more about request methods. These methods will create a new
instance of
[HttpClientRequest](/apidocs/io.helidon.webclient.api/io/helidon/webclient/api/HttpClientRequest.html)
which can then be configured to add optional settings that will
customize the behavior of the request.

## Customizing the Request

Configuration can be set for every request type before it is sent.

<div class="formalpara">

<div class="title">

Customizing a request

</div>

``` java
client.get()
        .uri("http://example.com") 
        .path("/path") 
        .queryParam("query", "parameter") 
        .fragment("someFragment") 
        .headers(headers -> headers.accept(MediaTypes.APPLICATION_JSON)); 
```

</div>

- Overrides `baseUri` from WebClient

- Adds path to the uri

- Adds query parameter to the request

- Adds fragment to the request

- Adds header to the request

For more information about these optional parameters, check out
[ClientRequestBase](/apidocs/io.helidon.webclient.api/io/helidon/webclient/api/ClientRequestBase.html)
API, which is a parent class of
[HttpClientRequest](/apidocs/io.helidon.webclient.api/io/helidon/webclient/api/HttpClientRequest.html).

[HttpClientRequest](/apidocs/io.helidon.webclient.api/io/helidon/webclient/api/HttpClientRequest.html)
class also provides specific header methods that help the user to set a
particular header. Some examples of these are:

- `contentType` (MediaType contentType)

- `accept` (MediaType…​ mediaTypes)

For more information about these methods, check out
[ClientRequest](/apidocs/io.helidon.webclient.api/io/helidon/webclient/api/ClientRequest.html)
API, which is a parent class of
[HttpClientRequest](/apidocs/io.helidon.webclient.api/io/helidon/webclient/api/HttpClientRequest.html).

## Sending the Request

Once the request setup is completed, the following methods can be used
to send it:

- `HttpClientResponse request()`

- `<E> ClientResponseTyped<E> request(Class<E> type)`

- `<E> E requestEntity(Class<E> type)`

- `HttpClientResponse submit(Object entity)`

- `<T> ClientResponseTyped<T> submit(Object entity, Class<T> requestedType)`

- `HttpClientResponse outputStream(OutputStreamHandler outputStreamConsumer)`

- `<T> ClientResponseTyped<T> outputStream(OutputStreamHandler outputStreamConsumer, Class<T> requestedType)`

Each of the methods will provide a way to allow response to be retrieved
in a particular response type. Refer to [ClientRequest
API](/apidocs/io.helidon.webclient.api/io/helidon/webclient/api/ClientRequest.html)
for more details about these methods.

<div class="formalpara">

<div class="title">

Execute a simple GET request to endpoint and receive a String response:

</div>

``` java
ClientResponseTyped<String> response = client.get()
        .path("/endpoint")
        .request(String.class);
String entityString = response.entity();
```

</div>

## Protocol Used

WebClient currently supports `HTTP/1.1` and `HTTP/2` protocols. Below
are the rules on which specific protocol will be used:

- Using plain socket triggers WebClient to process a request using
  `HTTP/1.1`.

- When using TLS, the client will use ALPN (protocol negotiation) to use
  appropriate HTTP version (either 1.1, or 2). `HTTP/2` has a higher
  weight, so it is chosen if supported by both sides.

- A specific protocol can be explicitly selected by calling
  `HttpClientRequest#protocolId(String)`.

<!-- -->

    String result = client.get()
            .protocolId("http/1.1")
            .requestEntity(String.class);

- If `HTTP/2` is used, an upgrade attempt will be performed. If it
  fails, the client falls-back to `HTTP/1.1`.

- The parameter `prior-knowledge` can be defined using `HTTP/2` protocol
  configuration. Please refer to [Setting Protocol
  configuration](#_setting_protocol_configuration) on how to customize
  `HTTP/2`. In such a case, `prior-knowledge` will be used and fail if
  it is unable to switch to `HTTP/2`.

## Adding Media Support

Webclient supports the following built-in Helidon Media Support
libraries:

1.  JSON Processing (JSON-P)

2.  JSON Binding (JSON-B)

3.  Jackson

They can be activated by adding their corresponding libraries into the
classpath. This can simply be done by adding their corresponding
dependencies.

<div class="formalpara">

<div class="title">

Add JSON-P support:

</div>

``` xml
<dependency>
    <groupId>io.helidon.http.media</groupId>
    <artifactId>helidon-http-media-jsonp</artifactId>
</dependency>
```

</div>

<div class="formalpara">

<div class="title">

Add JSON-B support:

</div>

``` xml
<dependency>
    <groupId>io.helidon.http.media</groupId>
    <artifactId>helidon-http-media-jsonb</artifactId>
</dependency>
```

</div>

<div class="formalpara">

<div class="title">

Add Jackson support:

</div>

``` xml
<dependency>
    <groupId>io.helidon.http.media</groupId>
    <artifactId>helidon-http-media-jackson</artifactId>
</dependency>
```

</div>

Users can also create their own Custom Media Support library and make
them work by following either of the approaches:

- Create a Provider of the Custom Media Support and expose it via
  Service Loader followed by adding the Media Support library to the
  classpath.

- Explicitly register the Custom Media Support from WebClient.

``` java
WebClient.builder()
        .mediaContext(it -> it
                .addMediaSupport(CustomMediaSupport.create())) 
        .build();
```

- Register CustomMedia support from the WebClient.

## DNS Resolving

Webclient provides three DNS resolver implementations out of the box:

- `Java DNS resolution` is the default.

- `First DNS resolution` uses the first IP address from a DNS lookup. To
  enable this option, add below dependency:

``` xml
<dependency>
    <groupId>io.helidon.webclient.dns.resolver</groupId>
    <artifactId>helidon-webclient-dns-resolver-first</artifactId>
</dependency>
```

- `Round-Robin DNS resolution` cycles through IP addresses from a DNS
  lookup. To enable this option, add this dependency:

``` xml
<dependency>
    <groupId>io.helidon.webclient.dns.resolver</groupId>
    <artifactId>helidon-webclient-dns-resolver-round-robin</artifactId>
</dependency>
```

# Configuring the WebClient

The class responsible for WebClient configuration is:

Type:
[io.helidon.webclient.api.WebClient](/apidocs/io.helidon.webclient.api/io/helidon/webclient/api/WebClient.html)

This is a standalone configuration type, prefix from configuration root:
`clients`

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
<td style="text-align: left;"><p><code>base-uri</code></p></td>
<td style="text-align: left;"><p>ClientUri</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Base uri used by the client in all
requests.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>connect-timeout</code></p></td>
<td style="text-align: left;"><p>Duration</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Connect timeout.</p>
<p>See io.helidon.common.socket.SocketOptions.connectTimeout()</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>connection-cache-size</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p><code>256</code></p></td>
<td style="text-align: left;"><p>Maximal size of the connection cache.
For most HTTP protocols, we may cache connections to various endpoints
for keep alive (or stream reuse in case of HTTP/2). This option limits
the size. Setting this number lower than the "usual" number of target
services will cause connections to be closed and reopened
frequently.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>content-encoding</code></p></td>
<td style="text-align: left;"><p><a
href="../config/io_helidon_http_encoding_ContentEncodingContext.xml">ContentEncodingContext</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Configure the listener specific
io.helidon.http.encoding.ContentEncodingContext. This method discards
all previously registered ContentEncodingContext. If no content encoding
context is registered, default encoding context is used.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>cookie-manager</code></p></td>
<td style="text-align: left;"><p><a
href="../config/io_helidon_webclient_api_WebClientCookieManager.xml">WebClientCookieManager</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>WebClient cookie manager.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>default-headers</code></p></td>
<td style="text-align: left;"><p>Map&lt;string, string&gt;</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Default headers to be used in every
request from configuration.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>follow-redirects</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Whether to follow redirects.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>keep-alive</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Determines if connection keep alive is
enabled (NOT socket keep alive, but HTTP connection keep alive, to
re-use the same connection for multiple requests).</p>
<p>See io.helidon.common.socket.SocketOptions.socketKeepAlive()</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>max-in-memory-entity</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p><code>131072</code></p></td>
<td style="text-align: left;"><p>If the entity is expected to be smaller
that this number of bytes, it would be buffered in memory to optimize
performance. If bigger, streaming will be used.</p>
<p>Note that for some entity types we cannot use streaming, as they are
already fully in memory (String, byte[]), for such cases, this option is
ignored. Default is 128Kb.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>max-redirects</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p><code>10</code></p></td>
<td style="text-align: left;"><p>Max number of followed redirects. This
is ignored if followRedirects() option is <code>false</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>media-context</code></p></td>
<td style="text-align: left;"><p><a
href="../config/io_helidon_http_media_MediaContext.xml">MediaContext</a></p></td>
<td style="text-align: left;"><p><code>create()</code></p></td>
<td style="text-align: left;"><p>Configure the listener specific
io.helidon.http.media.MediaContext. This method discards all previously
registered MediaContext. If no media context is registered, default
media context is used.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>media-type-parser-mode</code></p></td>
<td style="text-align: left;"><p>ParserMode (STRICT, RELAXED)</p></td>
<td style="text-align: left;"><p><code>ParserMode.STRICT</code></p></td>
<td style="text-align: left;"><p>Configure media type parsing mode for
HTTP <code>Content-Type</code> header.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>properties</code></p></td>
<td style="text-align: left;"><p>Map&lt;string, string&gt;</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Properties configured for this client.
These properties are propagated through client request, to be used by
services (and possibly for other purposes).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>protocol-configs</code></p></td>
<td
style="text-align: left;"><p>io.helidon.webclient.spi.ProtocolConfig[]
(service provider interface)</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Configuration of client
protocols.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>protocol-preference</code></p></td>
<td style="text-align: left;"><p>string[]</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>List of HTTP protocol IDs by order of
preference. If left empty, all discovered providers will be used,
ordered by weight.</p>
<p>For example if both HTTP/2 and HTTP/1.1 providers are available
(considering HTTP/2 has higher weights), for ALPN we will send h2 and
http/1.1 and decide based on response. If TLS is not used, we would
attempt an upgrade (or use prior knowledge if configured in
protocolConfigs()).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>proxy</code></p></td>
<td style="text-align: left;"><p><a
href="../config/io_helidon_webclient_api_Proxy.xml">Proxy</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Proxy configuration to be used for
requests.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>read-continue-timeout</code></p></td>
<td style="text-align: left;"><p>Duration</p></td>
<td style="text-align: left;"><p><code>PT1S</code></p></td>
<td style="text-align: left;"><p>Socket 100-Continue read timeout.
Default is 1 second. This read timeout is used when 100-Continue is sent
by the client, before it sends an entity.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>read-timeout</code></p></td>
<td style="text-align: left;"><p>Duration</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Read timeout.</p>
<p>See io.helidon.common.socket.SocketOptions.readTimeout()</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>relative-uris</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>false</code></p></td>
<td style="text-align: left;"><p>Can be set to <code>true</code> to
force the use of relative URIs in all requests, regardless of the
presence or absence of proxies or no-proxy lists.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>send-expect-continue</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Whether Expect-100-Continue header is
sent to verify server availability before sending an entity.</p>
<p>Defaults to <code>true</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>services</code></p></td>
<td
style="text-align: left;"><p>io.helidon.webclient.spi.WebClientService[]
(service provider interface)</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>WebClient services.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>share-connection-cache</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Whether to share connection cache
between all the WebClient instances in JVM.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>socket-options</code></p></td>
<td style="text-align: left;"><p><a
href="../config/io_helidon_common_socket_SocketOptions.xml">SocketOptions</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Socket options for connections opened
by this client. If there is a value explicitly configured on this type
and on the socket options, the one configured on this type’s builder
will win:</p>
<ul>
<li><p>readTimeout()</p></li>
<li><p>connectTimeout()</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>tls</code></p></td>
<td style="text-align: left;"><p><a
href="../config/io_helidon_common_tls_Tls.xml">Tls</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>TLS configuration for any TLS request
from this client. TLS can also be configured per request. TLS is used
when the protocol is set to <code>https</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>write-buffer-size</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p><code>4096</code></p></td>
<td style="text-align: left;"><p>Buffer size used when writing data to
the underlying socket on a client TCP connection. A value that is less
or equal to 1 can be set to disable buffering at this level. Note that
if writing data to the socket in small chunks, they may not be delivered
to the network immediately due to Nagle’s algorithm (i.e., if
TCP_NO_DELAY is turned off).</p></td>
</tr>
</tbody>
</table>

## Protocol Specific Configuration

Protocol specific configuration can be set using the `protocol-configs`
parameter. Webclient currently supports `HTTP/1.1.` and `HTTP/2`. Below
are the options for each of the protocol type:

- `HTTP/1.1`

Type:
[io.helidon.webclient.http1.Http1ClientProtocolConfig](/apidocs/io.helidon.webclient.http1/io/helidon/webclient/http1/Http1ClientProtocolConfig.html)

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
<td
style="text-align: left;"><p><code>default-keep-alive</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Whether to use keep alive by
default.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>max-header-size</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p><code>16384</code></p></td>
<td style="text-align: left;"><p>Configure the maximum allowed header
size of the response.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>max-status-line-length</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p><code>256</code></p></td>
<td style="text-align: left;"><p>Configure the maximum allowed length of
the status line from the response.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p><code>http_1_1</code></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>validate-request-headers</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>false</code></p></td>
<td style="text-align: left;"><p>Sets whether the request header format
is validated or not.</p>
<pre><code>Defaults to `false` as user has control on the header creation.</code></pre></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>validate-response-headers</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Sets whether the response header format
is validated or not.</p>
<pre><code>Defaults to `true`.</code></pre></td>
</tr>
</tbody>
</table>

- `HTTP/2`

Type:
[io.helidon.webclient.http2.Http2ClientProtocolConfig](/apidocs/io.helidon.webclient.http2/io/helidon/webclient/http2/Http2ClientProtocolConfig.html)

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
<td
style="text-align: left;"><p><code>flow-control-block-timeout</code></p></td>
<td style="text-align: left;"><p>Duration</p></td>
<td style="text-align: left;"><p><code>PT15S</code></p></td>
<td style="text-align: left;"><p>Timeout for blocking while waiting for
window update when window is depleted.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>initial-window-size</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p><code>65535</code></p></td>
<td style="text-align: left;"><p>Configure INITIAL_WINDOW_SIZE setting
for new HTTP/2 connections. Sends to the server the size of the largest
frame payload client is willing to receive. Defaults to
io.helidon.http.http2.WindowSize.DEFAULT_WIN_SIZE.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>max-frame-size</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p><code>16384</code></p></td>
<td style="text-align: left;"><p>Configure initial MAX_FRAME_SIZE
setting for new HTTP/2 connections. Maximum size of data frames in bytes
the client is prepared to accept from the server. Default value is
2^14(16_384).</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>max-header-list-size</code></p></td>
<td style="text-align: left;"><p>long</p></td>
<td style="text-align: left;"><p><code>-1</code></p></td>
<td style="text-align: left;"><p>Configure initial MAX_HEADER_LIST_SIZE
setting for new HTTP/2 connections. Sends to the server the maximum
header field section size client is prepared to accept. Defaults to
<code>-1</code>, which means "unconfigured".</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p><code>h2</code></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ping</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>false</code></p></td>
<td style="text-align: left;"><p>Check healthiness of cached connections
with HTTP/2.0 ping frame. Defaults to <code>false</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ping-timeout</code></p></td>
<td style="text-align: left;"><p>Duration</p></td>
<td style="text-align: left;"><p><code>PT0.5S</code></p></td>
<td style="text-align: left;"><p>Timeout for ping probe used for
checking healthiness of cached connections. Defaults to
<code>PT0.5S</code>, which means 500 milliseconds.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>prior-knowledge</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>false</code></p></td>
<td style="text-align: left;"><p>Prior knowledge of HTTP/2 capabilities
of the server. If server we are connecting to does not support HTTP/2
and prior knowledge is set to <code>false</code>, only features
supported by HTTP/1 will be available and attempts to use HTTP/2
specific will throw an UnsupportedOperationException.</p>
<p><u>Plain text connection</u></p>
<p>If prior knowledge is set to <code>true</code>, we will not attempt
an upgrade of connection and use prior knowledge. If prior knowledge is
set to <code>false</code>, we will initiate an HTTP/1 connection and
upgrade it to HTTP/2, if supported by the server. plaintext connection
(<code>h2c</code>).</p>
<p><u>TLS protected connection</u></p>
<p>If prior knowledge is set to <code>true</code>, we will negotiate
protocol using HTTP/2 only, failing if not supported. if prior knowledge
is set to <code>false</code>, we will negotiate protocol using both
HTTP/2 and HTTP/1, using the protocol supported by server.</p></td>
</tr>
</tbody>
</table>

## Example of a WebClient Runtime Configuration

``` java
Config config = Config.create();
WebClient client = WebClient.builder()
        .baseUri("http://localhost")
        .config(config.get("client"))
        .build();
```

## Example of a WebClient YAML Configuration

``` yaml
client:
  connect-timeout-millis: 2000
  read-timeout-millis: 2000
  follow-redirects: true 
  max-redirects: 5
  cookie-manager: 
    automatic-store-enabled: true
    default-cookies:
      flavor3: strawberry
      flavor4: raspberry
  default-headers: 
    Accept: '"application/json", "text/plain"'
  services: 
    metrics:
      - methods: ["PUT", "POST", "DELETE"]
        type: METER
        name-format: "client.meter.overall"
      - type: TIMER
        # meter per method
        name-format: "client.meter.%1$s"
      - methods: ["GET"]
        type: COUNTER
        errors: false
        name-format: "client.counter.%1$s.success"
        description: "Counter of successful GET requests"
      - methods: ["PUT", "POST", "DELETE"]
        type: COUNTER
        success: false
        name-format: "wc.counter.%1$s.error"
        description: "Counter of failed PUT, POST and DELETE requests"
    tracing:
  protocol-configs: 
    http_1_1:
      max-header-size: 20000
      validate-request-headers: true
    h2:
      prior-knowledge: true
  proxy: 
    host: "hostName"
    port: 80
    no-proxy: ["localhost:8080", ".helidon.io", "192.168.1.1"]
  tls: 
    trust:
      keystore:
        passphrase: "password"
        trust-store: true
        resource:
          resource-path: "client.p12"
```

- Client functional settings

- Cookie management

- Default client headers

- Client service configuration

- Protocol configuration

- Proxy configuration

- TLS configuration

# Examples

## Webclient with Proxy

Configure Proxy setup either programmatically or via the Helidon
configuration framework.

### Configuring Proxy in your code

Proxy can be set directly from WebClient builder.

``` java
Proxy proxy = Proxy.builder()
        .type(Proxy.ProxyType.HTTP)
        .host(PROXY_HOST)
        .port(PROXY_PORT)
        .build();
WebClient.builder()
        .proxy(proxy)
        .build();
```

Alternative is to set proxy directly from the request via
`HttpClientRequest`.

``` java
Proxy proxy = Proxy.create(); 
HttpClientResponse response = client.get("/proxiedresource")
        .proxy(proxy) 
        .request();
```

- Proxy instance configured using system settings (environment variables
  and system properties)

- Configure the proxy per client request

### Configuring Proxy in the config file

Proxy can also be configured in WebClient through the `application.yaml`
configuration file.

<div class="formalpara">

<div class="title">

WebClient Proxy configuration in `application.yaml`

</div>

``` yaml
client:
  proxy:
    host: "hostName"
    port: 80
    no-proxy: ["localhost:8080", ".helidon.io", "192.168.1.1"]
```

</div>

Then, in your application code, load the configuration from that file.

<div class="formalpara">

<div class="title">

WebClient initialization using the `application.yaml` file located on
the classpath

</div>

``` java
Config config = Config.create(); 
WebClient.builder()
        .config(config.get("client")) 
        .build();
```

</div>

- `application.yaml` is a default configuration source loaded when YAML
  support is on classpath, so we can just use `Config.create()`

- Passing the client configuration node

## WebClient TLS Setup

Configure TLS either programmatically or by the Helidon configuration
framework.

### Configuring TLS in your code

One way to configure TLS in WebClient is in your application code as
shown below.

``` java
WebClient.builder()
        .tls(it -> it.trust(t -> t
                .keystore(k -> k.passphrase("password")
                        .trustStore(true)
                        .keystore(r -> r.resourcePath("client.p12")))))
        .build();
```

### Configuring TLS in the config file

Another way to configure TLS in WebClient is through the
`application.yaml` configuration file.

<div class="formalpara">

<div class="title">

WebClient TLS configuration in `application.yaml`

</div>

``` yaml
client:
  tls:
    trust:
      keystore:
        passphrase: "password"
        trust-store: true
        resource:
          resource-path: "client.p12"
```

</div>

> [!NOTE]
> The `passphrase` value on the config file can be encrypted if stronger
> security is required. For more information on how secrets can be
> encrypted using a master password and store them in a configuration
> file, please see [Configuration
> Secrets](../mp/security/configuration-secrets.md).

In the application code, load the settings from the configuration file.

<div class="formalpara">

<div class="title">

WebClient initialization using the `application.yaml` file located on
the classpath

</div>

``` java
Config config = Config.create(); 
WebClient.builder()
        .config(config.get("client")) 
        .build();
```

</div>

- `application.yaml` is a default configuration source loaded when YAML
  support is on classpath, so we can just use `Config.create()`

- Passing the client configuration node

## Adding Service to WebClient

WebClient currently supports 3 built-in services namely `metrics`,
`tracing` and `security`.

### Enabling the service

In order for a service to function, their dependency needs to be added
in the application’s pom.xml. Below are examples on how to enable the
built-in services:

- `metrics`

<!-- -->

    <dependency>
        <groupId>io.helidon.webclient</groupId>
        <artifactId>helidon-webclient-metrics</artifactId>
    </dependency>

- `tracing`

<!-- -->

    <dependency>
        <groupId>io.helidon.webclient</groupId>
        <artifactId>helidon-webclient-tracing</artifactId>
    </dependency>

- `security`

<!-- -->

    <dependency>
        <groupId>io.helidon.webclient</groupId>
        <artifactId>helidon-webclient-security</artifactId>
    </dependency>

### Adding a service in your code

Services can be added in WebClient as shown in the code below.

``` java
WebClientService clientService = WebClientMetrics.counter()
        .methods(Method.GET)
        .nameFormat("example.metric.%1$s.%2$s")
        .build(); 

WebClient.builder()
        .addService(clientService) 
        .build();
```

- Creates new metric which will count all GET requests and has format of
  `example.metric.GET.<host-name>`

- Register the service in the client instance

### Adding service in the config file

Adding service in WebClient can also be done through the
`application.yaml` configuration file.

<div class="formalpara">

<div class="title">

WebClient Service configuration in `application.yaml`

</div>

``` yaml
webclient:
  services:
    metrics:
      - type: METER
        name-format: "client.meter.overall"
      - type: TIMER
        # meter per method
        name-format: "client.meter.%1$s"
      - methods: ["PUT", "POST", "DELETE"]
        type: COUNTER
        success: false
        name-format: "wc.counter.%1$s.error"
        description: "Counter of failed PUT, POST and DELETE requests"
    tracing:
```

</div>

Then, in your application code, load the configuration from that file.

<div class="formalpara">

<div class="title">

WebClient initialization using the `application.yaml` file located on
the classpath

</div>

``` java
Config config = Config.create(); 
WebClient.builder()
        .config(config.get("client")) 
        .build();
```

</div>

- `application.yaml` is a default configuration source loaded when YAML
  support is on classpath, so we can just use `Config.create()`

- Passing the client configuration node

## Setting Protocol configuration

Individual protocols can be customized using the `protocol-config`
parameter.

### Setting up protocol configuration in your code

Below is an example of customizing `HTTP/1.1` protocol in the
application code.

``` java
WebClient.builder()
        .addProtocolConfig(Http1ClientProtocolConfig.builder()
                                   .defaultKeepAlive(false)
                                   .validateRequestHeaders(true)
                                   .validateResponseHeaders(false)
                                   .build())
        .build();
```

### Setting up protocol configuration in the config file

Protocol configuration can also be set in the `application.yaml`
configuration file.

<div class="formalpara">

<div class="title">

Setting up `HTTP/1.1` and `HTTP/2` protocol using `application.yaml`
file.

</div>

``` yaml
webclient:
  protocol-configs:
    http_1_1:
      max-header-size: 20000
      validate-request-headers: true
    h2:
      prior-knowledge: true
```

</div>

Then, in your application code, load the configuration from that file.

<div class="formalpara">

<div class="title">

WebClient initialization using the `application.yaml` file located on
the classpath

</div>

``` java
Config config = Config.create(); 
WebClient.builder()
        .config(config.get("client")) 
        .build();
```

</div>

- `application.yaml` is a default configuration source loaded when YAML
  support is on classpath, so we can just use `Config.create()`

- Passing the client configuration node

# Context Propagation

WebClient supports the capability to propagate values from
`io.helidon.common.context.Context` over HTTP headers.

To enable this feature (implemented as a WebClient service), add the
following dependency to your pom file:

``` xml
<dependency>
    <groupId>io.helidon.webclient</groupId>
    <artifactId>helidon-webclient-context</artifactId>
</dependency>
```

Example configuration:

``` yaml
client:
  services:
    context:
      records:
          # This looks up a `java.lang.String` context value classified `X-Helidon-Tid` and sends it as a `X-Helidon_Tid` header
        - header: "X-Helidon-Tid"
          # This looks up a `java.lang.String[]` context value classified with the classifier and sends it as a `X-Helidon-Cid` header, in case the value is not present, values "first" and "second" are sent instead
        - classifier: "io.helidon.webclient.context.propagation.cid"
          header: "X-Helidon-Cid"
          default-value: [ "first", "second" ]
          array: true
```

Full configuration reference:

# WebClientContextService (webclient.context) Configuration

Type:
[io.helidon.webclient.context.WebClientContextService](/apidocs/io.helidon.webclient.context/io/helidon/webclient/context/WebClientContextService.html)

## Configuration options

| key | type | default value | description |
|----|----|----|----|
| `records` | [ContextRecordConfig\[\]](../config/io_helidon_common_context_http_ContextRecordConfig.md) |   | List of propagation records. |

Optional configuration options

# Reference

- [Helidon Webclient
  API](/apidocs/io.helidon.webclient.api/module-summary.html)

- [Helidon WebClient HTTP/1.1
  Support](/apidocs/io.helidon.webclient.http1/module-summary.html)

- [Helidon WebClient HTTP/2
  Support](/apidocs/io.helidon.webclient.http2/module-summary.html)

- [Helidon WebClient DNS Resolver First
  Support](/apidocs/io.helidon.webclient.dns.resolver.first/module-summary.html)

- [Helidon WebClient DNS Resolver Round Robin
  Support](/apidocs/io.helidon.webclient.dns.resolver.roundrobin/module-summary.html)

- [Helidon WebClient Metrics
  Support](/apidocs/io.helidon.webclient.metrics/module-summary.html)

- [Helidon WebClient Security
  Support](/apidocs/io.helidon.webclient.security/module-summary.html)

- [Helidon WebClient Tracing
  Support](/apidocs/io.helidon.webclient.tracing/module-summary.html)
