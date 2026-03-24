# RevocationConfig (common.tls) Configuration

Type: [io.helidon.common.tls.RevocationConfig](/apidocs/io.helidon.common.tls/io/helidon/common/tls/RevocationConfig.html)

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
<td style="text-align: left;"><p><code>check-only-end-entity</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>false</code></p></td>
<td style="text-align: left;"><p>Only check the revocation status of end-entity certificates. Default value is <code>false</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>enabled</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>false</code></p></td>
<td style="text-align: left;"><p>Flag indicating whether this revocation config is enabled.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>fallback-enabled</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Enable fallback to the less preferred checking option.</p>
<p>If the primary method for revocation checking fails to verify the revocation status of a certificate (such as using a CRL or OCSP), the checker will attempt alternative methods. This option ensures whether revocation checking is performed strictly according to the specified method, or should fallback to the one less preferred. OCSP is preferred over the CRL by default.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ocsp-responder-uri</code></p></td>
<td style="text-align: left;"><p>URI</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>The URI that identifies the location of the OCSP responder. This overrides the <code>ocsp.responderURL</code> security property and any responder specified in a certificate’s Authority Information Access Extension, as defined in RFC 5280.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>prefer-crl-over-ocsp</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>false</code></p></td>
<td style="text-align: left;"><p>Prefer CRL over OCSP. Default value is <code>false</code>. OCSP is preferred over the CRL by default.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>soft-fail-enabled</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>false</code></p></td>
<td style="text-align: left;"><p>Allow revocation check to succeed if the revocation status cannot be determined for one of the following reasons:</p>
<ul>
<li><p>The CRL or OCSP response cannot be obtained because of a network error.</p></li>
<li><p>The OCSP responder returns one of the following errors specified in section 2.3 of RFC 2560: internalError or tryLater.</p></li>
</ul></td>
</tr>
</tbody>
</table>
