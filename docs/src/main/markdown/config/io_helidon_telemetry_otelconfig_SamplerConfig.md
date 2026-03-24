# SamplerConfig (telemetry.otelconfig) Configuration

Type: [io.helidon.telemetry.otelconfig.SamplerConfig](/apidocs/io.helidon.telemetry.otelconfig/io/helidon/telemetry/otelconfig/SamplerConfig.html)

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
<td style="text-align: left;"><p><code>param</code></p></td>
<td style="text-align: left;"><p>double</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Sampler parameter.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>type</code></p></td>
<td style="text-align: left;"><p>SamplerType (ALWAYS_ON, ALWAYS_OFF, TRACEIDRATIO, PARENTBASED_ALWAYS_ON, PARENTBASED_ALWAYS_OFF, PARENTBASED_TRACEIDRATIO)</p></td>
<td style="text-align: left;"><p><code>SamplerType.DEFAULT</code></p></td>
<td style="text-align: left;"><p>Sampler type.</p>
<p>Allowed values:</p>
<ul>
<li><p><code>ALWAYS_ON</code>: Always on sampler.</p></li>
<li><p><code>ALWAYS_OFF</code>: Always off sampler.</p></li>
<li><p><code>TRACEIDRATIO</code>: Trace ID ratio-based sampler.</p></li>
<li><p><code>PARENTBASED_ALWAYS_ON</code>: Parent-based always-on sampler.</p></li>
<li><p><code>PARENTBASED_ALWAYS_OFF</code>: Parent-based always-off sampler.</p></li>
<li><p><code>PARENTBASED_TRACEIDRATIO</code>: Parent-based trace ID ration-based sampler.</p></li>
</ul></td>
</tr>
</tbody>
</table>
