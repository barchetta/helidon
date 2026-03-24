# GrpcReflectionFeature (webserver.grpc) Configuration

Type: [io.helidon.webserver.grpc.GrpcReflectionFeature](/apidocs/io.helidon.webserver.grpc/io/helidon/webserver/grpc/GrpcReflectionFeature.html)

*Config key*

``` text
grpc-reflection
```

This type provides the following service implementations:

- `io.helidon.webserver.spi.ServerFeatureProvider`

## Configuration options

| key | type | default value | description |
|----|----|----|----|
| `enabled` | boolean | `false` | This feature can be enabled. |
| `sockets` | string\[\] |   | List of sockets to register this feature on. If empty, it would get registered on all sockets. |

Optional configuration options
