Type:
[io.helidon.common.concurrency.limits.FixedLimit](/apidocs/io.helidon.common.concurrency.limits/io/helidon/common/concurrency/limits/FixedLimit.html)

<div class="formalpara">

<div class="title">

Config key

</div>

``` text
fixed
```

</div>

This type provides the following service implementations:

- `io.helidon.common.concurrency.limits.spi.LimitProvider`

# Configuration options

| key | type | default value | description |
|----|----|----|----|
| `enable-metrics` | boolean | `false` | Whether to collect metrics for the AIMD implementation. |
| `fair` | boolean | `false` | Whether the java.util.concurrent.Semaphore should be java.util.concurrent.Semaphore.isFair(). Defaults to `false`. |
| `permits` | int | `0` | Number of permit to allow. Defaults to FixedLimit.DEFAULT_LIMIT. When set to `0`, we switch to unlimited. |
| `queue-length` | int | `0` | How many requests can be enqueued waiting for a permit. Note that this may not be an exact behavior due to concurrent invocations. We use java.util.concurrent.Semaphore.getQueueLength() in the io.helidon.common.concurrency.limits.FixedLimit implementation. Default value is FixedLimit.DEFAULT_QUEUE_LENGTH. If set to {code 0}, there is no queueing. |
| `queue-timeout` | Duration | `PT1S` | How long to wait for a permit when enqueued. Defaults to FixedLimit.DEFAULT_QUEUE_TIMEOUT_DURATION |

Optional configuration options
