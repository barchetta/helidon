# SecretConfig (security.providers.config.vault.ConfigVaultProvider) Configuration

Provider of secrets defined in configuration itself

Type: [io.helidon.security.providers.config.vault.ConfigVaultProvider.SecretConfig](/apidocs/io.helidon.security.providers.config.vault/io/helidon/security/providers/config/vault/ConfigVaultProvider.SecretConfig.html)

This type provides the following service implementations:

- `io.helidon.security.SecretsProviderConfig`

## Configuration options

| key | type | default value | description |
|----|----|----|----|
| `value` | ConfiguredOption |   | Value of the secret, can be a reference to another configuration key, such as \${app.secret} |

Optional configuration options
