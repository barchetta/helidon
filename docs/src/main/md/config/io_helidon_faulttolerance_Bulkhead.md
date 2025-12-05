Type:
[io.helidon.faulttolerance.Bulkhead](/apidocs/io.helidon.faulttolerance/io/helidon/faulttolerance/Bulkhead.html)

This is a standalone configuration type, prefix from configuration root:
`fault-tolerance.bulkheads`

# Configuration options

| key | type | default value | description |
|----|----|----|----|
| `enable-metrics` | boolean | `false` | Flag to enable metrics for this instance. The value of this flag is combined with the global config entry io.helidon.faulttolerance.FaultTolerance.FT_METRICS_DEFAULT_ENABLED. If either of these flags is `true`, then metrics will be enabled for the instance. |
| `limit` | int | `10` | Maximal number of parallel requests going through this bulkhead. When the limit is reached, additional requests are enqueued. |
| `queue-length` | int | `10` | Maximal number of enqueued requests waiting for processing. When the limit is reached, additional attempts to invoke a request will receive a BulkheadException. |

Optional configuration options
