# SessionTokenMethodConfig (integrations.oci) Configuration

Type: [io.helidon.integrations.oci.SessionTokenMethodConfig](/apidocs/io.helidon.integrations.oci/io/helidon/integrations/oci/SessionTokenMethodConfig.html)

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
<td style="text-align: left;"><p><code>fingerprint</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>The OCI authentication fingerprint.</p>
<p>This configuration property must be provided in order to set the <a href="https://docs.oracle.com/en-us/iaas/Content/API/Concepts/apisigningkey.htm">API signing key’s fingerprint</a>. See com.oracle.bmc.auth.SimpleAuthenticationDetailsProvider.getFingerprint() for more details.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>initial-refresh-delay</code></p></td>
<td style="text-align: left;"><p>Duration</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Delay of the first refresh. Defaults to 0, to refresh immediately (implemented in the authentication details provider).</p>
<p>See com.oracle.bmc.auth.SessionTokenAuthenticationDetailsProvider.SessionTokenAuthenticationDetailsProviderBuilder.initialRefreshDelay(long)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>passphrase</code></p></td>
<td style="text-align: left;"><p>char[]</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>The OCI authentication passphrase.</p>
<p>This property must be provided in order to set the com.oracle.bmc.auth.SimpleAuthenticationDetailsProvider.getPassphraseCharacters().</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>private-key-path</code></p></td>
<td style="text-align: left;"><p>Path</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>The OCI authentication private key resource. A resource can be defined as a resource on classpath, file on the file system, base64 encoded text value in config, or plain-text value in config.</p>
<p>If not defined, we will use <code>".oci/sessions/DEFAULT/oci_api_key.pem</code> file in user home directory.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>refresh-period</code></p></td>
<td style="text-align: left;"><p>Duration</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Refresh period, i.e. how often refresh occurs. Defaults to 55 minutes (implemented in the authentication details provider).</p>
<p>See com.oracle.bmc.auth.SessionTokenAuthenticationDetailsProvider.SessionTokenAuthenticationDetailsProviderBuilder.refreshPeriod(long)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>region</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>The OCI region.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>session-lifetime-hours</code></p></td>
<td style="text-align: left;"><p>long</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Maximal lifetime of a session. Defaults to (and maximum is) 24 hours. Can only be set to a lower value.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>session-token</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Session token value. If both this value, and sessionTokenPath() is defined, this value is used.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>session-token-path</code></p></td>
<td style="text-align: left;"><p>Path</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Session token path. If both this value, and sessionToken() is defined, the value of sessionToken() is used.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>tenant-id</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>The OCI tenant id.</p>
<p>This property must be provided in order to set the com.oracle.bmc.auth.SimpleAuthenticationDetailsProvider.getTenantId().</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>user-id</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>The OCI user id.</p>
<p>This property must be provided in order to set the com.oracle.bmc.auth.SimpleAuthenticationDetailsProvider.getUserId().</p></td>
</tr>
</tbody>
</table>
