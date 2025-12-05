Secrets and Encryption provider using just configuration

Type:
[io.helidon.security.providers.config.vault.ConfigVaultProvider](/apidocs/io.helidon.security.providers.config.vault/io/helidon/security/providers/config/vault/ConfigVaultProvider.html)

<div class="formalpara">

<div class="title">

Config key

</div>

``` text
config-vault
```

</div>

This type provides the following service implementations:

- `io.helidon.security.spi.SecurityProvider`

- `io.helidon.security.spi.SecretsProvider`

- `io.helidon.security.spi.EncryptionProvider`

# Configuration options

| key | type | default value | description |
|----|----|----|----|
| `master-password` | string |   | Configure master password used for encryption/decryption. If master password cannot be obtained from any source (this method, configuration, system property, environment variable), encryption and decryption will not be supported. |

Required configuration options
