Type:
[io.helidon.faulttolerance.CircuitBreaker](/apidocs/io.helidon.faulttolerance/io/helidon/faulttolerance/CircuitBreaker.html)

This is a standalone configuration type, prefix from configuration root:
`fault-tolerance.circuit-breakers`

# Configuration options

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
<td style="text-align: left;"><p><code>delay</code></p></td>
<td style="text-align: left;"><p>Duration</p></td>
<td style="text-align: left;"><p><code>PT5S</code></p></td>
<td style="text-align: left;"><p>How long to wait before transitioning
from open to half-open state.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>enable-metrics</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>false</code></p></td>
<td style="text-align: left;"><p>Flag to enable metrics for this
instance. The value of this flag is combined with the global config
entry
io.helidon.faulttolerance.FaultTolerance.FT_METRICS_DEFAULT_ENABLED. If
either of these flags is <code>true</code>, then metrics will be enabled
for the instance.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>error-ratio</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p><code>60</code></p></td>
<td style="text-align: left;"><p>How many failures out of 100 will
trigger the circuit to open. This is adapted to the volume() used to
handle the window of requests. If errorRatio is 40, and volume is 10, 4
failed requests will open the circuit. Default is
DEFAULT_ERROR_RATIO.</p>
<p>See volume()</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>success-threshold</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p><code>1</code></p></td>
<td style="text-align: left;"><p>How many successful calls will close a
half-open circuit. Nevertheless, the first failed call will open the
circuit again. Default is DEFAULT_SUCCESS_THRESHOLD.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>volume</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p><code>10</code></p></td>
<td style="text-align: left;"><p>Rolling window size used to calculate
ratio of failed requests. Default is DEFAULT_VOLUME.</p>
<p>See errorRatio()</p></td>
</tr>
</tbody>
</table>
