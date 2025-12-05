Type:
[io.helidon.integrations.oci.OciConfig](/apidocs/io.helidon.integrations.oci/io/helidon/integrations/oci/OciConfig.html)

This is a standalone configuration type, prefix from configuration root:
`helidon.oci`

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
<td
style="text-align: left;"><p><code>allowed-authentication-methods</code></p></td>
<td style="text-align: left;"><p>string[]</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>List of attempted authentication
strategies in case
io.helidon.integrations.oci.OciConfig.authenticationMethod() is set to
AUTHENTICATION_METHOD_AUTO.</p>
<p>In case the list is empty, all available strategies will be tried,
ordered by their io.helidon.common.Weight</p>
<p>See
io.helidon.integrations.oci.OciConfig.authenticationMethod()</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>authentication-method</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p><code>auto</code></p></td>
<td style="text-align: left;"><p>Authentication method to use. If the
configured method is not available, an exception would be thrown for OCI
related services.</p>
<p>Known and supported authentication strategies for public OCI:</p>
<ul>
<li><p>AUTHENTICATION_METHOD_AUTO - use the list of
io.helidon.integrations.oci.OciConfig.allowedAuthenticationMethods() (in
the provided order), and choose the first one capable of providing
data</p></li>
<li><p>AuthenticationMethodConfig.METHOD - use configuration of the
application to obtain values needed to set up connectivity, uses
com.oracle.bmc.auth.SimpleAuthenticationDetailsProvider</p></li>
<li><p>AuthenticationMethodConfigFile.METHOD - use configuration file of
OCI (<code>home/.oci/config</code>), uses
com.oracle.bmc.auth.ConfigFileAuthenticationDetailsProvider</p></li>
<li><p><code>resource-principal</code> - use identity of the OCI
resource the service is executed on (fn), uses
com.oracle.bmc.auth.ResourcePrincipalAuthenticationDetailsProvider, and
is available in a separate module
<code>helidon-integrations-oci-authentication-resource</code></p></li>
<li><p><code>instance-principal</code> - use identity of the OCI
instance the service is running on, uses
com.oracle.bmc.auth.InstancePrincipalsAuthenticationDetailsProvider, and
is available in a separate module
<code>helidon-integrations-oci-authentication-resource</code></p></li>
<li><p><code>oke-workload-identity</code> - use identity of the OCI
Kubernetes workload, uses
<code>com.oracle.bmc.auth.okeworkloadidentity.OkeWorkloadIdentityAuthenticationDetailsProvider</code>,
and is available in a separate module
<code>helidon-integrations-oci-authentication-oke-workload</code></p></li>
</ul></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>authentication-timeout</code></p></td>
<td style="text-align: left;"><p>Duration</p></td>
<td style="text-align: left;"><p><code>PT10S</code></p></td>
<td style="text-align: left;"><p>Timeout of authentication operations,
where applicable. This is a timeout for each operation (if there are
retries, each timeout will be this duration). Defaults to 10
seconds.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>authentication.config</code></p></td>
<td style="text-align: left;"><p><a
href="../config/io_helidon_integrations_oci_ConfigMethodConfig.xml">ConfigMethodConfig</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Config method configuration (if
provided and used).</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>authentication.config-file</code></p></td>
<td style="text-align: left;"><p><a
href="../config/io_helidon_integrations_oci_ConfigFileMethodConfig.xml">ConfigFileMethodConfig</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Config file method configuration (if
provided and used).</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>authentication.session-token</code></p></td>
<td style="text-align: left;"><p><a
href="../config/io_helidon_integrations_oci_SessionTokenMethodConfig.xml">SessionTokenMethodConfig</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Session token method configuration (if
provided and used).</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>federation-endpoint</code></p></td>
<td style="text-align: left;"><p>URI</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Customization of federation endpoint
for authentication providers.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>imds-base-uri</code></p></td>
<td style="text-align: left;"><p>URI</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>The OCI IMDS URI (http URL pointing to
the metadata service, if customization needed).</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>imds-detect-retries</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Customize the number of retries to
contact IMDS service.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>imds-timeout</code></p></td>
<td style="text-align: left;"><p>Duration</p></td>
<td style="text-align: left;"><p><code>PT1S</code></p></td>
<td style="text-align: left;"><p>The OCI IMDS connection timeout. This
is used to auto-detect availability.</p>
<p>This configuration property is used when attempting to connect to the
metadata service.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>region</code></p></td>
<td style="text-align: left;"><p>Region</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Explicit region. The configured region
will be used by region provider. This may be ignored by authentication
detail providers, as in most cases region is provided by them.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>tenant-id</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>OCI tenant id for Instance Principal,
Resource Principal or OKE Workload.</p></td>
</tr>
</tbody>
</table>
