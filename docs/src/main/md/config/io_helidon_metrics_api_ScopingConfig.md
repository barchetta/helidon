Type:
[io.helidon.metrics.api.ScopingConfig](/apidocs/io.helidon.metrics.api/io/helidon/metrics/api/ScopingConfig.html)

# Configuration options

| key | type | default value | description |
|----|----|----|----|
| `default` | string | `application` | Default scope value to associate with meters that are registered without an explicit setting; no setting means meters are assigned scope io.helidon.metrics.api.Meter.Scope.DEFAULT. |
| `scopes` | [Map\<string, ScopeConfig\>](../config/io_helidon_metrics_api_ScopeConfig.md) |   | Settings for individual scopes. |
| `tag-name` | string | `scope` | Tag name for storing meter scope values in the underlying implementation meter registry. |

Optional configuration options
