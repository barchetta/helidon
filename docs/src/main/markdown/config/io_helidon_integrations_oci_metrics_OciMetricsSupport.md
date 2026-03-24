# OciMetricsSupport (integrations.oci.metrics) Configuration

Type: [io.helidon.integrations.oci.metrics.OciMetricsSupport](/apidocs/io.helidon.integrations.oci.metrics/io/helidon/integrations/oci/metrics/OciMetricsSupport.html)

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
<td style="text-align: left;"><p><code>batch-delay</code></p></td>
<td style="text-align: left;"><p>long</p></td>
<td style="text-align: left;"><p><code>1</code></p></td>
<td style="text-align: left;"><p>Sets the delay interval if metrics are posted in batches (defaults to <code>1</code>).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>batch-size</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p><code>50</code></p></td>
<td style="text-align: left;"><p>Sets the maximum no. of metrics to send in a batch (defaults to <code>50</code>).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>compartment-id</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Sets the compartment ID.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>delay</code></p></td>
<td style="text-align: left;"><p>long</p></td>
<td style="text-align: left;"><p><code>60</code></p></td>
<td style="text-align: left;"><p>Sets the delay interval between metric posting (defaults to <code>60</code>).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>description-enabled</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Sets whether the description should be enabled or not.</p>
<pre><code>Defaults to `true`.</code></pre></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>enabled</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Sets whether metrics transmission to OCI is enabled.</p>
<pre><code>Defaults to `true`.</code></pre></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>initial-delay</code></p></td>
<td style="text-align: left;"><p>long</p></td>
<td style="text-align: left;"><p><code>1</code></p></td>
<td style="text-align: left;"><p>Sets the initial delay before metrics are sent to OCI (defaults to <code>1</code>).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>namespace</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Sets the namespace.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>resource-group</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Sets the resource group.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scheduling-time-unit</code></p></td>
<td style="text-align: left;"><p>TimeUnit (NANOSECONDS, MICROSECONDS, MILLISECONDS, SECONDS, MINUTES, HOURS, DAYS)</p></td>
<td style="text-align: left;"><p><code>TimeUnit.SECONDS</code></p></td>
<td style="text-align: left;"><p>Sets the time unit applied to the initial delay and delay values (defaults to <code>TimeUnit.SECONDS</code>).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scopes</code></p></td>
<td style="text-align: left;"><p>String[]</p></td>
<td style="text-align: left;"><p><code>All scopes</code></p></td>
<td style="text-align: left;"><p>Sets which metrics scopes (e.g., base, vendor, application) should be sent to OCI.</p>
<pre><code>If this method is never invoked, defaults to all scopes.</code></pre></td>
</tr>
</tbody>
</table>
