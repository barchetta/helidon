# TaskConfig (scheduling) Configuration

Type: [io.helidon.scheduling.TaskConfig](/apidocs/io.helidon.scheduling/io/helidon/scheduling/TaskConfig.html)

## Configuration options

| key | type | default value | description |
|----|----|----|----|
| `enabled` | boolean | `true` | Whether the task is enabled. If disabled, the task will not be scheduled. Default value is `true`. |
| `id` | string |   | Identification of the started task. This can be used to later look up the instance, for example to cancel it. |

Optional configuration options
