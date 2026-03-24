# HeadersConfig (security.providers.httpsign.SignedHeadersConfig) Configuration

Type: [io.helidon.security.providers.httpsign.SignedHeadersConfig.HeadersConfig](/apidocs/io.helidon.security.providers.httpsign/io/helidon/security/providers/httpsign/SignedHeadersConfig.HeadersConfig.html)

## Configuration options

| key | type | default value | description |
|----|----|----|----|
| `always` | string\[\] |   | Headers that must be signed (and signature validation or creation should fail if not signed or present) |
| `if-present` | string\[\] |   | Headers that must be signed if present in request. |
| `method` | string |   | HTTP method this header configuration is bound to. If not present, it is considered default header configuration. |

Optional configuration options
