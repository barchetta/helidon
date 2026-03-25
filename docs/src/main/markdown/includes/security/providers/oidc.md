# Example code

##### Configuration options

<table class="tableblock frame-all grid-all stretch">
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th class="tableblock halign-left valign-top">Key</th>
<th class="tableblock halign-left valign-top">Kind</th>
<th class="tableblock halign-left valign-top">Type</th>
<th class="tableblock halign-left valign-top">Default Value</th>
<th class="tableblock halign-left valign-top">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td class="tableblock halign-left valign-top"><p><span id="a3a883-access-token-ip-check"></span> <code>access-token-ip-check</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>VALUE</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>Boolean</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>true</code></p></td>
<td class="tableblock halign-left valign-top"><p>Whether to check if current IP address matches the one access token was issued for</p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p><span id="a7e9b5-client-credentials-config"></span> <a href="../../../includes/security/providers/../../../config/io_helidon_security_providers_oidc_common_ClientCredentialsConfig.html"><code>client-credentials-config</code></a></p></td>
<td class="tableblock halign-left valign-top"><p><code>VALUE</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>i.h.s.p.o.c.ClientCredentialsConfig</code></p></td>
<td class="tableblock halign-left valign-top"><p> </p></td>
<td class="tableblock halign-left valign-top"><p>Set the configuration related to the client credentials flow</p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p><span id="a9b107-cookie-domain"></span> <code>cookie-domain</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>VALUE</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>String</code></p></td>
<td class="tableblock halign-left valign-top"><p> </p></td>
<td class="tableblock halign-left valign-top"><p>Domain the cookie is valid for</p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p><span id="a593cb-cookie-encryption-enabled"></span> <code>cookie-encryption-enabled</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>VALUE</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>Boolean</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>false</code></p></td>
<td class="tableblock halign-left valign-top"><p>Whether to encrypt token cookie created by this microservice</p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p><span id="aaabc9-cookie-encryption-id-enabled"></span> <code>cookie-encryption-id-enabled</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>VALUE</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>Boolean</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>true</code></p></td>
<td class="tableblock halign-left valign-top"><p>Whether to encrypt id token cookie created by this microservice</p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p><span id="ab14ce-cookie-encryption-name"></span> <code>cookie-encryption-name</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>VALUE</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>String</code></p></td>
<td class="tableblock halign-left valign-top"><p> </p></td>
<td class="tableblock halign-left valign-top">Name of the encryption configuration available through
Security#encrypt(String, byte[)&lt;/code&gt; and &lt;code&gt;Security#decrypt(String, String)&lt;/code&gt;]</td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p><span id="ac0d77-cookie-encryption-password"></span> <code>cookie-encryption-password</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>LIST</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>String</code></p></td>
<td class="tableblock halign-left valign-top"><p> </p></td>
<td class="tableblock halign-left valign-top"><p>Master password for encryption/decryption of cookies</p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p><span id="ad8fc7-cookie-encryption-refresh-enabled"></span> <code>cookie-encryption-refresh-enabled</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>VALUE</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>Boolean</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>true</code></p></td>
<td class="tableblock halign-left valign-top"><p>Whether to encrypt refresh token cookie created by this microservice</p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p><span id="a5da71-cookie-encryption-state-enabled"></span> <code>cookie-encryption-state-enabled</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>VALUE</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>Boolean</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>true</code></p></td>
<td class="tableblock halign-left valign-top"><p>Whether to encrypt state cookie created by this microservice</p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p><span id="a16963-cookie-encryption-tenant-enabled"></span> <code>cookie-encryption-tenant-enabled</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>VALUE</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>Boolean</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>true</code></p></td>
<td class="tableblock halign-left valign-top"><p>Whether to encrypt tenant name cookie created by this microservice</p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p><span id="ad2ea9-cookie-http-only"></span> <code>cookie-http-only</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>VALUE</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>Boolean</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>true</code></p></td>
<td class="tableblock halign-left valign-top"><p>When using cookie, if set to true, the HttpOnly attribute will be configured</p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p><span id="ae7d0f-cookie-max-age-seconds"></span> <code>cookie-max-age-seconds</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>VALUE</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>Long</code></p></td>
<td class="tableblock halign-left valign-top"><p> </p></td>
<td class="tableblock halign-left valign-top"><p>When using cookie, used to set MaxAge attribute of the cookie, defining how long the cookie is valid</p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p><span id="a423f0-cookie-name"></span> <code>cookie-name</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>VALUE</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>String</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>JSESSIONID</code></p></td>
<td class="tableblock halign-left valign-top"><p>Name of the cookie to use</p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p><span id="a47aa0-cookie-name-id-token"></span> <code>cookie-name-id-token</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>VALUE</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>String</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>JSESSIONID_2</code></p></td>
<td class="tableblock halign-left valign-top"><p>Name of the cookie to use for id token</p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p><span id="afcd78-cookie-name-refresh-token"></span> <code>cookie-name-refresh-token</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>VALUE</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>String</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>JSESSIONID_3</code></p></td>
<td class="tableblock halign-left valign-top"><p>The name of the cookie to use for the refresh token</p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p><span id="a3e5f9-cookie-name-state"></span> <code>cookie-name-state</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>VALUE</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>String</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>JSESSIONID_3</code></p></td>
<td class="tableblock halign-left valign-top"><p>The name of the cookie to use for the state storage</p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p><span id="afcf69-cookie-name-tenant"></span> <code>cookie-name-tenant</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>VALUE</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>String</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>HELIDON_TENANT</code></p></td>
<td class="tableblock halign-left valign-top"><p>The name of the cookie to use for the tenant name</p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p><span id="ae5841-cookie-path"></span> <code>cookie-path</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>VALUE</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>String</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>/</code></p></td>
<td class="tableblock halign-left valign-top"><p>Path the cookie is valid for</p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p><span id="a0a656-cookie-same-site"></span> <a href="../../../includes/security/providers/../../../config/io_helidon_http_SetCookie_SameSite.html"><code>cookie-same-site</code></a></p></td>
<td class="tableblock halign-left valign-top"><p><code>VALUE</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>i.h.h.S.SameSite</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>LAX</code></p></td>
<td class="tableblock halign-left valign-top"><p>When using cookie, used to set the SameSite cookie value</p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p><span id="a0f553-cookie-secure"></span> <code>cookie-secure</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>VALUE</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>Boolean</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>false</code></p></td>
<td class="tableblock halign-left valign-top"><p>When using cookie, if set to true, the Secure attribute will be configured</p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p><span id="a70aa3-cookie-use"></span> <code>cookie-use</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>VALUE</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>Boolean</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>true</code></p></td>
<td class="tableblock halign-left valign-top"><p>Whether to use cookie to store JWT between requests</p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p><span id="ad1309-cors"></span> <a href="../../../includes/security/providers/../../../config/io_helidon_cors_CrossOriginConfig.html"><code>cors</code></a></p></td>
<td class="tableblock halign-left valign-top"><p><code>VALUE</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>i.h.c.CrossOriginConfig</code></p></td>
<td class="tableblock halign-left valign-top"><p> </p></td>
<td class="tableblock halign-left valign-top"><p>Assign cross-origin resource sharing settings</p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p><span id="afd33a-force-https-redirects"></span> <code>force-https-redirects</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>VALUE</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>Boolean</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>false</code></p></td>
<td class="tableblock halign-left valign-top"><p>Force HTTPS for redirects to identity provider</p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p><span id="a069b5-frontend-uri"></span> <code>frontend-uri</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>VALUE</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>String</code></p></td>
<td class="tableblock halign-left valign-top"><p> </p></td>
<td class="tableblock halign-left valign-top"><p>Full URI of this application that is visible from user browser</p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p><span id="abf3fb-header-token"></span> <a href="../../../includes/security/providers/../../../config/io_helidon_security_util_TokenHandler.html"><code>header-token</code></a></p></td>
<td class="tableblock halign-left valign-top"><p><code>VALUE</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>i.h.s.u.TokenHandler</code></p></td>
<td class="tableblock halign-left valign-top"><p> </p></td>
<td class="tableblock halign-left valign-top"><p>A <code>TokenHandler</code> to process header containing a JWT</p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p><span id="a866f7-header-use"></span> <code>header-use</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>VALUE</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>Boolean</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>true</code></p></td>
<td class="tableblock halign-left valign-top"><p>Whether to expect JWT in a header field</p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p><span id="a5a4ae-id-token-signature-validation"></span> <code>id-token-signature-validation</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>VALUE</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>Boolean</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>true</code></p></td>
<td class="tableblock halign-left valign-top"><p>Whether id token signature check should be enabled</p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p><span id="ab5728-max-redirects"></span> <code>max-redirects</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>VALUE</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>Integer</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>5</code></p></td>
<td class="tableblock halign-left valign-top"><p>Configure maximal number of redirects when redirecting to an OIDC provider within a single authentication attempt</p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p><span id="ab32e8-optional"></span> <code>optional</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>VALUE</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>Boolean</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>false</code></p></td>
<td class="tableblock halign-left valign-top"><p>Whether authentication is required</p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p><span id="acf040-outbound"></span> <a href="../../../includes/security/providers/../../../config/io_helidon_security_providers_common_OutboundTarget.html"><code>outbound</code></a></p></td>
<td class="tableblock halign-left valign-top"><p><code>LIST</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>i.h.s.p.c.OutboundTarget</code></p></td>
<td class="tableblock halign-left valign-top"><p> </p></td>
<td class="tableblock halign-left valign-top"><p>Add a new target configuration</p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p><span id="aebe14-outbound-type"></span> <a href="../../../includes/security/providers/../../../config/io_helidon_security_providers_oidc_common_OidcOutboundType.html"><code>outbound-type</code></a></p></td>
<td class="tableblock halign-left valign-top"><p><code>VALUE</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>i.h.s.p.o.c.OidcOutboundType</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>USER_JWT</code></p></td>
<td class="tableblock halign-left valign-top"><p>Type of the OIDC outbound</p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p><span id="a6ccfb-pkce-challenge-method"></span> <a href="../../../includes/security/providers/../../../config/io_helidon_security_providers_oidc_common_PkceChallengeMethod.html"><code>pkce-challenge-method</code></a></p></td>
<td class="tableblock halign-left valign-top"><p><code>VALUE</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>i.h.s.p.o.c.PkceChallengeMethod</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>S256</code></p></td>
<td class="tableblock halign-left valign-top"><p>Proof Key Code Exchange (PKCE) challenge creation method</p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p><span id="a4050c-pkce-enabled"></span> <code>pkce-enabled</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>VALUE</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>Boolean</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>false</code></p></td>
<td class="tableblock halign-left valign-top"><p>Whether this provider should support PKCE</p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p><span id="ad84e8-propagate"></span> <code>propagate</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>VALUE</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>Boolean</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>false</code></p></td>
<td class="tableblock halign-left valign-top"><p>Whether to propagate identity</p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p><span id="a03394-proxy-port"></span> <code>proxy-port</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>VALUE</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>Integer</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>80</code></p></td>
<td class="tableblock halign-left valign-top"><p>Proxy port</p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p><span id="aa5960-query-id-token-param-name"></span> <code>query-id-token-param-name</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>VALUE</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>String</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>id_token</code></p></td>
<td class="tableblock halign-left valign-top"><p>Name of a query parameter that contains the JWT id token when parameter is used</p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p><span id="a4e9c0-query-param-name"></span> <code>query-param-name</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>VALUE</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>String</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>accessToken</code></p></td>
<td class="tableblock halign-left valign-top"><p>Name of a query parameter that contains the JWT access token when parameter is used</p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p><span id="a0b01e-query-param-tenant-name"></span> <code>query-param-tenant-name</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>VALUE</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>String</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>h_tenant</code></p></td>
<td class="tableblock halign-left valign-top"><p>Name of a query parameter that contains the tenant name when the parameter is used</p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p><span id="a3d4be-query-param-use"></span> <code>query-param-use</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>VALUE</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>Boolean</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>false</code></p></td>
<td class="tableblock halign-left valign-top"><p>Whether to use a query parameter to send JWT token from application to this server</p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p><span id="aa4ba9-redirect"></span> <code>redirect</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>VALUE</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>Boolean</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>false</code></p></td>
<td class="tableblock halign-left valign-top"><p>By default, the client should redirect to the identity server for the user to log in</p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p><span id="adf51c-redirect-attempt-param"></span> <code>redirect-attempt-param</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>VALUE</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>String</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>h_ra</code></p></td>
<td class="tableblock halign-left valign-top"><p>Configure the parameter used to store the number of attempts in redirect</p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p><span id="a21f20-redirect-uri"></span> <code>redirect-uri</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>VALUE</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>String</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>/oidc/redirect</code></p></td>
<td class="tableblock halign-left valign-top"><p>URI to register web server component on, used by the OIDC server to redirect authorization requests to after a user logs in or approves scopes</p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p><span id="aef163-tenants"></span> <a href="../../../includes/security/providers/../../../config/io_helidon_security_providers_oidc_common_TenantConfig.html"><code>tenants</code></a></p></td>
<td class="tableblock halign-left valign-top"><p><code>VALUE</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>i.h.s.p.o.c.TenantConfig</code></p></td>
<td class="tableblock halign-left valign-top"><p> </p></td>
<td class="tableblock halign-left valign-top"><p>Configurations of the tenants</p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p><span id="a5f4ac-token-signature-validation"></span> <code>token-signature-validation</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>VALUE</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>Boolean</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>true</code></p></td>
<td class="tableblock halign-left valign-top"><p>Whether access token signature check should be enabled</p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p><span id="a50324-use-jwt-groups"></span> <code>use-jwt-groups</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>VALUE</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>Boolean</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>true</code></p></td>
<td class="tableblock halign-left valign-top"><p>Claim <code>groups</code> from JWT will be used to automatically add groups to current subject (may be used with <code>jakarta.annotation.security.RolesAllowed</code> annotation)</p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p><span id="a85467-webclient"></span> <a href="../../../includes/security/providers/../../../config/io_helidon_webclient_api_WebClient.html"><code>webclient</code></a></p></td>
<td class="tableblock halign-left valign-top"><p><code>VALUE</code></p></td>
<td class="tableblock halign-left valign-top"><p><code>i.h.w.a.WebClient</code></p></td>
<td class="tableblock halign-left valign-top"><p> </p></td>
<td class="tableblock halign-left valign-top"><p>WebClient configuration used for outbound requests to the identity server. This configuration sets the values to the OIDC WebClient default configuration</p></td>
</tr>
</tbody>
</table>

###### Deprecated Options

| Key | Kind | Type | Default Value | Description |
|----|----|----|----|----|
| <span id="af9976-proxy-host"></span> `proxy-host` | `VALUE` | `String` |   | Proxy host to use |
| <span id="aa965f-proxy-protocol"></span> `proxy-protocol` | `VALUE` | `String` | `http` | Proxy protocol to use when proxy is used |
| <span id="abf0b4-relative-uris"></span> `relative-uris` | `VALUE` | `Boolean` | `false` | Can be set to `true` to force the use of relative URIs in all requests, regardless of the presence or absence of proxies or no-proxy lists |

#### Example code

See the [example](%7Bhelidon-github-examples-url%7D/security/idcs-login) on GitHub.

Configuration example

``` highlight
security:
  providers:
  - oidc:
      client-id: "client-id-of-this-service"
      client-secret: "${CLEAR=changeit}"
      identity-uri: "https://your-tenant.identity-server.com"
      frontend-uri: "http://my-service:8080"
      audience: "http://my-service"
      outbound:
        - name: "internal-services"
          hosts: ["*.example.org"]
          outbound-token:
            header: "X-Internal-Auth"
```

#### How does it work?

At Helidon startup, if OIDC provider is configured, the following will happen:

1.  `client-id`, `client-secret`, and `identityUri` are validated - these must provide values

2.  Unless all resources are configured as local resources, the provider attempts to contact the `oidc-metadata.resource` endpoint to retrieve all endpoints

At runtime, depending on configuration…​

If a request comes without a token or with insufficient scopes:

1.  If `redirect` is set to `true` (default), request is redirected to the authorization endpoint of the identity server. If set to false, `401` is returned

2.  User authenticates against the identity server

3.  The identity server redirects back to Helidon service with a code

4.  Helidon service contacts the identity server’s token endpoint, to exchange the code for a JWT

5.  The JWT is stored in a cookie (if cookie support is enabled, which it is by default)

6.  Helidon service redirects to original endpoint (on itself)

Helidon obtains a token from request (from cookie, header, or query parameter):

1.  Token is parsed as a singed JWT

2.  We validate the JWT signature either against local JWK or against the identity server’s introspection endpoint depending on configuration

3.  We validate the issuer and audience of the token if it matches the configured values

4.  A subject is created from the JWT, including scopes from the token

5.  We validate that we have sufficient scopes to proceed, and return `403` if not

6.  Handling is returned to security to process other security providers

#### Multiple tenants

The OIDC provider also supports multiple tenants. To enable this feature, it is required to do several steps.

1.  To enable the default multi-tenant support, add the `multi-tenant: true` option to the OIDC provider configuration

2.  Specify the desired way to provide the tenant name. This step is done over adding the `tenant-id-style` configuration option. For more information, see the table below

3.  Add the tenants section to the OIDC provider configuration

``` highlight
tenants:
   - name: "example-tenant"
     # ... tenant configuration options
```

There are four ways to provide the required tenant information to Helidon by default.

<table class="tableblock frame-all grid-all stretch">
<caption>Table 1. Possible <code>tenant-id-style</code> configuration options</caption>
<colgroup>
<col style="width: 22%" />
<col style="width: 44%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th class="tableblock halign-left valign-top">key</th>
<th class="tableblock halign-left valign-top">description</th>
<th class="tableblock halign-left valign-top">additional config options</th>
</tr>
</thead>
<tbody>
<tr>
<td class="tableblock halign-left valign-top"><p><code>host-header</code></p></td>
<td class="tableblock halign-left valign-top"><p>Tenant configuration will be selected based on your host present in the <code>Host</code> header value.</p></td>
<td class="tableblock halign-left valign-top"><p> </p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p><code>domain</code></p></td>
<td class="tableblock halign-left valign-top"><p>Similar to the <code>host-header</code> style, but now the tenant name is identified just as a part of the host name. By default, it selects the third domain level.</p>
<p>Example: Host header value from inbound request is <code>my.helidon.com</code> → domain level 3 is <code>my</code>, domain level 2 is <code>helidon</code> and domain level 1 is <code>com</code>.</p></td>
<td class="tableblock halign-left valign-top"><pre class="highlight"><code>tenant-id-domain-level: &lt;domain level&gt;</code></pre></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p><code>token-handler</code></p></td>
<td class="tableblock halign-left valign-top"><p>The tenant name information is expected to be provided through the configured custom header value.</p></td>
<td class="tableblock halign-left valign-top"><pre class="highlight"><code>tenant-id-handler:
  header: &quot;my-custom-header&quot;</code></pre></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p><code>none</code></p></td>
<td class="tableblock halign-left valign-top"><p>No tenant name finding is used. Default tenant name <code>@default</code> is used instead.</p></td>
<td class="tableblock halign-left valign-top"></td>
</tr>
</tbody>
</table>

You can also implement a custom way of discovering the tenant name and tenant configuration. The custom tenant name discovery from request can be done by implementing SPI:

`io.helidon.security.providers.oidc.common.spi.TenantIdProvider`

and the custom tenant configuration discovery can be provided by implementing SPI:

`io.helidon.security.providers.oidc.common.spi.TenantConfigProvider`

##### Available tenant config options

###### Configuration options

| Key | Kind | Type | Default Value | Description |
|----|----|----|----|----|
| <span id="a2e4f7-audience"></span> `audience` | `VALUE` | `String` |   | Audience of issued tokens |
| <span id="a37c39-authorization-endpoint-uri"></span> `authorization-endpoint-uri` | `VALUE` | `URI` |   | URI of an authorization endpoint used to redirect users to for logging-in |
| <span id="ad0521-base-scopes"></span> `base-scopes` | `VALUE` | `String` | `openid` | Configure base scopes |
| <span id="a7bcb9-check-audience"></span> `check-audience` | `VALUE` | `Boolean` | `true` | Configure audience claim check |
| <span id="a67ded-client-id"></span> `client-id` | `VALUE` | `String` |   | Client ID as generated by OIDC server |
| <span id="abd29e-client-secret"></span> `client-secret` | `VALUE` | `String` |   | Client secret as generated by OIDC server |
| <span id="a3942e-client-timeout-millis"></span> `client-timeout-millis` | `VALUE` | `Duration` | `30000` | Timeout of calls using web client |
| <span id="a989a6-decryption-keys-resource"></span> [`decryption-keys.resource`](../../../config/io_helidon_common_configurable_Resource.md) | `VALUE` | `i.h.c.c.Resource` |   | A resource pointing to JWK with private keys used for JWE content key decryption |
| <span id="aea75b-identity-uri"></span> `identity-uri` | `VALUE` | `URI` |   | URI of the identity server, base used to retrieve OIDC metadata |
| <span id="a0f21f-introspect-endpoint-uri"></span> `introspect-endpoint-uri` | `VALUE` | `URI` |   | Endpoint to use to validate JWT |
| <span id="aa6493-issuer"></span> `issuer` | `VALUE` | `String` |   | Issuer of issued tokens |
| <span id="aaf0a0-name"></span> `name` | `VALUE` | `String` |   | Name of the tenant |
| <span id="a14def-oidc-metadata-well-known"></span> `oidc-metadata-well-known` | `VALUE` | `Boolean` | `true` | If set to true, metadata will be loaded from default (well known) location, unless it is explicitly defined using oidc-metadata-resource |
| <span id="a23e2c-oidc-metadata-resource"></span> [`oidc-metadata.resource`](../../../config/io_helidon_common_configurable_Resource.md) | `VALUE` | `i.h.c.c.Resource` |   | Resource configuration for OIDC Metadata containing endpoints to various identity services, as well as information about the identity server |
| <span id="ac2900-optional-audience"></span> `optional-audience` | `VALUE` | `Boolean` | `false` | Allow audience claim to be optional |
| <span id="aa8075-scope-audience"></span> `scope-audience` | `VALUE` | `String` |   | Audience of the scope required by this application |
| <span id="af12f3-server-type"></span> `server-type` | `VALUE` | `String` | `@default` | Configure one of the supported types of identity servers |
| <span id="a8cb9d-sign-jwk-resource"></span> [`sign-jwk.resource`](../../../config/io_helidon_common_configurable_Resource.md) | `VALUE` | `i.h.c.c.Resource` |   | A resource pointing to JWK with public keys of signing certificates used to validate JWT |
| <span id="aa5a6b-token-endpoint-auth"></span> [`token-endpoint-auth`](../../../config/io_helidon_security_providers_oidc_common_OidcConfig_ClientAuthentication.md) | `VALUE` | `i.h.s.p.o.c.O.ClientAuthentication` | `CLIENT_SECRET_BASIC` | Type of authentication to use when invoking the token endpoint |
| <span id="a3ab59-token-endpoint-uri"></span> `token-endpoint-uri` | `VALUE` | `URI` |   | URI of a token endpoint used to obtain a JWT based on the authentication code |
| <span id="aa43d0-validate-jwt-with-jwk"></span> `validate-jwt-with-jwk` | `VALUE` | `Boolean` | `true` | Use JWK (a set of keys to validate signatures of JWT) to validate tokens |

##### How does that work?

Multi-tenant support requires to obtain tenant name from the incoming request. OIDC configuration is selected based on the received tenant name. The way this tenant name has to be provided is configured via `tenant-id-style` configuration. See [How to enable tenants](#tenant-enable) for more information. After matching tenant configuration with the received name, the rest of the OIDC flow if exactly the same as in [How does OIDC work](#oidc-workflow).

Base OIDC configuration is treated as a default tenant, which is used, if no tenant name is provided. This default tenant is having `@default` name specified.

It is also important to note, that each tenant configuration is based on the default tenant configuration (base OIDC configuration), and therefore its configuration do not need to change all the properties, if they do not differ from the base OIDC configuration.

### CORS Settings

CORS is (now) a single component configured either through config (key `cors`), or programmatically via `io.helidon.webserver.cors.CorsFeature`. To add proper CORS setup for the OIDC endpoint, use one of these. Component specific CORS setup will be removed from Helidon.
