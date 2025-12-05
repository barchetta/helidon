- a unified way for servers to export monitoring data—​telemetry—​to
  management agents, and

- a unified Java API which all application programmers can use to
  register and update {metrics} to expose telemetry data from their
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

# Instrumenting Your Service

You add {metrics} to your service

Later sections of this document describe how to do

# {metric_uc} Types

Helidon supports meters and summarized in the following table:

| {metric_uc} Type | Description |  |
|----|----|----|
|  | Monotonically-increasing `long` value. |  |
|  | Summary of samples each with a `long` value. Reports aggregate information over all samples (count, total, mean, max) as well as the distribution of sample values using percentiles and bucket counts. |  |
|  | Accumulation of short-duration (typically under a minute) intervals. Typically updated using a Java [`Duration`]({jdk-javadoc-url}/java.base/java/time/Duration.html) or by recording the time taken by a method invocation or lambda. Reports the count, total time, max, and mean; provides a of the samples. |  |
|  | View of a value that is assignment-compatible with a subtype of Java [`Number`]({jdk-javadoc-url}/java.base/java.lang.Number.html). The underlying value is updated by code elsewhere in the system, not by invoking methods on the gauge itself. |  |

Types of {metrics_uc}

# Categorizing Types of {Metrics_uc}

Helidon distinguishes among *scopes*, or categories, of

Helidon includes {metrics} in the built-in scopes described below.
Applications often register their own {metrics} in the `application`
scope but can create their own scopes and register {metrics} within
them.

| Built-in Scope | Typical Usage |
|----|----|
| `base` | OS or Java runtime measurements (available heap, disk space, etc.). |
| `vendor` | Implemented by vendors, including the `REST.request` metrics and other key performance indicator measurements (described in later sections). |
| `application` | Declared via annotations or programmatically registered by your service code. |

Built-in {metric} scopes

# Retrieving Metrics Reports from your Service

When you add the to your project, Helidon automatically provides a
built-in REST endpoint `{metrics-endpoint}` which responds with a report
of the registered {metrics} and their values.

Clients can request a particular output format.

| Format                   | Requested by                      |
|--------------------------|-----------------------------------|
| OpenMetrics (Prometheus) | default (`text/plain`)            |
| JSON                     | Header `Accept: application/json` |

Formats for `{metrics-endpoint}` output

Clients can also limit the report by specifying the scope as a query
parameter in the request URL:

- `{metrics-endpoint}?scope=base`

- `{metrics-endpoint}?scope=vendor`

- `{metrics-endpoint}?scope=application`

Further, clients can narrow down to a specific metric name by adding the
name as another query parameter, such as
`{metrics-endpoint}?scope=application&name=myCount`.

<div class="formalpara">

<div class="title">

Example Reporting: Prometheus format

</div>

``` bash
curl -s -H 'Accept: text/plain' -X GET http://localhost:8080{metrics-endpoint}
```

</div>

``` text
# HELP classloader_loadedClasses_count Displays the number of classes that are currently loaded in the Java virtual machine.
# TYPE classloader_loadedClasses_count gauge
classloader_loadedClasses_count{{prom-output-scope-prefix}scope="base",} 5297.0
```

See the summary of the [OpenMetrics and Prometheus
Format](#_openmetrics_and_prometheus_format) for more information.

<div class="formalpara">

<div class="title">

Example Reporting: JSON format

</div>

``` bash
curl -s -H 'Accept: application/json' -X GET http://localhost:8080{metrics-endpoint}
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

In addition to your application {metrics}, the reports contain other
{metrics} of interest such as system and VM information.

## OpenMetrics and Prometheus Format

The [OpenMetrics format]({openmetrics-format-doc-url}) and the
[Prometheus exposition format]({prometheus-exposition-format-doc-url})
are very similar in most important respects but are not identical. This
brief summary treats them as the same.

The OpenMetrics/Prometheus format represents each {metric} using three
lines of output as summarized in the following table.

| Line prefix | Purpose | Format |
|----|----|----|
| `# TYPE` | Displays the scope, name, and type of the {metric} | `TYPE <scope>:<output-name> <{metric}-type>` |
| `# HELP` | Displays the scope, name, and description of the {metric} | `HELP <scope>:<output-name> <registered description>` |
| (none) | Displays the scope, {metric} ID, and current value of the {metric} | `<scope>:<output-name> <current value>` |

OpenMetrics/Prometheus format

The OpenMetrics/Prometheus output converts {metric} IDs in these ways:

- Names in camel case are converted to "snake case" and dots are
  converted to underscores.

- Names include any units specified for the {metric}.

- For percentiles, the ID includes a tag identifying which percentile
  the line of output describes.

As the earlier example output showed, for a {metric} with multiple
values, such as a timer or a (with, among others, `max`, `mean`, and
`count`), the OpenMetrics/Prometheus output reports a "metric family"
which includes a separate family member {metric} for each of the
multiple values. The name for each member in the family is derived from
the registered name for the {metric} plus a suffix indicating which one
of the {metric}'s multiple values the line refers to.

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
<td
style="text-align: left;"><p><code>requests_count_total</code></p></td>
</tr>
<tr>
<td rowspan="4" style="text-align: left;"></td>
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
style="text-align: left;"><p><code>nameLengths{{prom-output-scope-prefix}scope="base",quantile="0.5",}</code></p></td>
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
style="text-align: left;"><p><code>vthreads_recentPinned_seconds{{prom-output-scope-prefix}scope="base",quantile="0.5",}</code></p></td>
</tr>
</tbody>
</table>

<sup>1</sup> The OpenMetrics/Prometheus output format reports a timer as
a `summary` with units of `seconds`.

## JSON Format

Unlike OpenMetrics/Prometheus output, which combines the data and the
metadata in a single response, you use an HTTP `GET` request to retrieve
metrics JSON *data* and an `OPTIONS` request to retrieve *metadata* in
JSON format.

Helidon groups {metrics} in the same scope together in JSON output as
shown in the following example.

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

### Understanding the JSON Metrics Data Format

The Helidon JSON format expresses each {metric} as either a single value
(for example, a counter) or a structure with multiple values (for
example, a timer).

<div class="formalpara">

<div class="title">

JSON output for a single-valued {metric} (for example, `Counter`)

</div>

``` json
"requests.count": 5
```

</div>

<div class="formalpara">

<div class="title">

JSON output for a multi-valued {metric} (for example, `Timer`)

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

### Understanding the JSON Metrics Metadata Format

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

Generally, the output for a given {metric} reflects only the metadata
that the application or Helidon code explicitly set on that {metric}.

One exception is that metadata for a timer always includes the `unit`
field. By default, Helidon formats timer data in JSON output as seconds,
regardless of any explicit `baseUnit` setting applied to the timers. But
as [described below](#controlling_timer_output) you can change this
behavior which can lead to different timers being formatted using
different units. Checking the metadata is the only way to know for sure
what units Helidon used to express a given timer, so Helidon always
includes `unit` in timer metadata.

### Controlling JSON Timer Output

By default, Helidon expresses timer data as seconds.

You can change this using configuration: \<1\> For *units* specify any
valid name for a
[`TimeUnit`]({jdk-javadoc-url}/java.base/java/util/concurrent/TimeUnit.html)
value (`SECONDS`, `MILLISECONDS`, etc.)

If you have configured `json-units-default`, Helidon formats each
timer’s data as follows:

1.  If code set `baseUnit` on the timer, Helidon uses those units for
    that timer.

2.  Otherwise, Helidon uses the default units you configured.

To enable the JSON output behavior from Helidon 3, specify
`json-units-default` as `NANOSECONDS`.

# The `MetricRegistry` API

To register or look up {metrics} programmatically, your service code
uses the
[`MetricRegistry`]({microprofile-metrics-javadoc-url}/org/eclipse/microprofile/metrics/MetricRegistry.html)
instance for the scope of interest: `base`, `vendor`, `application`, or
a custom scope.

Once it has a reference to a `MetricRegistry` your code can use the
reference to register new metrics, look up previously-registered
metrics, and remove metrics.

Helidon {flavor-uc} includes several pre-written example applications
illustrating aspects of metrics:

- [Enabling/disabling
  {metrics}]({helidon-github-examples-url}/metrics/filtering/se) using

[OpenMetrics format]({openmetrics-format-doc-url})

[Prometheus exposition format]({prometheus-exposition-format-doc-url})
