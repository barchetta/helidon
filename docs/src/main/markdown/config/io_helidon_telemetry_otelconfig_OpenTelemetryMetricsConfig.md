# OpenTelemetryMetricsConfig (telemetry.otelconfig) Configuration

Type: [io.helidon.telemetry.otelconfig.OpenTelemetryMetricsConfig](/apidocs/io.helidon.telemetry.otelconfig/io/helidon/telemetry/otelconfig/OpenTelemetryMetricsConfig.html)

## Configuration options

| key | type | default value | description |
|----|----|----|----|
| `attributes` | AttributesBuilder |   | Name/value pairs passed to OpenTelemetry. |
| `exporters` | Map\<string, MetricExporter\> |   | Metric exporter configurations, configurable using io.helidon.telemetry.otelconfig.MetricExporterConfig. |
| `readers` | [MetricReaderConfig\[\]](../config/../config/io_helidon_telemetry_otelconfig_MetricReaderConfig.md) |   | Settings for metric readers. |
| `views` | OpenTelemetryMetricsConfigSupport.ViewRegistration\[\] |   | Metric view information, configurable using io.helidon.telemetry.otelconfig.ViewRegistrationConfig. |

Optional configuration options
