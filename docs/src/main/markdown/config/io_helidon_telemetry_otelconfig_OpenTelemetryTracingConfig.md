# OpenTelemetryTracingConfig (telemetry.otelconfig) Configuration

Type: [io.helidon.telemetry.otelconfig.OpenTelemetryTracingConfig](/apidocs/io.helidon.telemetry.otelconfig/io/helidon/telemetry/otelconfig/OpenTelemetryTracingConfig.html)

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
<td style="text-align: left;"><p><code>attributes</code></p></td>
<td style="text-align: left;"><p>AttributesBuilder</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Name/value pairs passed to OpenTelemetry.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>exporters</code></p></td>
<td style="text-align: left;"><p>Map&lt;string, SpanExporter&gt;</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Span exporters.</p>
<p>The key in the map is a unique name—​of the user’s choice—​for the exporter config settings. The ProcessorConfig.exporters() config setting for a processor config specifies zero or more of these names to associate the exporters built from the exporter configs with the processor built from the processor config.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>processors</code></p></td>
<td style="text-align: left;"><p><a href="../config/../config/io_helidon_telemetry_otelconfig_ProcessorConfig.xml">ProcessorConfig[]</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Settings for span processors.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>sampler</code></p></td>
<td style="text-align: left;"><p>Sampler</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Tracing sampler.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>span-limits</code></p></td>
<td style="text-align: left;"><p>SpanLimits</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Tracing span limits.</p></td>
</tr>
</tbody>
</table>
