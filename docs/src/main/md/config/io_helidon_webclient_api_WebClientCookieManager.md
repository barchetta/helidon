Type:
[io.helidon.webclient.api.WebClientCookieManager](/apidocs/io.helidon.webclient.api/io/helidon/webclient/api/WebClientCookieManager.html)

# Configuration options

| key | type | default value | description |
|----|----|----|----|
| `automatic-store-enabled` | boolean | `false` | Whether automatic cookie store is enabled or not. |
| `cookie-policy` | CookiePolicy | `java.net.CookiePolicy.ACCEPT_ORIGINAL_SERVER` | Current cookie policy for this client. |
| `default-cookies` | Map\<string, string\> |   | Map of default cookies to include in all requests if cookies enabled. |

Optional configuration options
