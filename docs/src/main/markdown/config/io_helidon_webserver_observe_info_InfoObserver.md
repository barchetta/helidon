# InfoObserver (webserver.observe.info) Configuration

Type: [io.helidon.webserver.observe.info.InfoObserver](/apidocs/io.helidon.webserver.observe.info/io/helidon/webserver/observe/info/InfoObserver.html)

*Config key*

``` text
info
```

This type provides the following service implementations:

- `io.helidon.webserver.observe.spi.ObserveProvider`

## Configuration options

| key | type | default value | description |
|----|----|----|----|
| `enabled` | boolean | `true` | Whether this observer is enabled. |
| `endpoint` | string | `info` |  |
| `values` | Map\<string, string\> |   | Values to be exposed using this observability endpoint. |

Optional configuration options
