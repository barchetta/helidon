# MpOpenApiManagerConfig (microprofile.openapi) Configuration

Type: [io.helidon.microprofile.openapi.MpOpenApiManagerConfig](/apidocs/io.helidon.microprofile.openapi/io/helidon/microprofile/openapi/MpOpenApiManagerConfig.html)

## Configuration options

| key | type | default value | description |
|----|----|----|----|
| `mp.openapi.extensions.helidon.use-jaxrs-semantics` | boolean |   | If `true` and the `jakarta.ws.rs.core.Application` class returns a non-empty set, endpoints defined by other resources are not included in the OpenAPI document. |

Optional configuration options
