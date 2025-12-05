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

# Configuration options

| key | type | default value | description |
|----|----|----|----|
| `optional` | boolean | `false` | Whether authentication is required. By default, request will fail if the authentication cannot be verified. If set to false, request will process and this provider will abstain. |
| `outbound` | [OutboundTarget\[\]](../config/io_helidon_security_providers_common_OutboundTarget.md) |   | Add a new outbound target to configure identity propagation or explicit username/password. |
| `principal-type` | SubjectType (USER, SERVICE) | `USER` | Principal type this provider extracts (and also propagates). |
| `realm` | string | `helidon` | Set the realm to use when challenging users. |
| `users` | [ConfigUser\[\]](../config/io_helidon_security_providers_httpauth_ConfigUserStore_ConfigUser.md) |   | Set user store to validate users. Removes any other stores added through addUserStore(SecureUserStore). |

Optional configuration options
