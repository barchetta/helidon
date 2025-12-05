# Header Authentication Provider

Asserts user or service identity based on a value of a header.

## Setup

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

## Overview

Security provider that extracts a username (or service name) from a
header.

Type:
[io.helidon.security.providers.header.HeaderAtnProvider]({javadoc-base-url}/io.helidon.security.providers.header/io/helidon/security/providers/header/HeaderAtnProvider.html)

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

## Configuration options

| key | type | default value | description |
|----|----|----|----|
| `atn-token` | [TokenHandler](../../../config/io_helidon_security_util_TokenHandler.md) |   | Token handler to extract username from request. |
| `authenticate` | boolean | `true` | Whether to authenticate requests. |
| `optional` | boolean | `false` | Whether authentication is required. By default, request will fail if the username cannot be extracted. If set to false, request will process and this provider will abstain. |
| `outbound` | [OutboundTarget\[\]](../../../config/io_helidon_security_providers_common_OutboundTarget.md) |   | Configure outbound target for identity propagation. |
| `outbound-token` | [TokenHandler](../../../config/io_helidon_security_util_TokenHandler.md) |   | Token handler to create outbound headers to propagate identity. If not defined, atnTokenHandler will be used. |
| `principal-type` | SubjectType (USER, SERVICE) | `USER` | Principal type this provider extracts (and also propagates). |
| `propagate` | boolean | `false` | Whether to propagate identity. |

Optional configuration options

## Example code

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

## How does it work?

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
