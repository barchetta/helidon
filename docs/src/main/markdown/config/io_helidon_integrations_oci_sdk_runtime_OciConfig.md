# OciConfig (integrations.oci.sdk.runtime) Configuration

Type: [io.helidon.integrations.oci.sdk.runtime.OciConfig](/apidocs/io.helidon.integrations.oci.sdk.runtime/io/helidon/integrations/oci/sdk/runtime/OciConfig.html)

This is a standalone configuration type, prefix from configuration root: `oci`

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
<td style="text-align: left;"><p><code>auth-strategies</code></p></td>
<td style="text-align: left;"><p>string[] (auto, config, config-file, instance-principals, resource-principal)</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>The list of authentication strategies that will be attempted by com.oracle.bmc.auth.AbstractAuthenticationDetailsProvider when one is called for. This is only used if authStrategy() is not present.</p>
<ul>
<li><p><code>auto</code> - if present in the list, or if no value for this property exists.</p></li>
<li><p><code>config</code> - the com.oracle.bmc.auth.SimpleAuthenticationDetailsProvider will be used, customized with other configuration properties described here.</p></li>
<li><p><code>config-file</code> - the com.oracle.bmc.auth.ConfigFileAuthenticationDetailsProvider will be used, customized with other configuration properties described here.</p></li>
<li><p><code>instance-principals</code> - the com.oracle.bmc.auth.InstancePrincipalsAuthenticationDetailsProvider will be used.</p></li>
<li><p><code>resource-principal</code> - the com.oracle.bmc.auth.ResourcePrincipalAuthenticationDetailsProvider will be used.</p></li>
</ul>
<p>If there are more than one strategy descriptors defined, the first one that is deemed to be available/suitable will be used and all others will be ignored.</p>
<p>See io.helidon.integrations.oci.sdk.runtime.OciAuthenticationDetailsProvider.AuthStrategy</p>
<p>Allowed values:</p>
<ul>
<li><p><code>auto</code>: auto select first applicable</p></li>
<li><p><code>config</code>: simple authentication provider</p></li>
<li><p><code>config-file</code>: config file authentication provider</p></li>
<li><p><code>instance-principals</code>: instance principals authentication provider</p></li>
<li><p><code>resource-principal</code>: resource principal authentication provider</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>auth-strategy</code></p></td>
<td style="text-align: left;"><p>string (auto, config, config-file, instance-principals, resource-principal)</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>The singular authentication strategy to apply. This will be preferred over authStrategies() if both are present.</p>
<p>Allowed values:</p>
<ul>
<li><p><code>auto</code>: auto select first applicable</p></li>
<li><p><code>config</code>: simple authentication provider</p></li>
<li><p><code>config-file</code>: config file authentication provider</p></li>
<li><p><code>instance-principals</code>: instance principals authentication provider</p></li>
<li><p><code>resource-principal</code>: resource principals authentication provider</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>auth.fingerprint</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>The OCI authentication fingerprint.</p>
<p>This configuration property has an effect only when <code>config</code> is, explicitly or implicitly, present in the value for the authStrategies(). This is also known as simpleConfigIsPresent(). When it is present, this property must be provided in order to set the <a href="https://docs.oracle.com/en-us/iaas/Content/API/Concepts/apisigningkey.htm">API signing key’s fingerprint</a>. See com.oracle.bmc.auth.SimpleAuthenticationDetailsProvider.getFingerprint() for more details.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>auth.keyFile</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p><code>oci_api_key.pem</code></p></td>
<td style="text-align: left;"><p>The OCI authentication key file.</p>
<p>This configuration property has an effect only when <code>config</code> is, explicitly or implicitly, present in the value for the authStrategies(). This is also known as simpleConfigIsPresent(). When it is present, this property must be provided in order to set the com.oracle.bmc.auth.SimpleAuthenticationDetailsProvider.getPrivateKey(). This file must exist in the <code>user.home</code> directory. Alternatively, this property can be set using either authPrivateKey() or using authPrivateKeyPath().</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>auth.passphrase</code></p></td>
<td style="text-align: left;"><p>char[]</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>The OCI authentication passphrase.</p>
<p>This configuration property has an effect only when <code>config</code> is, explicitly or implicitly, present in the value for the authStrategies(). This is also known as simpleConfigIsPresent(). When it is present, this property must be provided in order to set the com.oracle.bmc.auth.SimpleAuthenticationDetailsProvider.getPassphraseCharacters().</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>auth.private-key</code></p></td>
<td style="text-align: left;"><p>char[]</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>The OCI authentication private key.</p>
<p>This configuration property has an effect only when <code>config</code> is, explicitly or implicitly, present in the value for the authStrategies(). This is also known as simpleConfigIsPresent(). When it is present, this property must be provided in order to set the com.oracle.bmc.auth.SimpleAuthenticationDetailsProvider.getPrivateKey(). Alternatively, this property can be set using either authKeyFile() residing in the <code>user.home</code> directory, or using authPrivateKeyPath().</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>auth.private-key-path</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>The OCI authentication key file path.</p>
<p>This configuration property has an effect only when <code>config</code> is, explicitly or implicitly, present in the value for the authStrategies(). This is also known as simpleConfigIsPresent(). When it is present, this property must be provided in order to set the com.oracle.bmc.auth.SimpleAuthenticationDetailsProvider.getPrivateKey(). This file path is an alternative for using authKeyFile() where the file must exist in the <code>user.home</code> directory. Alternatively, this property can be set using authPrivateKey().</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>auth.region</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>The OCI region.</p>
<p>This configuration property has an effect only when <code>config</code> is, explicitly or implicitly, present in the value for the authStrategies(). This is also known as simpleConfigIsPresent(). When it is present, either this property or com.oracle.bmc.auth.RegionProvider must be provide a value in order to set the com.oracle.bmc.auth.ConfigFileAuthenticationDetailsProvider.getRegion().</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>auth.tenant-id</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>The OCI tenant id.</p>
<p>This configuration property has an effect only when <code>config</code> is, explicitly or implicitly, present in the value for the authStrategies(). This is also known as simpleConfigIsPresent(). When it is present, this property must be provided in order to set the com.oracle.bmc.auth.ConfigFileAuthenticationDetailsProvider.getTenantId().</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>auth.user-id</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>The OCI user id.</p>
<p>This configuration property has an effect only when <code>config</code> is, explicitly or implicitly, present in the value for the authStrategies(). When it is present, this property must be provided in order to set the com.oracle.bmc.auth.ConfigFileAuthenticationDetailsProvider.getUserId().</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>config.path</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>The OCI configuration profile path.</p>
<p>This configuration property has an effect only when <code>config-file</code> is, explicitly or implicitly, present in the value for the authStrategies(). This is also known as fileConfigIsPresent(). When it is present, this property must also be present and then the com.oracle.bmc.ConfigFileReader.parse(String) method will be passed this value. It is expected to be passed with a valid OCI configuration file path.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>config.profile</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p><code>DEFAULT</code></p></td>
<td style="text-align: left;"><p>The OCI configuration/auth profile name.</p>
<p>This configuration property has an effect only when <code>config-file</code> is, explicitly or implicitly, present in the value for the authStrategies(). This is also known as fileConfigIsPresent(). When it is present, this property may also be optionally provided in order to override the default <code>DEFAULT</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>imds.hostname</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p><code>169.254.169.254</code></p></td>
<td style="text-align: left;"><p>The OCI IMDS hostname.</p>
<p>This configuration property is used to identify the metadata service url.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>imds.timeout.milliseconds</code></p></td>
<td style="text-align: left;"><p>Duration</p></td>
<td style="text-align: left;"><p><code>PT0.1S</code></p></td>
<td style="text-align: left;"><p>The OCI IMDS connection timeout. This is used to auto-detect availability.</p>
<p>This configuration property is used when attempting to connect to the metadata service.</p>
<p>See OciAvailability</p></td>
</tr>
</tbody>
</table>
