Type:
[io.helidon.webserver.observe.config.ConfigObserver](/apidocs/io.helidon.webserver.observe.config/io/helidon/webserver/observe/config/ConfigObserver.html)

<div class="formalpara">

<div class="title">

Config key

</div>

``` text
config
```

</div>

This type provides the following service implementations:

- `io.helidon.webserver.observe.spi.ObserveProvider`

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
<td style="text-align: left;"><p><code>endpoint</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p><code>config</code></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>permit-all</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Permit all access, even when not
authorized.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>secrets</code></p></td>
<td style="text-align: left;"><p>string[]</p></td>
<td
style="text-align: left;"><p><code>.*password, .*passphrase, .*secret</code></p></td>
<td style="text-align: left;"><p>Secret patterns (regular expressions)
to exclude from output. Any pattern that matches a key will cause the
output to be obfuscated and not contain the value.</p>
<p>Patterns always added:</p>
<ul>
<li><p><code>.*password</code></p></li>
<li><p><code>.*passphrase</code></p></li>
<li><p><code>.*secret</code></p></li>
</ul></td>
</tr>
</tbody>
</table>
