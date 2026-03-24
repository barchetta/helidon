# OtlpPublisher (metrics.providers.micrometer) Configuration

Type: [io.helidon.metrics.providers.micrometer.OtlpPublisher](/apidocs/io.helidon.metrics.providers.micrometer/io/helidon/metrics/providers/micrometer/OtlpPublisher.html)

*Config key*

``` text
otlp
```

This type provides the following service implementations:

- `io.helidon.metrics.spi.MetricsPublisherProvider`

## Configuration options

| key | type | default value | description |
|----|----|----|----|
| `aggregation-temporality` | AggregationTemporality (DELTA, CUMULATIVE) | `AggregationTemporality.CUMULATIVE` | Algorithm to use for adjusting values before transmission. |
| `base-time-unit` | TimeUnit (NANOSECONDS, MICROSECONDS, MILLISECONDS, SECONDS, MINUTES, HOURS, DAYS) | `TimeUnit.java.util.concurrent.TimeUnit.MILLISECONDS` | Base time unit for timers. |
| `batch-size` | int | `10000` | Number of measurements to send in a single request to the backend. |
| `enabled` | boolean | `true` | Whether the configured publisher is enabled. |
| `headers` | Map\<string, string\> |   | Headers to add to each transmission message. |
| `interval` | Duration | `PT60s` | Interval between successive transmissions of metrics data. |
| `max-bucket-count` | int | `160` | Maximum bucket count to apply to statistical histogram. |
| `max-buckets-per-meter` | Map\<string, int\> |   | Maximum number of buckets to use for specific meters. |
| `max-scale` | int | `20` | Maximum scale value to apply to statistical histogram. |
| `prefix` | string | `otlp` | The prefix for settings. |
| `properties` | Map\<string, string\> |   | Property values to be returned by the OTLP meter registry configuration. |
| `resource-attributes` | Map\<string, string\> |   | Attribute name/value pairs to be associated with all metrics transmissions. |
| `url` | string | `http://localhost:4318/v1/metrics` | URL to which to send metrics telemetry. |

Optional configuration options
