# CorsFeature (webserver.cors) Configuration

Type: [io.helidon.webserver.cors.CorsFeature](/apidocs/io.helidon.webserver.cors/io/helidon/webserver/cors/CorsFeature.html)

This is a standalone configuration type, prefix from configuration root: `cors`

This type provides the following service implementations:

- `io.helidon.webserver.spi.ServerFeatureProvider`

## Configuration options

| key | type | default value | description |
|----|----|----|----|
| `enabled` | boolean |   | This feature can be disabled. This feature is automatically enabled if there is at least one paths() defined. |

Required configuration options

| key | type | default value | description |
|----|----|----|----|
| `add-defaults` | boolean | `true` | Whether to add a default path configuration, that matches all paths, `GET, HEAD, POST` methods, and allows all origins, methods, and headers. This is always added as a last path. |
| `paths` | [CorsPathConfig\[\]](../config/../config/io_helidon_webserver_cors_CorsPathConfig.md) |   | Per path configuration. Default path is added, unless addDefaults() is set to `false`. |
| `sockets` | string\[\] |   | List of sockets to register this feature on. If empty, it would get registered on all sockets. |
| `weight` | double | `850.0` | Weight of the CORS feature. As it is used by other features, the default is quite high: `850.0`. |

Optional configuration options
