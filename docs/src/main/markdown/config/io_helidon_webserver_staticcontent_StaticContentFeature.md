# StaticContentFeature (webserver.staticcontent) Configuration

Type: [io.helidon.webserver.staticcontent.StaticContentFeature](/apidocs/io.helidon.webserver.staticcontent/io/helidon/webserver/staticcontent/StaticContentFeature.html)

*Config key*

``` text
static-content
```

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
<td style="text-align: left;"><p><code>classpath</code></p></td>
<td style="text-align: left;"><p><a href="../config/../config/io_helidon_webserver_staticcontent_ClasspathHandlerConfig.xml">ClasspathHandlerConfig[]</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>List of classpath based static content handlers.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>content-types</code></p></td>
<td style="text-align: left;"><p>Map&lt;string, MediaType&gt;</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Maps a filename extension to the response content type. To have a system-wide configuration, you can use the service loader SPI io.helidon.common.media.type.spi.MediaTypeDetector.</p>
<p>This method can override io.helidon.common.media.type.MediaTypes detection for a specific static content handler.</p>
<p>Handler will use a union of configuration defined here, and on the handler here when used from configuration.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>enabled</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Whether this feature is enabled, defaults to <code>true</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>memory-cache</code></p></td>
<td style="text-align: left;"><p><a href="../config/../config/io_helidon_webserver_staticcontent_MemoryCache.xml">MemoryCache</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Memory cache shared by the whole feature. If not configured, files are not cached in memory (except for explicitly marked files/resources in each section).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>path</code></p></td>
<td style="text-align: left;"><p><a href="../config/../config/io_helidon_webserver_staticcontent_FileSystemHandlerConfig.xml">FileSystemHandlerConfig[]</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>List of file system based static content handlers.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>sockets</code></p></td>
<td style="text-align: left;"><p>string[]</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Sockets names (listeners) that will host static content handlers, defaults to all configured sockets. Default socket name is <code>@default</code>.</p>
<p>This configures defaults for all handlers.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>temporary-storage</code></p></td>
<td style="text-align: left;"><p><a href="../config/../config/io_helidon_webserver_staticcontent_TemporaryStorage.xml">TemporaryStorage</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Temporary storage to use across all classpath handlers. If not defined, a default one will be created.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>weight</code></p></td>
<td style="text-align: left;"><p>double</p></td>
<td style="text-align: left;"><p><code>95.0</code></p></td>
<td style="text-align: left;"><p>Weight of the static content feature. Defaults to <code>95.0</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>welcome</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Welcome-file name. Default for all handlers. By default, we do not serve default files.</p></td>
</tr>
</tbody>
</table>
