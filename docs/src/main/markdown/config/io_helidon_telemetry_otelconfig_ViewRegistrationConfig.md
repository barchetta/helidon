# ViewRegistrationConfig (telemetry.otelconfig) Configuration

Type: [io.helidon.telemetry.otelconfig.ViewRegistrationConfig](/apidocs/io.helidon.telemetry.otelconfig/io/helidon/telemetry/otelconfig/ViewRegistrationConfig.html)

## Configuration options

| key | type | default value | description |
|----|----|----|----|
| `aggregation` | Aggregation |   | Aggregation for the metric view, configurable as an io.helidon.telemetry.otelconfig.AggregationType: `DROP, DEFAULT, SUM, LAST_VALUE, EXPLICIT_BUCKET_HISTOGRAM, BASE2_EXPONENTIAL_BUCKET_HISTOGRAM`. |
| `attribute-filter` | Predicate |   | Attribute name filter, configurable as a string compiled as a regular expression using java.util.regex.Pattern. |
| `cardinality-limit` | int |   | Cardinality limit. |
| `description` | string |   | Metric view description. |
| `instrument-selector` | InstrumentSelector |   | Instrument selector, configurable using io.helidon.telemetry.otelconfig.InstrumentSelectorConfig. |
| `name` | string |   | Metrics view name. |

Optional configuration options
