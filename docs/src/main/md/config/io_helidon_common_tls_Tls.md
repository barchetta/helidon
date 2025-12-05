Type:
[io.helidon.common.tls.Tls](/apidocs/io.helidon.common.tls/io/helidon/common/tls/Tls.html)

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
<td style="text-align: left;"><p><code>cipher-suite</code></p></td>
<td style="text-align: left;"><p>string[]</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Enabled cipher suites for TLS
communication.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>client-auth</code></p></td>
<td style="text-align: left;"><p>TlsClientAuth (REQUIRED, OPTIONAL,
NONE)</p></td>
<td
style="text-align: left;"><p><code>TlsClientAuth.NONE</code></p></td>
<td style="text-align: left;"><p>Configure requirement for mutual
TLS.</p>
<p>Allowed values:</p>
<ul>
<li><p><code>REQUIRED</code>: Mutual TLS is required. Server MUST
present a certificate trusted by the client, client MUST present a
certificate trusted by the server. This implies private key and trust
configuration for both server and client.</p></li>
<li><p><code>OPTIONAL</code>: Mutual TLS is optional. Server MUST
present a certificate trusted by the client, client MAY present a
certificate trusted by the server. This implies private key
configuration at least for server, trust configuration for at least
client.</p></li>
<li><p><code>NONE</code>: Mutual TLS is disabled. Server MUST present a
certificate trusted by the client, client does not present a
certificate. This implies private key configuration for server, trust
configuration for client.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>enabled</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Flag indicating whether Tls is
enabled.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>endpoint-identification-algorithm</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p><code>HTTPS</code></p></td>
<td style="text-align: left;"><p>Identification algorithm for SSL
endpoints.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>internal-keystore-provider</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Provider of the key stores used
internally to create a key and trust manager factories.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>internal-keystore-type</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Type of the key stores used internally
to create a key and trust manager factories.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>key-manager-factory-algorithm</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Algorithm of the key manager factory
used when private key is defined. Defaults to
javax.net.ssl.KeyManagerFactory.getDefaultAlgorithm().</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>manager</code></p></td>
<td style="text-align: left;"><p>io.helidon.common.tls.TlsManager
(service provider interface)</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>The Tls manager. If one is not
explicitly defined in the config then a default manager will be
created.</p>
<p>See ConfiguredTlsManager</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>private-key</code></p></td>
<td style="text-align: left;"><p>PrivateKey</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Private key to use. For server side
TLS, this is required. For client side TLS, this is optional (used when
mutual TLS is enabled).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>protocol</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p><code>TLS</code></p></td>
<td style="text-align: left;"><p>Configure the protocol used to obtain
an instance of javax.net.ssl.SSLContext.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>protocols</code></p></td>
<td style="text-align: left;"><p>string[]</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Enabled protocols for TLS
communication. Example of valid values for <code>TLS</code> protocol:
<code>TLSv1.3</code>, <code>TLSv1.2</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>provider</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Use explicit provider to obtain an
instance of javax.net.ssl.SSLContext.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>revocation</code></p></td>
<td style="text-align: left;"><p><a
href="../config/io_helidon_common_tls_RevocationConfig.xml">RevocationConfig</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Certificate revocation check
configuration.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>secure-random-algorithm</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Algorithm to use when creating a new
secure random.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>secure-random-provider</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Provider to use when creating a new
secure random. When defined, secureRandomAlgorithm() must be defined as
well.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>session-cache-size</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p><code>20480</code></p></td>
<td style="text-align: left;"><p>SSL session cache size.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>session-timeout</code></p></td>
<td style="text-align: left;"><p>Duration</p></td>
<td style="text-align: left;"><p><code>PT24H</code></p></td>
<td style="text-align: left;"><p>SSL session timeout.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>trust</code></p></td>
<td style="text-align: left;"><p>X509Certificate[]</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>List of certificates that form the
trust manager.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>trust-all</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>false</code></p></td>
<td style="text-align: left;"><p>Trust any certificate provided by the
other side of communication.</p>
<p><strong>This is a dangerous setting:</strong> if set to
<code>true</code>, any certificate will be accepted, throwing away most
of the security advantages of TLS. <strong>NEVER</strong> do this in
production.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>trust-manager-factory-algorithm</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Trust manager factory
algorithm.</p></td>
</tr>
</tbody>
</table>
