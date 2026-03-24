# GsonSupport (http.media.gson) Configuration

Type: [io.helidon.http.media.gson.GsonSupport](/apidocs/io.helidon.http.media.gson/io/helidon/http/media/gson/GsonSupport.html)

*Config key*

``` text
gson
```

This type provides the following service implementations:

- `io.helidon.http.media.spi.MediaSupportProvider`

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
<td style="text-align: left;"><p><code>accepted-media-types</code></p></td>
<td style="text-align: left;"><p>MediaType[]</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Types accepted by this media support. When server processes the response, it checks the <code>Accept</code> header, to choose the right media support, if there are more supports available for the provided entity object.</p>
<p>NOTE Make sure that you accept the type returned by contentType().</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>content-type</code></p></td>
<td style="text-align: left;"><p>HttpMediaType</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Content type to use if not configured (in response headers for server, and in request headers for client).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Name of the support. Each extension should provide its own default. This is to enable multiple instance of the same type.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>properties</code></p></td>
<td style="text-align: left;"><p>Map&lt;string, boolean&gt;</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Gson configuration properties. Properties are being ignored if specific Gson is set. Only <code>boolean</code> configuration values are supported.</p></td>
</tr>
</tbody>
</table>
