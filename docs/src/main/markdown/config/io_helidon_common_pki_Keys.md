# Keys (common.pki) Configuration

Type: [io.helidon.common.pki.Keys](/apidocs/io.helidon.common.pki/io/helidon/common/pki/Keys.html)

## Configuration options

| key | type | default value | description |
|----|----|----|----|
| `keystore` | [KeystoreKeys](../config/io_helidon_common_pki_KeystoreKeys.md) |   | Configure keys from a keystore. Once the config object is built, this option will ALWAYS be empty. All keys from the keystore will be populated to privateKey(), publicKey(), publicCert() etc. |
| `pem` | [PemKeys](../config/io_helidon_common_pki_PemKeys.md) |   | Configure keys from pem file(s). Once the config object is built, this option will ALWAYS be empty. All keys from the keystore will be populated to privateKey(), publicKey(), publicCert() etc. |

Optional configuration options
