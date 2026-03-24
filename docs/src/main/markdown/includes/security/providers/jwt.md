# JWT Provider

JWT token authentication and outbound security provider.

### Setup

*Maven dependency*

``` xml
<dependency>
    <groupId>io.helidon.security.providers</groupId>
    <artifactId>helidon-security-providers-jwt</artifactId>
</dependency>
```

### Overview

JWT authentication provider

Type: [io.helidon.security.providers.jwt.JwtProvider]({javadoc-base-url}/io.helidon.security.providers.jwt/io/helidon/security/providers/jwt/JwtProvider.md)

*Config key*

``` text
jwt
```

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
<td style="text-align: left;"><p><code>allow-impersonation</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>false</code></p></td>
<td style="text-align: left;"><p>Whether to allow impersonation by explicitly overriding username from outbound requests using io.helidon.security.EndpointConfig.PROPERTY_OUTBOUND_ID property. By default this is not allowed and identity can only be propagated.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>allow-unsigned</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>false</code></p></td>
<td style="text-align: left;"><p>Configure support for unsigned JWT. If this is set to <code>true</code> any JWT that has algorithm set to <code>none</code> and no <code>kid</code> defined will be accepted. Note that this has serious security impact - if JWT can be sent from a third party, this allows the third party to send ANY JWT and it would be accpted as valid.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>atn-token.handler</code></p></td>
<td style="text-align: left;"><p><a href="../../../includes/security/providers/../../../config/io_helidon_security_util_TokenHandler.xml">TokenHandler</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Token handler to extract username from request.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>atn-token.jwk.resource</code></p></td>
<td style="text-align: left;"><p><a href="../../../includes/security/providers/../../../config/io_helidon_common_configurable_Resource.xml">Resource</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>JWK resource used to verify JWTs created by other parties.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>atn-token.jwt-audience</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Audience expected in inbound JWTs.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>atn-token.verify-signature</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Configure whether to verify signatures. Signatures verification is enabled by default. You can configure the provider not to verify signatures.</p>
<p><strong>Make sure your service is properly secured on network level and only accessible from a secure endpoint that provides the JWTs when signature verification is disabled. If signature verification is disabled, this service will accept <em>ANY</em> JWT</strong></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>authenticate</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Whether to authenticate requests.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>optional</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>false</code></p></td>
<td style="text-align: left;"><p>Whether authentication is required. By default, request will fail if the username cannot be extracted. If set to false, request will process and this provider will abstain.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>principal-type</code></p></td>
<td style="text-align: left;"><p>SubjectType (USER, SERVICE)</p></td>
<td style="text-align: left;"><p><code>USER</code></p></td>
<td style="text-align: left;"><p>Principal type this provider extracts (and also propagates).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>propagate</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Whether to propagate identity.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>sign-token</code></p></td>
<td style="text-align: left;"><p><a href="../../../includes/security/providers/../../../config/io_helidon_security_providers_common_OutboundConfig.xml">OutboundConfig</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Configuration of outbound rules.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>sign-token.jwk.resource</code></p></td>
<td style="text-align: left;"><p><a href="../../../includes/security/providers/../../../config/io_helidon_common_configurable_Resource.xml">Resource</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>JWK resource used to sign JWTs created by us.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>sign-token.jwt-issuer</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Issuer used to create new JWTs.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>use-jwt-groups</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Claim <code>groups</code> from JWT will be used to automatically add groups to current subject (may be used with jakarta.annotation.security.RolesAllowed annotation).</p></td>
</tr>
</tbody>
</table>

### Example code

See the [example]({helidon-github-examples-url}/security/outbound-override) on GitHub.

*Configuration example*

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

### How does it work?

JSON Web Token (JWT) provider has support for authentication and outbound security.

Authentication is based on validating the token (signature, valid before etc.) and on asserting the subject of the JWT subject claim.

For outbound, we support either token propagation (e.g. the token from request is propagated further) or support for generating a brand new token based on configuration of this provider.
