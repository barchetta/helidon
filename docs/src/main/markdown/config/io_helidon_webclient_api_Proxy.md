# Proxy (webclient.api) Configuration

Type: [io.helidon.webclient.api.Proxy](/apidocs/io.helidon.webclient.api/io/helidon/webclient/api/Proxy.html)

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
<td style="text-align: left;"><p><code>force-http-connect</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Forces HTTP CONNECT with the proxy server. Otherwise it will not execute HTTP CONNECT when the request is plain HTTP with no authentication.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>host</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Sets a new host value.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>no-proxy</code></p></td>
<td style="text-align: left;"><p>string[]</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Configure a host pattern that is not going through a proxy.</p>
<p>Options are:</p>
<ul>
<li><p>IP Address, such as <code>192.168.1.1</code></p></li>
<li><p>IP V6 Address, such as <code>[2001:db8:85a3:8d3:1319:8a2e:370:7348]</code></p></li>
<li><p>Hostname, such as <code>localhost</code></p></li>
<li><p>Domain name, such as <code>helidon.io</code></p></li>
<li><p>Domain name and all sub-domains, such as <code>.helidon.io</code> (leading dot)</p></li>
<li><p>Combination of all options from above with a port, such as <code>.helidon.io:80</code></p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>password</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Sets a new password for the proxy.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>port</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Sets a port value.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>type</code></p></td>
<td style="text-align: left;"><p>Proxy.ProxyType (NONE, SYSTEM, HTTP)</p></td>
<td style="text-align: left;"><p><code>HTTP</code></p></td>
<td style="text-align: left;"><p>Sets a new proxy type.</p>
<p>Allowed values:</p>
<ul>
<li><p><code>NONE</code>: No proxy.</p></li>
<li><p><code>SYSTEM</code>: Proxy obtained from system.</p></li>
<li><p><code>HTTP</code>: HTTP proxy.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>username</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Sets a new username for the proxy.</p></td>
</tr>
</tbody>
</table>
