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

# Configuration options

| key | type | default value | description |
|----|----|----|----|
| `atn-token` | [TokenHandler](../config/io_helidon_security_util_TokenHandler.md) |   | Token handler to extract username from request. |
| `authenticate` | boolean | `true` | Whether to authenticate requests. |
| `optional` | boolean | `false` | Whether authentication is required. By default, request will fail if the username cannot be extracted. If set to false, request will process and this provider will abstain. |
| `outbound` | [OutboundTarget\[\]](../config/io_helidon_security_providers_common_OutboundTarget.md) |   | Configure outbound target for identity propagation. |
| `outbound-token` | [TokenHandler](../config/io_helidon_security_util_TokenHandler.md) |   | Token handler to create outbound headers to propagate identity. If not defined, atnTokenHandler will be used. |
| `principal-type` | SubjectType (USER, SERVICE) | `USER` | Principal type this provider extracts (and also propagates). |
| `propagate` | boolean | `false` | Whether to propagate identity. |

Optional configuration options
