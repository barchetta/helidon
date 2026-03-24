# SpanProcessorConfig (telemetry.otelconfig) Configuration

Type: [io.helidon.telemetry.otelconfig.SpanProcessorConfig](/apidocs/io.helidon.telemetry.otelconfig/io/helidon/telemetry/otelconfig/SpanProcessorConfig.html)

## Configuration options

<table style="width:100%;">
<caption>Required configuration options</caption>
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
<td style="text-align: left;"><p>SpanProcessorType (SIMPLE, BATCH)</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Span processor type.</p>
<p>Allowed values:</p>
<ul>
<li><p><code>SIMPLE</code>: Simple Span Processor.</p></li>
<li><p><code>BATCH</code>: Batch Span Processor.</p></li>
</ul></td>
</tr>
</tbody>
</table>

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
<td style="text-align: left;"><p><code>exporters</code></p></td>
<td style="text-align: left;"><p>string[]</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Name(s) of the span exporter(s) this span processor should use; specifying no names uses all configured exporters (or if no exporters are configured, the default OpenTelemetry exporter(s)).</p>
<p>Each name must be the name of one of the configured OpenTelemetryTracingConfig.exporterConfigs().</p></td>
</tr>
</tbody>
</table>
