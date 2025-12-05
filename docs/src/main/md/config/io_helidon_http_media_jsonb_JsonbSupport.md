Type:
[io.helidon.http.media.jsonb.JsonbSupport](/apidocs/io.helidon.http.media.jsonb/io/helidon/http/media/jsonb/JsonbSupport.html)

<div class="formalpara">

<div class="title">

Config key

</div>

``` text
jsonb
```

</div>

This type provides the following service implementations:

- `io.helidon.http.media.spi.MediaSupportProvider`

# Configuration options

| key | type | default value | description |
|----|----|----|----|
| `boolean-properties` | Map\<string, boolean\> |   | Jsonb `boolean` configuration properties. Properties are being ignored if specific Jsonb is set. |
| `class-properties` | Map\<string, Class\> |   | Jsonb Class configuration properties. Properties are being ignored if specific Jsonb is set. |
| `name` | string | `jsonb` | Name of the support. Default value is `jsonb`. |
| `properties` | Map\<string, string\> |   | Jsonb String configuration properties. Properties are being ignored if specific Jsonb is set. |

Optional configuration options
