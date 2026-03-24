# RequestedUriDiscoveryContext (http) Configuration

Type: [io.helidon.http.RequestedUriDiscoveryContext](/apidocs/io.helidon.http/io/helidon/http/RequestedUriDiscoveryContext.html)

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
<td style="text-align: left;"><p><code>true if 'types' or 'trusted-proxies' is set; false otherwise</code></p></td>
<td style="text-align: left;"><p>Sets whether requested URI discovery is enabled for requestes arriving on the socket.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>trusted-proxies</code></p></td>
<td style="text-align: left;"><p><a href="../config/../config/io_helidon_common_configurable_AllowList.xml">AllowList</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Sets the trusted proxies for requested URI discovery for requests arriving on the socket.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>types</code></p></td>
<td style="text-align: left;"><p>RequestedUriDiscoveryContext.RequestedUriDiscoveryType[] (FORWARDED, X_FORWARDED, HOST)</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Sets the discovery types for requested URI discovery for requests arriving on the socket.</p>
<p>Allowed values:</p>
<ul>
<li><p><code>FORWARDED</code>: The <code>io.helidon.http.Header#FORWARDED</code> header is used to discover the original requested URI.</p></li>
<li><p><code>X_FORWARDED</code>: The <code>io.helidon.http.Header#X_FORWARDED_PROTO</code>, <code>io.helidon.http.Header#X_FORWARDED_HOST</code>, <code>io.helidon.http.Header#X_FORWARDED_PORT</code>, <code>io.helidon.http.Header#X_FORWARDED_PREFIX</code> headers are used to discover the original requested URI.</p></li>
<li><p><code>HOST</code>: This is the default, only the <code>io.helidon.http.Header#HOST</code> header is used to discover requested URI.</p></li>
</ul></td>
</tr>
</tbody>
</table>
