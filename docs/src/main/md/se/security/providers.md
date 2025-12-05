# Implemented Security Providers

Helidon provides the following security providers for endpoint
protection:

| Provider | Type | Outbound supported | Description |
|----|----|----|----|
| [OIDC Provider](#_oidc_provider) | Authentication | ✅ | Open ID Connect supporting JWT, Scopes, Groups and OIDC code flow |
| [HTTP Basic Authentication](#_http_basic_authentication_provider) | Authentication | ✅ | HTTP Basic Authentication support |
| [HTTP Digest Authentication](#_http_digest_authentication_provider) | Authentication | 🚫 | HTTP Digest Authentication support |
| [Header Assertion](#_header_authentication_provider) | Authentication | ✅ | Asserting a user based on a header value |
| [HTTP Signatures](#_http_signatures_provider) | Authentication | ✅ | Protecting service to service communication through signatures |
| [IDCS Roles](#_idcs_role_mapper) | Role Mapping | 🚫 | Retrieves roles from IDCS provider for authenticated user |
| [ABAC Authorization](#_abac_provider) | Authorization | 🚫 | Attribute based access control authorization policies |

The following providers are no longer evolved:

| Provider | Type | Outbound supported | Description |
|----|----|----|----|
| [Google Login](#_google_login_provider) | Authentication | ✅ | **Deprecated**! Authenticates a token from request against Google servers |
| [JWT Provider](#_jwt_provider) | Authentication | ✅ | JWT tokens passed from frontend |

# OIDC Provider

Open ID Connect security provider.

## Maven Coordinates

<div class="formalpara">

<div class="title">

Maven dependency

</div>

``` xml
<dependency>
    <groupId>io.helidon.security.providers</groupId>
    <artifactId>helidon-security-providers-oidc</artifactId>
</dependency>
```

</div>

### Overview

In Helidon SE, we need to register the redirection support with routing
(in addition to `SecurityFeature` that integrates with `WebServer`).
This is not required when `redirect` is set to false.

<div class="formalpara">

<div class="title">

Adding support for OIDC redirects

</div>

``` java
WebServer.builder()
        .addFeature(SecurityFeature.builder()
                            .config(config.get("security"))
                            .build())
        .routing(r -> r.addFeature(OidcFeature.create(config)))
        .build();
```

</div>

Open ID Connect security provider

Type:
[io.helidon.security.providers.oidc.OidcProvider](/apidocs/io.helidon.security.providers.oidc/io/helidon/security/providers/oidc/OidcProvider.html)

<div class="formalpara">

<div class="title">

Config key

</div>

``` text
oidc
```

</div>

This type provides the following service implementations:

- `io.helidon.security.spi.AuthenticationProvider`

- `io.helidon.security.spi.SecurityProvider`

### Configuration options

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
style="text-align: left;"><p><code>access-token-ip-check</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Whether to check if current IP address
matches the one access token was issued for. This check helps with
cookie replay attack prevention.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>audience</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Audience of issued tokens.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>authorization-endpoint-uri</code></p></td>
<td style="text-align: left;"><p>URI</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>URI of an authorization endpoint used
to redirect users to for logging-in.</p>
<p>If not defined, it is obtained from oidcMetadata(Resource), if that
is not defined an attempt is made to use
identityUri(URI)/oauth2/v1/authorize.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>base-scopes</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p><code>openid</code></p></td>
<td style="text-align: left;"><p>Configure base scopes. By default, this
is DEFAULT_BASE_SCOPES. If scope has a qualifier, it must be used
here.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>check-audience</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Configure audience claim
check.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>client-credentials-config</code></p></td>
<td style="text-align: left;"><p><a
href="../../config/io_helidon_security_providers_oidc_common_ClientCredentialsConfig.xml">ClientCredentialsConfig</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Set the configuration related to the
client credentials flow.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>client-id</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Client ID as generated by OIDC
server.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>client-secret</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Client secret as generated by OIDC
server. Used to authenticate this application with the server when
requesting JWT based on a code.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>client-timeout-millis</code></p></td>
<td style="text-align: left;"><p>Duration</p></td>
<td style="text-align: left;"><p><code>30000</code></p></td>
<td style="text-align: left;"><p>Timeout of calls using web
client.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>cookie-domain</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Domain the cookie is valid for. Not
used by default.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>cookie-encryption-enabled</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>false</code></p></td>
<td style="text-align: left;"><p>Whether to encrypt token cookie created
by this microservice. Defaults to <code>false</code>.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>cookie-encryption-id-enabled</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Whether to encrypt id token cookie
created by this microservice. Defaults to <code>true</code>.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>cookie-encryption-name</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Name of the encryption configuration
available through Security.encrypt(String, byte[]) and
Security.decrypt(String, String). If configured and encryption is
enabled for any cookie, Security MUST be configured in global or current
<code>io.helidon.common.context.Context</code> (this is done
automatically in Helidon MP).</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>cookie-encryption-password</code></p></td>
<td style="text-align: left;"><p>char[]</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Master password for
encryption/decryption of cookies. This must be configured to the same
value on each microservice using the cookie.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>cookie-encryption-refresh-enabled</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Whether to encrypt refresh token cookie
created by this microservice. Defaults to <code>true</code>.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>cookie-encryption-state-enabled</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Whether to encrypt state cookie created
by this microservice. Defaults to <code>true</code>.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>cookie-encryption-tenant-enabled</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Whether to encrypt tenant name cookie
created by this microservice. Defaults to <code>true</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>cookie-http-only</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>When using cookie, if set to true, the
HttpOnly attribute will be configured. Defaults to
OidcCookieHandler.Builder.DEFAULT_HTTP_ONLY.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>cookie-max-age-seconds</code></p></td>
<td style="text-align: left;"><p>long</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>When using cookie, used to set MaxAge
attribute of the cookie, defining how long the cookie is valid. Not used
by default.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>cookie-name</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p><code>JSESSIONID</code></p></td>
<td style="text-align: left;"><p>Name of the cookie to use. Defaults to
DEFAULT_COOKIE_NAME.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>cookie-name-id-token</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p><code>JSESSIONID_2</code></p></td>
<td style="text-align: left;"><p>Name of the cookie to use for id token.
Defaults to DEFAULT_COOKIE_NAME_2.</p>
<p>This cookie is only used when logout is enabled, as otherwise it is
not needed. Content of this cookie is encrypted.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>cookie-name-refresh-token</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p><code>JSESSIONID_3</code></p></td>
<td style="text-align: left;"><p>The name of the cookie to use for the
refresh token. Defaults to DEFAULT_REFRESH_COOKIE_NAME.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>cookie-name-state</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p><code>JSESSIONID_3</code></p></td>
<td style="text-align: left;"><p>The name of the cookie to use for the
state storage. Defaults to DEFAULT_STATE_COOKIE_NAME.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>cookie-name-tenant</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p><code>HELIDON_TENANT</code></p></td>
<td style="text-align: left;"><p>The name of the cookie to use for the
tenant name. Defaults to DEFAULT_TENANT_COOKIE_NAME.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>cookie-path</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p><code>/</code></p></td>
<td style="text-align: left;"><p>Path the cookie is valid for. Defaults
to "/".</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>cookie-same-site</code></p></td>
<td style="text-align: left;"><p>SameSite (LAX, STRICT, NONE)</p></td>
<td style="text-align: left;"><p><code>LAX</code></p></td>
<td style="text-align: left;"><p>When using cookie, used to set the
SameSite cookie value. Can be "Strict" or "Lax".</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>cookie-secure</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>false</code></p></td>
<td style="text-align: left;"><p>When using cookie, if set to true, the
Secure attribute will be configured. Defaults to false.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>cookie-use</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Whether to use cookie to store JWT
between requests. Defaults to DEFAULT_COOKIE_USE.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>cors</code></p></td>
<td style="text-align: left;"><p><a
href="../../config/io_helidon_cors_CrossOriginConfig.xml">CrossOriginConfig</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Assign cross-origin resource sharing
settings.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>force-https-redirects</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>false</code></p></td>
<td style="text-align: left;"><p>Force HTTPS for redirects to identity
provider. Defaults to <code>false</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>frontend-uri</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Full URI of this application that is
visible from user browser. Used to redirect request back from identity
server after successful login.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>header-token</code></p></td>
<td style="text-align: left;"><p><a
href="../../config/io_helidon_security_util_TokenHandler.xml">TokenHandler</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>A TokenHandler to process header
containing a JWT. Default is "Authorization" header with a prefix
"bearer ".</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>header-use</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Whether to expect JWT in a header
field.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>id-token-signature-validation</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Whether id token signature check should
be enabled. Signature check is enabled by default, and it is highly
recommended to not change that. Change this setting only when you really
know what you are doing, otherwise it could case security
issues.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>identity-uri</code></p></td>
<td style="text-align: left;"><p>URI</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>URI of the identity server, base used
to retrieve OIDC metadata.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>introspect-endpoint-uri</code></p></td>
<td style="text-align: left;"><p>URI</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Endpoint to use to validate JWT. Either
use this or set signJwk(JwkKeys) or signJwk(Resource).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>issuer</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Issuer of issued tokens.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>max-redirects</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p><code>5</code></p></td>
<td style="text-align: left;"><p>Configure maximal number of redirects
when redirecting to an OIDC provider within a single authentication
attempt.</p>
<p>Defaults to DEFAULT_MAX_REDIRECTS</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>oidc-metadata-well-known</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>If set to true, metadata will be loaded
from default (well known) location, unless it is explicitly defined
using oidc-metadata-resource. If set to false, it would not be loaded
even if oidc-metadata-resource is not defined. In such a case all URIs
must be explicitly defined (e.g. token-endpoint-uri).</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>oidc-metadata.resource</code></p></td>
<td style="text-align: left;"><p><a
href="../../config/io_helidon_common_configurable_Resource.xml">Resource</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Resource configuration for OIDC
Metadata containing endpoints to various identity services, as well as
information about the identity server.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>optional</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>false</code></p></td>
<td style="text-align: left;"><p>Whether authentication is required. By
default, request will fail if the authentication cannot be verified. If
set to true, request will process and this provider will
abstain.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>optional-audience</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>false</code></p></td>
<td style="text-align: left;"><p>Allow audience claim to be
optional.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>outbound</code></p></td>
<td style="text-align: left;"><p><a
href="../../config/io_helidon_security_providers_common_OutboundTarget.xml">OutboundTarget[]</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Add a new target
configuration.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>pkce-challenge-method</code></p></td>
<td style="text-align: left;"><p>PkceChallengeMethod (PLAIN,
S256)</p></td>
<td style="text-align: left;"><p><code>S256</code></p></td>
<td style="text-align: left;"><p>Proof Key Code Exchange (PKCE)
challenge creation method. Default value is
PkceChallengeMethod.S256.</p>
<p>Allowed values:</p>
<ul>
<li><p><code>PLAIN</code>: No hashing will be applied. Challenge string
will be the same as verifier.</p></li>
<li><p><code>S256</code>: SHA-256 algorithm is used to hash the verifier
value.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>pkce-enabled</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>false</code></p></td>
<td style="text-align: left;"><p>Whether this provider should support
PKCE. Default value is <code>false</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>propagate</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>false</code></p></td>
<td style="text-align: left;"><p>Whether to propagate identity.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><span
class="line-through"><code>proxy-host</code></span></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p><strong>Deprecated</strong> Proxy host
to use. When defined, triggers usage of proxy for HTTP requests. Setting
to empty String has the same meaning as setting to null - disables
proxy.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>proxy-port</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p><code>80</code></p></td>
<td style="text-align: left;"><p>Proxy port. Defaults to
DEFAULT_PROXY_PORT</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><span
class="line-through"><code>proxy-protocol</code></span></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p><code>http</code></p></td>
<td style="text-align: left;"><p><strong>Deprecated</strong> Proxy
protocol to use when proxy is used. Defaults to
DEFAULT_PROXY_PROTOCOL.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>query-id-token-param-name</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p><code>id_token</code></p></td>
<td style="text-align: left;"><p>Name of a query parameter that contains
the JWT id token when parameter is used.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>query-param-name</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p><code>accessToken</code></p></td>
<td style="text-align: left;"><p>Name of a query parameter that contains
the JWT access token when parameter is used.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>query-param-tenant-name</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p><code>h_tenant</code></p></td>
<td style="text-align: left;"><p>Name of a query parameter that contains
the tenant name when the parameter is used. Defaults to
DEFAULT_TENANT_PARAM_NAME.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>query-param-use</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>false</code></p></td>
<td style="text-align: left;"><p>Whether to use a query parameter to
send JWT token from application to this server.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>redirect</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>false</code></p></td>
<td style="text-align: left;"><p>By default, the client should redirect
to the identity server for the user to log in. This behavior can be
overridden by setting redirect to false. When token is not present in
the request, the client will not redirect and just return appropriate
error response code.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>redirect-attempt-param</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p><code>h_ra</code></p></td>
<td style="text-align: left;"><p>Configure the parameter used to store
the number of attempts in redirect.</p>
<p>Defaults to DEFAULT_ATTEMPT_PARAM</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>redirect-uri</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p><code>/oidc/redirect</code></p></td>
<td style="text-align: left;"><p>URI to register web server component
on, used by the OIDC server to redirect authorization requests to after
a user logs in or approves scopes. Note that usually the redirect URI
configured here must be the same one as configured on OIDC server.</p>
<p>Defaults to DEFAULT_REDIRECT_URI</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><span
class="line-through"><code>relative-uris</code></span></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>false</code></p></td>
<td style="text-align: left;"><p><strong>Deprecated</strong> Can be set
to <code>true</code> to force the use of relative URIs in all requests,
regardless of the presence or absence of proxies or no-proxy lists. By
default, requests that use the Proxy will have absolute URIs. Set this
flag to <code>true</code> if the host is unable to accept absolute URIs.
Defaults to DEFAULT_RELATIVE_URIS.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scope-audience</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Audience of the scope required by this
application. This is prefixed to the scope name when requesting scopes
from the identity server. Defaults to empty string.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>server-type</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p><code>@default</code></p></td>
<td style="text-align: left;"><p>Configure one of the supported types of
identity servers.</p>
<p>If the type does not have an explicit mapping, a warning is logged
and the default implementation is used.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>sign-jwk.resource</code></p></td>
<td style="text-align: left;"><p><a
href="../../config/io_helidon_common_configurable_Resource.xml">Resource</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>A resource pointing to JWK with public
keys of signing certificates used to validate JWT.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>tenants</code></p></td>
<td style="text-align: left;"><p><a
href="../../config/io_helidon_security_providers_oidc_common_TenantConfig.xml">TenantConfig</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Configurations of the tenants</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>token-endpoint-auth</code></p></td>
<td style="text-align: left;"><p>ClientAuthentication
(CLIENT_SECRET_BASIC, CLIENT_SECRET_POST, CLIENT_SECRET_JWT,
PRIVATE_KEY_JWT, CLIENT_CERTIFICATE, NONE)</p></td>
<td
style="text-align: left;"><p><code>CLIENT_SECRET_BASIC</code></p></td>
<td style="text-align: left;"><p>Type of authentication to use when
invoking the token endpoint. Current supported options:</p>
<ul>
<li><p>io.helidon.security.providers.oidc.common.OidcConfig.ClientAuthentication.CLIENT_SECRET_BASIC</p></li>
<li><p>io.helidon.security.providers.oidc.common.OidcConfig.ClientAuthentication.CLIENT_SECRET_POST</p></li>
<li><p>io.helidon.security.providers.oidc.common.OidcConfig.ClientAuthentication.NONE</p></li>
</ul>
<p>Allowed values:</p>
<ul>
<li><p><code>CLIENT_SECRET_BASIC</code>: Clients that have received a
client_secret value from the Authorization Server authenticate with the
Authorization Server in accordance with Section 2.3.1 of OAuth 2.0
[RFC6749] using the HTTP Basic authentication scheme. This is the
default client authentication.</p></li>
<li><p><code>CLIENT_SECRET_POST</code>: Clients that have received a
client_secret value from the Authorization Server, authenticate with the
Authorization Server in accordance with Section 2.3.1 of OAuth 2.0
[RFC6749] by including the Client Credentials in the request
body.</p></li>
<li><p><code>CLIENT_SECRET_JWT</code>: Clients that have received a
client_secret value from the Authorization Server create a JWT using an
HMAC SHA algorithm, such as HMAC SHA-256. The HMAC (Hash-based Message
Authentication Code) is calculated using the octets of the UTF-8
representation of the client_secret as the shared key. The Client
authenticates in accordance with JSON Web Token (JWT) Profile for OAuth
2.0 Client Authentication and Authorization Grants [OAuth.JWT] and
Assertion Framework for OAuth 2.0 Client Authentication and
Authorization Grants [OAuth.Assertions].</p></li>
</ul>
<p>The JWT MUST contain the following REQUIRED Claim Values and MAY
contain the following OPTIONAL Claim Values.</p>
<p>Required: <code>iss, sub, aud, jti, exp</code></p>
<p>Optional: <code>iat</code> - <code>PRIVATE_KEY_JWT</code>: Clients
that have registered a public key sign a JWT using that key. The Client
authenticates in accordance with JSON Web Token (JWT) Profile for OAuth
2.0 Client Authentication and Authorization Grants [OAuth.JWT] and
Assertion Framework for OAuth 2.0 Client Authentication and
Authorization Grants [OAuth.Assertions].</p>
<p>The JWT MUST contain the following REQUIRED Claim Values and MAY
contain the following OPTIONAL Claim Values.</p>
<p>Required: <code>iss, sub, aud, jti, exp</code></p>
<p>Optional: <code>iat</code> - <code>CLIENT_CERTIFICATE</code>:
Authentication is done via the client certificate used with MTLS. The
Returned access token is bound to this client certificate. The Client
needs to have MTLS enabled for the OIDC. - <code>NONE</code>: The Client
does not authenticate itself at the Token Endpoint, either because it
uses only the Implicit Flow (and so does not use the Token Endpoint) or
because it is a Public Client with no Client Secret or other
authentication mechanism.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>token-endpoint-uri</code></p></td>
<td style="text-align: left;"><p>URI</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>URI of a token endpoint used to obtain
a JWT based on the authentication code. If not defined, it is obtained
from oidcMetadata(Resource), if that is not defined an attempt is made
to use identityUri(URI)/oauth2/v1/token.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>token-signature-validation</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Whether access token signature check
should be enabled. Signature check is enabled by default, and it is
highly recommended to not change that. Change this setting only when you
really know what you are doing, otherwise it could case security
issues.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>use-jwt-groups</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Claim <code>groups</code> from JWT will
be used to automatically add groups to current subject (may be used with
jakarta.annotation.security.RolesAllowed annotation).</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>validate-jwt-with-jwk</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Use JWK (a set of keys to validate
signatures of JWT) to validate tokens. Use this method when you want to
use default values for JWK or introspection endpoint URI.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>webclient</code></p></td>
<td style="text-align: left;"><p><a
href="../../config/io_helidon_webclient_api_WebClient.xml">WebClient</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>WebClient configuration used for
outbound requests to the identity server. This configuration sets the
values to the OIDC WebClient default configuration.</p></td>
</tr>
</tbody>
</table>

## Example code

See the
[example](https://github.com/helidon-io/helidon-examples/tree/helidon-4.x/examples/security/idcs-login)
on GitHub.

<div class="formalpara">

<div class="title">

Configuration example

</div>

``` yaml
security:
  providers:
  - oidc:
      client-id: "client-id-of-this-service"
      client-secret: "${CLEAR=changeit}"
      identity-uri: "https://your-tenant.identity-server.com"
      frontend-uri: "http://my-service:8080"
      audience: "http://my-service"
      cors:
        allow-origins: ["https://foo.com", "https://there.com"]
        allow-methods: ["PUT", "DELETE"]
      outbound:
        - name: "internal-services"
          hosts: ["*.example.org"]
          outbound-token:
            header: "X-Internal-Auth"
```

</div>

## How does it work?

At Helidon startup, if OIDC provider is configured, the following will
happen:

1.  `client-id`, `client-secret`, and `identityUri` are validated -
    these must provide values

2.  Unless all resources are configured as local resources, the provider
    attempts to contact the `oidc-metadata.resource` endpoint to
    retrieve all endpoints

At runtime, depending on configuration…​

If a request comes without a token or with insufficient scopes:

1.  If `redirect` is set to `true` (default), request is redirected to
    the authorization endpoint of the identity server. If set to false,
    `401` is returned

2.  User authenticates against the identity server

3.  The identity server redirects back to Helidon service with a code

4.  Helidon service contacts the identity server’s token endpoint, to
    exchange the code for a JWT

5.  The JWT is stored in a cookie (if cookie support is enabled, which
    it is by default)

6.  Helidon service redirects to original endpoint (on itself)

Helidon obtains a token from request (from cookie, header, or query
parameter):

1.  Token is parsed as a singed JWT

2.  We validate the JWT signature either against local JWK or against
    the identity server’s introspection endpoint depending on
    configuration

3.  We validate the issuer and audience of the token if it matches the
    configured values

4.  A subject is created from the JWT, including scopes from the token

5.  We validate that we have sufficient scopes to proceed, and return
    `403` if not

6.  Handling is returned to security to process other security providers

## Multiple tenants

The OIDC provider also supports multiple tenants. To enable this
feature, it is required to do several steps.

1.  To enable the default multi-tenant support, add the
    `multi-tenant: true` option to the OIDC provider configuration

2.  Specify the desired way to provide the tenant name. This step is
    done over adding the `tenant-id-style` configuration option. For
    more information, see the table below

3.  Add the tenants section to the OIDC provider configuration

``` yaml
tenants:
   - name: "example-tenant"
     # ... tenant configuration options
```

There are four ways to provide the required tenant information to
Helidon by default.

<table>
<caption>Possible <code>tenant-id-style</code> configuration
options</caption>
<colgroup>
<col style="width: 22%" />
<col style="width: 44%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">key</th>
<th style="text-align: left;">description</th>
<th style="text-align: left;">additional config options</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>host-header</code></p></td>
<td style="text-align: left;"><p>Tenant configuration will be selected
based on your host present in the <code>Host</code> header
value.</p></td>
<td style="text-align: left;"><p> </p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>domain</code></p></td>
<td style="text-align: left;"><p>Similar to the <code>host-header</code>
style, but now the tenant name is identified just as a part of the host
name. By default, it selects the third domain level.</p>
<p>Example: Host header value from inbound request is
<code>my.helidon.com</code> → domain level 3 is <code>my</code>, domain
level 2 is <code>helidon</code> and domain level 1 is
<code>com</code>.</p></td>
<td style="text-align: left;"><div class="sourceCode" id="cb1"><pre
class="sourceCode yaml"><code class="sourceCode yaml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">tenant-id-domain-level</span><span class="kw">:</span><span class="at"> &lt;domain level&gt;</span></span></code></pre></div></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>token-handler</code></p></td>
<td style="text-align: left;"><p>The tenant name information is expected
to be provided through the configured custom header value.</p></td>
<td style="text-align: left;"><div class="sourceCode" id="cb2"><pre
class="sourceCode yaml"><code class="sourceCode yaml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a><span class="fu">tenant-id-handler</span><span class="kw">:</span></span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a><span class="at">  </span><span class="fu">header</span><span class="kw">:</span><span class="at"> </span><span class="st">&quot;my-custom-header&quot;</span></span></code></pre></div></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>none</code></p></td>
<td style="text-align: left;"><p>No tenant name finding is used. Default
tenant name <code>@default</code> is used instead.</p></td>
<td style="text-align: left;"></td>
</tr>
</tbody>
</table>

You can also implement a custom way of discovering the tenant name and
tenant configuration. The custom tenant name discovery from request can
be done by implementing SPI:

`io.helidon.security.providers.oidc.common.spi.TenantIdProvider`

and the custom tenant configuration discovery can be provided by
implementing SPI:

`io.helidon.security.providers.oidc.common.spi.TenantConfigProvider`

### Available tenant config options

Open ID Connect tenant configuration

Type:
[io.helidon.security.providers.oidc.common.TenantConfig](/apidocs/io.helidon.security.providers.oidc.common/io/helidon/security/providers/oidc/common/TenantConfig.html)

#### Configuration options

| key    | type   | default value | description         |
|--------|--------|---------------|---------------------|
| `name` | string |               | Name of the tenant. |

Required configuration options

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
<td style="text-align: left;"><p><code>audience</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Audience of issued tokens.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>authorization-endpoint-uri</code></p></td>
<td style="text-align: left;"><p>URI</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>URI of an authorization endpoint used
to redirect users to for logging-in.</p>
<p>If not defined, it is obtained from oidcMetadata(Resource), if that
is not defined an attempt is made to use
identityUri(URI)/oauth2/v1/authorize.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>base-scopes</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p><code>openid</code></p></td>
<td style="text-align: left;"><p>Configure base scopes. By default, this
is DEFAULT_BASE_SCOPES. If scope has a qualifier, it must be used
here.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>check-audience</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Configure audience claim
check.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>client-id</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Client ID as generated by OIDC
server.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>client-secret</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Client secret as generated by OIDC
server. Used to authenticate this application with the server when
requesting JWT based on a code.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>client-timeout-millis</code></p></td>
<td style="text-align: left;"><p>Duration</p></td>
<td style="text-align: left;"><p><code>30000</code></p></td>
<td style="text-align: left;"><p>Timeout of calls using web
client.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>identity-uri</code></p></td>
<td style="text-align: left;"><p>URI</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>URI of the identity server, base used
to retrieve OIDC metadata.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>introspect-endpoint-uri</code></p></td>
<td style="text-align: left;"><p>URI</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Endpoint to use to validate JWT. Either
use this or set signJwk(JwkKeys) or signJwk(Resource).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>issuer</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Issuer of issued tokens.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>oidc-metadata-well-known</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>If set to true, metadata will be loaded
from default (well known) location, unless it is explicitly defined
using oidc-metadata-resource. If set to false, it would not be loaded
even if oidc-metadata-resource is not defined. In such a case all URIs
must be explicitly defined (e.g. token-endpoint-uri).</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>oidc-metadata.resource</code></p></td>
<td style="text-align: left;"><p><a
href="../../config/io_helidon_common_configurable_Resource.xml">Resource</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Resource configuration for OIDC
Metadata containing endpoints to various identity services, as well as
information about the identity server.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>optional-audience</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>false</code></p></td>
<td style="text-align: left;"><p>Allow audience claim to be
optional.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scope-audience</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Audience of the scope required by this
application. This is prefixed to the scope name when requesting scopes
from the identity server. Defaults to empty string.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>server-type</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p><code>@default</code></p></td>
<td style="text-align: left;"><p>Configure one of the supported types of
identity servers.</p>
<p>If the type does not have an explicit mapping, a warning is logged
and the default implementation is used.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>sign-jwk.resource</code></p></td>
<td style="text-align: left;"><p><a
href="../../config/io_helidon_common_configurable_Resource.xml">Resource</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>A resource pointing to JWK with public
keys of signing certificates used to validate JWT.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>token-endpoint-auth</code></p></td>
<td style="text-align: left;"><p>ClientAuthentication
(CLIENT_SECRET_BASIC, CLIENT_SECRET_POST, CLIENT_SECRET_JWT,
PRIVATE_KEY_JWT, CLIENT_CERTIFICATE, NONE)</p></td>
<td
style="text-align: left;"><p><code>CLIENT_SECRET_BASIC</code></p></td>
<td style="text-align: left;"><p>Type of authentication to use when
invoking the token endpoint. Current supported options:</p>
<ul>
<li><p>io.helidon.security.providers.oidc.common.OidcConfig.ClientAuthentication.CLIENT_SECRET_BASIC</p></li>
<li><p>io.helidon.security.providers.oidc.common.OidcConfig.ClientAuthentication.CLIENT_SECRET_POST</p></li>
<li><p>io.helidon.security.providers.oidc.common.OidcConfig.ClientAuthentication.NONE</p></li>
</ul>
<p>Allowed values:</p>
<ul>
<li><p><code>CLIENT_SECRET_BASIC</code>: Clients that have received a
client_secret value from the Authorization Server authenticate with the
Authorization Server in accordance with Section 2.3.1 of OAuth 2.0
[RFC6749] using the HTTP Basic authentication scheme. This is the
default client authentication.</p></li>
<li><p><code>CLIENT_SECRET_POST</code>: Clients that have received a
client_secret value from the Authorization Server, authenticate with the
Authorization Server in accordance with Section 2.3.1 of OAuth 2.0
[RFC6749] by including the Client Credentials in the request
body.</p></li>
<li><p><code>CLIENT_SECRET_JWT</code>: Clients that have received a
client_secret value from the Authorization Server create a JWT using an
HMAC SHA algorithm, such as HMAC SHA-256. The HMAC (Hash-based Message
Authentication Code) is calculated using the octets of the UTF-8
representation of the client_secret as the shared key. The Client
authenticates in accordance with JSON Web Token (JWT) Profile for OAuth
2.0 Client Authentication and Authorization Grants [OAuth.JWT] and
Assertion Framework for OAuth 2.0 Client Authentication and
Authorization Grants [OAuth.Assertions].</p></li>
</ul>
<p>The JWT MUST contain the following REQUIRED Claim Values and MAY
contain the following OPTIONAL Claim Values.</p>
<p>Required: <code>iss, sub, aud, jti, exp</code></p>
<p>Optional: <code>iat</code> - <code>PRIVATE_KEY_JWT</code>: Clients
that have registered a public key sign a JWT using that key. The Client
authenticates in accordance with JSON Web Token (JWT) Profile for OAuth
2.0 Client Authentication and Authorization Grants [OAuth.JWT] and
Assertion Framework for OAuth 2.0 Client Authentication and
Authorization Grants [OAuth.Assertions].</p>
<p>The JWT MUST contain the following REQUIRED Claim Values and MAY
contain the following OPTIONAL Claim Values.</p>
<p>Required: <code>iss, sub, aud, jti, exp</code></p>
<p>Optional: <code>iat</code> - <code>CLIENT_CERTIFICATE</code>:
Authentication is done via the client certificate used with MTLS. The
Returned access token is bound to this client certificate. The Client
needs to have MTLS enabled for the OIDC. - <code>NONE</code>: The Client
does not authenticate itself at the Token Endpoint, either because it
uses only the Implicit Flow (and so does not use the Token Endpoint) or
because it is a Public Client with no Client Secret or other
authentication mechanism.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>token-endpoint-uri</code></p></td>
<td style="text-align: left;"><p>URI</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>URI of a token endpoint used to obtain
a JWT based on the authentication code. If not defined, it is obtained
from oidcMetadata(Resource), if that is not defined an attempt is made
to use identityUri(URI)/oauth2/v1/token.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>validate-jwt-with-jwk</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Use JWK (a set of keys to validate
signatures of JWT) to validate tokens. Use this method when you want to
use default values for JWK or introspection endpoint URI.</p></td>
</tr>
</tbody>
</table>

### How does that work?

Multi-tenant support requires to obtain tenant name from the incoming
request. OIDC configuration is selected based on the received tenant
name. The way this tenant name has to be provided is configured via
`tenant-id-style` configuration. See [How to enable
tenants](#tenant-enable) for more information. After matching tenant
configuration with the received name, the rest of the OIDC flow if
exactly the same as in [How does OIDC work](#oidc-workflow).

Base OIDC configuration is treated as a default tenant, which is used,
if no tenant name is provided. This default tenant is having `@default`
name specified.

It is also important to note, that each tenant configuration is based on
the default tenant configuration (base OIDC configuration), and
therefore its configuration do not need to change all the properties, if
they do not differ from the base OIDC configuration.

# CORS Settings

As an experimental feature, you can set up cross-origin handling for the
redirect and logout endpoints in an optional `cors` block inside the
`oidc` configuration.

The table below lists the configuration keys that identify the CORS
characteristics.

| config key | type | default | description | CORS header name |
|----|----|----|----|----|
| `allow-credentials` | boolean | `false` | Sets the allow credentials flag. | `Access-Control-Allow-Credentials` |
| `allow-headers` | string\[\] | `*` | Sets the allowed headers. | `Access-Control-Allow-Headers` |
| `allow-methods` | string\[\] | `*` | Sets the allowed methods. | `Access-Control-Allow-Methods` |
| `allow-origins` | string\[\] | `*` | Sets the allowed origins. | `Access-Control-Allow-Origins` |
| `expose-headers` | string\[\] |   | Sets the expose headers. | `Access-Control-Expose-Headers` |
| `max-age-seconds` | long | `3600` | Sets the maximum age. | `Access-Control-Max-Age` |
| `enabled` | boolean | `true` | Sets whether this config should be enabled or not. | n/a |

If the cross-origin configuration is disabled (`enabled` = false), then
the Helidon CORS implementation ignores the cross-origin configuration
entry.

The following example of basic cross-origin configuration, when
explicitly loaded and used by your application code, limits cross-origin
resource sharing for `PUT` and `DELETE` operations to only `foo.com` and
`there.com`:

``` yaml
restrictive-cors:
  allow-origins: ["https://foo.com", "https://there.com"]
  allow-methods: ["PUT", "DELETE"]
```

## HTTP Basic Authentication Provider

HTTP Basic authentication support

### Setup

<div class="formalpara">

<div class="title">

Maven dependency

</div>

``` xml
<dependency>
    <groupId>io.helidon.security.providers</groupId>
    <artifactId>helidon-security-providers-http-auth</artifactId>
</dependency>
```

</div>

### Overview

HTTP Basic Authentication provider

Type:
[io.helidon.security.providers.httpauth.HttpBasicAuthProvider](/apidocs/io.helidon.security.providers.httpauth/io/helidon/security/providers/httpauth/HttpBasicAuthProvider.html)

<div class="formalpara">

<div class="title">

Config key

</div>

``` text
http-basic-auth
```

</div>

This type provides the following service implementations:

- `io.helidon.security.spi.SecurityProvider`

- `io.helidon.security.spi.AuthenticationProvider`

### Configuration options

| key | type | default value | description |
|----|----|----|----|
| `optional` | boolean | `false` | Whether authentication is required. By default, request will fail if the authentication cannot be verified. If set to false, request will process and this provider will abstain. |
| `outbound` | [OutboundTarget\[\]](../../config/io_helidon_security_providers_common_OutboundTarget.md) |   | Add a new outbound target to configure identity propagation or explicit username/password. |
| `principal-type` | SubjectType (USER, SERVICE) | `USER` | Principal type this provider extracts (and also propagates). |
| `realm` | string | `helidon` | Set the realm to use when challenging users. |
| `users` | [ConfigUser\[\]](../../config/io_helidon_security_providers_httpauth_ConfigUserStore_ConfigUser.md) |   | Set user store to validate users. Removes any other stores added through addUserStore(SecureUserStore). |

Optional configuration options

### Example code

See the
[example](https://github.com/helidon-io/helidon-examples/tree/helidon-4.x/examples/security/outbound-override)
on GitHub.

<div class="formalpara">

<div class="title">

Configuration example

</div>

``` yaml
security:
  providers:
  - http-basic-auth:
      realm: "helidon"
      users:
      - login: "john"
        password: "${CLEAR=changeit}"
        roles: ["admin"]
      - login: "jack"
        password: "changeit"
        roles: ["user", "admin"]
      outbound:
        - name: "internal-services"
          hosts: ["*.example.org"]
          # Propagates current user's identity or identity from request property
          outbound-token:
            header: "X-Internal-Auth"
        - name: "partner-service"
          hosts: ["*.partner.org"]
          # Uses this username and password
          username: "partner-user-1"
          password: "${CLEAR=changeit}"
```

</div>

### How does it work?

See <https://tools.ietf.org/html/rfc7617>.

**Authentication of request**

When a request is received without the `Authorization: basic …​.` header,
a challenge is returned to provide such authentication.

When a request is received with the `Authorization: basic …​.` header,
the username and password is validated against configured users (and
users obtained from custom service if any provided).

Subject is created based on the username and roles provided by the user
store.

**Identity propagation**

When identity propagation is configured, there are several options for
identifying username and password to propagate:

1.  We propagate the current username and password (inbound request must
    be authenticated using basic authentication).

2.  We use username and password from an explicitly configured property
    (See `EndpointConfig.PROPERTY_OUTBOUND_ID` and
    `EndpointConfig.PROPERTY_OUTBOUND_SECRET`)

3.  We use username and password associated with an outbound target (see
    example configuration above)

Identity is propagated only if:

1.  There is an outbound target configured for the endpoint

2.  Or there is an explicitly configured username/password for the
    current request (through request property)

**Custom user store**

Java service loader service
`io.helidon.security.providers.httpauth.spi.UserStoreService` can be
implemented to provide users to the provider, such as when validated
against an internal database or LDAP server. The user store is defined
so you never need the clear text password of the user.

*Warning on security of HTTP Basic Authentication (or lack thereof)*

Basic authentication uses base64 encoded username and password and
passes it over the network. Base64 is only encoding, not encryption - so
anybody that gets hold of the header value can learn the actual username
and password of the user. This is a security risk and an attack vector
that everybody should be aware of before using HTTP Basic
Authentication. We recommend using this approach only for testing and
demo purposes.

## HTTP Digest Authentication Provider

HTTP Digest authentication support

### Setup

<div class="formalpara">

<div class="title">

Maven dependency

</div>

``` xml
<dependency>
    <groupId>io.helidon.security.providers</groupId>
    <artifactId>helidon-security-providers-http-auth</artifactId>
</dependency>
```

</div>

### Overview

Http digest authentication security provider

Type:
[io.helidon.security.providers.httpauth.HttpDigestAuthProvider](/apidocs/io.helidon.security.providers.httpauth/io/helidon/security/providers/httpauth/HttpDigestAuthProvider.html)

<div class="formalpara">

<div class="title">

Config key

</div>

``` text
http-digest-auth
```

</div>

This type provides the following service implementations:

- `io.helidon.security.spi.SecurityProvider`

- `io.helidon.security.spi.AuthenticationProvider`

### Configuration options

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
<td style="text-align: left;"><p>Algorithm (MD5)</p></td>
<td style="text-align: left;"><p><code>MD5</code></p></td>
<td style="text-align: left;"><p>Digest algorithm to use.</p>
<p>Allowed values:</p>
<ul>
<li><p><code>MD5</code>: MD5 algorithm.</p></li>
</ul></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>nonce-timeout-millis</code></p></td>
<td style="text-align: left;"><p>long</p></td>
<td style="text-align: left;"><p><code>86400000</code></p></td>
<td style="text-align: left;"><p>How long will the nonce value be valid.
When timed-out, browser will re-request username/password.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>optional</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>false</code></p></td>
<td style="text-align: left;"><p>Whether authentication is required. By
default, request will fail if the authentication cannot be verified. If
set to false, request will process and this provider will
abstain.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>principal-type</code></p></td>
<td style="text-align: left;"><p>SubjectType (USER, SERVICE)</p></td>
<td style="text-align: left;"><p><code>USER</code></p></td>
<td style="text-align: left;"><p>Principal type this provider extracts
(and also propagates).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>qop</code></p></td>
<td style="text-align: left;"><p>Qop (NONE, AUTH)</p></td>
<td style="text-align: left;"><p><code>NONE</code></p></td>
<td style="text-align: left;"><p>Only <code>AUTH</code> supported. If
left empty, uses the legacy approach (older RFC version).
<code>AUTH-INT</code> is not supported.</p>
<p>Allowed values:</p>
<ul>
<li><p><code>NONE</code>: Legacy approach - used internally to parse
headers. Do not use this option when building provider. If you want to
support only legacy RFC, please use
HttpDigestAuthProvider.Builder.noDigestQop(). Only AUTH is supported, as
auth-int requires access to message body.</p></li>
<li><p><code>AUTH</code>: QOP "auth" - stands for
"authentication".</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>realm</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p><code>Helidon</code></p></td>
<td style="text-align: left;"><p>Set the realm to use when challenging
users.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>server-secret</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>The nonce is encrypted using this
secret - to make sure the nonce we get back was generated by us and to
make sure we can safely time-out nonce values. This secret must be the
same for all service instances (or all services that want to share the
same authentication). Defaults to a random password - e.g. if deployed
to multiple servers, the authentication WILL NOT WORK. You MUST provide
your own password to work in a distributed environment with non-sticky
load balancing.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>users</code></p></td>
<td style="text-align: left;"><p><a
href="../../config/io_helidon_security_providers_httpauth_ConfigUserStore_ConfigUser.xml">ConfigUser[]</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Set user store to obtain passwords and
roles based on logins.</p></td>
</tr>
</tbody>
</table>

### Example code

<div class="formalpara">

<div class="title">

Configuration example

</div>

``` yaml
security:
  providers:
  - http-digest-auth:
      realm: "helidon"
      server-secret: "${CLEAR=service-wide-secret-not-known-outside}"
      users:
      - login: "john"
        password: "${CLEAR=changeit}"
        roles: ["admin"]
      - login: "jack"
        password: "changeit"
        roles: ["user", "admin"]
```

</div>

### How does it work?

See <https://tools.ietf.org/html/rfc7616>.

**Authentication of request**

When a request is received without the `Authorization: digest …​.`
header, a challenge is returned to provide such authentication using
`WWW-Authenticate` header.

When a request is received with the `Authorization: digest …​.` header,
the request is validated against configured users (and users obtained
from custom service if any provided).

Subject is created based on the username and roles provided by the user
store.

**Custom user store**

Java service loader service
`io.helidon.security.providers.httpauth.spi.UserStoreService` can be
implemented to provide users to the provider, such as when validated
against an internal database or LDAP server. The user store is defined
so you never need the clear text password of the user.

*Note on security of HTTP Digest Authentication*

These authentication schemes should be *obsolete*, though they provide a
very easy way to test a protected resource.

## Header Authentication Provider

Asserts user or service identity based on a value of a header.

### Setup

<div class="formalpara">

<div class="title">

Maven dependency

</div>

``` xml
<dependency>
    <groupId>io.helidon.security.providers</groupId>
    <artifactId>helidon-security-providers-header</artifactId>
</dependency>
```

</div>

### Overview

Security provider that extracts a username (or service name) from a
header.

Type:
[io.helidon.security.providers.header.HeaderAtnProvider](/apidocs/io.helidon.security.providers.header/io/helidon/security/providers/header/HeaderAtnProvider.html)

<div class="formalpara">

<div class="title">

Config key

</div>

``` text
header-atn
```

</div>

This type provides the following service implementations:

- `io.helidon.security.spi.SecurityProvider`

- `io.helidon.security.spi.AuthenticationProvider`

### Configuration options

| key | type | default value | description |
|----|----|----|----|
| `atn-token` | [TokenHandler](../../config/io_helidon_security_util_TokenHandler.md) |   | Token handler to extract username from request. |
| `authenticate` | boolean | `true` | Whether to authenticate requests. |
| `optional` | boolean | `false` | Whether authentication is required. By default, request will fail if the username cannot be extracted. If set to false, request will process and this provider will abstain. |
| `outbound` | [OutboundTarget\[\]](../../config/io_helidon_security_providers_common_OutboundTarget.md) |   | Configure outbound target for identity propagation. |
| `outbound-token` | [TokenHandler](../../config/io_helidon_security_util_TokenHandler.md) |   | Token handler to create outbound headers to propagate identity. If not defined, atnTokenHandler will be used. |
| `principal-type` | SubjectType (USER, SERVICE) | `USER` | Principal type this provider extracts (and also propagates). |
| `propagate` | boolean | `false` | Whether to propagate identity. |

Optional configuration options

### Example code

<div class="formalpara">

<div class="title">

Configuration example

</div>

``` yaml
security:
  providers:
    header-atn:
      atn-token:
        header: "X-AUTH-USER"
      outbound:
        - name: "internal-services"
          hosts: ["*.example.org"]
          # propagates the current user or service id using the same header as authentication
        - name: "partner-service"
          hosts: ["*.partner.org"]
          # propagates an explicit username in a custom header
          username: "service-27"
          outbound-token:
            header: "X-Service-Auth"
```

</div>

### How does it work?

This provider inspects a specified request header and extracts the
username/service name from it and asserts it as current subject’s
principal.

This can be used when we use perimeter authentication (e.g. there is a
gateway that takes care of authentication and propagates the user in a
header).

**Identity propagation**

Identity is propagated only if an outbound target matches the target
service.

The following options exist when propagating identity: 1. We propagate
the current username using the configured header 2. We use username
associated with an outbound target (see example configuration above)

**Caution**

When using this provider, you must be sure the header cannot be
explicitly configured by a user or another service. All requests should
go through a gateway that removes this header from inbound traffic, and
only configures it for authenticated users/services. Another option is
to use this with fully trusted parties (such as services within a single
company, on a single protected network not accessible to any users), and
of course for testing and demo purposes.

## HTTP Signatures Provider

Support for HTTP Signatures.

### Setup

<div class="formalpara">

<div class="title">

Maven dependency

</div>

``` xml
<dependency>
    <groupId>io.helidon.security.providers</groupId>
    <artifactId>helidon-security-providers-http-sign</artifactId>
</dependency>
```

</div>

### Overview

HTTP header signature provider.

Type:
[io.helidon.security.providers.httpsign.HttpSignProvider](/apidocs/io.helidon.security.providers.httpsign/io/helidon/security/providers/httpsign/HttpSignProvider.html)

<div class="formalpara">

<div class="title">

Config key

</div>

``` text
http-signatures
```

</div>

This type provides the following service implementations:

- `io.helidon.security.spi.AuthenticationProvider`

### Configuration options

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
style="text-align: left;"><p><code>backward-compatible-eol</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>false</code></p></td>
<td style="text-align: left;"><p>Enable support for Helidon versions
before 3.0.0 (exclusive).</p>
<p>Until version 3.0.0 (exclusive) there was a trailing end of line
added to the signed data. To be able to communicate cross versions, we
must configure this when talking to older versions of Helidon. Default
value is <code>false</code>. In Helidon 2.x, this switch exists as well
and the default is <code>true</code>, to allow communication between
versions as needed.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>headers</code></p></td>
<td style="text-align: left;"><p>HttpSignHeader[] (SIGNATURE,
AUTHORIZATION, CUSTOM)</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Add a header that is validated on
inbound requests. Provider may support more than one header to
validate.</p>
<p>Allowed values:</p>
<ul>
<li><p><code>SIGNATURE</code>: Creates (or validates) a "Signature"
header.</p></li>
<li><p><code>AUTHORIZATION</code>: Creates (or validates) an
"Authorization" header, that contains "Signature" as the beginning of
its content (the rest of the header is the same as for
SIGNATURE.</p></li>
<li><p><code>CUSTOM</code>: Custom provided using a
io.helidon.security.util.TokenHandler.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>inbound.keys</code></p></td>
<td style="text-align: left;"><p><a
href="../../config/io_helidon_security_providers_httpsign_InboundClientDefinition.xml">InboundClientDefinition[]</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Add inbound configuration. This is used
to validate signature and authenticate the party.</p>
<p>The same can be done through configuration:</p>
<pre><code>{
 name = &quot;http-signatures&quot;
 class = &quot;HttpSignProvider&quot;
 http-signatures {
     inbound {
         # This configures the InboundClientDefinition
         keys: [
         {
             key-id = &quot;service1&quot;
             hmac.secret = &quot;${CLEAR=password}&quot;
         }]
     }
 }
}</code></pre></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>optional</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Set whether the signature is optional.
If set to true (default), this provider will
SecurityResponse.SecurityStatus.ABSTAIN from this request if signature
is not present. If set to false, this provider will
SecurityResponse.SecurityStatus.FAILURE fail if signature is not
present.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>outbound</code></p></td>
<td style="text-align: left;"><p><a
href="../../config/io_helidon_security_providers_common_OutboundConfig.xml">OutboundConfig</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Add outbound targets to this builder.
The targets are used to chose what to do for outbound communication. The
targets should have OutboundTargetDefinition attached through
OutboundTarget.Builder.customObject(Class, Object) to tell us how to
sign the request.</p>
<p>The same can be done through configuration:</p>
<pre><code>{
 name = &quot;http-signatures&quot;
 class = &quot;HttpSignProvider&quot;
 http-signatures {
     targets: [
     {
         name = &quot;service2&quot;
         hosts = [&quot;localhost&quot;]
         paths = [&quot;/service2/.*&quot;]
&#10;         # This configures the OutboundTargetDefinition
         signature {
             key-id = &quot;service1&quot;
             hmac.secret = &quot;${CLEAR=password}&quot;
         }
     }]
 }
}</code></pre></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>realm</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p><code>helidon</code></p></td>
<td style="text-align: left;"><p>Realm to use for challenging inbound
requests that do not have "Authorization" header in case header is
HttpSignHeader.AUTHORIZATION and singatures are not optional.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>sign-headers</code></p></td>
<td style="text-align: left;"><p><a
href="../../config/io_helidon_security_providers_httpsign_SignedHeadersConfig_HeadersConfig.xml">HeadersConfig[]</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Override the default inbound required
headers (e.g. headers that MUST be signed and headers that MUST be
signed IF present).</p>
<p>Defaults:</p>
<ul>
<li><p>get, head, delete methods: date, (request-target), host are
mandatory; authorization if present (unless we are creating/validating
the HttpSignHeader.AUTHORIZATION ourselves</p></li>
<li><p>put, post: same as above, with addition of: content-length,
content-type and digest if present</p></li>
<li><p>for other methods: date, (request-target)</p></li>
</ul>
<p>Note that this provider DOES NOT validate the "Digest" HTTP header,
only the signature.</p></td>
</tr>
</tbody>
</table>

### Example code

See the
[example](https://github.com/helidon-io/helidon-examples/tree/helidon-4.x/examples/security/webserver-signatures)
on GitHub.

<div class="formalpara">

<div class="title">

Configuration example

</div>

``` yaml
security:
  providers:
    - http-signatures:
        inbound:
          keys:
            - key-id: "service1-hmac"
              principal-name: "Service1 - HMAC signature"
              hmac.secret: "${CLEAR=changeit}"
            - key-id: "service1-rsa"
              principal-name: "Service1 - RSA signature"
              public-key:
                keystore:
                  resource.path: "src/main/resources/keystore.p12"
                  passphrase: "changeit"
                  cert.alias: "service_cert"
        outbound:
          - name: "service2-hmac"
            hosts: ["localhost"]
            paths: ["/service2"]
            signature:
              key-id: "service1-hmac"
              hmac.secret: "${CLEAR=changeit}"
          - name: "service2-rsa"
            hosts: ["localhost"]
            paths: ["/service2-rsa.*"]
            signature:
              key-id: "service1-rsa"
              private-key:
                keystore:
                  resource.path: "src/main/resources/keystore.p12"
                  passphrase: "changeit"
                  key.alias: "myPrivateKey"
```

</div>

### Signature basics

- standard: based on
  <https://tools.ietf.org/html/draft-cavage-http-signatures-03>

- key-id: an arbitrary string used to locate signature configuration -
  when a request is received the provider locates validation
  configuration based on this id (e.g. HMAC shared secret or RSA public
  key). Commonly used meanings are: key fingerprint (RSA); API Key

### How does it work?

**Inbound Signatures** We act as a server and another party is calling
us with a signed HTTP request. We validate the signature and assume
identity of the caller.

**Outbound Signatures** We act as a client and we sign our outgoing
requests. If there is a matching `outbound` target specified in
configuration, its configuration will be applied for signing the
outgoing request, otherwise there is no signature added

## IDCS Role Mapper

A role mapper to retrieve roles from Oracle IDCS.

### Setup

<div class="formalpara">

<div class="title">

Maven dependency

</div>

``` xml
<dependency>
    <groupId>io.helidon.security.providers</groupId>
    <artifactId>helidon-security-providers-idcs-mapper</artifactId>
</dependency>
```

</div>

### Single-tenant IDCS Role Mapper

IDCS role mapping provider

Type:
[io.helidon.security.providers.idcs.mapper.IdcsRoleMapperProvider](/apidocs/io.helidon.security.providers.idcs.mapper/io/helidon/security/providers/idcs/mapper/IdcsRoleMapperProvider.html)

<div class="formalpara">

<div class="title">

Config key

</div>

``` text
idcs-role-mapper
```

</div>

This type provides the following service implementations:

- `io.helidon.security.spi.SecurityProvider`

- `io.helidon.security.spi.SubjectMappingProvider`

### Configuration options

| key | type | default value | description |
|----|----|----|----|
| `cache-config` | [EvictableCache](../../config/io_helidon_security_providers_common_EvictableCache.md) |   | Use explicit io.helidon.security.providers.common.EvictableCache for role caching. |
| `default-idcs-subject-type` | string | `user` | Configure subject type to use when requesting roles from IDCS. Can be either IDCS_SUBJECT_TYPE_USER or IDCS_SUBJECT_TYPE_CLIENT. Defaults to IDCS_SUBJECT_TYPE_USER. |
| `oidc-config` | [OidcConfig](../../config/io_helidon_security_providers_oidc_common_OidcConfig.md) |   | Use explicit io.helidon.security.providers.oidc.common.OidcConfig instance, e.g. when using it also for OIDC provider. |
| `subject-types` | SubjectType\[\] (USER, SERVICE) | `USER` | Add a supported subject type. If none added, io.helidon.security.SubjectType.USER is used. If any added, only the ones added will be used (e.g. if you want to use both io.helidon.security.SubjectType.USER and io.helidon.security.SubjectType.SERVICE, both need to be added. |

Optional configuration options

### Multi-tenant IDCS Role Mapper

Multitenant IDCS role mapping provider

Type:
[io.helidon.security.providers.idcs.mapper.IdcsMtRoleMapperProvider](/apidocs/io.helidon.security.providers.idcs.mapper/io/helidon/security/providers/idcs/mapper/IdcsMtRoleMapperProvider.html)

<div class="formalpara">

<div class="title">

Config key

</div>

``` text
idcs-role-mapper
```

</div>

This type provides the following service implementations:

- `io.helidon.security.spi.SecurityProvider`

- `io.helidon.security.spi.SubjectMappingProvider`

### Configuration options

| key | type | default value | description |
|----|----|----|----|
| `cache-config` | [EvictableCache](../../config/io_helidon_security_providers_common_EvictableCache.md) |   | Use explicit io.helidon.security.providers.common.EvictableCache for role caching. |
| `default-idcs-subject-type` | string | `user` | Configure subject type to use when requesting roles from IDCS. Can be either IDCS_SUBJECT_TYPE_USER or IDCS_SUBJECT_TYPE_CLIENT. Defaults to IDCS_SUBJECT_TYPE_USER. |
| `idcs-app-name-handler` | [TokenHandler](../../config/io_helidon_security_util_TokenHandler.md) |   | Configure token handler for IDCS Application name. By default the header IdcsMtRoleMapperProvider.IDCS_APP_HEADER is used. |
| `idcs-tenant-handler` | [TokenHandler](../../config/io_helidon_security_util_TokenHandler.md) |   | Configure token handler for IDCS Tenant ID. By default the header IdcsMtRoleMapperProvider.IDCS_TENANT_HEADER is used. |
| `oidc-config` | [OidcConfig](../../config/io_helidon_security_providers_oidc_common_OidcConfig.md) |   | Use explicit io.helidon.security.providers.oidc.common.OidcConfig instance, e.g. when using it also for OIDC provider. |
| `subject-types` | SubjectType\[\] (USER, SERVICE) | `USER` | Add a supported subject type. If none added, io.helidon.security.SubjectType.USER is used. If any added, only the ones added will be used (e.g. if you want to use both io.helidon.security.SubjectType.USER and io.helidon.security.SubjectType.SERVICE, both need to be added. |

Optional configuration options

### Example code

See the
[example](https://github.com/helidon-io/helidon-examples/tree/helidon-4.x/examples/security/idcs-login/)
on GitHub.

<div class="formalpara">

<div class="title">

Configuration example

</div>

``` yaml
security:
  providers:
    - idcs-role-mapper:
        multitenant: false
        oidc-config:
            client-id: "client-id"
            client-secret: "changeit"
            identity-uri: "IDCS identity server address"
```

</div>

### How does it work?

The provider asks the IDCS server to provide list of roles for the
currently authenticated user. The result is cached for a certain period
of time (see `cache-config` above).

## ABAC Provider

Attribute based access control authorization provider.

### Setup

<div class="formalpara">

<div class="title">

Maven dependency

</div>

``` xml
<dependency>
    <groupId>io.helidon.security.providers</groupId>
    <artifactId>helidon-security-providers-abac</artifactId>
</dependency>
```

</div>

### Overview

Attribute Based Access Control provider

Type:
[io.helidon.security.providers.abac.AbacProvider](/apidocs/io.helidon.security.providers.abac/io/helidon/security/providers/abac/AbacProvider.html)

<div class="formalpara">

<div class="title">

Config key

</div>

``` text
abac
```

</div>

This type provides the following service implementations:

- `io.helidon.security.spi.SecurityProvider`

- `io.helidon.security.spi.AuthorizationProvider`

### Configuration options

| key | type | default value | description |
|----|----|----|----|
| `fail-if-none-validated` | boolean | `true` | Whether to fail if NONE of the attributes is validated. |
| `fail-on-unvalidated` | boolean | `true` | Whether to fail if any attribute is left unvalidated. |

Optional configuration options

### Example code

See the
[example](https://github.com/helidon-io/helidon-examples/tree/helidon-4.x/examples/security/attribute-based-access-control)
on GitHub.

<div class="formalpara">

<div class="title">

Configuration example

</div>

``` yaml
security:
  providers:
    - abac:
```

</div>

### Configuration options

The following table shows all configuration options of the provider and
their default values

| key | default value | description |
|----|----|----|
| `fail-on-unvalidated` | `true` | "Unvalidated" means: an attribute is defined, but there is no validator available for it |
| `fail-if-none-validated` | `true` | "None validated" means: there was not a single attribute that was validated |

### How does it work?

ABAC uses available validators and validates them against attributes of
the authenticated user.

Combinations of `fail-on-unvalidated` and `fail-if-none-validated`:

1.  `true` & `true`: Will fail if any attribute is not validated and if
    any has failed validation

2.  `false` & `true`: Will fail if there is one or more attributes
    present and NONE of them is validated or if any has failed
    validation, Will NOT fail if there is at least one validated
    attribute and any number of not validated attributes (and NONE
    failed)

3.  `false` & `false`: Will fail if there is any attribute that failed
    validation, Will NOT fail if there are no failed validation or if
    there are NONE validated

Any attribute of the following objects can be used:

- environment (such as time of request) - e.g. env.time.year

- subject (user) - e.g. subject.principal.id

- subject (service) - e.g. service.principal.id

- object (must be explicitly invoked by developer in code, as object
  cannot be automatically added to security context) - e.g. object.owner

This provider checks that all defined ABAC validators are validated. If
there is a definition for a validator that is not checked, the request
is denied (depending on configuration as mentioned above).

ABAC provider also allows an object to be used in authorization process,
such as when evaluating if an object’s owner is the current user. The
following example uses the Expression language validator to demonstrate
the point in a JAX-RS resource:

<div class="formalpara">

<div class="title">

Example of using an object

</div>

``` java
@Authenticated
@Path("/abac")
public class AbacResource {
    @GET
    @Authorized(explicit = true)
    @PolicyStatement("${env.time.year >= 2017 && object.owner == subject.principal.id}")
    public Response process(@Context SecurityContext context) {
        // probably looked up from a database
        SomeResource res = new SomeResource("user");
        AuthorizationResponse atzResponse = context.authorize(res);

        if (atzResponse.isPermitted()) {
            //do the update
            return Response.ok().entity("fine, sir").build();
        } else {
            return Response.status(Response.Status.FORBIDDEN)
                    .entity(atzResponse.description().orElse("Access not granted"))
                    .build();
        }
    }
}
```

</div>

**The following validators are implemented:**

- [Roles](#_role_validator)

- [Scopes](#_scope_validator)

- [EL Policy](#_expression_language_policy_validator)

### Role Validator

Checks whether user/service is in either of the required role(s).

Configuration Key: `role-validator`

Annotations: `@RolesAllowed`, `@RoleValidator.Roles`

<div class="formalpara">

<div class="title">

Configuration example for `WebServer`

</div>

``` yaml
security:
  web-server.paths:
    - path: "/user/*"
      roles-allowed: ["user"]
```

</div>

<div class="formalpara">

<div class="title">

JAX-RS example

</div>

``` java
@RolesAllowed("user")
@RoleValidator.Roles(value = "service_role", subjectType = SubjectType.SERVICE)
@Authenticated
@Path("/abac")
public class AbacResource {
}
```

</div>

#### Interaction with JAX-RS sub-resource locators

When using sub-resource locators in JAX-RS, the roles allowed are
collected from each "level" of execution: - Application class
annotations - Resource class annotations + resource method annotations -
Sub-resource class annotations + sub-resource method annotations -
Sub-resource class annotations + sub-resource method annotations (for
every sub-resource on the path)

The `RolesAllowed` or `Roles` annotation to be used is the last one in
the path as defined above.

*Example 1:* There is a `RolesAllowed("admin")` defined on a
sub-resource locator resource class. In this case the required role is
`admin`.

*Example 2:* There is a `RolesAllowed("admin")` defined on a
sub-resource locator resource class and a `RolesAllowed("user")` defined
on the method of the sub-resource that provides the response. In this
case the required role is `user`.

### Scope Validator

Checks whether user has all the required scopes.

Configuration Key: `scope-validator`

Annotations: `@Scope`

<div class="formalpara">

<div class="title">

Configuration example for `WebServer`

</div>

``` yaml
security:
  web-server.paths:
    - path: "/user/*"
      abac.scopes:
        ["calendar_read", "calendar_edit"]
```

</div>

<div class="formalpara">

<div class="title">

JAX-RS example

</div>

``` java
@Scope("calendar_read")
@Scope("calendar_edit")
@Authenticated
@Path("/abac")
public class AbacResource {
}
```

</div>

### Expression Language Policy Validator

Policy executor using Java EE policy expression language (EL)

Configuration Key: `policy-javax-el`

Annotations: `@PolicyStatement`

Example of a policy statement: `${env.time.year >= 2017}`

<div class="formalpara">

<div class="title">

Configuration example for `WebServer`

</div>

``` yaml
security:
  web-server.paths:
    - path: "/user/*"
      policy:
        statement: "hasScopes('calendar_read','calendar_edit') AND timeOfDayBetween('8:15', '17:30')"
```

</div>

<div class="formalpara">

<div class="title">

JAX-RS example

</div>

``` java
@PolicyStatement("${env.time.year >= 2017}")
@Authenticated
@Path("/abac")
public class AbacResource {
}
```

</div>

<div class="formalpara">

<div class="title">

Configuration example for `JAX-RS` over the configuration

</div>

``` yaml
server:
  features:
    security:
      endpoints:
        - path: "/somePath"
          config:
            abac.policy-validator.statement: "\\${env.time.year >= 2017}"
```

</div>

## Google Login Provider

<span class="line-through">Authenticates a token from request against
Google identity provider</span>

This provider is deprecated and will be removed in a future version of
Helidon. Please use our OpenID Connect security provider instead.

### Setup

<div class="formalpara">

<div class="title">

Maven dependency

</div>

``` xml
<dependency>
    <groupId>io.helidon.security.providers</groupId>
    <artifactId>helidon-security-providers-google-login</artifactId>
</dependency>
```

</div>

### Overview

Google Authentication provider

Type:
[io.helidon.security.providers.google.login.GoogleTokenProvider](/apidocs/io.helidon.security.providers.google.login/io/helidon/security/providers/google/login/GoogleTokenProvider.html)

<div class="formalpara">

<div class="title">

Config key

</div>

``` text
google-login
```

</div>

This type provides the following service implementations:

- `io.helidon.security.spi.SecurityProvider`

- `io.helidon.security.spi.AuthenticationProvider`

### Configuration options

| key | type | default value | description |
|----|----|----|----|
| `client-id` | string |   | Google application client id, to validate that the token was generated by Google for us. |
| `optional` | boolean | `false` | If set to true, this provider will return io.helidon.security.SecurityResponse.SecurityStatus.ABSTAIN instead of failing in case of invalid request. |
| `outbound` | [OutboundConfig](../../config/io_helidon_security_providers_common_OutboundConfig.md) |   | Outbound configuration - a set of outbound targets that will have the token propagated. |
| `proxy-host` | string |   | Set proxy host when talking to Google. |
| `proxy-port` | int | `80` | Set proxy port when talking to Google. |
| `realm` | string | `helidon` | Set the authentication realm to build challenge, defaults to "helidon". |
| `token` | [TokenHandler](../../config/io_helidon_security_util_TokenHandler.md) | `` `Authorization` header with `bearer` prefix `` | Token provider to extract Google access token from request, defaults to "Authorization" header with a "bearer " prefix. |

Optional configuration options

### Example code

See the
[example](https://github.com/helidon-io/helidon-examples/tree/helidon-4.x/examples/security/google-login)
on GitHub.

<div class="formalpara">

<div class="title">

Configuration example

</div>

``` yaml
security:
  providers:
    - provider:
        client-id: "Google client id"
```

</div>

### How does it work?

We expect to receive a token (with sufficient scopes) from the inbound
request, such as when using the Google login button on a page. The page
has access to the token in javascript and can send it to backend with
every request in a header field (`Authorization` with \`bearer \` prefix
is assumed by default).

Once we receive the token in Helidon, we parse it and:

1.  Validate if it timed out locally

2.  Return a cached response (see `EvictableCache` with default values)

3.  Otherwise verify using Google API - `GoogleIdTokenVerifier`

We build a subject from the Google token with the following attributes
filled (if in token):

- userId

- email

- name

- emailVerified

- locale

- family_name

- given_name

- picture (URL)

**Outbound security** The token will be propagated to outbound calls if
an outbound target exists that matches the invoked endpoint (see
`outbound` configuration above).

## JWT Provider

JWT token authentication and outbound security provider.

### Setup

<div class="formalpara">

<div class="title">

Maven dependency

</div>

``` xml
<dependency>
    <groupId>io.helidon.security.providers</groupId>
    <artifactId>helidon-security-providers-jwt</artifactId>
</dependency>
```

</div>

### Overview

JWT authentication provider

Type:
[io.helidon.security.providers.jwt.JwtProvider](/apidocs/io.helidon.security.providers.jwt/io/helidon/security/providers/jwt/JwtProvider.html)

<div class="formalpara">

<div class="title">

Config key

</div>

``` text
jwt
```

</div>

This type provides the following service implementations:

- `io.helidon.security.spi.SecurityProvider`

- `io.helidon.security.spi.AuthenticationProvider`

### Configuration options

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
style="text-align: left;"><p><code>allow-impersonation</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>false</code></p></td>
<td style="text-align: left;"><p>Whether to allow impersonation by
explicitly overriding username from outbound requests using
io.helidon.security.EndpointConfig.PROPERTY_OUTBOUND_ID property. By
default this is not allowed and identity can only be
propagated.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>allow-unsigned</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>false</code></p></td>
<td style="text-align: left;"><p>Configure support for unsigned JWT. If
this is set to <code>true</code> any JWT that has algorithm set to
<code>none</code> and no <code>kid</code> defined will be accepted. Note
that this has serious security impact - if JWT can be sent from a third
party, this allows the third party to send ANY JWT and it would be
accpted as valid.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>atn-token.handler</code></p></td>
<td style="text-align: left;"><p><a
href="../../config/io_helidon_security_util_TokenHandler.xml">TokenHandler</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Token handler to extract username from
request.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>atn-token.jwk.resource</code></p></td>
<td style="text-align: left;"><p><a
href="../../config/io_helidon_common_configurable_Resource.xml">Resource</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>JWK resource used to verify JWTs
created by other parties.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>atn-token.jwt-audience</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Audience expected in inbound
JWTs.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>atn-token.verify-signature</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Configure whether to verify signatures.
Signatures verification is enabled by default. You can configure the
provider not to verify signatures.</p>
<p><strong>Make sure your service is properly secured on network level
and only accessible from a secure endpoint that provides the JWTs when
signature verification is disabled. If signature verification is
disabled, this service will accept <em>ANY</em> JWT</strong></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>authenticate</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Whether to authenticate
requests.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>optional</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>false</code></p></td>
<td style="text-align: left;"><p>Whether authentication is required. By
default, request will fail if the username cannot be extracted. If set
to false, request will process and this provider will abstain.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>principal-type</code></p></td>
<td style="text-align: left;"><p>SubjectType (USER, SERVICE)</p></td>
<td style="text-align: left;"><p><code>USER</code></p></td>
<td style="text-align: left;"><p>Principal type this provider extracts
(and also propagates).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>propagate</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Whether to propagate identity.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>sign-token</code></p></td>
<td style="text-align: left;"><p><a
href="../../config/io_helidon_security_providers_common_OutboundConfig.xml">OutboundConfig</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Configuration of outbound
rules.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>sign-token.jwk.resource</code></p></td>
<td style="text-align: left;"><p><a
href="../../config/io_helidon_common_configurable_Resource.xml">Resource</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>JWK resource used to sign JWTs created
by us.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>sign-token.jwt-issuer</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Issuer used to create new
JWTs.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>use-jwt-groups</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Claim <code>groups</code> from JWT will
be used to automatically add groups to current subject (may be used with
jakarta.annotation.security.RolesAllowed annotation).</p></td>
</tr>
</tbody>
</table>

### Example code

See the
[example](https://github.com/helidon-io/helidon-examples/tree/helidon-4.x/examples/security/outbound-override)
on GitHub.

<div class="formalpara">

<div class="title">

Configuration example

</div>

``` yaml
security:
  providers:
    - provider:
        atn-token:
          jwk.resource.resource-path: "verifying-jwk.json"
          jwt-audience: "http://my.service"
        sign-token:
          jwk.resource.resource-path: "signing-jwk.json"
          jwt-issuer: "http://my.server/identity"
          outbound:
          - name: "propagate-token"
            hosts: ["*.internal.org"]
          - name: "generate-token"
            hosts: ["1.partner-service"]
            jwk-kid: "partner-1"
            jwt-kid: "helidon"
            jwt-audience: "http://1.partner-service"
```

</div>

### How does it work?

JSON Web Token (JWT) provider has support for authentication and
outbound security.

Authentication is based on validating the token (signature, valid before
etc.) and on asserting the subject of the JWT subject claim.

For outbound, we support either token propagation (e.g. the token from
request is propagated further) or support for generating a brand new
token based on configuration of this provider.

# Reference

- [Helidon Security
  Examples](https://github.com/oracle/helidon/tree/mainexamples/security)

- [Helidon OIDC
  JavaDoc](/apidocs/io.helidon.security.providers.oidc/module-summary.html)

- [Helidon HTTP Authentication
  JavaDoc](/apidocs/io.helidon.security.providers.httpauth/module-summary.html)

- [Helidon Header Authentication
  JavaDoc](/apidocs/io.helidon.security.providers.header/module-summary.html)

- [Helidon HTTP Signature
  JavaDoc](/apidocs/io.helidon.security.providers.httpsign/module-summary.html)

- [Helidon IDCS Role Mapper
  JavaDoc](/apidocs/io.helidon.security.providers.idcs.mapper/module-summary.html)

- [Helidon ABAC
  JavaDoc](/apidocs/io.helidon.security.providers.abac/module-summary.html)

- [Helidon Google Login
  JavaDoc](/apidocs/io.helidon.security.providers.google.login/module-summary.html)

- [Helidon JWT
  JavaDoc](/apidocs/io.helidon.security.providers.jwt/module-summary.html)
