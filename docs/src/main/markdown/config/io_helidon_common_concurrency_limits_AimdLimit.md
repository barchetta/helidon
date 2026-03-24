# AimdLimit (common.concurrency.limits) Configuration

Type: [io.helidon.common.concurrency.limits.AimdLimit](/apidocs/io.helidon.common.concurrency.limits/io/helidon/common/concurrency/limits/AimdLimit.html)

*Config key*

``` text
aimd
```

This type provides the following service implementations:

- `io.helidon.common.concurrency.limits.spi.LimitProvider`

## Configuration options

| key | type | default value | description |
|----|----|----|----|
| `backoff-ratio` | double | `0.9` | Backoff ratio to use for the algorithm. The value must be within \[0.5, 1.0). |
| `enable-metrics` | boolean | `false` | Whether to collect metrics for the AIMD implementation. |
| `fair` | boolean | `false` | Whether the java.util.concurrent.Semaphore should be java.util.concurrent.Semaphore.isFair(). Defaults to `false`. |
| `initial-limit` | int | `20` | Initial limit. The value must be within \[minLimit(), maxLimit()\]. |
| `max-limit` | int | `200` | Maximal limit. The value must be same or higher than minLimit(). |
| `min-limit` | int | `20` | Minimal limit. The value must be same or lower than maxLimit(). |
| `queue-length` | int | `0` | How many requests can be enqueued waiting for a permit after the max limit is reached. Note that this may not be an exact behavior due to concurrent invocations. We use java.util.concurrent.Semaphore.getQueueLength() in the io.helidon.common.concurrency.limits.AimdLimit implementation. Default value is `0`. If set to {code 0}, there is no queueing. |
| `queue-timeout` | Duration | `PT1S` | How long to wait for a permit when enqueued. Defaults to `PT1S` |
| `timeout` | Duration | `PT5S` | Timeout that when exceeded is the same as if the task failed. |

Optional configuration options
