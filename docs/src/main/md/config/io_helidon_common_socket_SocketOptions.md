Type:
[io.helidon.common.socket.SocketOptions](/apidocs/io.helidon.common.socket/io/helidon/common/socket/SocketOptions.html)

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
<td style="text-align: left;"><p><code>connect-timeout</code></p></td>
<td style="text-align: left;"><p>Duration</p></td>
<td style="text-align: left;"><p><code>PT10S</code></p></td>
<td style="text-align: left;"><p>Socket connect timeout. Default is 10
seconds.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>read-timeout</code></p></td>
<td style="text-align: left;"><p>Duration</p></td>
<td style="text-align: left;"><p><code>PT30S</code></p></td>
<td style="text-align: left;"><p>Socket read timeout. Default is 30
seconds.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>socket-keep-alive</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Configure socket keep alive. Default is
<code>true</code>.</p>
<p>See java.net.StandardSocketOptions.SO_KEEPALIVE</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>socket-receive-buffer-size</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Socket receive buffer size.</p>
<p>See java.net.StandardSocketOptions.SO_RCVBUF</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>socket-reuse-address</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Socket reuse address. Default is
<code>true</code>.</p>
<p>See java.net.StandardSocketOptions.SO_REUSEADDR</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>socket-send-buffer-size</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Socket send buffer size.</p>
<p>See java.net.StandardSocketOptions.SO_SNDBUF</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>tcp-no-delay</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>false</code></p></td>
<td style="text-align: left;"><p>This option may improve performance on
some systems. Default is <code>false</code>.</p>
<p>See java.net.StandardSocketOptions.TCP_NODELAY</p></td>
</tr>
</tbody>
</table>
