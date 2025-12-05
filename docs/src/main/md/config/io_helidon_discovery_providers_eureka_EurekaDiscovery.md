Type:
[io.helidon.discovery.providers.eureka.EurekaDiscovery](/apidocs/io.helidon.discovery.providers.eureka/io/helidon/discovery/providers/eureka/EurekaDiscovery.html)

<div class="formalpara">

<div class="title">

Config key

</div>

``` text
eureka
```

</div>

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
<td style="text-align: left;"><p><code>cache</code></p></td>
<td style="text-align: left;"><p><a
href="../config/io_helidon_discovery_providers_eureka_CacheConfig.xml">CacheConfig</a></p></td>
<td
style="text-align: left;"><p><code>io.helidon.discovery.providers.eureka.EurekaDiscoveryConfigBlueprint.create()</code></p></td>
<td style="text-align: left;"><p>The CacheConfig to use controlling how
a local cache of Eureka server information is used.</p>
<p>See CacheConfig</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>client</code></p></td>
<td style="text-align: left;"><p>Http1Client</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>The Http1Client to use to communicate
with the Eureka server. To be useful, the client must have a
io.helidon.webclient.http1.Http1ClientConfig prototype whose
io.helidon.webclient.http1.Http1ClientConfig.Builder.baseUri(io.helidon.webclient.api.ClientUri)
property is set to the endpoint of a Eureka Server instance. Often this
value will be something like {@code <a
href="http://example.com:8761/eureka}">http://example.com:8761/eureka}</a>.</p>
<p>See Http1Client</p>
<p>See
io.helidon.webclient.http1.Http1ClientConfig.Builder.baseUri(io.helidon.webclient.api.ClientUri)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>prefer-ip-address</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Whether the &lt;dfn&gt;host&lt;/dfn&gt;
component of any java.net.URI URI should be set to the IP address stored
by Eureka, or the hostname; <code>false</code> by default.</p></td>
</tr>
</tbody>
</table>
