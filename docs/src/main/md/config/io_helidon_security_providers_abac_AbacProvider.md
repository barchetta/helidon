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

# Configuration options

| key | type | default value | description |
|----|----|----|----|
| `fail-if-none-validated` | boolean | `true` | Whether to fail if NONE of the attributes is validated. |
| `fail-on-unvalidated` | boolean | `true` | Whether to fail if any attribute is left unvalidated. |

Optional configuration options
