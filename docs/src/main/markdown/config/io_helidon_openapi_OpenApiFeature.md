# OpenApiFeature (openapi) Configuration

Type: [io.helidon.openapi.OpenApiFeature](/apidocs/io.helidon.openapi/io/helidon/openapi/OpenApiFeature.html)

This is a standalone configuration type, prefix from configuration root: `openapi`

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
<td style="text-align: left;"><p><span class="line-through"><code>cors</code></span></p></td>
<td style="text-align: left;"><p><a href="../config/../config/io_helidon_cors_CrossOriginConfig.xml">CrossOriginConfig</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p><strong>Deprecated</strong> CORS config.</p>
<p>@deprecated feature specific CORS configuration is deprecated and will be removed; use either config based CORS setup (configuration key <code>cors</code>, or programmatic setup using the <code>io.helidon.webserver.cors.CorsFeature</code> server feature</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>enabled</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Sets whether the feature should be enabled.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>manager</code></p></td>
<td style="text-align: left;"><p>io.helidon.openapi.OpenApiManager (service provider interface)</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>OpenAPI manager.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>permit-all</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Whether to allow anybody to access the endpoint.</p>
<p>See roles()</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>roles</code></p></td>
<td style="text-align: left;"><p>string[]</p></td>
<td style="text-align: left;"><p><code>openapi</code></p></td>
<td style="text-align: left;"><p>Hints for role names the user is expected to be in.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>services</code></p></td>
<td style="text-align: left;"><p>io.helidon.openapi.OpenApiService[] (service provider interface)</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>OpenAPI services.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>sockets</code></p></td>
<td style="text-align: left;"><p>string[]</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>List of sockets to register this feature on. If empty, it would get registered on all sockets.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>static-file</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Path of the static OpenAPI document file. Default types are <code>json</code>, <code>yaml</code>, and <code>yml</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>web-context</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p><code>/openapi</code></p></td>
<td style="text-align: left;"><p>Web context path for the OpenAPI endpoint.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>weight</code></p></td>
<td style="text-align: left;"><p>double</p></td>
<td style="text-align: left;"><p><code>90.0</code></p></td>
<td style="text-align: left;"><p>Weight of the OpenAPI feature. This is quite low, to be registered after routing. <code>90.0</code>.</p></td>
</tr>
</tbody>
</table>
