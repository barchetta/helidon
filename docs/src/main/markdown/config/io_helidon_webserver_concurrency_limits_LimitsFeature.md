# LimitsFeature (webserver.concurrency.limits) Configuration

Type: [io.helidon.webserver.concurrency.limits.LimitsFeature](/apidocs/io.helidon.webserver.concurrency.limits/io/helidon/webserver/concurrency/limits/LimitsFeature.html)

*Config key*

``` text
limits
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
<td style="text-align: left;"><p><code>concurrency-limit</code></p></td>
<td style="text-align: left;"><p>io.helidon.common.concurrency.limits.Limit (service provider interface)</p>
<p>Such as:</p>
<ul>
<li><p><a href="../config/../config/io_helidon_common_concurrency_limits_ThroughputLimit.xml">throughput (ThroughputLimit)</a></p></li>
<li><p><a href="../config/../config/io_helidon_common_concurrency_limits_FixedLimit.xml">fixed (FixedLimit)</a></p></li>
<li><p><a href="../config/../config/io_helidon_common_concurrency_limits_AimdLimit.xml">aimd (AimdLimit)</a></p></li>
</ul></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Concurrency limit to use to limit concurrent execution of incoming requests. The default is to have unlimited concurrency.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>enabled</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Whether this feature is enabled, defaults to <code>true</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>sockets</code></p></td>
<td style="text-align: left;"><p>string[]</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>List of sockets to register this feature on. If empty, it would get registered on all sockets.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>weight</code></p></td>
<td style="text-align: left;"><p>double</p></td>
<td style="text-align: left;"><p><code>2000.0</code></p></td>
<td style="text-align: left;"><p>Weight of the context feature. As it is used by other features, the default is quite high: <code>2000.0</code>.</p></td>
</tr>
</tbody>
</table>
