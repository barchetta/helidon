# KeystoreKeys (common.pki) Configuration

Type: [io.helidon.common.pki.KeystoreKeys](/apidocs/io.helidon.common.pki/io/helidon/common/pki/KeystoreKeys.html)

## Configuration options

| key | type | default value | description |
|----|----|----|----|
| `resource` | [Resource](../config/io_helidon_common_configurable_Resource.md) |   | Keystore resource definition. |

Required configuration options

| key | type | default value | description |
|----|----|----|----|
| `cert-chain.alias` | string |   | Alias of an X.509 chain. |
| `cert.alias` | string |   | Alias of X.509 certificate of public key. Used to load both the certificate and public key. |
| `key.alias` | string |   | Alias of the private key in the keystore. |
| `key.passphrase` | char\[\] |   | Pass-phrase of the key in the keystore (used for private keys). This is (by default) the same as keystore passphrase - only configure if it differs from keystore passphrase. |
| `passphrase` | char\[\] |   | Pass-phrase of the keystore (supported with JKS and PKCS12 keystores). |
| `trust-store` | boolean | `false` | If you want to build a trust store, call this method to add all certificates present in the keystore to certificate list. |
| `type` | string | `PKCS12` | Set type of keystore. Defaults to `PKCS12`, expected are other keystore types supported by java then can store keys under aliases. |

Optional configuration options
