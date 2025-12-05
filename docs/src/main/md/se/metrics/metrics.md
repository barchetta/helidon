# Overview

Helidon SE metrics is a neutral metrics API which provides

- a unified way for Helidon servers to export monitoring
  data—​telemetry—​to management agents, and

- a unified Java API which all application programmers can use to
  register and update meters to expose telemetry data from their
  services.

Metrics is one of the Helidon observability features.

> [!NOTE]
> Beginning with Helidon 4.1, strongly consider assigning the config
> setting
>
> ``` properties
> metrics.gc-time-type = gauge
> ```
>
> See the [longer discussion below](#controlling-gc-time) in the
> Configuration section.

## A Word about Terminology

Helidon SE uses the term "metrics" to refer to the subsystem in Helidon
which manages the registration of, updates to, and reporting of
aggregate statistical measurements about the service. The term "meter"
refers to an entity which collects these measurements, such as a counter
or a timer.

# Maven Coordinates

To enable metrics, add the following dependency to your project’s
`pom.xml` (see [Managing
Dependencies](../../about/managing-dependencies.md)).

<div class="formalpara">

<div class="title">

Packaging the metrics API

</div>

``` xml
<dependency>
    <groupId>io.helidon.metrics</groupId>
    <artifactId>helidon-metrics-api</artifactId>
</dependency>
```

</div>

This dependency adds the metrics API and a no-op implementation of that
API to your project. The no-op implementation:

- does not register meters in a registry

- does not update meter values

- does not expose the metrics endpoint for reporting meter values.

To include the full-featured metrics implementation, add the following
dependency to your project:

<div class="formalpara">

<div class="title">

Packaging a full-featured metrics implementation

</div>

``` xml
<dependency>
    <groupId>io.helidon.webserver.observe</groupId>
    <artifactId>helidon-webserver-observe-metrics</artifactId>
</dependency>
```

</div>

Adding this dependency packages the full-featured metrics implementation
and support for the metrics endpoint with your service.

You might notice the transitive dependency
`io.helidon.metrics.providers:helidon-metrics-providers-micrometer` in
your project. This component contains an implementation of the Helidon
metrics API that uses Micrometer as the underlying metrics technology.

Helidon provides several built-in meters in a separate artifact. To
include the build-in meters, add the following dependency to your
project:

<div class="formalpara">

<div class="title">

Packaging the built-in meters

</div>

``` xml
<dependency>
    <groupId>io.helidon.metrics</groupId>
    <artifactId>helidon-metrics-system-meters</artifactId>
    <scope>runtime</scope>
</dependency>
```

</div>

# Usage

## Instrumenting Your Service

You add meters to your service by writing code which explicitly invokes
the metrics API to register meters, retrieve previously-registered
meters, and update meter values.

Later sections of this document describe how to do this.

## Meter Types

Helidon supports meters inspired by [Micrometer](https://micrometer.io)
and summarized in the following table:

|  |  |  |
|----|----|----|
| Meter Type | Description | Micrometer reference |
| [`Counter`](/apidocs/io.helidon.metrics.api/io/helidon/metrics/api/Counter.html) | Monotonically-increasing `long` value. | [Counters](https://docs.micrometer.io/micrometer/reference/concepts/counters.html) |
| [`DistributionSummary`](/apidocs/io.helidon.metrics.api/io/helidon/metrics/api/DistributionSummary.html) | Summary of samples each with a `long` value. Reports aggregate information over all samples (count, total, mean, max) as well as the distribution of sample values using percentiles and bucket counts. | [Distribution summaries](https://docs.micrometer.io/micrometer/reference/concepts/distribution-summaries.html) |
| [`Timer`](/apidocs/io.helidon.metrics.api/io/helidon/metrics/api/Timer.html) | Accumulation of short-duration (typically under a minute) intervals. Typically updated using a Java [`Duration`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/time/Duration.html) or by recording the time taken by a method invocation or lambda. Reports the count, total time, max, and mean; provides a distribution summary of the samples. | [Timers](https://docs.micrometer.io/micrometer/reference/concepts/timers.html) |
| [`Gauge<? extends Number>`](/apidocs/io.helidon.metrics.api/io/helidon/metrics/api/Gauge.html) | View of a value that is assignment-compatible with a subtype of Java [`Number`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java.lang.Number.html). The underlying value is updated by code elsewhere in the system, not by invoking methods on the gauge itself. | [Gauges](https://docs.micrometer.io/micrometer/reference/concepts/gauges.html) |

Types of Meters

## Categorizing Types of Meters

Helidon distinguishes among *scopes*, or categories, of meters.

Helidon includes meters in the built-in scopes described below.
Applications often register their own meters in the `application` scope
but can create their own scopes and register meters within them.

| Built-in Scope | Typical Usage |
|----|----|
| `base` | OS or Java runtime measurements (available heap, disk space, etc.). |
| `vendor` | Implemented by vendors, including the `REST.request` metrics and other key performance indicator measurements (described in later sections). |
| `application` | Declared via annotations or programmatically registered by your service code. |

Built-in meter scopes

When an application creates a new meter it can specify which scope the
meter belongs to. If the application does not specify a scope for a new
meter, the default scope is `application`.

## Meter Registry

Helidon stores all meters in a *meter registry*. Typically, applications
use the global meter registry which is the registry where Helidon stores
built-in meters. Application code refers to the global registry using
`Metrics.globalRegistry()`.

## Retrieving Metrics Reports from your Service

When you add the `helidon-webserver-observe-metrics` dependency to your
project, Helidon automatically provides a built-in REST endpoint
`/observe/metrics` which responds with a report of the registered meters
and their values.

Clients can request a particular output format.

| Format                   | Requested by                      |
|--------------------------|-----------------------------------|
| OpenMetrics (Prometheus) | default (`text/plain`)            |
| JSON                     | Header `Accept: application/json` |

Formats for `/observe/metrics` output

Clients can also limit the report by specifying the scope as a query
parameter in the request URL:

- `/observe/metrics?scope=base`

- `/observe/metrics?scope=vendor`

- `/observe/metrics?scope=application`

Further, clients can narrow down to a specific metric name by adding the
name as another query parameter, such as
`/observe/metrics?scope=application&name=myCount`.

<div class="formalpara">

<div class="title">

Example Reporting: Prometheus format

</div>

``` bash
curl -s -H 'Accept: text/plain' -X GET http://localhost:8080/observe/metrics
```

</div>

``` text
# HELP classloader_loadedClasses_count Displays the number of classes that are currently loaded in the Java virtual machine.
# TYPE classloader_loadedClasses_count gauge
classloader_loadedClasses_count{scope="base",} 5297.0
```

See the summary of the [OpenMetrics and Prometheus
Format](#_openmetrics_and_prometheus_format) for more information.

<div class="formalpara">

<div class="title">

Example Reporting: JSON format

</div>

``` bash
curl -s -H 'Accept: application/json' -X GET http://localhost:8080/observe/metrics
```

</div>

<div class="formalpara">

<div class="title">

JSON response:

</div>

``` json
{
   "base" : {
      "memory.maxHeap" : 3817865216,
      "memory.committedHeap" : 335544320
    }
}
```

</div>

In addition to your application meters, the reports contain other meters
of interest such as system and VM information.

### OpenMetrics and Prometheus Format

The [OpenMetrics
format](https://github.com/prometheus/OpenMetrics/blob/main/specification/OpenMetrics.md)
and the [Prometheus exposition
format](https://github.com/prometheus/docs/blob/main/content/docs/instrumenting/exposition_formats.md)
are very similar in most important respects but are not identical. This
brief summary treats them as the same.

The OpenMetrics/Prometheus format represents each meter using three
lines of output as summarized in the following table.

| Line prefix | Purpose | Format |
|----|----|----|
| `# TYPE` | Displays the scope, name, and type of the meter | `TYPE <scope>:<output-name> <meter-type>` |
| `# HELP` | Displays the scope, name, and description of the meter | `HELP <scope>:<output-name> <registered description>` |
| (none) | Displays the scope, meter ID, and current value of the meter | `<scope>:<output-name> <current value>` |

OpenMetrics/Prometheus format

The OpenMetrics/Prometheus output converts meter IDs in these ways:

- Names in camel case are converted to "snake case" and dots are
  converted to underscores.

- Names include any units specified for the meter.

- For percentiles, the ID includes a tag identifying which percentile
  the line of output describes.

As the earlier example output showed, for a meter with multiple values,
such as a timer or a distribution summary, (with, among others, `max`,
`mean`, and `count`), the OpenMetrics/Prometheus output reports a
"metric family" which includes a separate family member meter for each
of the multiple values. The name for each member in the family is
derived from the registered name for the meter plus a suffix indicating
which one of the meter’s multiple values the line refers to.

The following table summarizes the naming for each meter type.

<table>
<caption>OpenMetrics/Prometheus Meter Naming</caption>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Meter Type</th>
<th style="text-align: left;">Example registered name</th>
<th style="text-align: left;">Meter family member</th>
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
<td
style="text-align: left;"><p><code>requests_count_total</code></p></td>
</tr>
<tr>
<td rowspan="4"
style="text-align: left;"><p><code>DistributionSummary</code></p></td>
<td rowspan="4"
style="text-align: left;"><p><code>nameLengths</code></p></td>
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
<td
style="text-align: left;"><p><code>nameLengths{scope="base",quantile="0.5",}</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>Gauge</code></p></td>
<td
style="text-align: left;"><p><code>classloader.loadedClasses.count</code></p></td>
<td style="text-align: left;"><p>value</p></td>
<td style="text-align: left;"><p>none</p></td>
<td
style="text-align: left;"><p><code>classloader_loadedClasses_count</code></p></td>
</tr>
<tr>
<td rowspan="4" style="text-align: left;"><p><code>Timer</code>
<sup>1</sup></p></td>
<td rowspan="4"
style="text-align: left;"><p><code>vthreads.recentPinned</code></p></td>
<td style="text-align: left;"><p>count</p></td>
<td style="text-align: left;"><p><code>_count</code></p></td>
<td
style="text-align: left;"><p><code>vthreads_recentPinned_seconds_count</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>sum</p></td>
<td style="text-align: left;"><p><code>_sum</code></p></td>
<td
style="text-align: left;"><p><code>vthreads_recentPinned_seconds_sum</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>max</p></td>
<td style="text-align: left;"><p><code>_max</code></p></td>
<td
style="text-align: left;"><p><code>vthreads_recentPinned_seconds_max</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>percentile</p></td>
<td style="text-align: left;"><p>none</p></td>
<td
style="text-align: left;"><p><code>vthreads_recentPinned_seconds{scope="base",quantile="0.5",}</code></p></td>
</tr>
</tbody>
</table>

<sup>1</sup> The OpenMetrics/Prometheus output format reports a timer as
a `summary` with units of `seconds`.

### JSON Format

Unlike OpenMetrics/Prometheus output, which combines the data and the
metadata in a single response, you use an HTTP `GET` request to retrieve
metrics JSON *data* and an `OPTIONS` request to retrieve *metadata* in
JSON format.

Helidon groups meters in the same scope together in JSON output as shown
in the following example.

<div class="formalpara">

<div class="title">

JSON metrics output structured by scope (partial)

</div>

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

</div>

- Note the `application`, `vendor`, and `base` sections.

If an HTTP request [selects by scope](#scope-specific-retrieval), the
output omits the extra level of structure that identifies the scope as
shown in the following example.

<div class="formalpara">

<div class="title">

JSON metrics output for the `base` scope (partial)

</div>

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

</div>

#### Understanding the JSON Metrics Data Format

The Helidon JSON format expresses each meter as either a single value
(for example, a counter) or a structure with multiple values (for
example, a timer).

<div class="formalpara">

<div class="title">

JSON output for a single-valued meter (for example, `Counter`)

</div>

``` json
"requests.count": 5
```

</div>

<div class="formalpara">

<div class="title">

JSON output for a multi-valued meter (for example, `Timer`)

</div>

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

</div>

By default, Helidon formats time values contained in JSON output as
seconds. You can change this behavior [as described
below](#controlling_timer_output).

#### Understanding the JSON Metrics Metadata Format

Access the metrics endpoint with an HTTP `OPTIONS` request and the
`Accept: application/json` header to retrieve metadata in JSON format.

<div class="formalpara">

<div class="title">

Example `Counter` metadata

</div>

``` json
"requests.count": {
  "type": "counter",
  "description": "Each request (regardless of HTTP method) will increase this counter"
    }
```

</div>

<div class="formalpara">

<div class="title">

Example `Timer` metadata

</div>

``` json
"getTimer": {
  "type": "timer",
  "unit": "seconds",
  "description": "Timer for getting the default greeting"
}
```

</div>

Generally, the output for a given meter reflects only the metadata that
the application or Helidon code explicitly set on that meter.

One exception is that metadata for a timer always includes the `unit`
field. By default, Helidon formats timer data in JSON output as seconds,
regardless of any explicit `baseUnit` setting applied to the timers. But
as [described below](#controlling_timer_output) you can change this
behavior which can lead to different timers being formatted using
different units. Checking the metadata is the only way to know for sure
what units Helidon used to express a given timer, so Helidon always
includes `unit` in timer metadata.

#### Controlling JSON Timer Output

By default, Helidon expresses timer data as seconds.

You can change this using configuration:

<div class="formalpara">

<div class="title">

Setting default timer units for JSON in `application.yaml`

</div>

``` yaml
metrics:
  timers:
    json-units-default: units 
```

</div>

- For *units* specify any valid name for a
  [`TimeUnit`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/concurrent/TimeUnit.html)
  value (`SECONDS`, `MILLISECONDS`, etc.)

If you have configured `json-units-default`, Helidon formats each
timer’s data as follows:

1.  If code set `baseUnit` on the timer, Helidon uses those units for
    that timer.

2.  Otherwise, Helidon uses the default units you configured.

To enable the JSON output behavior from Helidon 3, specify
`json-units-default` as `NANOSECONDS`.

## Enabling the Metrics REST Service

If you add the dependencies described above, your service automatically
supports the metrics REST endpoint as long as the `WebServer` is
configured to discover features automatically.

If you disable auto-discovery, you can add the metrics observer
explicitly.

1.  Create an instance of `MetricsObserver`, either directly as shown
    below or using its builder.

2.  Include the `MetricsObserver` instance in your application’s
    `ObserveFeature`.

3.  Register your `ObserveFeature` with your `WebServer`.

``` java
ObserveFeature observe = ObserveFeature.builder()
        .config(config.get("server.features.observe"))
        .addObserver(MetricsObserver.create())
        .build();

WebServer server = WebServer.builder()
        .config(Config.global().get("server"))
        .featuresDiscoverServices(false)
        .addFeature(observe)
        .routing(Main::routing)
        .build()
        .start();
```

# API

To work with Helidon Metrics in your code, follow these steps:

1.  Use the static `globalRegistry` method on the
    [`Metrics`](/apidocs/io.helidon.metrics.api/io/helidon/metrics/api/Metrics.html)
    interface to get a reference to the global
    [`MeterRegistry`](/apidocs/io.helidon.metrics.api/io/helidon/metrics/api/MeterRegistry.html)
    instance.

2.  Use the `MeterRegistry` instance to register new meters and look up
    previously-registered meters.

3.  Use the meter reference returned from the `MeterRegistry` to update
    the meter or get its value.

You can also use the `MeterRegistry` to remove an existing meter.

## Helidon Metrics API

The Helidon Metrics API defines the classes and interfaces for meter
types and other related items.

The following table summarizes the meter types.

| Meter Type | Usage |
|----|----|
| [`Counter`](/apidocs/io.helidon.metrics.api/io/helidon/metrics/api/Counter.html) | Monotonically increasing count of events. |
| [`Gauge`](/apidocs/io.helidon.metrics.api/io/helidon/metrics/api/Gauge.html) | Access to a value managed by other code in the service. |
| [`DistributionSummary`](/apidocs/io.helidon.metrics.api/io/helidon/metrics/api/DistributionSummary.html) | Calculates the distribution of a value. |
| [`Timer`](/apidocs/io.helidon.metrics.api/io/helidon/metrics/api/Timer.html) | Frequency of invocations and the distribution of how long the invocations take. |

Meter Types

Each meter type has its own set of methods for updating and retrieving
the value.

## The `MeterRegistry` API

To register or look up meters programmatically, your service code uses
the global `MeterRegistry`. Simply invoke `Metrics.globalRegistry()` to
get a reference to the global meter registry.

To locate an existing meter or register a new one, your code:

1.  Creates a builder of the appropriate type of meter, setting the name
    and possibly other characteristics of the meter.

2.  Invokes the `MeterRegistry.getOrCreate` method, passing the builder.

The meter registry returns a reference to a previously-registered meter
with the specified name and tags or, if none exists, a newly-registered
meter. Your code can then operate on the returned meter as needed to
record new measurements or retrieve existing data.

The example code in the [Examples](#_examples) section below illustrates
how to register, retrieve, and update meters.

## Accessing the Underlying Implementation: `unwrap`

The neutral Helidon metrics API is an abstraction of common metrics
behavior independent from any given implementation. As such, we
intentionally excluded some implementation-specific behavior from the
API.

Sometimes you might want access to methods that are present in a
particular metrics implementation but not in the Helidon API. Helidon
allows that via the `unwrap` method on the meter types and on their
builders. Each full implementation of the Helidon meter types and their
builders refers to a delegate meter or delegate builder internally. The
`unwrap` method lets you obtain the delegate, cast to the type you want.

Of course, using this technique binds your code to a particular metrics
implementation.

The
[`Wrapper`](/apidocs/io.helidon.metrics.api/io/helidon/metrics/api/Wrapper.html)
interface declares the `unwrap` method which accepts a class parameter
to which the delegate is cast. You can then invoke any method declared
on the implementation-specific type.

# Configuration

To control how the Helidon metrics subsystem behaves, add a `metrics`
section to your configuration file, such as `application.yaml`.

Certain default configuration values depend on the fact that you are
using Helidon SE as described in the [second table
below](#flavor-specific-defaults).

Type:
[io.helidon.webserver.observe.metrics.MetricsObserver](/apidocs/io.helidon.webserver.observe.metrics/io/helidon/webserver/observe/metrics/MetricsObserver.html)

This is a standalone configuration type, prefix from configuration root:
`metrics`

This type provides the following service implementations:

- `io.helidon.webserver.observe.spi.ObserveProvider`

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
<td style="text-align: left;"><p><code>app-name</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Value for the application tag to be
added to each meter ID.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>app-tag-name</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Name for the application tag to be
added to each meter ID.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>built-in-meter-name-format</code></p></td>
<td style="text-align: left;"><p>BuiltInMeterNameFormat (SNAKE,
CAMEL)</p></td>
<td
style="text-align: left;"><p><code>BuiltInMeterNameFormat.CAMEL</code></p></td>
<td style="text-align: left;"><p>Output format for built-in meter
names.</p>
<pre><code>BuiltInMeterNameFormat.SNAKE selects &quot;snake_case&quot; which does not conform to the MicroProfile
Metrics specification.</code></pre>
<p>Allowed values:</p>
<ul>
<li><p><code>SNAKE</code>: Snake-case.</p></li>
<li><p><code>CAMEL</code>: Camel-case (which is compatible with the
MicroProfile Metrics spec).</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>enabled</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Whether metrics functionality is
enabled.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>endpoint</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p><code>metrics</code></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><span
class="line-through"><code>gc-time-type</code></span></p></td>
<td style="text-align: left;"><p>GcTimeType (GAUGE, COUNTER)</p></td>
<td
style="text-align: left;"><p><code>GcTimeType.COUNTER</code></p></td>
<td style="text-align: left;"><p><strong>Deprecated</strong> Whether the
<code>gc.time</code> meter should be registered as a gauge (vs. a
counter). The <code>gc.time</code> meter is inspired by the MicroProfile
Metrics spec, in which the meter was originally checked to be a counter
but starting in 5.1 was checked be a gauge. For the duration of Helidon
4.x users can choose which type of meter Helidon registers for
<code>gc.time</code>. @deprecated Provided for backward compatibility
only; no replacement</p>
<p>Allowed values:</p>
<ul>
<li><p><code>GAUGE</code>: Implement the meter as a gauge. This is
backward-incompatible with Helidon 4.0.x releases but complies with
MicroProfile 5.1.</p></li>
<li><p><code>COUNTER</code>: Implement the meter as a counter. This is
backward-compatible with Helidon 4.0.x releases but does not comply with
MicroProfile 5.1.</p></li>
</ul></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>key-performance-indicators</code></p></td>
<td style="text-align: left;"><p><a
href="../../config/io_helidon_metrics_api_KeyPerformanceIndicatorMetricsConfig.xml">KeyPerformanceIndicatorMetricsConfig</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Key performance indicator metrics
settings.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>permit-all</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Whether to allow anybody to access the
endpoint.</p>
<p>See roles()</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><span
class="line-through"><code>rest-request-enabled</code></span></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p><strong>Deprecated</strong> Whether
automatic REST request metrics should be measured (as indicated by the
deprecated config key <code>rest-request-enabled</code>, the config key
using a hyphen instead of a dot separator).</p>
<p>@deprecated Use <code>rest-request.enabled</code> instead.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>rest-request.enabled</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>false</code></p></td>
<td style="text-align: left;"><p>Whether automatic REST request metrics
should be measured.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>roles</code></p></td>
<td style="text-align: left;"><p>string[]</p></td>
<td style="text-align: left;"><p><code>observe</code></p></td>
<td style="text-align: left;"><p>Hints for role names the user is
expected to be in.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scoping</code></p></td>
<td style="text-align: left;"><p><a
href="../../config/io_helidon_metrics_api_ScopingConfig.xml">ScopingConfig</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Settings related to scoping
management.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>tags</code></p></td>
<td style="text-align: left;"><p><a
href="../../config/io_helidon_metrics_api_Tag.xml">Tag[]</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Global tags.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>timers.json-units-default</code></p></td>
<td style="text-align: left;"><p>TimeUnit (NANOSECONDS, MICROSECONDS,
MILLISECONDS, SECONDS, MINUTES, HOURS, DAYS)</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Default units for timer output in JSON
if not specified on a given timer.</p>
<p>If the configuration key is absent, the Helidon JSON output uses
java.util.concurrent.TimeUnit.SECONDS. If the configuration key is
present, Helidon formats each timer using that timer’s specific units
(if set) and the config value otherwise.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>virtual-threads.enabled</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>false</code></p></td>
<td style="text-align: left;"><p>Whether Helidon should expose meters
related to virtual threads.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>virtual-threads.pinned.threshold</code></p></td>
<td style="text-align: left;"><p>Duration</p></td>
<td style="text-align: left;"><p><code>PT0.020S</code></p></td>
<td style="text-align: left;"><p>Threshold for sampling pinned virtual
threads to include in the pinned threads meter.</p></td>
</tr>
</tbody>
</table>

| Key                | Default Value |
|--------------------|---------------|
| `app-tag-name`     | `app`         |
| `scoping.tag-name` | `scope`       |
| `scoping.default`  | `application` |

Default Values Specific to Helidon SE

## Controlling the Meter Type for `gc.time`

To date Helidon 4 releases have implemented the system-provided meter
`gc.time` as a counter. In fact, a gauge is more suitable for the
approximate time the JVM has spent doing garbage collection.

Helidon 4.4.0-SNAPSHOT continues to use a counter by default to preserve
backward compatibility, but you can choose to use a gauge by setting the
configuration property `metrics.gc-time-type` to `gauge`. You can also
set the config property to `counter` which is the default.

Why should you care? In fact, this distinction might not make a
difference for many users. But for others the differences between the
programmatic APIs for `Counter` and `Gauge` would affect application
code that works directly with the `gc-time` meter. Further, the
difference in output—​particularly in the OpenMetrics/Prometheus
format—​might affect their application or downstream monitoring tools.

The ability to choose the meter type for `gc.time` is deprecated and is
planned for removal in a future major release of Helidon at which time
Helidon will always use a gauge.

# Examples

Helidon SE includes several pre-written example applications
illustrating aspects of metrics:

- [Enabling/disabling
  meters](https://github.com/helidon-io/helidon-examples/tree/helidon-4.x/examples/metrics/filtering/se)
  using `MetricsObserver` and `MetricsConfig`

- [Controlling key performance indicator
  metrics](https://github.com/helidon-io/helidon-examples/tree/helidon-4.x/examples/metrics/kpi)
  using configuration and `KeyPerformanceIndicatorMetricsSettings`.

The rest of this section shows how to add a custom meter to your code
and how to configure the Helidon metrics subsystem.

## Example Application Code

The following example, based on the Helidon SE QuickStart application,
shows how to register and update a new `Counter` in application code.
The counter tracks the number of times any of the service endpoints is
accessed.

<div class="formalpara">

<div class="title">

Define and use a `Counter`

</div>

``` java
public class GreetService implements HttpService {

    private final Counter accessCtr = Metrics.globalRegistry() 
            .getOrCreate(Counter.builder("accessctr")); 

    @Override
    public void routing(HttpRules rules) {
        rules
                .any(this::countAccess) 
                .get("/", this::getDefaultMessageHandler)
                .get("/{name}", this::getMessageHandler)
                .put("/greeting", this::updateGreetingHandler);

    }

    void countAccess(ServerRequest request,
                     ServerResponse response) {

        accessCtr.increment(); 
        response.next();
    }

    void getDefaultMessageHandler(ServerRequest request,
                                  ServerResponse response) {
        // ...
    }

    void getMessageHandler(ServerRequest request,
                           ServerResponse response) {
        // ...
    }

    void updateGreetingHandler(ServerRequest request,
                               ServerResponse response) {
        // ...
    }
}
```

</div>

- Get the global meter registry.

- Create (or find) a counter named "accessctr" in the global registry.

- Route every request to the `countAccess` method.

- Increment the access counter for every request.

Perform the following steps to see the new counter in action.

<div class="formalpara">

<div class="title">

Build and run the application

</div>

``` bash
mvn package
java -jar target/helidon-quickstart-se.jar
```

</div>

<div class="formalpara">

<div class="title">

Retrieve `application` metrics

</div>

``` bash
curl 'http://localhost:8080/observe/metrics?scope=application' 
```

</div>

<div class="formalpara">

<div class="title">

Response

</div>

``` text
# HELP accessctr_total
# TYPE accessctr_total counter
accessctr_total{scope="application",} 0.0 
```

</div>

- Access the metrics endpoint, selecting only application meters.

- Note the counter is zero; we have not accessed a service endpoint yet.

<div class="formalpara">

<div class="title">

Access a service endpoint to retrieve a greeting

</div>

``` bash
curl http://localhost:8080/greet
```

</div>

<div class="formalpara">

<div class="title">

JSON response:

</div>

``` json
{"message":"Hello World"}
```

</div>

<div class="formalpara">

<div class="title">

Retrieve `application` metrics again

</div>

``` bash
curl 'http://localhost:8080/observe/metrics?scope=application'
```

</div>

<div class="formalpara">

<div class="title">

Response

</div>

``` text
# HELP accessctr_total
# TYPE accessctr_total counter
accessctr_total{scope="application",} 1.0 
```

</div>

- The counter now reports 1, reflecting our earlier access to the
  `/greet` endpoint.

## Example Configuration

Metrics configuration is quite extensive and powerful and, therefore, a
bit complicated. The rest of this section illustrates some of the most
common scenarios:

- [Disable metrics entirely.](#config-disable)

- [Choose whether to report virtual threads
  meters](#config-virtual-threads).

- [Choose whether to collect extended key performance indicator
  metrics.](#config-kpi)

### Disable Metrics Subsystem

<div class="formalpara">

<div class="title">

Disabling metrics entirely

</div>

``` yaml
server:
  features:
    observe:
      observers:
        metrics:
          enabled: false
```

</div>

Helidon does not update metrics, and the `/observe/metrics` endpoints
respond with `404`.

### Configuring Virtual Threads Meters

#### Enabling Virtual Threads Meters

Gathering data to compute the meters for virtual threads is designed to
be as efficient as possible, but doing so still imposes a load on the
server and by default Helidon does not report meters related to virtual
threads.

To enable the meters describing virtual threads include a config setting
as shown in the following example.

<div class="formalpara">

<div class="title">

Enabling virtual thread meters

</div>

``` yaml
metrics:
  virtual-threads:
    enabled: true
```

</div>

#### Controlling Measurements of Pinned Virtual Threads

Helidon measures pinned virtual threads only when the thread is pinned
for a length of time at or above a threshold. Control the threshold as
shown in the example below.

<div class="formalpara">

<div class="title">

Setting virtual thread pinning threshold to 100 ms

</div>

``` yaml
metrics:
  virtual-threads:
    pinned:
      threshold: PT0.100S
```

</div>

The threshold value is a `Duration` string, such as `PT0.100S` for 100
milliseconds.

### Collecting Basic and Extended Key Performance Indicator (KPI) Meters

Any time you include the Helidon metrics module in your application,
Helidon tracks a basic performance indicator meter: a `Counter` of all
requests received (`requests.count`)

Helidon SE also includes additional, extended KPI meters which are
disabled by default:

- current number of requests in-flight - a `Gauge` (`requests.inFlight`)
  of requests currently being processed

- long-running requests - a `Counter` (`requests.longRunning`) measuring
  the total number of requests which take at least a given amount of
  time to complete; configurable, defaults to 10000 milliseconds (10
  seconds)

- load - a `Counter` (`requests.load`) measuring the number of requests
  worked on (as opposed to received)

- deferred - a `Gauge` (`requests.deferred`) measuring delayed request
  processing (work on a request was delayed after Helidon received the
  request)

You can enable and control these meters using configuration:

<div class="formalpara">

<div class="title">

Controlling extended KPI meters

</div>

``` yaml
server:
  features:
    observe:
      observers:
        metrics:
          key-performance-indicators:
            extended: true
            long-running:
              threshold-ms: 2000
```

</div>

# Additional Information

## References

[Micrometer Metrics concepts
documentation](https://docs.micrometer.io/micrometer/reference/concepts)

[OpenMetrics
format](https://github.com/prometheus/OpenMetrics/blob/main/specification/OpenMetrics.md)

[Prometheus exposition
format](https://github.com/prometheus/docs/blob/main/content/docs/instrumenting/exposition_formats.md)

## Support for the Prometheus Metrics API

- [Maven Coordinates](#maven-coordinates)

- [Usage](#_usage)

- [API](#_api)

Helidon provides optional support for the Prometheus metrics API.

To use it, your service registers Prometheus support with your routing
set-up. You can customize its configuration. For information about using
Prometheus, see the Prometheus documentation:
<https://prometheus.io/docs/introduction/overview/>.

> [!NOTE]
> Helidon’s fully-functional, built-in metrics implementation supports
> Prometheus (OpenMetrics) output. Use the optional support described in
> *this* section only if you want to use the Prometheus *API* from your
> application code.

### Maven Coordinates

<div class="formalpara">

<div class="title">

Dependency for Helidon Prometheus API support

</div>

``` xml
<dependency>
    <groupId>io.helidon.metrics</groupId>
    <artifactId>helidon-metrics-prometheus</artifactId>
</dependency>
```

</div>

### Usage

Your application code uses the Prometheus API to manage metrics. To
expose those metrics to clients via a REST endpoint, your code uses the
`PrometheusSupport` interface which Helidon provides.

### API

Your code creates a
[`PrometheusSupport`](/apidocs/io.helidon.metrics.prometheus/io/helidon/metrics/prometheus/PrometheusSupport.html)
object either using a static factory method (shown in the following
example) or by using its
[`Builder`](/apidocs/io.helidon.metrics.prometheus/io/helidon/metrics/prometheus/PrometheusSupport.Builder.html).

``` java
routing
        .addFeature(PrometheusSupport.create())
        .register("/myapp", new MyService());
```

This example uses the default Prometheus `CollectorRegistry`. By
default, the `PrometheusSupport` and exposes its REST endpoint at the
path `/metrics`. Use the builder obtained by
`PrometheusSupport.builder()` to configure a different
`CollectorRegistry` or a different path.
