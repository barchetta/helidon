# Beginning with Helidon 4.1, strongly consider assigning the config setting

- a unified way for servers to export monitoring data—​telemetry—​to management agents, and

- a unified Java API which all application programmers can use to register and update {metrics} to expose telemetry data from their services.

Metrics is one of the Helidon observability features.

> [!NOTE]
> Beginning with Helidon 4.1, strongly consider assigning the config setting
>
> ``` properties
> metrics.gc-time-type = gauge
> ```
>
> See the [longer discussion below](#controlling-gc-time) in the Configuration section.

## Instrumenting Your Service

You add {metrics} to your service

Later sections of this document describe how to do

## {metric_uc} Types

Helidon supports meters and summarized in the following table:

| {metric_uc} Type | Description |  |
|----|----|----|
|  | Monotonically-increasing `long` value. |  |
|  | Summary of samples each with a `long` value. Reports aggregate information over all samples (count, total, mean, max) as well as the distribution of sample values using percentiles and bucket counts. |  |
|  | Accumulation of short-duration (typically under a minute) intervals. Typically updated using a Java [`Duration`]({jdk-javadoc-url}/java.base/java/time/Duration.md) or by recording the time taken by a method invocation or lambda. Reports the count, total time, max, and mean; provides a of the samples. |  |
|  | View of a value that is assignment-compatible with a subtype of Java [`Number`]({jdk-javadoc-url}/java.base/java.lang.Number.md). The underlying value is updated by code elsewhere in the system, not by invoking methods on the gauge itself. |  |

Types of {metrics_uc}

## Categorizing Types of {Metrics_uc}

Helidon distinguishes among *scopes*, or categories, of

Helidon includes {metrics} in the built-in scopes described below. Applications often register their own {metrics} in the `application` scope but can create their own scopes and register {metrics} within them.

| Built-in Scope | Typical Usage |
|----|----|
| `base` | OS or Java runtime measurements (available heap, disk space, etc.). |
| `vendor` | Implemented by vendors, including the `REST.request` metrics and other key performance indicator measurements (described in later sections). |
| `application` | Declared via annotations or programmatically registered by your service code. |

Built-in {metric} scopes

## Publishing Metrics for External Access

Helidon’s Micrometer-based metrics implementation includes these ways of publishing metrics data to external systems:

- Prometheus/OpenMetrics

- OTLP (OpenTelemetry Protocol)

### Configuring Publishers

> [!NOTE]
> The configuration of metrics publishers as described below is a [preview feature]({javadoc-base-url}/io.helidon.common.features.api/io/helidon/common/features/api/Preview.md) which Helidon intends to keep, but its external interface or behavior might evolve between dot releases.

You can configure publishers in the `publishers` configuration section under the top level `metrics` node or under `server.features.observe.observers.metrics`. If you do not set up publishers explicitly, Helidon uses an inferred Prometheus publisher for backward compatibility. See [this later section](#understanding_inferred) for details.

Publishers in Helidon’s Micrometer-based metrics implementation use Micrometer `MeterRegistry` implementations. For each enabled publisher, Helidon adds the corresponding meter registry to Micrometer’s global registry. This has these important effects:

- {meters_uc} which Helidon or your code registers using the Helidon metrics API are registered in all active Micrometer meter registries.

- Each Helidon meter registered has an implementation in every active Micrometer meter registry.

- When Helidon or your code updates a Helidon {meter}, Micrometer applies the change to every corresponding {meter} from each active meter registry.

As a result, configuring more than one active meter registry can affect performance.

> [!NOTE]
> Make sure at least one of the configured publishers is enabled. If not, Micrometer does not have any active meter registry implementations and the registered metrics are no-ops. Helidon logs a warning in this case during the metrics observer initialization.

#### Configuring an OTLP Publisher

If you configure an OTLP publisher, Helidon exports metrics data periodically to a backend system you configure.

### Configuration options

| Key | Kind | Type | Default Value | Description |
|----|----|----|----|----|
| <span id="a5a031-aggregation-temporality"></span> [`aggregation-temporality`](../../config/io_micrometer_registry_otlp_AggregationTemporality.md) | `VALUE` | `i.m.r.o.AggregationTemporality` | `CUMULATIVE` | Algorithm to use for adjusting values before transmission |
| <span id="a726ba-base-time-unit"></span> [`base-time-unit`](../../config/java_util_concurrent_TimeUnit.md) | `VALUE` | `TimeUnit` | `java.util.concurrent.TimeUnit.MILLISECONDS` | Base time unit for timers |
| <span id="ace1fb-batch-size"></span> `batch-size` | `VALUE` | `Integer` | `10000` | Number of measurements to send in a single request to the backend |
| <span id="a6b5d5-enabled"></span> `enabled` | `VALUE` | `Boolean` | `true` | Whether the configured publisher is enabled |
| <span id="a821e5-headers"></span> `headers` | `MAP` | `String` |   | Headers to add to each transmission message |
| <span id="afbfb5-interval"></span> `interval` | `VALUE` | `Duration` | `PT60s` | Interval between successive transmissions of metrics data |
| <span id="a65cf0-max-bucket-count"></span> `max-bucket-count` | `VALUE` | `Integer` | `160` | Maximum bucket count to apply to statistical histogram |
| <span id="a11feb-max-buckets-per-meter"></span> `max-buckets-per-meter` | `MAP` | `Integer` |   | Maximum number of buckets to use for specific meters |
| <span id="a52180-max-scale"></span> `max-scale` | `VALUE` | `Integer` | `20` | Maximum scale value to apply to statistical histogram |
| <span id="a00636-name"></span> `name` | `VALUE` | `String` |   | `N/A` |
| <span id="a64095-prefix"></span> `prefix` | `VALUE` | `String` | `otlp` | The prefix for settings |
| <span id="afb329-properties"></span> `properties` | `MAP` | `String` |   | Property values to be returned by the OTLP meter registry configuration |
| <span id="a5f081-resource-attributes"></span> `resource-attributes` | `MAP` | `String` |   | Attribute name/value pairs to be associated with all metrics transmissions |
| <span id="a1f8b3-url"></span> `url` | `VALUE` | `String` | `http://localhost:4318/v1/metrics` | URL to which to send metrics telemetry |

The configuration directly mirrors the Micrometer `OtlpMeterRegistry` settings so you can control all behavior which Micrometer exposes for the meter registry.

The following example sets up an OTLP publisher to transmit metrics data every 30 seconds.

*Example OTLP publisher settings*

``` yaml
metrics:
  publishers:         
    otlp:  
      interval: PT30S
      url: 'http://somehost.com:4318/v1/metrics'
```

- Introduces the configured publishers.

- Configures an OTLP publisher to transmit every 30 seconds to the given endpoint.

#### Configuring a Prometheus Publisher

If you configure a Prometheus publisher or rely on the inferred one, Helidon can make the metrics data available in the Prometheus/OpenMetrics format. (To serve the data at the metrics endpoint in your service, your project must also depend on the Helidon metrics observer component.)

### Configuration options

| Key | Kind | Type | Default Value | Description |
|----|----|----|----|----|
| <span id="a6614e-descriptions"></span> `descriptions` | `VALUE` | `Boolean` |   | Whether to include meter descriptions in Prometheus output |
| <span id="a248f8-enabled"></span> `enabled` | `VALUE` | `Boolean` | `true` | Whether the configured publisher is enabled |
| <span id="ae8bbc-interval"></span> `interval` | `VALUE` | `Duration` |   | Step size used in computing "windowed" statistics |
| <span id="abd446-name"></span> `name` | `VALUE` | `String` |   | `N/A` |
| <span id="a3221e-prefix"></span> `prefix` | `VALUE` | `String` |   | Property name prefix |

#### Understanding the Inferred Prometheus Publisher

As described earlier, Helidon prepares an inferred Prometheus publisher if you do not set up any publishers.

Note that Helidon uses the inferred publisher *only* if you add *no* publishers explicitly, either in the configuration or programmatically. If you specify any publishers explicitly, Helidon uses only the ones you set up.

In particular, Helidon *does not* use the inferred Prometheus publisher if you create a `metrics.publishers` section containing only an OTLP publisher.

You can configure other publishers and still have Helidon use the default one by simply adding the `prometheus` publisher entry. You do not need to specify further settings for it.

*Using an OLTP publisher **and** the default Prometheus publisher*

``` yaml
metrics:
  publishers:
    prometheus:
    otlp:
      interval: PT20S
```

### Writing Additional Publishers

You can write other publishers by following these steps:

1.  Choose one of the Micrometer `MeterRegistry` implementations for the type of publishing you want to support. (for example [`DatadogMeterRegistry`](https://github.com/micrometer-metrics/micrometer/tree/main/implementations/micrometer-registry-datadog))

2.  Create a config blueprint which exposes the meter registry’s [settable properties from `DatadogConfig`](https://github.com/micrometer-metrics/micrometer/blob/main/implementations/micrometer-registry-datadog/src/main/java/io/micrometer/datadog/DatadogConfig.java).

3.  Write a `DatadogPublisher` class which implements Helidon’s `MetricsPublisher` for Datadog.

4.  Write a `DatadogPublisherProvider` class which implements Helidon’s `MetricsPublisherProvider` for your publisher.

5.  Advertise your provider so Java service loading can find it, creating a `META-INF/services/io.helidon.metrics.spi.PublisherProvider` file listing your implementation class.

Look at Helidon’s [OTLP publisher blueprint]({https://github.com/helidon-io/helidon/tree/main/metrics/providers/micrometer/src/main/java/io/helidon/metrics/providers/micrometer/OtlpPublisherConfigBlueprint.java) and the related types as an example.

Refer to your publisher in configuration using the config key you set up in the publisher provider.

*Example config using a hypothetical Datadog publisher*

``` yaml
metrics:
  publishers:
    micrometer-datadog:
      interval: PT15S
```

### Using and Controlling the Metrics Endpoint

When you add the to your project, and if you explicitly set up a Prometheus publisher or use the default one, Helidon provides a built-in REST endpoint `{metrics-endpoint}` which responds with a report of the registered {metrics} and their values.

Clients can request a particular output format from the endpoint.

| Format                   | Requested by                      |
|--------------------------|-----------------------------------|
| OpenMetrics (Prometheus) | default (`text/plain`)            |
| JSON                     | Header `Accept: application/json` |

Formats for `{metrics-endpoint}` output

Clients can also limit the report by specifying the scope as a query parameter in the request URL:

- `{metrics-endpoint}?scope=base`

- `{metrics-endpoint}?scope=vendor`

- `{metrics-endpoint}?scope=application`

Further, clients can narrow down to a specific metric name by adding the name as another query parameter, such as `{metrics-endpoint}?scope=application&name=myCount`.

*Example Reporting: Prometheus format*

``` bash
curl -s -H 'Accept: text/plain' -X GET http://localhost:8080{metrics-endpoint}
```

``` text
# HELP classloader_loadedClasses_count Displays the number of classes that are currently loaded in the Java virtual machine.
# TYPE classloader_loadedClasses_count gauge
classloader_loadedClasses_count{{prom-output-scope-prefix}scope="base",} 5297.0
```

See the summary of the [OpenMetrics and Prometheus Format](#_openmetrics_and_prometheus_format) for more information.

*Example Reporting: JSON format*

``` bash
curl -s -H 'Accept: application/json' -X GET http://localhost:8080{metrics-endpoint}
```

*JSON response:*

``` json
{
   "base" : {
      "memory.maxHeap" : 3817865216,
      "memory.committedHeap" : 335544320
    }
}
```

In addition to your application {metrics}, the reports contain other {metrics} of interest such as system and VM information.

### OpenMetrics and Prometheus Format

The [OpenMetrics format]({openmetrics-format-doc-url}) and the [Prometheus exposition format]({prometheus-exposition-format-doc-url}) are very similar in most important respects but are not identical. This brief summary treats them as the same.

The OpenMetrics/Prometheus format represents each {metric} using three lines of output as summarized in the following table.

| Line prefix | Purpose | Format |
|----|----|----|
| `# TYPE` | Displays the scope, name, and type of the {metric} | `TYPE <scope>:<output-name> <{metric}-type>` |
| `# HELP` | Displays the scope, name, and description of the {metric} | `HELP <scope>:<output-name> <registered description>` |
| (none) | Displays the scope, {metric} ID, and current value of the {metric} | `<scope>:<output-name> <current value>` |

OpenMetrics/Prometheus format

The OpenMetrics/Prometheus output converts {metric} IDs in these ways:

- Names in camel case are converted to "snake case" and dots are converted to underscores.

- Names include any units specified for the {metric}.

- For percentiles, the ID includes a tag identifying which percentile the line of output describes.

As the earlier example output showed, for a {metric} with multiple values, such as a timer or a (with, among others, `max`, `mean`, and `count`), the OpenMetrics/Prometheus output reports a "metric family" which includes a separate family member {metric} for each of the multiple values. The name for each member in the family is derived from the registered name for the {metric} plus a suffix indicating which one of the {metric}'s multiple values the line refers to.

The following table summarizes the naming for each {metric} type.

<table>
<caption>OpenMetrics/Prometheus {metric_uc} Naming</caption>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">{metric_uc} Type</th>
<th style="text-align: left;">Example registered name</th>
<th style="text-align: left;">{metric_uc} family member</th>
<th style="text-align: left;">Name Suffix</th>
<th style="text-align: left;">Example displayed name</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>Counter</code></p></td>
<td style="text-align: left;"><p><code>requests.count</code></p></td>
<td style="text-align: left;"><p>count</p></td>
<td style="text-align: left;"><p><code>_total</code></p></td>
<td style="text-align: left;"><p><code>requests_count_total</code></p></td>
</tr>
<tr>
<td rowspan="4" style="text-align: left;"></td>
<td rowspan="4" style="text-align: left;"><p><code>nameLengths</code></p></td>
<td style="text-align: left;"><p>count</p></td>
<td style="text-align: left;"><p><code>_count</code></p></td>
<td style="text-align: left;"><p><code>nameLengths_count</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>sum</p></td>
<td style="text-align: left;"><p><code>_sum</code></p></td>
<td style="text-align: left;"><p><code>nameLengths_sum</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>max</p></td>
<td style="text-align: left;"><p><code>_max</code></p></td>
<td style="text-align: left;"><p><code>nameLengths_max</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>percentile</p></td>
<td style="text-align: left;"><p>none</p></td>
<td style="text-align: left;"><p><code>nameLengths{{prom-output-scope-prefix}scope="base",quantile="0.5",}</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>Gauge</code></p></td>
<td style="text-align: left;"><p><code>classloader.loadedClasses.count</code></p></td>
<td style="text-align: left;"><p>value</p></td>
<td style="text-align: left;"><p>none</p></td>
<td style="text-align: left;"><p><code>classloader_loadedClasses_count</code></p></td>
</tr>
<tr>
<td rowspan="4" style="text-align: left;"><p><code>Timer</code> <sup>1</sup></p></td>
<td rowspan="4" style="text-align: left;"><p><code>vthreads.recentPinned</code></p></td>
<td style="text-align: left;"><p>count</p></td>
<td style="text-align: left;"><p><code>_count</code></p></td>
<td style="text-align: left;"><p><code>vthreads_recentPinned_seconds_count</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>sum</p></td>
<td style="text-align: left;"><p><code>_sum</code></p></td>
<td style="text-align: left;"><p><code>vthreads_recentPinned_seconds_sum</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>max</p></td>
<td style="text-align: left;"><p><code>_max</code></p></td>
<td style="text-align: left;"><p><code>vthreads_recentPinned_seconds_max</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>percentile</p></td>
<td style="text-align: left;"><p>none</p></td>
<td style="text-align: left;"><p><code>vthreads_recentPinned_seconds{{prom-output-scope-prefix}scope="base",quantile="0.5",}</code></p></td>
</tr>
</tbody>
</table>

<sup>1</sup> The OpenMetrics/Prometheus output format reports a timer as a `summary` with units of `seconds`.

### JSON Format

Unlike OpenMetrics/Prometheus output, which combines the data and the metadata in a single response, you use an HTTP `GET` request to retrieve metrics JSON *data* and an `OPTIONS` request to retrieve *metadata* in JSON format.

Helidon groups {metrics} in the same scope together in JSON output as shown in the following example.

*JSON metrics output structured by scope (partial)*

``` json
{
  "application": {  
    "getTimer": {
      "type": "timer",
      "unit": "seconds",
      "description": "Timer for getting the default greeting"
    }
  },
  "vendor": {       
    "requests.count": {
      "type": "counter",
      "description": "Each request (regardless of HTTP method) will increase this counter"
    }
  },
  "base": {         
    "cpu.systemLoadAverage": {
      "type": "gauge",
      "description": "Displays the system load average for the last minute."
    },
    "classloader.loadedClasses.count": {
      "type": "gauge",
      "description": "Displays the number of classes that are currently loaded in the Java virtual machine."
    }
  }
}
```

- Note the `application`, `vendor`, and `base` sections.

If an HTTP request [selects by scope](#scope-specific-retrieval), the output omits the extra level of structure that identifies the scope as shown in the following example.

*JSON metrics output for the `base` scope (partial)*

``` json
{
  "cpu.systemLoadAverage": {
    "type": "gauge",
     "description": "Displays the system load average for the last minute."
  },
  "classloader.loadedClasses.count": {
    "type": "gauge",
    "description": "Displays the number of classes that are currently loaded in the Java virtual machine."
  }
}
```

#### Understanding the JSON Metrics Data Format

The Helidon JSON format expresses each {metric} as either a single value (for example, a counter) or a structure with multiple values (for example, a timer).

*JSON output for a single-valued {metric} (for example, `Counter`)*

``` json
"requests.count": 5
```

*JSON output for a multi-valued {metric} (for example, `Timer`)*

``` json
"getTimer": {
  "count": 3,
  "max": 0.0030455,
  "mean": 0.0011060836666666666,
  "elapsedTime": 0.003318251,
  "p0.5": 0.000151552,
  "p0.75": 0.003141632,
  "p0.95": 0.003141632,
  "p0.98": 0.003141632,
  "p0.99": 0.003141632,
  "p0.999": 0.003141632
}
```

By default, Helidon formats time values contained in JSON output as seconds. You can change this behavior [as described below](#controlling_timer_output).

#### Understanding the JSON Metrics Metadata Format

Access the metrics endpoint with an HTTP `OPTIONS` request and the `Accept: application/json` header to retrieve metadata in JSON format.

*Example `Counter` metadata*

``` json
"requests.count": {
  "type": "counter",
  "description": "Each request (regardless of HTTP method) will increase this counter"
    }
```

*Example `Timer` metadata*

``` json
"getTimer": {
  "type": "timer",
  "unit": "seconds",
  "description": "Timer for getting the default greeting"
}
```

Generally, the output for a given {metric} reflects only the metadata that the application or Helidon code explicitly set on that {metric}.

One exception is that metadata for a timer always includes the `unit` field. By default, Helidon formats timer data in JSON output as seconds, regardless of any explicit `baseUnit` setting applied to the timers. But as [described below](#controlling_timer_output) you can change this behavior which can lead to different timers being formatted using different units. Checking the metadata is the only way to know for sure what units Helidon used to express a given timer, so Helidon always includes `unit` in timer metadata.

#### Controlling JSON Timer Output

By default, Helidon expresses timer data as seconds.

You can change this using configuration: \<1\> For *units* specify any valid name for a [`TimeUnit`]({jdk-javadoc-url}/java.base/java/util/concurrent/TimeUnit.md) value (`SECONDS`, `MILLISECONDS`, etc.)

If you have configured `json-units-default`, Helidon formats each timer’s data as follows:

1.  If code set `baseUnit` on the timer, Helidon uses those units for that timer.

2.  Otherwise, Helidon uses the default units you configured.

To enable the JSON output behavior from Helidon 3, specify `json-units-default` as `NANOSECONDS`.

## The `MetricRegistry` API

To register or look up {metrics} programmatically, your service code uses the [`MetricRegistry`]({microprofile-metrics-javadoc-url}/org/eclipse/microprofile/metrics/MetricRegistry.md) instance for the scope of interest: `base`, `vendor`, `application`, or a custom scope.

Once it has a reference to a `MetricRegistry` your code can use the reference to register new metrics, look up previously-registered metrics, and remove metrics.

Helidon {flavor-uc} includes several pre-written example applications illustrating aspects of metrics:

- [Enabling/disabling {metrics}]({helidon-github-examples-url}/metrics/filtering/se) using

[OpenMetrics format]({openmetrics-format-doc-url})

[Prometheus exposition format]({prometheus-exposition-format-doc-url})
