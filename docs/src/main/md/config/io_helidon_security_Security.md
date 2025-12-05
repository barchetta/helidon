Configuration of security providers, integration and other security
options

Type:
[io.helidon.security.Security](/apidocs/io.helidon.security/io/helidon/security/Security.html)

This is a standalone configuration type, prefix from configuration root:
`security`

# Configuration options

<table style="width:100%;">
<caption>Required configuration options</caption>
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
<td style="text-align: left;"><p><code>providers</code></p></td>
<td
style="text-align: left;"><p>io.helidon.security.spi.SecurityProvider[]
(service provider interface)</p>
<p>Such as:</p>
<ul>
<li><p><a
href="../config/io_helidon_security_providers_idcs_mapper_IdcsRoleMapperProvider.xml">idcs-role-mapper
(IdcsRoleMapperProvider)</a></p></li>
<li><p><a
href="../config/io_helidon_security_providers_config_vault_ConfigVaultProvider.xml">config-vault
(ConfigVaultProvider)</a></p></li>
<li><p><a
href="../config/io_helidon_security_providers_jwt_JwtProvider.xml">jwt
(JwtProvider)</a></p></li>
<li><p><a
href="../config/io_helidon_security_providers_httpauth_HttpBasicAuthProvider.xml">http-basic-auth
(HttpBasicAuthProvider)</a></p></li>
<li><p><a
href="../config/io_helidon_security_providers_idcs_mapper_IdcsMtRoleMapperProvider.xml">idcs-role-mapper
(IdcsMtRoleMapperProvider)</a></p></li>
<li><p><a
href="../config/io_helidon_security_providers_google_login_GoogleTokenProvider.xml">google-login
(GoogleTokenProvider)</a></p></li>
<li><p><a
href="../config/io_helidon_security_providers_oidc_OidcProvider.xml">oidc
(OidcProvider)</a></p></li>
<li><p><a
href="../config/io_helidon_security_providers_httpauth_HttpDigestAuthProvider.xml">http-digest-auth
(HttpDigestAuthProvider)</a></p></li>
<li><p><a
href="../config/io_helidon_security_providers_header_HeaderAtnProvider.xml">header-atn
(HeaderAtnProvider)</a></p></li>
<li><p><a
href="../config/io_helidon_security_providers_abac_AbacProvider.xml">abac
(AbacProvider)</a></p></li>
</ul></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Add a provider, works as
addProvider(io.helidon.security.spi.SecurityProvider, String), where the
name is set to <code>Class#getSimpleName()</code>.</p></td>
</tr>
</tbody>
</table>

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
style="text-align: left;"><p><code>default-authentication-provider</code></p></td>
<td style="text-align: left;"><p>string (service provider
interface)</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>ID of the default authentication
provider</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>default-authorization-provider</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>ID of the default authorization
provider</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>enabled</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Security can be disabled using
configuration, or explicitly. By default, security instance is enabled.
Disabled security instance will not perform any checks and allow all
requests.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>environment.server-time</code></p></td>
<td style="text-align: left;"><p><a
href="../config/io_helidon_security_SecurityTime.xml">SecurityTime</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Server time to use when evaluating
security policies that depend on time.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>provider-policy.class-name</code></p></td>
<td style="text-align: left;"><p>Class</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Provider selection policy class name,
only used when type is set to CLASS</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>provider-policy.type</code></p></td>
<td style="text-align: left;"><p>ProviderSelectionPolicyType (FIRST,
COMPOSITE, CLASS)</p></td>
<td style="text-align: left;"><p><code>FIRST</code></p></td>
<td style="text-align: left;"><p>Type of the policy.</p>
<p>Allowed values:</p>
<ul>
<li><p><code>FIRST</code>: Choose first provider from the list by
default. Choose provider with the name defined when explicit provider
requested.</p></li>
<li><p><code>COMPOSITE</code>: Can compose multiple providers together
to form a single logical provider.</p></li>
<li><p><code>CLASS</code>: Explicit class for a custom
ProviderSelectionPolicyType.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>secrets</code></p></td>
<td style="text-align: left;"><p>Map&lt;string, string&gt; (documented
for specific cases)</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Configured secrets</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>secrets.*.config</code></p></td>
<td
style="text-align: left;"><p>io.helidon.security.SecretsProviderConfig
(service provider interface)</p>
<p>Such as:</p>
<ul>
<li><p><a
href="../config/io_helidon_security_providers_config_vault_ConfigVaultProvider_SecretConfig.xml">SecretConfig</a></p></li>
</ul></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Configuration specific to the secret
provider</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>secrets.*.name</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Name of the secret, used for
lookup</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>secrets.*.provider</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Name of the secret provider</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>tracing.enabled</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Whether or not tracing should be
enabled. If set to false, security tracer will be a no-op
tracer.</p></td>
</tr>
</tbody>
</table>
