Type:
[io.helidon.http.media.gson.GsonSupport](/apidocs/io.helidon.http.media.gson/io/helidon/http/media/gson/GsonSupport.html)

<div class="formalpara">

<div class="title">

Config key

</div>

``` text
gson
```

</div>

This type provides the following service implementations:

- `io.helidon.http.media.spi.MediaSupportProvider`

# Configuration options

| key | type | default value | description |
|----|----|----|----|
| `name` | string | `gson` | Name of the support. Default value is `gson`. |
| `properties` | Map\<string, boolean\> |   | Gson configuration properties. Properties are being ignored if specific Gson is set. Only `boolean` configuration values are supported. |

Optional configuration options
