Type:
[io.helidon.telemetry.otelconfig.OtlpExporterConfig](/apidocs/io.helidon.telemetry.otelconfig/io/helidon/telemetry/otelconfig/OtlpExporterConfig.html)

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
<td style="text-align: left;"><p><code>certificate</code></p></td>
<td style="text-align: left;"><p><a
href="../config/io_helidon_common_configurable_Resource.xml">Resource</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Trusted certificates.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>client.certificate</code></p></td>
<td style="text-align: left;"><p><a
href="../config/io_helidon_common_configurable_Resource.xml">Resource</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>TLS certificate.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>client.key</code></p></td>
<td style="text-align: left;"><p><a
href="../config/io_helidon_common_configurable_Resource.xml">Resource</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>TLS client key.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>compression</code></p></td>
<td style="text-align: left;"><p>CompressionType (GZIP, NONE)</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Compression the exporter uses.</p>
<p>Allowed values:</p>
<ul>
<li><p><code>GZIP</code>: GZIP compression.</p></li>
<li><p><code>NONE</code>: No compression.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>endpoint</code></p></td>
<td style="text-align: left;"><p>URI</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Endpoint of the collector to which the
exporter should transmit.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>headers</code></p></td>
<td style="text-align: left;"><p>Map&lt;string, string&gt;</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Headers added to each export
message.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>protocol</code></p></td>
<td style="text-align: left;"><p>OtlpExporterProtocolType (HTTP_PROTO,
GRPC)</p></td>
<td
style="text-align: left;"><p><code>OtlpExporterProtocolType.DEFAULT</code></p></td>
<td style="text-align: left;"><p>Exporter protocol type.</p>
<p>Allowed values:</p>
<ul>
<li><p><code>HTTP_PROTO</code>: http/proto protocol type.</p></li>
<li><p><code>GRPC</code>: grpc protocol type.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>retry-policy</code></p></td>
<td style="text-align: left;"><p>RetryPolicy</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Retry policy.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>timeout</code></p></td>
<td style="text-align: left;"><p>Duration</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Exporter timeout.</p></td>
</tr>
</tbody>
</table>
