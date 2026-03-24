# HttpConfigBase (webclient.api) Configuration

Type: [io.helidon.webclient.api.HttpConfigBase](/apidocs/io.helidon.webclient.api/io/helidon/webclient/api/HttpConfigBase.html)

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
<td style="text-align: left;"><p><code>connect-timeout</code></p></td>
<td style="text-align: left;"><p>Duration</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Connect timeout.</p>
<p>See io.helidon.common.socket.SocketOptions.connectTimeout()</p></td>
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
<td style="text-align: left;"><p>Determines if connection keep alive is enabled (NOT socket keep alive, but HTTP connection keep alive, to re-use the same connection for multiple requests).</p>
<p>See io.helidon.common.socket.SocketOptions.socketKeepAlive()</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>max-redirects</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p><code>10</code></p></td>
<td style="text-align: left;"><p>Max number of followed redirects. This is ignored if followRedirects() option is <code>false</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>properties</code></p></td>
<td style="text-align: left;"><p>Map&lt;string, string&gt;</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Properties configured for this client. These properties are propagated through client request, to be used by services (and possibly for other purposes).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>proxy</code></p></td>
<td style="text-align: left;"><p><a href="../config/../config/io_helidon_webclient_api_Proxy.xml">Proxy</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Proxy configuration to be used for requests.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>read-timeout</code></p></td>
<td style="text-align: left;"><p>Duration</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Read timeout.</p>
<p>See io.helidon.common.socket.SocketOptions.readTimeout()</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>tls</code></p></td>
<td style="text-align: left;"><p><a href="../config/../config/io_helidon_common_tls_Tls.xml">Tls</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>TLS configuration for any TLS request from this client. TLS can also be configured per request. TLS is used when the protocol is set to <code>https</code>.</p></td>
</tr>
</tbody>
</table>
