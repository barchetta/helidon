# PemKeys (common.pki) Configuration

Type: [io.helidon.common.pki.PemKeys](/apidocs/io.helidon.common.pki/io/helidon/common/pki/PemKeys.html)

## Configuration options

| key | type | default value | description |
|----|----|----|----|
| `cert-chain.resource` | [Resource](../config/io_helidon_common_configurable_Resource.md) |   | Load certificate chain from PEM resource. |
| `certificates.resource` | [Resource](../config/io_helidon_common_configurable_Resource.md) |   | Read one or more certificates in PEM format from a resource definition. Used eg: in a trust store. |
| `key.passphrase` | char\[\] |   | Passphrase for private key. If the key is encrypted (and in PEM PKCS#8 format), this passphrase will be used to decrypt it. |
| `key.resource` | [Resource](../config/io_helidon_common_configurable_Resource.md) |   | Read a private key from PEM format from a resource definition. |
| `public-key.resource` | [Resource](../config/io_helidon_common_configurable_Resource.md) |   | Read a public key from PEM format from a resource definition. |

Optional configuration options
