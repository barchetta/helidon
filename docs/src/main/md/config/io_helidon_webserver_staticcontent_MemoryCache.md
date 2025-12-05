Type:
[io.helidon.webserver.staticcontent.MemoryCache](/apidocs/io.helidon.webserver.staticcontent/io/helidon/webserver/staticcontent/MemoryCache.html)

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
<td style="text-align: left;"><p><code>capacity</code></p></td>
<td style="text-align: left;"><p>Size</p></td>
<td style="text-align: left;"><p><code>50 mB</code></p></td>
<td style="text-align: left;"><p>Capacity of the cached bytes of file
content. If set to <code>0</code>, the cache is unlimited. To disable
caching, set enabled() to <code>false</code>, or do not configure a
memory cache at all.</p>
<p>The capacity must be less than java.lang.Long.MAX_VALUE bytes, though
you must be careful still, as it must fit into the heap size.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>enabled</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Whether the cache is enabled, defaults
to <code>true</code>.</p></td>
</tr>
</tbody>
</table>
