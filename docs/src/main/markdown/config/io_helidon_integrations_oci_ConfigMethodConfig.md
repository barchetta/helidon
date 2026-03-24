# ConfigMethodConfig (integrations.oci) Configuration

Type: [io.helidon.integrations.oci.ConfigMethodConfig](/apidocs/io.helidon.integrations.oci/io/helidon/integrations/oci/ConfigMethodConfig.html)

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
<td style="text-align: left;"><p><code>passphrase</code></p></td>
<td style="text-align: left;"><p>char[]</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>The OCI authentication passphrase.</p>
<p>This property must be provided in order to set the com.oracle.bmc.auth.SimpleAuthenticationDetailsProvider.getPassphraseCharacters().</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>private-key</code></p></td>
<td style="text-align: left;"><p><a href="../config/../config/io_helidon_common_configurable_Resource.xml">Resource</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>The OCI authentication private key resource. A resource can be defined as a resource on classpath, file on the file system, base64 encoded text value in config, or plain-text value in config.</p>
<p>If not defined, we will use <code>.oci/oic_api_key.pem</code> file in user home directory.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>region</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>The OCI region.</p></td>
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
