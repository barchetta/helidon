# Retry (faulttolerance) Configuration

Type: [io.helidon.faulttolerance.Retry](/apidocs/io.helidon.faulttolerance/io/helidon/faulttolerance/Retry.html)

This is a standalone configuration type, prefix from configuration root: `fault-tolerance.retries`

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
<td style="text-align: left;"><p><code>calls</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p><code>3</code></p></td>
<td style="text-align: left;"><p>Number of calls (first try + retries).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>delay</code></p></td>
<td style="text-align: left;"><p>Duration</p></td>
<td style="text-align: left;"><p><code>PT0.2S</code></p></td>
<td style="text-align: left;"><p>Base delay between try and retry. Defaults to <code>200 ms</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>delay-factor</code></p></td>
<td style="text-align: left;"><p>double</p></td>
<td style="text-align: left;"><p><code>-1.0</code></p></td>
<td style="text-align: left;"><p>Delay retry policy factor. If unspecified (value of <code>-1</code>), Jitter retry policy would be used, unless jitter is also unspecified.</p>
<p>Default when Retry.DelayingRetryPolicy is used is <code>2</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>enable-metrics</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>false</code></p></td>
<td style="text-align: left;"><p>Flag to enable metrics for this instance. The value of this flag is combined with the global config entry io.helidon.faulttolerance.FaultTolerance.FT_METRICS_DEFAULT_ENABLED. If either of these flags is <code>true</code>, then metrics will be enabled for the instance.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>jitter</code></p></td>
<td style="text-align: left;"><p>Duration</p></td>
<td style="text-align: left;"><p><code>PT-1S</code></p></td>
<td style="text-align: left;"><p>Jitter for Retry.JitterRetryPolicy. If unspecified (value of <code>-1</code>), delaying retry policy is used. If both this value, and delayFactor() are specified, delaying retry policy would be used.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>overall-timeout</code></p></td>
<td style="text-align: left;"><p>Duration</p></td>
<td style="text-align: left;"><p><code>PT1S</code></p></td>
<td style="text-align: left;"><p>Overall timeout of all retries combined.</p></td>
</tr>
</tbody>
</table>
