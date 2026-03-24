# ObserveFeature (webserver.observe) Configuration

Type: [io.helidon.webserver.observe.ObserveFeature](/apidocs/io.helidon.webserver.observe/io/helidon/webserver/observe/ObserveFeature.html)

*Config key*

``` text
observe
```

This type provides the following service implementations:

- `io.helidon.webserver.spi.ServerFeatureProvider`

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
<td style="text-align: left;"><p><span class="line-through"><code>cors</code></span></p></td>
<td style="text-align: left;"><p><a href="../config/../config/io_helidon_cors_CrossOriginConfig.xml">CrossOriginConfig</a></p></td>
<td style="text-align: left;"><p><code>@io.helidon.cors.CrossOriginConfig@.create()</code></p></td>
<td style="text-align: left;"><p><strong>Deprecated</strong> Cors support inherited by each observe provider, unless explicitly configured.</p>
<p>@deprecated feature specific CORS configuration is deprecated and will be removed; use either config based CORS setup (configuration key <code>cors</code>, or programmatic setup using the <code>io.helidon.webserver.cors.CorsFeature</code> server feature</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>enabled</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Whether the observe support is enabled.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>endpoint</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p><code>/observe</code></p></td>
<td style="text-align: left;"><p>Root endpoint to use for observe providers. By default, all observe endpoint are under this root endpoint.</p>
<p>Example:</p>
<p>If root endpoint is <code>/observe</code> (the default), and default health endpoint is <code>health</code> (relative), health endpoint would be <code>/observe/health</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>observers</code></p></td>
<td style="text-align: left;"><p>io.helidon.webserver.observe.spi.Observer[] (service provider interface)</p>
<p>Such as:</p>
<ul>
<li><p><a href="../config/../config/io_helidon_webserver_observe_log_LogObserver.xml">log (LogObserver)</a></p></li>
<li><p><a href="../config/../config/io_helidon_webserver_observe_tracing_TracingObserver.xml">tracing (TracingObserver)</a></p></li>
<li><p><a href="../config/../config/io_helidon_webserver_observe_config_ConfigObserver.xml">config (ConfigObserver)</a></p></li>
<li><p><a href="../config/../config/io_helidon_webserver_observe_info_InfoObserver.xml">info (InfoObserver)</a></p></li>
<li><p><a href="../config/../config/io_helidon_webserver_observe_metrics_MetricsObserver.xml">metrics (MetricsObserver)</a></p></li>
<li><p><a href="../config/../config/io_helidon_webserver_observe_health_HealthObserver.xml">health (HealthObserver)</a></p></li>
</ul></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Observers to use with this observe features. Each observer type is registered only once, unless it uses a custom name (default name is the same as the type).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>sockets</code></p></td>
<td style="text-align: left;"><p>string[]</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Sockets the observability endpoint should be exposed on. If not defined, defaults to the default socket (<code>@default</code>. Each observer may have its own configuration of sockets that are relevant to it, this only controls the endpoints!</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>weight</code></p></td>
<td style="text-align: left;"><p>double</p></td>
<td style="text-align: left;"><p><code>80.0</code></p></td>
<td style="text-align: left;"><p>Change the weight of this feature. This may change the order of registration of this feature. By default, observability weight is <code>80.0</code> so it is registered after routing.</p></td>
</tr>
</tbody>
</table>
