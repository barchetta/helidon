Type:
[io.helidon.security.providers.common.OutboundTarget](/apidocs/io.helidon.security.providers.common/io/helidon/security/providers/common/OutboundTarget.html)

# Configuration options

| key    | type   | default value | description                                 |
|--------|--------|---------------|---------------------------------------------|
| `name` | string |               | Configure the name of this outbound target. |

Required configuration options

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
<td style="text-align: left;"><p><code>hosts</code></p></td>
<td style="text-align: left;"><p>string[]</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Add supported host for this target. May
be called more than once to add more hosts.</p>
<p>Valid examples:</p>
<ul>
<li><p>localhost</p></li>
<li><p>www.google.com</p></li>
<li><p>127.0.0.1</p></li>
<li><p>*.oracle.com</p></li>
<li><p>192.169.<strong>.</strong></p></li>
<li><p><strong>.google.</strong></p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>methods</code></p></td>
<td style="text-align: left;"><p>string[]</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Add supported method for this target.
May be called more than once to add more methods. The method is tested
as is ignoring case against the used method.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>paths</code></p></td>
<td style="text-align: left;"><p>string[]</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Add supported paths for this target.
May be called more than once to add more paths. The path is tested as is
against called path, and also tested as a regular expression.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>transport</code></p></td>
<td style="text-align: left;"><p>string[]</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Add supported transports for this
target. May be called more than once to add more transports.</p>
<p>Valid examples:</p>
<ul>
<li><p>http</p></li>
<li><p>https</p></li>
</ul>
<p>There is no wildcard support</p></td>
</tr>
</tbody>
</table>
