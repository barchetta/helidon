Type:
[io.helidon.webserver.ErrorHandling](/apidocs/io.helidon.webserver/io/helidon/webserver/ErrorHandling.html)

# Configuration options

| key | type | default value | description |
|----|----|----|----|
| `include-entity` | boolean | `false` | Whether to include a response entity when mapping a io.helidon.http.RequestException using a io.helidon.http.DirectHandler. Response entities may include data that is reflected back from the original request, albeit escaped to prevent potential attacks. |
| `log-all-messages` | boolean | `false` | Whether to log all messages in a io.helidon.http.RequestException or not. If set to `false`, only those that return `true` for io.helidon.http.RequestException.safeMessage() are logged. |

Optional configuration options
