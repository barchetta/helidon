Type:
[io.helidon.telemetry.otelconfig.HelidonOpenTelemetry](/apidocs/io.helidon.telemetry.otelconfig/io/helidon/telemetry/otelconfig/HelidonOpenTelemetry.html)

This is a standalone configuration type, prefix from configuration root:
`telemetry`

# Configuration options

| key | type | default value | description |
|----|----|----|----|
| `service` | string |   | Service name used in sending telemetry data to the collector. |

Required configuration options

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
<td style="text-align: left;"><p><code>enabled</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Whether the OpenTelemetry support is
enabled.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>global</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Whether the
io.opentelemetry.api.OpenTelemetry instance created from this
configuration should be made the global one.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>propagators</code></p></td>
<td style="text-align: left;"><p>TextMapPropagator[]</p></td>
<td
style="text-align: left;"><p><code>new java.util.ArrayList&lt;&gt;(io.helidon.telemetry.otelconfig.ContextPropagationType.DEFAULT_PROPAGATORS)</code></p></td>
<td style="text-align: left;"><p>OpenTelemetry
io.opentelemetry.context.propagation.TextMapPropagator instances added
explicitly by the app.</p>
<p>Default: ContextPropagationType.DEFAULT_NAMES. See
io.helidon.telemetry.otelconfig.ContextPropagationType</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>signals.tracing</code></p></td>
<td style="text-align: left;"><p><a
href="../config/io_helidon_telemetry_otelconfig_OpenTelemetryTracingConfig.xml">OpenTelemetryTracingConfig</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>OpenTelemetry tracing
settings.</p></td>
</tr>
</tbody>
</table>
