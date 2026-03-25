# IDCS Role Mapper

A role mapper to retrieve roles from Oracle IDCS.

### Setup

*Maven dependency*

``` xml
<dependency>
    <groupId>io.helidon.security.providers</groupId>
    <artifactId>helidon-security-providers-idcs-mapper</artifactId>
</dependency>
```

### Single-tenant IDCS Role Mapper

### Configuration options

| Key | Kind | Type | Default Value | Description |
|----|----|----|----|----|
| <span id="aed3ab-cache-config"></span> [`cache-config`](../../../config/io_helidon_security_providers_common_EvictableCache.md) | `VALUE` | `i.h.s.p.c.EvictableCache` |   | Use explicit `io.helidon.security.providers.common.EvictableCache` for role caching |
| <span id="aa2e00-default-idcs-subject-type"></span> `default-idcs-subject-type` | `VALUE` | `String` | `user` | Configure subject type to use when requesting roles from IDCS |
| <span id="a630af-oidc-config"></span> [`oidc-config`](../../../config/io_helidon_security_providers_oidc_common_OidcConfig.md) | `VALUE` | `i.h.s.p.o.c.OidcConfig` |   | Use explicit `io.helidon.security.providers.oidc.common.OidcConfig` instance, e.g |
| <span id="a477d4-subject-types"></span> [`subject-types`](../../../config/io_helidon_security_SubjectType.md) | `LIST` | `i.h.s.SubjectType` | `USER` | Add a supported subject type |

### Multi-tenant IDCS Role Mapper

### Configuration options

| Key | Kind | Type | Default Value | Description |
|----|----|----|----|----|
| <span id="a6bc4c-cache-config"></span> [`cache-config`](../../../config/io_helidon_security_providers_common_EvictableCache.md) | `VALUE` | `i.h.s.p.c.EvictableCache` |   | Use explicit `io.helidon.security.providers.common.EvictableCache` for role caching |
| <span id="a75027-default-idcs-subject-type"></span> `default-idcs-subject-type` | `VALUE` | `String` | `user` | Configure subject type to use when requesting roles from IDCS |
| <span id="a89a70-idcs-app-name-handler"></span> [`idcs-app-name-handler`](../../../config/io_helidon_security_util_TokenHandler.md) | `VALUE` | `i.h.s.u.TokenHandler` |   | Configure token handler for IDCS Application name |
| <span id="af8920-idcs-tenant-handler"></span> [`idcs-tenant-handler`](../../../config/io_helidon_security_util_TokenHandler.md) | `VALUE` | `i.h.s.u.TokenHandler` |   | Configure token handler for IDCS Tenant ID |
| <span id="a2275a-oidc-config"></span> [`oidc-config`](../../../config/io_helidon_security_providers_oidc_common_OidcConfig.md) | `VALUE` | `i.h.s.p.o.c.OidcConfig` |   | Use explicit `io.helidon.security.providers.oidc.common.OidcConfig` instance, e.g |
| <span id="ab2c38-subject-types"></span> [`subject-types`](../../../config/io_helidon_security_SubjectType.md) | `LIST` | `i.h.s.SubjectType` | `USER` | Add a supported subject type |

### Example code

See the [example]({helidon-github-examples-url}/security/idcs-login/) on GitHub.

*Configuration example*

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

### How does it work?

The provider asks the IDCS server to provide list of roles for the currently authenticated user. The result is cached for a certain period of time (see `cache-config` above).
