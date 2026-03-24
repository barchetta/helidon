# EurekaRegistrationServerFeature (integrations.eureka) Configuration

Type: [io.helidon.integrations.eureka.EurekaRegistrationServerFeature](/apidocs/io.helidon.integrations.eureka/io/helidon/integrations/eureka/EurekaRegistrationServerFeature.html)

*Config key*

``` text
eureka
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
<td style="text-align: left;"><p><code>enabled</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Whether this feature will be enabled.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>instance</code></p></td>
<td style="text-align: left;"><p><a href="../config/../config/io_helidon_integrations_eureka_InstanceInfoConfig.xml">InstanceInfoConfig</a></p></td>
<td style="text-align: left;"><p><code>io.helidon.integrations.eureka.EurekaRegistrationConfigBlueprint.create()</code></p></td>
<td style="text-align: left;"><p>An InstanceInfoConfig describing the service instance to be registered.</p>
<p>See InstanceInfoConfig</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>weight</code></p></td>
<td style="text-align: left;"><p>double</p></td>
<td style="text-align: left;"><p><code>100.0</code></p></td>
<td style="text-align: left;"><p>The (zero or positive) io.helidon.common.Weighted weight of this instance.</p></td>
</tr>
</tbody>
</table>
