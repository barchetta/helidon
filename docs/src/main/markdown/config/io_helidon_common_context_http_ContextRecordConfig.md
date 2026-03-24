# ContextRecordConfig (common.context.http) Configuration

Type: [io.helidon.common.context.http.ContextRecordConfig](/apidocs/io.helidon.common.context.http/io/helidon/common/context/http/ContextRecordConfig.html)

## Configuration options

| key | type | default value | description |
|----|----|----|----|
| `array` | boolean |   | Whether to treat the option as an array of strings. This would be read from the context as an array. |
| `classifier` | string |   | String classifier of the value that will be used with io.helidon.common.context.Context.get(Object, Class). |
| `default-value` | string |   | Default value to send if not configured in context. |
| `default-values` | string\[\] |   | Default values to send if not configured in context. In case default values is an empty array, it will not be sent over the network if not present in context. |
| `header` | HeaderName |   | Name of the header to use when sending the context value over the network. |

Optional configuration options
