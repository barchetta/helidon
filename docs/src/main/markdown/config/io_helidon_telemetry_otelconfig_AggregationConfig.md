# AggregationConfig (telemetry.otelconfig) Configuration

Type: [io.helidon.telemetry.otelconfig.AggregationConfig](/apidocs/io.helidon.telemetry.otelconfig/io/helidon/telemetry/otelconfig/AggregationConfig.html)

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
<td style="text-align: left;"><p><code>type</code></p></td>
<td style="text-align: left;"><p>AggregationType (DROP, DEFAULT, SUM, LAST_VALUE, EXPLICIT_BUCKET_HISTOGRAM, BASE2_EXPONENTIAL_BUCKET_HISTOGRAM)</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Type of aggregation to apply.</p>
<p>Allowed values:</p>
<ul>
<li><p><code>DROP</code>: Drops all metrics; exports no metrics.</p></li>
<li><p><code>DEFAULT</code>: Default aggregation for a given instrument type.</p></li>
<li><p><code>SUM</code>: Aggregates measurements into a double sum or long sum.</p></li>
<li><p><code>LAST_VALUE</code>: Records the last seen measurement as a double aauge or long gauge.</p></li>
<li><p><code>EXPLICIT_BUCKET_HISTOGRAM</code>: Aggregates measurements into a histogram using default or explicit bucket boundaries.</p></li>
<li><p><code>BASE2_EXPONENTIAL_BUCKET_HISTOGRAM</code>: Aggregates measurements into a base-2 exponential histogram using default or explicit maximum number of buckets and maximum scale.</p></li>
</ul></td>
</tr>
</tbody>
</table>
