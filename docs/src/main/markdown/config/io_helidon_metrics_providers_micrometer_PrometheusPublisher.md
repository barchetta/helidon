# PrometheusPublisher (metrics.providers.micrometer) Configuration

Type: [io.helidon.metrics.providers.micrometer.PrometheusPublisher](/apidocs/io.helidon.metrics.providers.micrometer/io/helidon/metrics/providers/micrometer/PrometheusPublisher.html)

*Config key*

``` text
prometheus
```

This type provides the following service implementations:

- `io.helidon.metrics.spi.MetricsPublisherProvider`

## Configuration options

| key | type | default value | description |
|----|----|----|----|
| `descriptions` | boolean |   | Whether to include meter descriptions in Prometheus output. |
| `enabled` | boolean | `true` | Whether the configured publisher is enabled. |
| `interval` | Duration |   | Step size used in computing "windowed" statistics. Micrometer advises that this value should be close to the interval with which backend systems scrape the Prometheus-format metrics data. |
| `prefix` | string |   | Property name prefix. |

Optional configuration options
