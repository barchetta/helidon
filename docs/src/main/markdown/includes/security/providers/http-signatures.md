# HTTP Signatures Provider

Support for HTTP Signatures.

### Setup

*Maven dependency*

``` xml
<dependency>
    <groupId>io.helidon.security.providers</groupId>
    <artifactId>helidon-security-providers-http-sign</artifactId>
</dependency>
```

### Overview

### Configuration options

| Key | Kind | Type | Default Value | Description |
|----|----|----|----|----|
| <span id="ac1d34-backward-compatible-eol"></span> `backward-compatible-eol` | `VALUE` | `Boolean` | `false` | Enable support for Helidon versions before 3.0.0 (exclusive) |
| <span id="acc108-headers"></span> [`headers`](../../../config/io_helidon_security_providers_httpsign_HttpSignHeader.md) | `LIST` | `i.h.s.p.h.HttpSignHeader` |   | Add a header that is validated on inbound requests |
| <span id="abbc62-inbound-keys"></span> [`inbound.keys`](../../../config/io_helidon_security_providers_httpsign_InboundClientDefinition.md) | `LIST` | `i.h.s.p.h.InboundClientDefinition` |   | Add inbound configuration |
| <span id="a9cb96-optional"></span> `optional` | `VALUE` | `Boolean` | `true` | Set whether the signature is optional |
| <span id="af2400-outbound"></span> [`outbound`](../../../config/io_helidon_security_providers_common_OutboundConfig.md) | `VALUE` | `i.h.s.p.c.OutboundConfig` |   | Add outbound targets to this builder |
| <span id="a4938a-realm"></span> `realm` | `VALUE` | `String` | `helidon` | Realm to use for challenging inbound requests that do not have "Authorization" header in case header is `HttpSignHeader#AUTHORIZATION` and singatures are not optional |
| <span id="a4ba7d-sign-headers"></span> [`sign-headers`](../../../config/io_helidon_security_providers_httpsign_SignedHeadersConfig_HeadersConfig.md) | `LIST` | `i.h.s.p.h.S.HeadersConfig` |   | Override the default inbound required headers (e.g |

### Example code

See the [example]({helidon-github-examples-url}/security/webserver-signatures) on GitHub.

*Configuration example*

``` yaml
security:
  providers:
    - http-signatures:
        inbound:
          keys:
            - key-id: "service1-hmac"
              principal-name: "Service1 - HMAC signature"
              hmac.secret: "${CLEAR=changeit}"
            - key-id: "service1-rsa"
              principal-name: "Service1 - RSA signature"
              public-key:
                keystore:
                  resource.path: "src/main/resources/keystore.p12"
                  passphrase: "changeit"
                  cert.alias: "service_cert"
        outbound:
          - name: "service2-hmac"
            hosts: ["localhost"]
            paths: ["/service2"]
            signature:
              key-id: "service1-hmac"
              hmac.secret: "${CLEAR=changeit}"
          - name: "service2-rsa"
            hosts: ["localhost"]
            paths: ["/service2-rsa.*"]
            signature:
              key-id: "service1-rsa"
              private-key:
                keystore:
                  resource.path: "src/main/resources/keystore.p12"
                  passphrase: "changeit"
                  key.alias: "myPrivateKey"
```

### Signature basics

- standard: based on <https://tools.ietf.org/html/draft-cavage-http-signatures-03>

- key-id: an arbitrary string used to locate signature configuration - when a request is received the provider locates validation configuration based on this id (e.g. HMAC shared secret or RSA public key). Commonly used meanings are: key fingerprint (RSA); API Key

### How does it work?

**Inbound Signatures** We act as a server and another party is calling us with a signed HTTP request. We validate the signature and assume identity of the caller.

**Outbound Signatures** We act as a client and we sign our outgoing requests. If there is a matching `outbound` target specified in configuration, its configuration will be applied for signing the outgoing request, otherwise there is no signature added
