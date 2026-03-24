# CorsPathConfig (webserver.cors) Configuration

Type: [io.helidon.webserver.cors.CorsPathConfig](/apidocs/io.helidon.webserver.cors/io/helidon/webserver/cors/CorsPathConfig.html)

### Configuration options

<table class="tableblock frame-all grid-all stretch" style="width:100%;">
<caption>Table 1. Optional configuration options</caption>
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
