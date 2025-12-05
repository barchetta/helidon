Type:
[io.helidon.integrations.eureka.InstanceInfoConfig](/apidocs/io.helidon.integrations.eureka/io/helidon/integrations/eureka/InstanceInfoConfig.html)

# Configuration options

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
<td style="text-align: left;"><p><code>appGroup</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p><code>unknown</code></p></td>
<td style="text-align: left;"><p>The app group name.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>asgName</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>The ASG name.
&lt;abbr&gt;ASG&lt;/abbr&gt; stands for Auto Scaling Group.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>healthCheckUrl</code></p></td>
<td style="text-align: left;"><p>URI</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>The health check URL.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>healthCheckUrlPath</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>The health check URL path (used if any
health check URL is not explicitly set).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>homePageUrl</code></p></td>
<td style="text-align: left;"><p>URI</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>The home page URL.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>homePageUrlPath</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p><code>/</code></p></td>
<td style="text-align: left;"><p>The home page URL path (used if the
homepage URL is not explicitly set).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>hostName</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>The hostname.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>instanceId</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>The instance id.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ipAddr</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>The IP address.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>lease</code></p></td>
<td style="text-align: left;"><p><a
href="../config/io_helidon_integrations_eureka_LeaseInfoConfig.xml">LeaseInfoConfig</a></p></td>
<td
style="text-align: left;"><p><code>io.helidon.integrations.eureka.InstanceInfoConfigBlueprint.create()</code></p></td>
<td style="text-align: left;"><p>The LeaseInfoConfig.</p>
<p>See LeaseInfoConfig</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>metadata</code></p></td>
<td style="text-align: left;"><p>Map&lt;string, string&gt;</p></td>
<td
style="text-align: left;"><p><code>@java.util.Map@.of()</code></p></td>
<td style="text-align: left;"><p>Metadata.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p><code>unknown</code></p></td>
<td style="text-align: left;"><p>The app name.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>port</code></p></td>
<td style="text-align: left;"><p><a
href="../config/io_helidon_integrations_eureka_PortInfoConfig.xml">PortInfoConfig</a></p></td>
<td
style="text-align: left;"><p><code>io.helidon.integrations.eureka.InstanceInfoConfigBlueprint.create()</code></p></td>
<td style="text-align: left;"><p>(Non-secure) port information.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>secureHealthCheckUrl</code></p></td>
<td style="text-align: left;"><p>URI</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>The secure health check URL.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>securePort</code></p></td>
<td style="text-align: left;"><p><a
href="../config/io_helidon_integrations_eureka_PortInfoConfig.xml">PortInfoConfig</a></p></td>
<td
style="text-align: left;"><p><code>io.helidon.integrations.eureka.InstanceInfoConfigBlueprint.create()</code></p></td>
<td style="text-align: left;"><p>Secure port information.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>secureVipAddress</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>The secure VIP address.
&lt;abbr&gt;VIP&lt;/abbr&gt; stands for Virtual IP.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>statusPageUrl</code></p></td>
<td style="text-align: left;"><p>URI</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>The status page URL.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>statusPageUrlPath</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p><code>/Status</code></p></td>
<td style="text-align: left;"><p>The status page URL path (used if
status page URL is not explicitly set).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>traffic.enabled</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Whether traffic is enabled on startup
(normally <code>true</code>).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>vipAddress</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>The VIP address.
&lt;abbr&gt;VIP&lt;/abbr&gt; stands for Virtual IP.</p></td>
</tr>
</tbody>
</table>
