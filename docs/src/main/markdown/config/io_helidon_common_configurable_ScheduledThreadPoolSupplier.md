# ScheduledThreadPoolSupplier (common.configurable) Configuration

Type: [io.helidon.common.configurable.ScheduledThreadPoolSupplier](/apidocs/io.helidon.common.configurable/io/helidon/common/configurable/ScheduledThreadPoolSupplier.html)

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
<td style="text-align: left;"><p><code>core-pool-size</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p><code>16</code></p></td>
<td style="text-align: left;"><p>Core pool size of the thread pool executor. Defaults to <code>16</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>is-daemon</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Is daemon of the thread pool executor. Defaults to <code>true</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>prestart</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>false</code></p></td>
<td style="text-align: left;"><p>Whether to prestart core threads in this thread pool executor. Defaults to <code>false</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>thread-name-prefix</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p><code>helidon-</code></p></td>
<td style="text-align: left;"><p>Name prefix for threads in this thread pool executor. Defaults to <code>helidon-</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>virtual-threads</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>When configured to <code>true</code>, an unbounded virtual executor service (project Loom) will be used.</p>
<p>If enabled, all other configuration options of this executor service are ignored!</p></td>
</tr>
</tbody>
</table>
