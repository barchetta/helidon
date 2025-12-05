Type:
[io.helidon.webserver.context.ContextFeature](/apidocs/io.helidon.webserver.context/io/helidon/webserver/context/ContextFeature.html)

<div class="formalpara">

<div class="title">

Config key

</div>

``` text
context
```

</div>

This type provides the following service implementations:

- `io.helidon.webserver.spi.ServerFeatureProvider`

# Configuration options

| key | type | default value | description |
|----|----|----|----|
| `records` | [ContextRecordConfig\[\]](../config/io_helidon_common_context_http_ContextRecordConfig.md) |   | List of propagation records. |
| `sockets` | string\[\] |   | List of sockets to register this feature on. If empty, it would get registered on all sockets. |
| `weight` | double | `1100.0` | Weight of the context feature. As it is used by other features, the default is quite high: io.helidon.webserver.context.ContextFeature.WEIGHT. |

Optional configuration options
