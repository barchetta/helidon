# Timeout (faulttolerance) Configuration

Type: [io.helidon.faulttolerance.Timeout](/apidocs/io.helidon.faulttolerance/io/helidon/faulttolerance/Timeout.html)

This is a standalone configuration type, prefix from configuration root: `fault-tolerance.timeouts`

## Configuration options

| key | type | default value | description |
|----|----|----|----|
| `current-thread` | boolean | `false` | Flag to indicate that code must be executed in current thread instead of in an executor’s thread. This flag is `false` by default. |
| `enable-metrics` | boolean | `false` | Flag to enable metrics for this instance. The value of this flag is combined with the global config entry io.helidon.faulttolerance.FaultTolerance.FT_METRICS_DEFAULT_ENABLED. If either of these flags is `true`, then metrics will be enabled for the instance. |
| `timeout` | Duration | `PT10S` | Duration to wait before timing out. Defaults to `10 seconds`. |

Optional configuration options
