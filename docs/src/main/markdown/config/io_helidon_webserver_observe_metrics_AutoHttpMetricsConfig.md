# AutoHttpMetricsConfig (webserver.observe.metrics) Configuration

Type: [io.helidon.webserver.observe.metrics.AutoHttpMetricsConfig](/apidocs/io.helidon.webserver.observe.metrics/io/helidon/webserver/observe/metrics/AutoHttpMetricsConfig.html)

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
<td style="text-align: left;"><p><a href="../config/../config/io_helidon_webserver_observe_metrics_AutoHttpMetricsPathConfig.xml">AutoHttpMetricsPathConfig[]</a></p></td>
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
