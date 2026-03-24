# BaseHandlerConfig (webserver.staticcontent) Configuration

Type: [io.helidon.webserver.staticcontent.BaseHandlerConfig](/apidocs/io.helidon.webserver.staticcontent/io/helidon/webserver/staticcontent/BaseHandlerConfig.html)

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
<td style="text-align: left;"><p><code>cached-files</code></p></td>
<td style="text-align: left;"><p>string[]</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>A set of files that are cached in memory at startup. These files are never removed from the in-memory cache, though their overall size is added to the memory cache used bytes. When using classpath, the set must contain explicit list of all files that should be cached, when using file system, it can contain a directory, and all files under that directory (recursive) would be cached as well.</p>
<p>Note that files cached through this method may use more than the max-bytes configured for the in-memory cache (i.e. this option wins over the maximal size in bytes), so kindly be careful with what is pushed to the cache.</p>
<p><em>Files cached in memory will never be re-loaded, even if changed, until server restart!</em></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>content-types</code></p></td>
<td style="text-align: left;"><p>Map&lt;string, MediaType&gt;</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Maps a filename extension to the response content type. To have a system-wide configuration, you can use the service loader SPI io.helidon.common.media.type.spi.MediaTypeDetector.</p>
<p>This method can override io.helidon.common.media.type.MediaTypes detection for a specific static content handler.</p>
<p>Handler will use a union of configuration on the io.helidon.webserver.staticcontent.StaticContentConfig and here when used from configuration.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>context</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p><code>/</code></p></td>
<td style="text-align: left;"><p>Context that will serve this handler’s static resources, defaults to <code>/</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>enabled</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Whether this handle is enabled, defaults to <code>true</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>memory-cache</code></p></td>
<td style="text-align: left;"><p><a href="../config/../config/io_helidon_webserver_staticcontent_MemoryCache.xml">MemoryCache</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Handles will use memory cache configured on StaticContentConfig.memoryCache() by default. In case a memory cache is configured here, it will replace the memory cache used by the static content feature, and this handle will use a dedicated memory cache instead.</p>
<p>To disable memory caching for a single handler, create the configuration, and set <code>enabled: false</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>record-cache-capacity</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Configure capacity of cache used for resources. This cache will make sure the media type and location is discovered faster.</p>
<p>To cache content (bytes) in memory, use io.helidon.webserver.staticcontent.BaseHandlerConfig.memoryCache()</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>sockets</code></p></td>
<td style="text-align: left;"><p>string[]</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Sockets names (listeners) that will host this static content handler, defaults to all configured sockets. Default socket name is <code>@default</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>welcome</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Welcome-file name. In case a directory is requested, this file would be served if present. There is no welcome file by default.</p></td>
</tr>
</tbody>
</table>
