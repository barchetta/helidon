Type:
[io.helidon.webserver.security.SecurityFeature](/apidocs/io.helidon.webserver.security/io/helidon/webserver/security/SecurityFeature.html)

<div class="formalpara">

<div class="title">

Config key

</div>

``` text
security
```

</div>

This type provides the following service implementations:

- `io.helidon.webserver.spi.ServerFeatureProvider`

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
<td style="text-align: left;"><p><code>defaults</code></p></td>
<td style="text-align: left;"><p><a
href="../config/io_helidon_webserver_security_SecurityHandler.xml">SecurityHandler</a></p></td>
<td
style="text-align: left;"><p><code>SecurityHandler.create()</code></p></td>
<td style="text-align: left;"><p>The default security handler.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>paths</code></p></td>
<td style="text-align: left;"><p><a
href="../config/io_helidon_webserver_security_PathsConfig.xml">PathsConfig[]</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Configuration for webserver
paths.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>security</code></p></td>
<td style="text-align: left;"><p><a
href="../config/io_helidon_security_Security.xml">Security</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Security associated with this feature.
If not specified here, the feature uses security registered with
io.helidon.common.context.Contexts.globalContext(), if not found, it
creates a new instance from root of configuration (using
<code>security</code> key).</p>
<p>This configuration allows usage of a different security instance for
a specific security feature setup.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>weight</code></p></td>
<td style="text-align: left;"><p>double</p></td>
<td style="text-align: left;"><p><code>800.0</code></p></td>
<td style="text-align: left;"><p>Weight of the security feature. Value
is: io.helidon.webserver.security.SecurityFeature.WEIGHT.</p></td>
</tr>
</tbody>
</table>
