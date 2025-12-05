Type:
[io.helidon.telemetry.otelconfig.SpanExporterConfig](/apidocs/io.helidon.telemetry.otelconfig/io/helidon/telemetry/otelconfig/SpanExporterConfig.html)

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
<td style="text-align: left;"><p><code>type</code></p></td>
<td style="text-align: left;"><p>ExporterType (OTLP, ZIPKIN, CONSOLE,
LOGGING_OTLP)</p></td>
<td
style="text-align: left;"><p><code>ExporterType.DEFAULT</code></p></td>
<td style="text-align: left;"><p>Span exporter type.</p>
<p>Allowed values:</p>
<ul>
<li><p><code>OTLP</code>: OpenTelemetry Protocol
io.opentelemetry.exporter.otlp.http.trace.OtlpHttpSpanExporter and
io.opentelemetry.exporter.otlp.trace.OtlpGrpcSpanExporter.</p></li>
<li><p><code>ZIPKIN</code>: Zipkin
io.opentelemetry.exporter.zipkin.ZipkinSpanExporter.</p></li>
<li><p><code>CONSOLE</code>: Console
(io.opentelemetry.exporter.logging.LoggingSpanExporter.</p></li>
<li><p><code>LOGGING_OTLP</code>: JSON logging to console
io.opentelemetry.exporter.logging.otlp.OtlpJsonLoggingSpanExporter.</p></li>
</ul></td>
</tr>
</tbody>
</table>
