# CrossOriginConfig (cors) Configuration

Type: [io.helidon.cors.CrossOriginConfig](/apidocs/io.helidon.cors/io/helidon/cors/CrossOriginConfig.html)

## Configuration options

| key | type | default value | description |
|----|----|----|----|
| `allow-credentials` | boolean | `false` | Sets the allow credentials flag. |
| `allow-headers` | string\[\] | `*` | Sets the allow headers. |
| `allow-methods` | string\[\] | `*` | Sets the allow methods. |
| `allow-origins` | string\[\] | `*` | Sets the allowOrigins. |
| `enabled` | boolean | `true` | Sets whether this config should be enabled or not. |
| `expose-headers` | string\[\] |   | Sets the expose headers. |
| `max-age-seconds` | long | `3600` | Sets the maximum age. |
| `path-pattern` | string | `{+}` | Updates the path prefix for this cross-origin config. |

Optional configuration options
