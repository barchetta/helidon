# WsConfig (webserver.websocket) Configuration

Type: [io.helidon.webserver.websocket.WsConfig](/apidocs/io.helidon.webserver.websocket/io/helidon/webserver/websocket/WsConfig.html)

*Config key*

``` text
websocket
```

This type provides the following service implementations:

- `io.helidon.webserver.spi.ProtocolConfigProvider`

## Configuration options

| key | type | default value | description |
|----|----|----|----|
| `max-frame-length` | int | `1048576` | Max WebSocket frame size supported by the server on a read operation. Default is 1 MB. |
| `name` | string | `websocket` | Name of this configuration. |
| `origins` | string\[\] |   | WebSocket origins. |

Optional configuration options
