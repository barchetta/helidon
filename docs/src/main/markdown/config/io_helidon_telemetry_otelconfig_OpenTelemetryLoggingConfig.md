# OpenTelemetryLoggingConfig (telemetry.otelconfig) Configuration

Type: [io.helidon.telemetry.otelconfig.OpenTelemetryLoggingConfig](/apidocs/io.helidon.telemetry.otelconfig/io/helidon/telemetry/otelconfig/OpenTelemetryLoggingConfig.html)

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
<td style="text-align: left;"><p><code>enabled</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Whether the OpenTelemetry logger should be enabled. (Passed to OpenTelemetry.)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>exporters</code></p></td>
<td style="text-align: left;"><p>Map&lt;string, LogRecordExporter&gt;</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Log record exporters.</p>
<p>The key in the map is a unique name—​of the user’s choice—​for the exporter config settings. The ProcessorConfig.exporters() config setting for a processor config specifies zero or more of these names to associate the exporters built from the exporter configs with the processor built from the processor config.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>log-limits</code></p></td>
<td style="text-align: left;"><p>LogLimits</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Log limits to apply to log transmission.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>minimum-severity</code></p></td>
<td style="text-align: left;"><p>Severity (UNDEFINED_SEVERITY_NUMBER, TRACE, TRACE2, TRACE3, TRACE4, DEBUG, DEBUG2, DEBUG3, DEBUG4, INFO, INFO2, INFO3, INFO4, WARN, WARN2, WARN3, WARN4, ERROR, ERROR2, ERROR3, ERROR4, FATAL, FATAL2, FATAL3, FATAL4)</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Minimum severity level of log records to process.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>processors</code></p></td>
<td style="text-align: left;"><p><a href="../config/../config/io_helidon_telemetry_otelconfig_ProcessorConfig.xml">ProcessorConfig[]</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Settings for logging processors.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>trace-based</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Whether to include &lt;em&gt;only&lt;/em&gt; log records from traces which are sampled. Defaults to the OpenTelemetry default.</p></td>
</tr>
</tbody>
</table>
