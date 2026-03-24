# AutoHttpMetricsPathConfig (webserver.observe.metrics) Configuration

Type: [io.helidon.webserver.observe.metrics.AutoHttpMetricsPathConfig](/apidocs/io.helidon.webserver.observe.metrics/io/helidon/webserver/observe/metrics/AutoHttpMetricsPathConfig.html)

## Configuration options

| key | type | default value | description |
|----|----|----|----|
| `enabled` | boolean | `true` | Whether automatic metrics are to be enabled for requests which match the specified io.helidon.http.PathMatcher and HTTP methods. |
| `methods` | string\[\] |   | HTTP methods for which this path config applies; default is to match all HTTP methods. |
| `path` | string |   | Path matching expression for this path config entry. |

Optional configuration options
