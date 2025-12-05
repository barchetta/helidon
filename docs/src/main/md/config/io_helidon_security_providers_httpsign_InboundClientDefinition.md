Type:
[io.helidon.security.providers.httpsign.InboundClientDefinition](/apidocs/io.helidon.security.providers.httpsign/io/helidon/security/providers/httpsign/InboundClientDefinition.html)

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
<td style="text-align: left;"><p><code>algorithm</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Algorithm of signature used by this
client. Currently supported:</p>
<ul>
<li><p>rsa-sha256 - asymmetric based on public/private keys</p></li>
<li><p>hmac-sha256 - symmetric based on a shared secret</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>hmac.secret</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Helper method to configure a
password-like secret (instead of byte based hmacSecret(byte[]). The
password is transformed to bytes with StandardCharsets.UTF_8
charset.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>key-id</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>The key id of this client to map to
this signature validation configuration.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>principal-name</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>The principal name of the client,
defaults to keyId if not configured.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>principal-type</code></p></td>
<td style="text-align: left;"><p>SubjectType (USER, SERVICE)</p></td>
<td style="text-align: left;"><p><code>SERVICE</code></p></td>
<td style="text-align: left;"><p>The type of principal we have
authenticated (either user or service, defaults to service).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>public-key</code></p></td>
<td style="text-align: left;"><p><a
href="../config/io_helidon_common_pki_Keys.xml">Keys</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>For algorithms based on public/private
key (such as rsa-sha256), this provides access to the public key of the
client.</p></td>
</tr>
</tbody>
</table>
