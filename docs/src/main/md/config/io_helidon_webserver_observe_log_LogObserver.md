Type:
[io.helidon.webserver.observe.log.LogObserver](/apidocs/io.helidon.webserver.observe.log/io/helidon/webserver/observe/log/LogObserver.html)

<div class="formalpara">

<div class="title">

Config key

</div>

``` text
log
```

</div>

This type provides the following service implementations:

- `io.helidon.webserver.observe.spi.ObserveProvider`

# Configuration options

| key | type | default value | description |
|----|----|----|----|
| `endpoint` | string | `log` |  |
| `permit-all` | boolean |   | Permit all access, even when not authorized. |
| `stream` | [LogStreamConfig](../config/io_helidon_webserver_observe_log_LogStreamConfig.md) | `@io.helidon.webserver.observe.log.LogStreamConfig@.create()` | Configuration of log stream. |

Optional configuration options
