Type:
[io.helidon.webclient.http1.Http1ClientProtocolConfig](/apidocs/io.helidon.webclient.http1/io/helidon/webclient/http1/Http1ClientProtocolConfig.html)

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
