# PeriodicMetricReaderConfig (telemetry.otelconfig) Configuration

Type: [io.helidon.telemetry.otelconfig.PeriodicMetricReaderConfig](/apidocs/io.helidon.telemetry.otelconfig/io/helidon/telemetry/otelconfig/PeriodicMetricReaderConfig.html)

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
<td style="text-align: left;"><p><code>exporter</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Name of the configured metric exporter to use for this metric reader.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>interval</code></p></td>
<td style="text-align: left;"><p>Duration</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Metric reader read interval.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>type</code></p></td>
<td style="text-align: left;"><p>MetricReaderType (PERIODIC)</p></td>
<td style="text-align: left;"><p><code>MetricReaderType.PERIODIC</code></p></td>
<td style="text-align: left;"><p>Metric reader type.</p>
<p>Allowed values:</p>
<ul>
<li><p><code>PERIODIC</code>: Periodic metric reader type.</p></li>
</ul></td>
</tr>
</tbody>
</table>
