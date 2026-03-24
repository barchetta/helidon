# MetricsObserver (webserver.observe.metrics) Configuration

Type: [io.helidon.webserver.observe.metrics.MetricsObserver](/apidocs/io.helidon.webserver.observe.metrics/io/helidon/webserver/observe/metrics/MetricsObserver.html)

This is a standalone configuration type, prefix from configuration root: `metrics`

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
<td style="text-align: left;"><p>Value for the application tag to be added to each meter ID.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>app-tag-name</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Name for the application tag to be added to each meter ID.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>auto-http-metrics</code></p></td>
<td style="text-align: left;"><p><a href="../config/../config/io_helidon_webserver_observe_metrics_AutoHttpMetricsConfig.xml">AutoHttpMetricsConfig</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Automatic metrics collection settings.</p></td>
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
<td style="text-align: left;"><p>Whether this observer is enabled.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>enabled</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Whether metrics functionality is enabled.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>endpoint</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p><code>metrics</code></p></td>
<td style="text-align: left;"></td>
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
<td style="text-align: left;"><p><a href="../config/../config/io_helidon_metrics_api_KeyPerformanceIndicatorMetricsConfig.xml">KeyPerformanceIndicatorMetricsConfig</a></p></td>
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
<li><p><a href="../config/../config/io_helidon_metrics_providers_micrometer_OtlpPublisher.xml">otlp (OtlpPublisher)</a></p></li>
<li><p><a href="../config/../config/io_helidon_metrics_providers_micrometer_PrometheusPublisher.xml">prometheus (PrometheusPublisher)</a></p></li>
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
<td style="text-align: left;"><p><a href="../config/../config/io_helidon_metrics_api_ScopingConfig.xml">ScopingConfig</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Settings related to scoping management.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>tags</code></p></td>
<td style="text-align: left;"><p><a href="../config/../config/io_helidon_metrics_api_Tag.xml">Tag[]</a></p></td>
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
