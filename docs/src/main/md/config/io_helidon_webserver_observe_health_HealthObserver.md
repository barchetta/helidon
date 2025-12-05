Type:
[io.helidon.webserver.observe.health.HealthObserver](/apidocs/io.helidon.webserver.observe.health/io/helidon/webserver/observe/health/HealthObserver.html)

This is a standalone configuration type, prefix from configuration root:
`health`

This type provides the following service implementations:

- `io.helidon.webserver.observe.spi.ObserveProvider`

# Configuration options

| key | type | default value | description |
|----|----|----|----|
| `details` | boolean | `false` | Whether details should be printed. By default, health only returns a io.helidon.http.Status.NO_CONTENT_204 for success, io.helidon.http.Status.SERVICE_UNAVAILABLE_503 for health down, and io.helidon.http.Status.INTERNAL_SERVER_ERROR_500 in case of error with no entity. When details are enabled, health returns io.helidon.http.Status.OK_200 for success, same codes otherwise and a JSON entity with detailed information about each health check executed. |
| `endpoint` | string | `health` |  |
| `exclude` | string\[\] |   | Health check names to exclude in computing the overall health of the server. |
| `use-system-services` | boolean | `true` | Whether to use services discovered by java.util.ServiceLoader. By default, all io.helidon.health.spi.HealthCheckProvider based health checks are added. |

Optional configuration options
