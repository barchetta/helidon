# LogStreamConfig (webserver.observe.log) Configuration

Type: [io.helidon.webserver.observe.log.LogStreamConfig](/apidocs/io.helidon.webserver.observe.log/io/helidon/webserver/observe/log/LogStreamConfig.html)

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
<td style="text-align: left;"><p><code>content-type</code></p></td>
<td style="text-align: left;"><p>HttpMediaType</p></td>
<td style="text-align: left;"><p><code>@io.helidon.http.HttpMediaTypes@.PLAINTEXT_UTF_8</code></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>enabled</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Whether stream is enabled.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>idle-message-timeout</code></p></td>
<td style="text-align: left;"><p>Duration</p></td>
<td style="text-align: left;"><p><code>PT5S</code></p></td>
<td style="text-align: left;"><p>How long to wait before we send the idle message, to make sure we keep the stream alive.</p>
<p>See idleString()</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>idle-string</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p>`% `</p></td>
<td style="text-align: left;"><p>String sent when there are no log messages within the idleMessageTimeout().</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>queue-size</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p><code>100</code></p></td>
<td style="text-align: left;"><p>Length of the in-memory queue that buffers log messages from loggers before sending them over the network. If the messages are produced faster than we can send them to client, excess messages are DISCARDED, and will not be sent.</p></td>
</tr>
</tbody>
</table>
