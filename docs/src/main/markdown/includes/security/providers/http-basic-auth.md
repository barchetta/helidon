# HTTP Basic Authentication Provider

HTTP Basic authentication support

### Setup

*Maven dependency*

``` xml
<dependency>
    <groupId>io.helidon.security.providers</groupId>
    <artifactId>helidon-security-providers-http-auth</artifactId>
</dependency>
```

### Overview

HTTP Basic Authentication provider

Type: [io.helidon.security.providers.httpauth.HttpBasicAuthProvider]({javadoc-base-url}/io.helidon.security.providers.httpauth/io/helidon/security/providers/httpauth/HttpBasicAuthProvider.md)

*Config key*

``` text
http-basic-auth
```

This type provides the following service implementations:

- `io.helidon.security.spi.SecurityProvider`

- `io.helidon.security.spi.AuthenticationProvider`

### Configuration options

| key | type | default value | description |
|----|----|----|----|
| `optional` | boolean | `false` | Whether authentication is required. By default, request will fail if the authentication cannot be verified. If set to false, request will process and this provider will abstain. |
| `outbound` | [OutboundTarget\[\]](../../../includes/security/providers/../../../config/io_helidon_security_providers_common_OutboundTarget.md) |   | Add a new outbound target to configure identity propagation or explicit username/password. |
| `principal-type` | SubjectType (USER, SERVICE) | `USER` | Principal type this provider extracts (and also propagates). |
| `realm` | string | `helidon` | Set the realm to use when challenging users. |
| `users` | [ConfigUserStore.ConfigUser\[\]](../../../includes/security/providers/../../../config/io_helidon_security_providers_httpauth_ConfigUserStore_ConfigUser.md) |   | Set user store to validate users. Removes any other stores added through addUserStore(SecureUserStore). |

Optional configuration options

### Example code

See the [example]({helidon-github-examples-url}/security/outbound-override) on GitHub.

*Configuration example*

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

### How does it work?

See <https://tools.ietf.org/html/rfc7617>.

**Authentication of request**

When a request is received without the `Authorization: basic …​.` header, a challenge is returned to provide such authentication.

When a request is received with the `Authorization: basic …​.` header, the username and password is validated against configured users (and users obtained from custom service if any provided).

Subject is created based on the username and roles provided by the user store.

**Identity propagation**

When identity propagation is configured, there are several options for identifying username and password to propagate:

1.  We propagate the current username and password (inbound request must be authenticated using basic authentication).

2.  We use username and password from an explicitly configured property (See `EndpointConfig.PROPERTY_OUTBOUND_ID` and `EndpointConfig.PROPERTY_OUTBOUND_SECRET`)

3.  We use username and password associated with an outbound target (see example configuration above)

Identity is propagated only if:

1.  There is an outbound target configured for the endpoint

2.  Or there is an explicitly configured username/password for the current request (through request property)

**Custom user store**

Java service loader service `io.helidon.security.providers.httpauth.spi.UserStoreService` can be implemented to provide users to the provider, such as when validated against an internal database or LDAP server. The user store is defined so you never need the clear text password of the user.

*Warning on security of HTTP Basic Authentication (or lack thereof)*

Basic authentication uses base64 encoded username and password and passes it over the network. Base64 is only encoding, not encryption - so anybody that gets hold of the header value can learn the actual username and password of the user. This is a security risk and an attack vector that everybody should be aware of before using HTTP Basic Authentication. We recommend using this approach only for testing and demo purposes.
