# RestServiceSettings (webserver.servicecommon) Configuration

Type: [io.helidon.webserver.servicecommon.RestServiceSettings](/apidocs/io.helidon.servicecommon/io/helidon/webserver/servicecommon/RestServiceSettings.html)

## Configuration options

| key | type | default value | description |
|----|----|----|----|
| `cors` | [Map\<string, CrossOriginConfig\>](../config/io_helidon_cors_CrossOriginConfig.md) |   | Sets the cross-origin config builder for use in establishing CORS support for the service endpoints. |
| `enabled` | boolean | `true` | Is this service enabled or not. |
| `routing` | string |   | Sets the routing name to use for setting up the service’s endpoint. |
| `web-context` | string |   | Sets the web context to use for the service’s endpoint. |

Optional configuration options
