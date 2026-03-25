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

### Configuration options

| Key | Kind | Type | Default Value | Description |
|----|----|----|----|----|
| <span id="a8e9cb-allow-impersonation"></span> `allow-impersonation` | `VALUE` | `Boolean` | `false` | Whether to allow impersonation by explicitly overriding username from outbound requests using `io.helidon.security.EndpointConfig#PROPERTY_OUTBOUND_ID` property |
| <span id="ac7a36-allow-unsigned"></span> `allow-unsigned` | `VALUE` | `Boolean` | `false` | Configure support for unsigned JWT |
| <span id="a31c89-atn-token-handler"></span> [`atn-token.handler`](../../../config/io_helidon_security_util_TokenHandler.md) | `VALUE` | `i.h.s.u.TokenHandler` |   | Token handler to extract username from request |
| <span id="ab9ed4-atn-token-jwk-resource"></span> [`atn-token.jwk.resource`](../../../config/io_helidon_common_configurable_Resource.md) | `VALUE` | `i.h.c.c.Resource` |   | JWK resource used to verify JWTs created by other parties |
| <span id="a7fd00-atn-token-jwt-audience"></span> `atn-token.jwt-audience` | `VALUE` | `String` |   | Audience expected in inbound JWTs |
| <span id="a1483b-atn-token-verify-signature"></span> `atn-token.verify-signature` | `VALUE` | `Boolean` | `true` | Configure whether to verify signatures |
| <span id="a2bd0c-authenticate"></span> `authenticate` | `VALUE` | `Boolean` | `true` | Whether to authenticate requests |
| <span id="ac625d-optional"></span> `optional` | `VALUE` | `Boolean` | `false` | Whether authentication is required |
| <span id="af07ea-principal-type"></span> [`principal-type`](../../../config/io_helidon_security_SubjectType.md) | `VALUE` | `i.h.s.SubjectType` | `USER` | Principal type this provider extracts (and also propagates) |
| <span id="a5a95f-propagate"></span> `propagate` | `VALUE` | `Boolean` | `true` | Whether to propagate identity |
| <span id="a9294b-sign-token"></span> [`sign-token`](../../../config/io_helidon_security_providers_common_OutboundConfig.md) | `VALUE` | `i.h.s.p.c.OutboundConfig` |   | Configuration of outbound rules |
| <span id="adc22c-sign-token-jwk-resource"></span> [`sign-token.jwk.resource`](../../../config/io_helidon_common_configurable_Resource.md) | `VALUE` | `i.h.c.c.Resource` |   | JWK resource used to sign JWTs created by us |
| <span id="ab60c1-sign-token-jwt-issuer"></span> `sign-token.jwt-issuer` | `VALUE` | `String` |   | Issuer used to create new JWTs |
| <span id="a8cde7-use-jwt-groups"></span> `use-jwt-groups` | `VALUE` | `Boolean` | `true` | Claim `groups` from JWT will be used to automatically add groups to current subject (may be used with `jakarta.annotation.security.RolesAllowed` annotation) |

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
