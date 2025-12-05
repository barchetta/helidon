Type:
[io.helidon.webserver.http1.Http1Config](/apidocs/io.helidon.webserver.http1/io/helidon/webserver/http1/Http1Config.html)

<div class="formalpara">

<div class="title">

Config key

</div>

``` text
http_1_1
```

</div>

This type provides the following service implementations:

- `io.helidon.webserver.spi.ProtocolConfigProvider`

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
<td
style="text-align: left;"><p><code>continue-immediately</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>false</code></p></td>
<td style="text-align: left;"><p>When true WebServer answers to expect
continue with 100 continue immediately, not waiting for user to actually
request the data.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>max-headers-size</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p><code>16384</code></p></td>
<td style="text-align: left;"><p>Maximal size of received headers in
bytes.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>max-prologue-length</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p><code>4096</code></p></td>
<td style="text-align: left;"><p>Maximal size of received HTTP prologue
(GET /path HTTP/1.1).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>recv-log</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Logging of received packets. Uses trace
and debug levels on logger of Http1LoggingConnectionListener with suffix
of <code>.recv`</code>.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>requested-uri-discovery</code></p></td>
<td style="text-align: left;"><p><a
href="../config/io_helidon_http_RequestedUriDiscoveryContext.xml">RequestedUriDiscoveryContext</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Requested URI discovery
settings.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>send-log</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Logging of sent packets. Uses trace and
debug levels on logger of Http1LoggingConnectionListener with suffix of
<code>.send`</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>validate-path</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>If set to false, any path is accepted
(even containing illegal characters).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>validate-prologue</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>If set to false, any query and fragment
is accepted (even containing illegal characters). Validation of path is
controlled by validatePath().</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>validate-request-headers</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Whether to validate headers. If set to
false, any value is accepted, otherwise validates headers + known
headers are validated by format (content length is always validated as
it is part of protocol processing (other headers may be validated if
features use them)).</p>
<pre><code>Defaults to `true`.</code></pre></td>
</tr>
<tr>
<td style="text-align: left;"><p><span
class="line-through"><code>validate-request-host-header</code></span></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p><strong>Deprecated</strong> Request
host header validation. When host header is invalid, we return
io.helidon.http.Status.BAD_REQUEST_400.</p>
<p>The validation is done according to RFC-3986 (see
io.helidon.common.uri.UriValidator). This is a requirement of the HTTP
specification.</p>
<p>This option allows you to disable the "full-blown" validation
("simple" validation is still in - the port must be parseable to
integer).</p>
<p>@deprecated this switch exists for temporary backward compatible
behavior, and will be removed in a future Helidon version</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>validate-response-headers</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>false</code></p></td>
<td style="text-align: left;"><p>Whether to validate headers. If set to
false, any value is accepted, otherwise validates headers + known
headers are validated by format (content length is always validated as
it is part of protocol processing (other headers may be validated if
features use them)).</p>
<pre><code>Defaults to `false` as user has control on the header creation.</code></pre></td>
</tr>
</tbody>
</table>
