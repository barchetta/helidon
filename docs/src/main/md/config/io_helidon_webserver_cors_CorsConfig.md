Type:
[io.helidon.webserver.cors.CorsFeature](/apidocs/io.helidon.webserver.cors/io/helidon/webserver/cors/CorsFeature.html)

<div class="formalpara">

<div class="title">

Config key

</div>

``` text
cors
```

</div>

This type provides the following service implementations:

- `io.helidon.webserver.spi.ServerFeatureProvider`

# Configuration options

| key       | type    | default value | description                   |
|-----------|---------|---------------|-------------------------------|
| `enabled` | boolean |               | This feature can be disabled. |

Required configuration options

| key | type | default value | description |
|----|----|----|----|
| `sockets` | string\[\] |   | List of sockets to register this feature on. If empty, it would get registered on all sockets. |
| `weight` | double | `850.0` | Weight of the CORS feature. As it is used by other features, the default is quite high: CorsFeature.WEIGHT. |

Optional configuration options
