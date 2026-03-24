# Cron (scheduling) Configuration

Type: [io.helidon.scheduling.Cron](/apidocs/io.helidon.scheduling/io/helidon/scheduling/Cron.html)

## Configuration options

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
<td style="text-align: left;"><p>Cron expression for specifying period of execution.</p>
<p><strong>Examples:</strong></p>
<ul>
<li><p><code>0/2 * * * * ? *</code> - Every 2 seconds</p></li>
<li><p><code>0 45 9 ? * *</code> - Every day at 9:45</p></li>
<li><p><code>0 15 8 ? * MON-FRI</code> - Every workday at 8:15</p></li>
</ul></td>
</tr>
</tbody>
</table>

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
<td style="text-align: left;"><p><code>concurrent</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Allow concurrent execution if previous task didn’t finish before next execution. Default value is <code>true</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>enabled</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Whether the task is enabled. If disabled, the task will not be scheduled. Default value is <code>true</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>id</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Identification of the started task. This can be used to later look up the instance, for example to cancel it.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>zone</code></p></td>
<td style="text-align: left;"><p>ZoneId</p></td>
<td style="text-align: left;"><p><code>@java.time.ZoneId@.systemDefault()</code></p></td>
<td style="text-align: left;"><p>Time zone to use for cron expression evaluation. Defaults to java.time.ZoneId.systemDefault().</p>
<p>The time zone determines when the cron expression triggers. For example, a cron expression <code>0 0 9 * * ?</code> (every day at 9:00 AM) with zone <code>America/New_York</code> will trigger at 9:00 AM Eastern Time, regardless of the system’s default time zone.</p></td>
</tr>
</tbody>
</table>
