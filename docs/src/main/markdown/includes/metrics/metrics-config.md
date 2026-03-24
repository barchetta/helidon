# Configuration

To control how the Helidon metrics subsystem behaves, add a `metrics` section to

Certain default configuration values depend on the fact that you are using Helidon {flavor-uc} as described in the [second table below](#flavor-specific-defaults).

Type: [io.helidon.metrics.api.MetricsConfig]({javadoc-base-url}/io.helidon.metrics.api/io/helidon/metrics/api/MetricsConfig.md)

This is a standalone configuration type, prefix from configuration root: `metrics`

### Configuration options

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
<td style="text-align: left;"><p>Value for the application tag to be added to each meter ID.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>app-tag-name</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Name for the application tag to be added to each meter ID.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>built-in-meter-name-format</code></p></td>
<td style="text-align: left;"><p>BuiltInMeterNameFormat (SNAKE, CAMEL)</p></td>
<td style="text-align: left;"><p><code>BuiltInMeterNameFormat.CAMEL</code></p></td>
<td style="text-align: left;"><p>Output format for built-in meter names.</p>
<p>BuiltInMeterNameFormat.SNAKE selects "snake_case" which does not conform to the MicroProfile Metrics specification.</p>
<p>Allowed values:</p>
<ul>
<li><p><code>SNAKE</code>: Snake-case.</p></li>
<li><p><code>CAMEL</code>: Camel-case (which is compatible with the MicroProfile Metrics spec).</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>enabled</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Whether metrics functionality is enabled.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><span class="line-through"><code>gc-time-type</code></span></p></td>
<td style="text-align: left;"><p>GcTimeType (GAUGE, COUNTER)</p></td>
<td style="text-align: left;"><p><code>GcTimeType.COUNTER</code></p></td>
<td style="text-align: left;"><p><strong>Deprecated</strong> Whether the <code>gc.time</code> meter should be registered as a gauge (vs. a counter). The <code>gc.time</code> meter is inspired by the MicroProfile Metrics spec, in which the meter was originally checked to be a counter but starting in 5.1 was checked be a gauge. For the duration of Helidon 4.x users can choose which type of meter Helidon registers for <code>gc.time</code>.</p>
<p>@deprecated Provided for backward compatibility only; no replacement</p>
<p>Allowed values:</p>
<ul>
<li><p><code>GAUGE</code>: Implement the meter as a gauge. This is backward-incompatible with Helidon 4.0.x releases but complies with MicroProfile 5.1.</p></li>
<li><p><code>COUNTER</code>: Implement the meter as a counter. This is backward-compatible with Helidon 4.0.x releases but does not comply with MicroProfile 5.1.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>key-performance-indicators</code></p></td>
<td style="text-align: left;"><p><a href="../../includes/metrics/../../config/io_helidon_metrics_api_KeyPerformanceIndicatorMetricsConfig.xml">KeyPerformanceIndicatorMetricsConfig</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Key performance indicator metrics settings.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>permit-all</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Whether to allow anybody to access the endpoint.</p>
<p>See roles()</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>publishers</code></p></td>
<td style="text-align: left;"><p>io.helidon.metrics.api.MetricsPublisher[] (service provider interface)</p>
<p>Such as:</p>
<ul>
<li><p><a href="../../includes/metrics/../../config/io_helidon_metrics_providers_micrometer_OtlpPublisher.xml">otlp (OtlpPublisher)</a></p></li>
<li><p><a href="../../includes/metrics/../../config/io_helidon_metrics_providers_micrometer_PrometheusPublisher.xml">prometheus (PrometheusPublisher)</a></p></li>
</ul></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Metrics publishers which make the metrics data available to external systems. Helidon’s Micrometer-based metrics provider includes <code>micrometer-prometheus</code> (used by default) and <code>micrometer-otlp</code>. See the config reference entries for <code>io.helidon.metrics.providers.micrometer.PrometheusPublisher</code> and <code>io.helidon.metrics.providers.micrometer.OtlpPublisher</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><span class="line-through"><code>rest-request-enabled</code></span></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p><strong>Deprecated</strong> Whether automatic REST request metrics should be measured (as indicated by the deprecated config key <code>rest-request-enabled</code>, the config key using a hyphen instead of a dot separator).</p>
<p>@deprecated Use <code>rest-request.enabled</code> instead.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>rest-request.enabled</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>false</code></p></td>
<td style="text-align: left;"><p>Whether automatic REST request metrics should be measured.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>roles</code></p></td>
<td style="text-align: left;"><p>string[]</p></td>
<td style="text-align: left;"><p><code>observe</code></p></td>
<td style="text-align: left;"><p>Hints for role names the user is expected to be in.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scoping</code></p></td>
<td style="text-align: left;"><p><a href="../../includes/metrics/../../config/io_helidon_metrics_api_ScopingConfig.xml">ScopingConfig</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Settings related to scoping management.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>tags</code></p></td>
<td style="text-align: left;"><p><a href="../../includes/metrics/../../config/io_helidon_metrics_api_Tag.xml">Tag[]</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Global tags.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>timers.json-units-default</code></p></td>
<td style="text-align: left;"><p>TimeUnit (NANOSECONDS, MICROSECONDS, MILLISECONDS, SECONDS, MINUTES, HOURS, DAYS)</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Default units for timer output in JSON if not specified on a given timer.</p>
<p>If the configuration key is absent, the Helidon JSON output uses java.util.concurrent.TimeUnit.SECONDS. If the configuration key is present, Helidon formats each timer using that timer’s specific units (if set) and the config value otherwise.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>virtual-threads.enabled</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>false</code></p></td>
<td style="text-align: left;"><p>Whether Helidon should expose meters related to virtual threads.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>virtual-threads.pinned.threshold</code></p></td>
<td style="text-align: left;"><p>Duration</p></td>
<td style="text-align: left;"><p><code>PT0.020S</code></p></td>
<td style="text-align: left;"><p>Threshold for sampling pinned virtual threads to include in the pinned threads meter.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>warn-on-multiple-registries</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Whether to log warnings when multiple registries are created.</p>
<p>By far most applications use a single meter registry, but certain app or library programming errors can cause Helidon to create more than one. By default, Helidon logs warning messages for each additional meter registry created. This setting allows users with apps that &lt;em&gt;need&lt;/em&gt; multiple meter registries to suppress those warnings.</p></td>
</tr>
</tbody>
</table>

| Key                | Default Value |
|--------------------|---------------|
| `app-tag-name`     |               |
| `scoping.tag-name` |               |
| `scoping.default`  |               |

Default Values Specific to Helidon {flavor-uc}

### Controlling the {metric_uc} Type for `gc.time`

To date Helidon 4 releases have implemented the system-provided {metric} `gc.time` as a counter. In fact, a gauge is more suitable for the approximate time the JVM has spent doing garbage

Helidon {helidon-version} continues to use a counter by default to preserve backward compatibility, but you can choose to use a gauge by setting the configuration property `metrics.gc-time-type` to `gauge`. You can also set the config property to `counter` which is the default.

Why should you care? In fact, this distinction might not make a difference for many users. But for others the differences between the programmatic APIs for `Counter` and `Gauge` would affect application code that works directly with the `gc-time` {metric}. Further, the difference in output—​particularly in the OpenMetrics/Prometheus format—​might affect their application or downstream monitoring tools.

The ability to choose the {metric} type for `gc.time` is deprecated and is planned for removal in a future major release of Helidon at which time Helidon will always use a gauge.

### Controlling the Metrics Observer

Helidon can make the registered {metrics} and their current values available externally at an endpoint ({metrics-endpoint} by default). You can control aspects of how Helidon furnishes this information under the `server.features.observe.observers.metrics` configuration section.

| key | type | default value | description |
|----|----|----|----|
| `auto` | [AutoHttpMetricsConfig](../../config/io_helidon_webserver_observe_metrics_AutoHttpMetricsConfig.md) |   | Automatic metrics collection settings. |
| `enabled` | boolean | `true` | Whether this observer is enabled. |
| `endpoint` | string | `{metrics-endpoint}` | Path at which clients can retrieve metrics information. |

Optional configuration options

#### Selecting REST Endpoints for Automatic Measurement

You can choose which endpoints to include in Helidon’s automatic measurements using the `auto-http-metrics` config section.

Type: [io.helidon.webserver.observe.metrics.AutoHttpMetricsConfig]({javadoc-base-url}/io.helidon.webserver.observe.metrics/io/helidon/webserver/observe/metrics/AutoHttpMetricsConfig.md)

#### Configuration options

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
<td style="text-align: left;"><p>Whether automatic metrics collection as a whole is enabled.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>opt-in</code></p></td>
<td style="text-align: left;"><p>string[]</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Elective attribute for which to opt in. Each string in the list is of the form <code>meter-name:attribute-name</code> where <code>meter-name</code> is the name of the meter and <code>attribute-name</code> is the name of an attribute (tag) which is optional on that meter.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>paths</code></p></td>
<td style="text-align: left;"><p><a href="../../includes/metrics/../../config/io_helidon_webserver_observe_metrics_AutoHttpMetricsPathConfig.xml">AutoHttpMetricsPathConfig[]</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Automatic metrics collection settings. Default excludes built-in Helidon paths (e.g., metrics, health). A request’s path and HTTP method are checked against each entry under <code>paths</code> in order.</p>
<ul>
<li><p>If a request matches no entry, then the request is measured.</p></li>
<li><p>If a request matches multiple entries, then the first match wins.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>sockets</code></p></td>
<td style="text-align: left;"><p>string[]</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Socket names for sockets to be instrumented with automatic metrics. Defaults to all sockets.</p></td>
</tr>
</tbody>
</table>

The `paths` section contains zero or more entries, each entry having the following settings:

<table>
<caption><code>path</code> entry settings</caption>
<colgroup>
<col style="width: 13%" />
<col style="width: 6%" />
<col style="width: 13%" />
<col style="width: 66%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Key</th>
<th style="text-align: left;">Required</th>
<th style="text-align: left;">Default Value</th>
<th style="text-align: left;">Usage</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>path</code></p></td>
<td style="text-align: left;"><p>yes</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Path-matching expression:</p>
<ul>
<li><p>an exact match (<code>/greet</code>)</p></li>
<li><p>a prefix match (<code>/greet/*</code>)</p></li>
<li><p>a pattern match (<code>/greet/{name}</code>)</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>methods</code></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>all HTTP method types</p></td>
<td style="text-align: left;"><p>Which HTTP methods match this entry</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>enabled</code></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Whether requests that match this entry should be measured</p></td>
</tr>
</tbody>
</table>

Helidon decides whether to measure incoming requests as follows:

- If you omit the `auto-http-metrics` configuration, Helidon measures all endpoints.

- If you specify the `auto-http-metrics` configuration, by default Helidon does not measure built-in endpoints such as metrics, health, and openapi. You can add items under `auto-http-metrics.paths` to control more exactly which endpoints to measure.

- If you include the `paths` section, Helidon checks a request against the path entries in order. A given request matches an entry if its path matches the path pattern and its HTTP method is in the `methods` list. If there is no `methods` list for an entry, all HTTP methods match the entry.

- If a request matches an entry, the entry’s `enabled` setting determines if the request should be measured.

- If a request matches multiple entries, the first match wins.

- If a request matches no entry, it is measured.

The `auto-http-metrics.sockets` setting controls which sockets are included in the measurements; if not set, Helidon measures requests on all sockets.

<div>

<div class="title">

Including and Excluding Endpoints from Automatic Measurement

</div>

- Measure `/greet` for only `GET` and `HEAD` requests.

- Do not measure the personalized greeting requests.

- Measure only endpoints on the default socket and the socket named `private`. Endpoints on other sockets (such as if you had an `admin` socket) are not measured.

</div>

The [AutoHttpMetricsConfig documentation](../../config/io_helidon_webserver_observe_metrics_AutoHttpMetricsConfig.md) describes the configuration more fully.

### Example Configuration

Metrics configuration is quite extensive and powerful and, therefore, a bit complicated. The rest of this section illustrates some of the most common scenarios:

- [Disable metrics entirely.](#config-disable)

- [Choose whether to report virtual threads {metrics}](#config-virtual-threads).

- [Choose whether to collect extended key performance indicator metrics.](#config-kpi)

#### Disable Metrics Subsystem

*Disabling metrics entirely*

Helidon does not update metrics, and the `{metrics-endpoint}` endpoints respond with `404`.

#### Configuring Virtual Threads {metrics_uc}

##### Enabling Virtual Threads {metrics_uc}

Gathering data to compute the {metrics} for virtual threads is designed to be as efficient as possible, but doing so still imposes a load on the server and by default Helidon does not report {metrics} related to virtual threads.

To enable the {metrics} describing virtual threads include a config setting as shown in the following example.

##### Controlling Measurements of Pinned Virtual Threads

*Enabling virtual thread {metrics}*

Helidon measures pinned virtual threads only when the thread is pinned for a length of time at or above a threshold. Control the threshold as shown in the example below.

*Setting virtual thread pinning threshold to 100 ms*

The threshold value is a `Duration` string, such as `PT0.100S` for 100 milliseconds.

#### Collecting Basic and Extended Key Performance Indicator (KPI) {metrics_uc}

Any time you include the Helidon metrics module in your application, Helidon tracks a basic performance indicator {metric}: a `Counter` of all requests received (`requests.count`)

Helidon {h1-prefix} also includes additional, extended KPI {metrics} which are disabled by default:

- current number of requests in-flight - a `Gauge` (`requests.inFlight`) of requests currently being processed

- long-running requests - a `Counter` (`requests.longRunning`) measuring the total number of requests which take at least a given amount of time to complete; configurable, defaults to 10000 milliseconds (10 seconds)

- load - a `Counter` (`requests.load`) measuring the number of requests worked on (as opposed to received)

- deferred - a `Gauge` (`requests.deferred`) measuring delayed request processing (work on a request was delayed after Helidon received the request)

You can enable and control these {metrics} using configuration:
