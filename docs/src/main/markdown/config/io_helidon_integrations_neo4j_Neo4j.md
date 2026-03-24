# Neo4j (integrations.neo4j) Configuration

Type: [io.helidon.integrations.neo4j.Neo4j](/apidocs/io.helidon.integrations.neo4j/io/helidon/integrations/neo4j/Neo4j.html)

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
<td style="text-align: left;"><p><code>authentication-enabled</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Enable authentication.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>certificate</code></p></td>
<td style="text-align: left;"><p>Path</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Set certificate path.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>connection-acquisition-timeout</code></p></td>
<td style="text-align: left;"><p>Duration</p></td>
<td style="text-align: left;"><p><code>PT1M</code></p></td>
<td style="text-align: left;"><p>Set connection acquisition timeout.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>encrypted</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Enable encrypted field.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>hostname-verification-enabled</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Enable hostname verification.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>idle-time-before-connection-test</code></p></td>
<td style="text-align: left;"><p>Duration</p></td>
<td style="text-align: left;"><p><code>PT1MS</code></p></td>
<td style="text-align: left;"><p>Set idle time.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>log-leaked-sessions</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Enable log leaked sessions.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>max-connection-lifetime</code></p></td>
<td style="text-align: left;"><p>Duration</p></td>
<td style="text-align: left;"><p><code>PT5H</code></p></td>
<td style="text-align: left;"><p>Set max life time.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>max-connection-pool-size</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p><code>100</code></p></td>
<td style="text-align: left;"><p>Set pool size.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>metrics-enabled</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Enable metrics.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>password</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Create password.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>trust-strategy</code></p></td>
<td style="text-align: left;"><p>Neo4j.Builder.TrustStrategy (TRUST_ALL_CERTIFICATES, TRUST_CUSTOM_CA_SIGNED_CERTIFICATES, TRUST_SYSTEM_CA_SIGNED_CERTIFICATES)</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Set trust strategy.</p>
<p>Allowed values:</p>
<ul>
<li><p><code>TRUST_ALL_CERTIFICATES</code>: Trust all.</p></li>
<li><p><code>TRUST_CUSTOM_CA_SIGNED_CERTIFICATES</code>: Trust custom certificates.</p></li>
<li><p><code>TRUST_SYSTEM_CA_SIGNED_CERTIFICATES</code>: Trust system CA.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>uri</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Create uri.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>username</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Create username.</p></td>
</tr>
</tbody>
</table>
