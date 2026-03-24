# ThroughputLimit (common.concurrency.limits) Configuration

Type: [io.helidon.common.concurrency.limits.ThroughputLimit](/apidocs/io.helidon.common.concurrency.limits/io/helidon/common/concurrency/limits/ThroughputLimit.html)

*Config key*

``` text
throughput
```

This type provides the following service implementations:

- `io.helidon.common.concurrency.limits.spi.LimitProvider`

## Configuration options

<table style="width:100%;">
<caption>Optional configuration options</caption>
<colgroup>
<col style="width: 23%" />
<col style="width: 23%" />
<col style="width: 15%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">key</th>
<th style="text-align: left;">type</th>
<th style="text-align: left;">default value</th>
<th style="text-align: left;">description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>amount</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p><code>0</code></p></td>
<td style="text-align: left;"><p>Number of operations to allow during the relevant time window. Defaults to <code>0</code>. When set to <code>0</code>, we switch to unlimited.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>duration</code></p></td>
<td style="text-align: left;"><p>Duration</p></td>
<td style="text-align: left;"><p><code>PT1S</code></p></td>
<td style="text-align: left;"><p>Duration of the time window over which operations will be counted. Defaults to <code>PT1S</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>enable-metrics</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>false</code></p></td>
<td style="text-align: left;"><p>Whether to collect metrics for the throughput limit implementation.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>fair</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>false</code></p></td>
<td style="text-align: left;"><p>Whether the java.util.concurrent.Semaphore should be java.util.concurrent.Semaphore.isFair(). Defaults to <code>false</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>queue-length</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p><code>0</code></p></td>
<td style="text-align: left;"><p>How many requests can be enqueued waiting for a permit. Note that this may not be an exact behavior due to concurrent invocations. We use java.util.concurrent.Semaphore.getQueueLength() in the io.helidon.common.concurrency.limits.ThroughputLimit implementation. Default value is <code>0</code>. If set to {code 0}, there is no queueing.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>queue-timeout</code></p></td>
<td style="text-align: left;"><p>Duration</p></td>
<td style="text-align: left;"><p><code>PT1S</code></p></td>
<td style="text-align: left;"><p>How long to wait for a permit when enqueued. Defaults to <code>PT1S</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>rate-limiting-algorithm</code></p></td>
<td style="text-align: left;"><p>RateLimitingAlgorithmType (TOKEN_BUCKET, FIXED_RATE)</p></td>
<td style="text-align: left;"><p><code>RateLimitingAlgorithmType.TOKEN_BUCKET</code></p></td>
<td style="text-align: left;"><p>The rate limiting algorithm to apply.</p>
<p>Rate limiting algorithm is by default RateLimitingAlgorithmType.TOKEN_BUCKET.</p>
<p>Allowed values:</p>
<ul>
<li><p><code>TOKEN_BUCKET</code>: Requests require tokens from a bucket that fills over time.</p></li>
<li><p><code>FIXED_RATE</code>: Requests are processed at a fixed rate.</p></li>
</ul></td>
</tr>
</tbody>
</table>
