Type:
[io.helidon.telemetry.otelconfig.ZipkinExporterConfig](/apidocs/io.helidon.telemetry.otelconfig/io/helidon/telemetry/otelconfig/ZipkinExporterConfig.html)

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
<td style="text-align: left;"><p><code>compression</code></p></td>
<td style="text-align: left;"><p>CompressionType (GZIP, NONE)</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Compression type.</p>
<p>Allowed values:</p>
<ul>
<li><p><code>GZIP</code>: GZIP compression.</p></li>
<li><p><code>NONE</code>: No compression.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>encoder</code></p></td>
<td style="text-align: left;"><p>SpanBytesEncoder (JSON_V1, THRIFT,
JSON_V2, PROTO3)</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Encoder type.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>endpoint</code></p></td>
<td style="text-align: left;"><p>URI</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Collector endpoint to which this
exporter should transmit.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>timeout</code></p></td>
<td style="text-align: left;"><p>Duration</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Exporter timeout.</p></td>
</tr>
</tbody>
</table>
