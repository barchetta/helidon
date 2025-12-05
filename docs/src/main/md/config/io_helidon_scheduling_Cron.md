Type:
[io.helidon.scheduling.Cron](/apidocs/io.helidon.scheduling/io/helidon/scheduling/Cron.html)

# Configuration options

<table style="width:100%;">
<caption>Required configuration options</caption>
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
<td style="text-align: left;"><p><code>expression</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Cron expression for specifying period
of execution.</p>
<p><strong>Examples:</strong></p>
<ul>
<li><p><code>0/2 * * * * ? *</code> - Every 2 seconds</p></li>
<li><p><code>0 45 9 ? * *</code> - Every day at 9:45</p></li>
<li><p><code>0 15 8 ? * MON-FRI</code> - Every workday at 8:15</p></li>
</ul></td>
</tr>
</tbody>
</table>

| key | type | default value | description |
|----|----|----|----|
| `concurrent` | boolean | `true` | Allow concurrent execution if previous task didn’t finish before next execution. Default value is `true`. |
| `id` | string |   | Identification of the started task. This can be used to later look up the instance, for example to cancel it. |

Optional configuration options
