# Configuration

To control how the Helidon metrics subsystem behaves, add a `metrics`
section to

Certain default configuration values depend on the fact that you are
using Helidon {flavor-uc} as described in the [second table
below](#flavor-specific-defaults).

Type:
[io.helidon.webserver.observe.metrics.MetricsObserver]({javadoc-base-url}/io.helidon.webserver.observe.metrics/io/helidon/webserver/observe/metrics/MetricsObserver.html)

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
| `app-tag-name`     |               |
| `scoping.tag-name` |               |
| `scoping.default`  |               |

Default Values Specific to Helidon {flavor-uc}

## Controlling the {metric_uc} Type for `gc.time`

To date Helidon 4 releases have implemented the system-provided {metric}
`gc.time` as a counter. In fact, a gauge is more suitable for the
approximate time the JVM has spent doing garbage

Helidon {helidon-version} continues to use a counter by default to
preserve backward compatibility, but you can choose to use a gauge by
setting the configuration property `metrics.gc-time-type` to `gauge`.
You can also set the config property to `counter` which is the default.

Why should you care? In fact, this distinction might not make a
difference for many users. But for others the differences between the
programmatic APIs for `Counter` and `Gauge` would affect application
code that works directly with the `gc-time` {metric}. Further, the
difference in output—​particularly in the OpenMetrics/Prometheus
format—​might affect their application or downstream monitoring tools.

The ability to choose the {metric} type for `gc.time` is deprecated and
is planned for removal in a future major release of Helidon at which
time Helidon will always use a gauge.

## Example Configuration

Metrics configuration is quite extensive and powerful and, therefore, a
bit complicated. The rest of this section illustrates some of the most
common scenarios:

- [Disable metrics entirely.](#config-disable)

- [Choose whether to report virtual threads
  {metrics}](#config-virtual-threads).

- [Choose whether to collect extended key performance indicator
  metrics.](#config-kpi)

### Disable Metrics Subsystem

<div class="formalpara">

<div class="title">

Disabling metrics entirely

</div>

Helidon does not update metrics, and the `{metrics-endpoint}` endpoints
respond with `404`.

</div>

### Configuring Virtual Threads {metrics_uc}

#### Enabling Virtual Threads {metrics_uc}

Gathering data to compute the {metrics} for virtual threads is designed
to be as efficient as possible, but doing so still imposes a load on the
server and by default Helidon does not report {metrics} related to
virtual threads.

To enable the {metrics} describing virtual threads include a config
setting as shown in the following example.

#### Controlling Measurements of Pinned Virtual Threads

<div class="formalpara">

<div class="title">

Enabling virtual thread {metrics}

</div>

Helidon measures pinned virtual threads only when the thread is pinned
for a length of time at or above a threshold. Control the threshold as
shown in the example below.

</div>

<div class="formalpara">

<div class="title">

Setting virtual thread pinning threshold to 100 ms

</div>

The threshold value is a `Duration` string, such as `PT0.100S` for 100
milliseconds.

</div>

### Collecting Basic and Extended Key Performance Indicator (KPI) {metrics_uc}

Any time you include the Helidon metrics module in your application,
Helidon tracks a basic performance indicator {metric}: a `Counter` of
all requests received (`requests.count`)

Helidon {h1-prefix} also includes additional, extended KPI {metrics}
which are disabled by default:

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

You can enable and control these {metrics} using configuration:
