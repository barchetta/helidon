Type:
[io.helidon.http.media.MediaContext](/apidocs/io.helidon.http.media/io/helidon/http/media/MediaContext.html)

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
<td style="text-align: left;"><p><code>fallback</code></p></td>
<td style="text-align: left;"><p><a
href="../config/io_helidon_http_media_MediaContext.xml">MediaContext</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Existing context to be used as a
fallback for this context.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>media-supports</code></p></td>
<td style="text-align: left;"><p>io.helidon.http.media.MediaSupport[]
(service provider interface)</p>
<p>Such as:</p>
<ul>
<li><p><a
href="../config/io_helidon_http_media_jackson_JacksonSupport.xml">jackson
(JacksonSupport)</a></p></li>
<li><p><a
href="../config/io_helidon_http_media_jsonb_JsonbSupport.xml">jsonb
(JsonbSupport)</a></p></li>
<li><p><a
href="../config/io_helidon_http_media_gson_GsonSupport.xml">gson
(GsonSupport)</a></p></li>
</ul></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Media supports to use. This instance
has priority over provider(s) discovered by service loader. The
providers are used in order of calling this method, where the first
support added is the first one to be queried for readers and
writers.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>register-defaults</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Should we register defaults of Helidon,
such as String media support.</p></td>
</tr>
</tbody>
</table>
