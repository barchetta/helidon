# GrpcConfig (webserver.grpc) Configuration

Type: [io.helidon.webserver.grpc.GrpcConfig](/apidocs/io.helidon.webserver.grpc/io/helidon/webserver/grpc/GrpcConfig.html)

*Config key*

``` text
grpc
```

This type provides the following service implementations:

- `io.helidon.webserver.spi.ProtocolConfigProvider`

## Configuration options

| key | type | default value | description |
|----|----|----|----|
| `enable-compression` | boolean | `true` | Whether to support compression if requested by a client. If explicitly disabled, no compression will ever be used by the server even if a client-compatible compressor is found. |
| `enable-metrics` | boolean | `false` | Whether to collect metrics for gRPC server calls. |
| `grpc-services` | io.helidon.webserver.grpc.spi.GrpcServerService\[\] (service provider interface) |   | gRPC server services. These services will not be discovered automatically. |
| `max-read-buffer-size` | int | `2097152` | Max size of gRPC reading buffer. If receiving an entity larger than this, processing will be aborted. This can help prevent DoS attacks. Default set to 2 MB. |

Optional configuration options
