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

IDCS role mapping provider

Type: [io.helidon.security.providers.idcs.mapper.IdcsRoleMapperProvider]({javadoc-base-url}/io.helidon.security.providers.idcs.mapper/io/helidon/security/providers/idcs/mapper/IdcsRoleMapperProvider.md)

*Config key*

``` text
idcs-role-mapper
```

This type provides the following service implementations:

- `io.helidon.security.spi.SecurityProvider`

- `io.helidon.security.spi.SubjectMappingProvider`

### Configuration options

| key | type | default value | description |
|----|----|----|----|
| `cache-config` | [EvictableCache](../../../config/io_helidon_security_providers_common_EvictableCache.md) |   | Use explicit io.helidon.security.providers.common.EvictableCache for role caching. |
| `default-idcs-subject-type` | string | `user` | Configure subject type to use when requesting roles from IDCS. Can be either IDCS_SUBJECT_TYPE_USER or IDCS_SUBJECT_TYPE_CLIENT. Defaults to IDCS_SUBJECT_TYPE_USER. |
| `oidc-config` | [OidcConfig](../../../config/io_helidon_security_providers_oidc_common_OidcConfig.md) |   | Use explicit io.helidon.security.providers.oidc.common.OidcConfig instance, e.g. when using it also for OIDC provider. |
| `subject-types` | SubjectType\[\] (USER, SERVICE) | `USER` | Add a supported subject type. If none added, io.helidon.security.SubjectType.USER is used. If any added, only the ones added will be used (e.g. if you want to use both io.helidon.security.SubjectType.USER and io.helidon.security.SubjectType.SERVICE, both need to be added. |

Optional configuration options

### Multi-tenant IDCS Role Mapper

Multitenant IDCS role mapping provider

Type: [io.helidon.security.providers.idcs.mapper.IdcsMtRoleMapperProvider]({javadoc-base-url}/io.helidon.security.providers.idcs.mapper/io/helidon/security/providers/idcs/mapper/IdcsMtRoleMapperProvider.md)

*Config key*

``` text
idcs-role-mapper
```

This type provides the following service implementations:

- `io.helidon.security.spi.SecurityProvider`

- `io.helidon.security.spi.SubjectMappingProvider`

### Configuration options

| key | type | default value | description |
|----|----|----|----|
| `cache-config` | [EvictableCache](../../../config/io_helidon_security_providers_common_EvictableCache.md) |   | Use explicit io.helidon.security.providers.common.EvictableCache for role caching. |
| `default-idcs-subject-type` | string | `user` | Configure subject type to use when requesting roles from IDCS. Can be either IDCS_SUBJECT_TYPE_USER or IDCS_SUBJECT_TYPE_CLIENT. Defaults to IDCS_SUBJECT_TYPE_USER. |
| `idcs-app-name-handler` | [TokenHandler](../../../config/io_helidon_security_util_TokenHandler.md) |   | Configure token handler for IDCS Application name. By default the header `X-RESOURCE-SERVICE-INSTANCE-IDENTITY-APPNAME` is used. |
| `idcs-tenant-handler` | [TokenHandler](../../../config/io_helidon_security_util_TokenHandler.md) |   | Configure token handler for IDCS Tenant ID. By default the header `X-USER-IDENTITY-SERVICE-GUID` is used. |
| `oidc-config` | [OidcConfig](../../../config/io_helidon_security_providers_oidc_common_OidcConfig.md) |   | Use explicit io.helidon.security.providers.oidc.common.OidcConfig instance, e.g. when using it also for OIDC provider. |
| `subject-types` | SubjectType\[\] (USER, SERVICE) | `USER` | Add a supported subject type. If none added, io.helidon.security.SubjectType.USER is used. If any added, only the ones added will be used (e.g. if you want to use both io.helidon.security.SubjectType.USER and io.helidon.security.SubjectType.SERVICE, both need to be added. |

Optional configuration options

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
