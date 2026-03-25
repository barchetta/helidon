# Header Authentication Provider

Asserts user or service identity based on a value of a header.

### Setup

*Maven dependency*

``` xml
<dependency>
    <groupId>io.helidon.security.providers</groupId>
    <artifactId>helidon-security-providers-header</artifactId>
</dependency>
```

### Overview

### Configuration options

| Key | Kind | Type | Default Value | Description |
|----|----|----|----|----|
| <span id="a9672f-atn-token"></span> [`atn-token`](../../../config/io_helidon_security_util_TokenHandler.md) | `VALUE` | `i.h.s.u.TokenHandler` |   | Token handler to extract username from request |
| <span id="a25377-authenticate"></span> `authenticate` | `VALUE` | `Boolean` | `true` | Whether to authenticate requests |
| <span id="adbdf3-optional"></span> `optional` | `VALUE` | `Boolean` | `false` | Whether authentication is required |
| <span id="aa4f36-outbound"></span> [`outbound`](../../../config/io_helidon_security_providers_common_OutboundTarget.md) | `LIST` | `i.h.s.p.c.OutboundTarget` |   | Configure outbound target for identity propagation |
| <span id="ad5021-outbound-token"></span> [`outbound-token`](../../../config/io_helidon_security_util_TokenHandler.md) | `VALUE` | `i.h.s.u.TokenHandler` |   | Token handler to create outbound headers to propagate identity |
| <span id="aa8e94-principal-type"></span> [`principal-type`](../../../config/io_helidon_security_SubjectType.md) | `VALUE` | `i.h.s.SubjectType` | `USER` | Principal type this provider extracts (and also propagates) |
| <span id="a0309f-propagate"></span> `propagate` | `VALUE` | `Boolean` | `false` | Whether to propagate identity |

### Example code

*Configuration example*

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

### How does it work?

This provider inspects a specified request header and extracts the username/service name from it and asserts it as current subject’s principal.

This can be used when we use perimeter authentication (e.g. there is a gateway that takes care of authentication and propagates the user in a header).

**Identity propagation**

Identity is propagated only if an outbound target matches the target service.

The following options exist when propagating identity: 1. We propagate the current username using the configured header 2. We use username associated with an outbound target (see example configuration above)

**Caution**

When using this provider, you must be sure the header cannot be explicitly configured by a user or another service. All requests should go through a gateway that removes this header from inbound traffic, and only configures it for authenticated users/services. Another option is to use this with fully trusted parties (such as services within a single company, on a single protected network not accessible to any users), and of course for testing and demo purposes.
