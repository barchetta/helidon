Type:
[io.helidon.webserver.grpc.GrpcConfig](/apidocs/io.helidon.webserver.grpc/io/helidon/webserver/grpc/GrpcConfig.html)

<div class="formalpara">

<div class="title">

Config key

</div>

``` text
grpc
```

</div>

This type provides the following service implementations:

- `io.helidon.webserver.spi.ProtocolConfigProvider`

# Configuration options

| key | type | default value | description |
|----|----|----|----|
| `enable-compression` | boolean | `true` | Whether to support compression if requested by a client. If explicitly disabled, no compression will be ever be used by the server even if a client-compatible compressor is found. |
| `enable-metrics` | boolean | `false` | Whether to collect metrics for gRPC server calls. |

Optional configuration options
