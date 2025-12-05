Type:
[io.helidon.common.configurable.Resource](/apidocs/io.helidon.common.configurable/io/helidon/common/configurable/Resource.html)

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
<td style="text-align: left;"><p><code>content</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Binary content of the resource (base64
encoded).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>content-plain</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Plain content of the resource
(text).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>description</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Description of this resource when
configured through plain text or binary.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>path</code></p></td>
<td style="text-align: left;"><p>Path</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Resource is located on
filesystem.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>proxy-host</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Host of the proxy when using
URI.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>proxy-port</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p><code>80</code></p></td>
<td style="text-align: left;"><p>Port of the proxy when using
URI.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>resource-path</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Resource is located on
classpath.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>uri</code></p></td>
<td style="text-align: left;"><p>URI</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Resource is available on a
java.net.URI.</p>
<p>See proxy() See useProxy()</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>use-proxy</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Whether to use proxy. If set to
<code>false</code>, proxy will not be used even if configured. When set
to <code>true</code> (default), proxy will be used if
configured.</p></td>
</tr>
</tbody>
</table>
