Type:
[io.helidon.http.media.jackson.JacksonSupport](/apidocs/io.helidon.http.media.jackson/io/helidon/http/media/jackson/JacksonSupport.html)

<div class="formalpara">

<div class="title">

Config key

</div>

``` text
jackson
```

</div>

This type provides the following service implementations:

- `io.helidon.http.media.spi.MediaSupportProvider`

# Configuration options

| key | type | default value | description |
|----|----|----|----|
| `name` | string | `jackson` | Name of the support. Default value is `jackson`. |
| `properties` | Map\<string, boolean\> |   | Jackson configuration properties. Properties are being ignored if specific JacksonSupport is set. Only `boolean` configuration values are supported. |

Optional configuration options
