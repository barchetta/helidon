# Http2Config (webserver.http2) Configuration

Type: [io.helidon.webserver.http2.Http2Config](/apidocs/io.helidon.webserver.http2/io/helidon/webserver/http2/Http2Config.html)

*Config key*

``` text
http_2
```

This type provides the following service implementations:

- `io.helidon.webserver.spi.ProtocolConfigProvider`

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
<td style="text-align: left;"><p><code>flow-control-timeout</code></p></td>
<td style="text-align: left;"><p>Duration</p></td>
<td style="text-align: left;"><p><code>PT15S</code></p></td>
<td style="text-align: left;"><p>Outbound flow control blocking timeout configured as java.time.Duration or text in ISO-8601 format. Blocking timeout defines an interval to wait for the outbound window size changes(incoming window updates). Default value is <code>PT15S</code>.</p>
<table>
<caption>*ISO_8601 format examples:*</caption>
<tbody>
<tr>
<td>PT0.1S</td>
<td>100 milliseconds</td>
</tr>
<tr>
<td>PT0.5S</td>
<td>500 milliseconds</td>
</tr>
<tr>
<td>PT2S</td>
<td>2 seconds</td>
</tr>
</tbody>
</table>
<p>See <a href="https://en.wikipedia.org/wiki/ISO_8601#Durations">ISO_8601 Durations</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>initial-window-size</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p><code>1048576</code></p></td>
<td style="text-align: left;"><p>This setting indicates the sender’s maximum window size in bytes for stream-level flow control. Default and maximum value is 2<sup>31</sup>-1 = 2147483647 bytes. This setting affects the window size of HTTP/2 connection. Any value greater than 2147483647 causes an error. Any value smaller than initial window size causes an error. See RFC 9113 section 6.9.1 for details.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>max-buffered-entity-size</code></p></td>
<td style="text-align: left;"><p>Size</p></td>
<td style="text-align: left;"><p><code>64 KB</code></p></td>
<td style="text-align: left;"><p>Configure the maximum size allowed for an entity that can be explicitly buffered by the application by calling io.helidon.http.media.ReadableEntity.buffer.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>max-concurrent-streams</code></p></td>
<td style="text-align: left;"><p>long</p></td>
<td style="text-align: left;"><p><code>8192</code></p></td>
<td style="text-align: left;"><p>Maximum number of concurrent streams that the server will allow. Defaults to <code>8192</code>. This limit is directional: it applies to the number of streams that the sender permits the receiver to create. It is recommended that this value be no smaller than 100 to not unnecessarily limit parallelism See RFC 9113 section 6.5.2 for details.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>max-empty-frames</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p><code>10</code></p></td>
<td style="text-align: left;"><p>Maximum number of consecutive empty frames allowed on connection.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>max-frame-size</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p><code>16384</code></p></td>
<td style="text-align: left;"><p>The size of the largest frame payload that the sender is willing to receive in bytes. Default value is <code>16384</code> and maximum value is 2<sup>24</sup>-1 = 16777215 bytes. See RFC 9113 section 6.5.2 for details.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>max-header-list-size</code></p></td>
<td style="text-align: left;"><p>long</p></td>
<td style="text-align: left;"><p><code>8192</code></p></td>
<td style="text-align: left;"><p>The maximum field section size that the sender is prepared to accept in bytes. See RFC 9113 section 6.5.2 for details. Default is 8192.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>max-rapid-resets</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p><code>50</code></p></td>
<td style="text-align: left;"><p>Maximum number of rapid resets(stream RST sent by client before any data have been sent by server). When reached within rapidResetCheckPeriod(), GOAWAY is sent to client and connection is closed. Default value is <code>50</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>rapid-reset-check-period</code></p></td>
<td style="text-align: left;"><p>Duration</p></td>
<td style="text-align: left;"><p><code>PT10S</code></p></td>
<td style="text-align: left;"><p>Period for counting rapid resets(stream RST sent by client before any data have been sent by server). Default value is <code>PT10S</code>.</p>
<p>See <a href="https://en.wikipedia.org/wiki/ISO_8601#Durations">ISO_8601 Durations</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>requested-uri-discovery</code></p></td>
<td style="text-align: left;"><p><a href="../config/../config/io_helidon_http_RequestedUriDiscoveryContext.xml">RequestedUriDiscoveryContext</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Requested URI discovery settings.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>send-error-details</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>false</code></p></td>
<td style="text-align: left;"><p>Whether to send error message over HTTP to client. Defaults to <code>false</code>, as exception message may contain internal information that could be used as an attack vector. Use with care and in cases where both server and clients are under your full control (such as for testing).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>validate-path</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>If set to false, any path is accepted (even containing illegal characters).</p></td>
</tr>
</tbody>
</table>
