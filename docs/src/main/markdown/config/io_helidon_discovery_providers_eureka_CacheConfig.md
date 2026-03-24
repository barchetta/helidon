# CacheConfig (discovery.providers.eureka) Configuration

Type: [io.helidon.discovery.providers.eureka.CacheConfig](/apidocs/io.helidon.discovery.providers.eureka/io/helidon/discovery/providers/eureka/CacheConfig.html)

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
<td style="text-align: left;"><p><code>compute-changes</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Whether the state of the cache should be computed from changes reported by Eureka, or replaced in full; <code>true</code> by default.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>defer-sync</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>false</code></p></td>
<td style="text-align: left;"><p>Whether to defer immediate cache synchronization; <code>false</code> by default.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>enabled</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Whether a local cache of Eureka information is used or not; <code>true</code> by default.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>fetch-thread-name</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p><code>Eureka registry fetch thread</code></p></td>
<td style="text-align: left;"><p>The name of the Thread used to retrieve service information from the Eureka server; "Eureka registry fetch thread" by default.</p>
<p>See Thread.Builder.name(String)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>sync-interval</code></p></td>
<td style="text-align: left;"><p>Duration</p></td>
<td style="text-align: left;"><p><code>PT30S</code></p></td>
<td style="text-align: left;"><p>The time between retrievals of service information from the Eureka server; 30 seconds by default.</p>
<p>See Duration.parse(CharSequence)</p></td>
</tr>
</tbody>
</table>
