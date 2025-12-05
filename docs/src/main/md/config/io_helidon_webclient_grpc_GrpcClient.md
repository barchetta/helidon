Type:
[io.helidon.webclient.grpc.GrpcClient](/apidocs/io.helidon.webclient.grpc/io/helidon/webclient/grpc/GrpcClient.html)

# Configuration options

| key | type | default value | description |
|----|----|----|----|
| `enable-metrics` | boolean | `false` | Whether to collect metrics for gRPC client calls. |
| `grpc-services` | io.helidon.webclient.grpc.spi.GrpcClientService\[\] (service provider interface) |   | gRPC client services. A gRPC service needs to be explicitly added to be enabled given that `discoveredServices` is `false`. |
| `protocol-config` | [GrpcClientProtocolConfig](../config/io_helidon_webclient_grpc_GrpcClientProtocolConfig.md) | `create()` | gRPC specific configuration. |

Optional configuration options
