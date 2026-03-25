# Configuration

To control how the Helidon metrics subsystem behaves, add a `metrics` section to

Certain default configuration values depend on the fact that you are using Helidon {flavor-uc} as described in the [second table below](#flavor-specific-defaults).

### Configuration options

| Key | Kind | Type | Default Value | Description |
|----|----|----|----|----|
| <span id="ab3e25-app-name"></span> `app-name` | `VALUE` | `String` |   | Value for the application tag to be added to each meter ID |
| <span id="a0590e-app-tag-name"></span> `app-tag-name` | `VALUE` | `String` |   | Name for the application tag to be added to each meter ID |
| <span id="a24eaf-built-in-meter-name-format"></span> [`built-in-meter-name-format`](../../config/io_helidon_metrics_api_BuiltInMeterNameFormat.md) | `VALUE` | `i.h.m.a.BuiltInMeterNameFormat` | `CAMEL` | Output format for built-in meter names |
| <span id="aac68d-enabled"></span> `enabled` | `VALUE` | `Boolean` | `true` | Whether metrics functionality is enabled |
| <span id="a90f80-key-performance-indicators"></span> [`key-performance-indicators`](../../config/io_helidon_metrics_api_KeyPerformanceIndicatorMetricsConfig.md) | `VALUE` | `i.h.m.a.KeyPerformanceIndicatorMetricsConfig` |   | Key performance indicator metrics settings |
| <span id="acbf94-permit-all"></span> `permit-all` | `VALUE` | `Boolean` | `true` | Whether to allow anybody to access the endpoint |
| <span id="ae7437-publishers"></span> [`publishers`](../../config/io_helidon_metrics_api_MetricsPublisher.md) | `LIST` | `i.h.m.a.MetricsPublisher` |   | Metrics publishers which make the metrics data available to external systems |
| <span id="af1711-publishers-discover-services"></span> `publishers-discover-services` | `VALUE` | `Boolean` | `false` | Whether to enable automatic service discovery for `publishers` |
| <span id="a1e75d-rest-request-enabled"></span> `rest-request.enabled` | `VALUE` | `Boolean` | `false` | Whether automatic REST request metrics should be measured |
| <span id="a3d689-roles"></span> `roles` | `LIST` | `String` | `observe` | Hints for role names the user is expected to be in |
| <span id="ae0eb0-scoping"></span> [`scoping`](../../config/io_helidon_metrics_api_ScopingConfig.md) | `VALUE` | `i.h.m.a.ScopingConfig` |   | Settings related to scoping management |
| <span id="a995f3-tags"></span> `tags` | `LIST` | `i.h.m.a.MetricsConfigSupport` |   | Global tags |
| <span id="a977e0-timers-json-units-default"></span> [`timers.json-units-default`](../../config/java_util_concurrent_TimeUnit.md) | `VALUE` | `TimeUnit` |   | Default units for timer output in JSON if not specified on a given timer |
| <span id="a9178f-virtual-threads-enabled"></span> `virtual-threads.enabled` | `VALUE` | `Boolean` | `false` | Whether Helidon should expose meters related to virtual threads |
| <span id="a628d9-virtual-threads-pinned-threshold"></span> `virtual-threads.pinned.threshold` | `VALUE` | `Duration` | `PT0.020S` | Threshold for sampling pinned virtual threads to include in the pinned threads meter |
| <span id="adb8b4-warn-on-multiple-registries"></span> `warn-on-multiple-registries` | `VALUE` | `Boolean` | `true` | Whether to log warnings when multiple registries are created |

#### Deprecated Options

| Key | Kind | Type | Default Value | Description |
|----|----|----|----|----|
| <span id="a12103-gc-time-type"></span> [`gc-time-type`](../../config/io_helidon_metrics_api_GcTimeType.md) | `VALUE` | `i.h.m.a.GcTimeType` | `COUNTER` | Whether the `gc.time` meter should be registered as a gauge (vs |
| <span id="aa1220-rest-request-enabled"></span> `rest-request-enabled` | `VALUE` | `Boolean` |   | Whether automatic REST request metrics should be measured (as indicated by the deprecated config key `rest-request-enabled`, the config key using a hyphen instead of a dot separator) |

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

#### Configuration options

| Key | Kind | Type | Default Value | Description |
|----|----|----|----|----|
| <span id="a9ac57-enabled"></span> `enabled` | `VALUE` | `Boolean` | `true` | Whether automatic metrics collection as a whole is enabled |
| <span id="a61ecb-opt-in"></span> `opt-in` | `LIST` | `String` |   | Elective attribute for which to opt in |
| <span id="a6fb0d-paths"></span> [`paths`](../../config/io_helidon_webserver_observe_metrics_AutoHttpMetricsPathConfig.md) | `LIST` | `i.h.w.o.m.AutoHttpMetricsPathConfig` |   | Automatic metrics collection settings |
| <span id="af4ffb-sockets"></span> `sockets` | `LIST` | `String` |   | Socket names for sockets to be instrumented with automatic metrics |

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
