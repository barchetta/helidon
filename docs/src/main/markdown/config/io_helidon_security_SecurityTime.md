# SecurityTime (security) Configuration

Type: [io.helidon.security.SecurityTime](/apidocs/io.helidon.security/io/helidon/security/SecurityTime.html)

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
<td style="text-align: left;"><p><code>day-of-month</code></p></td>
<td style="text-align: left;"><p>long</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Set an explicit value for one of the time fields (such as ChronoField.YEAR).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>hour-of-day</code></p></td>
<td style="text-align: left;"><p>long</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Set an explicit value for one of the time fields (such as ChronoField.YEAR).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>millisecond</code></p></td>
<td style="text-align: left;"><p>long</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Set an explicit value for one of the time fields (such as ChronoField.YEAR).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>minute</code></p></td>
<td style="text-align: left;"><p>long</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Set an explicit value for one of the time fields (such as ChronoField.YEAR).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>month</code></p></td>
<td style="text-align: left;"><p>long</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Set an explicit value for one of the time fields (such as ChronoField.YEAR).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>second</code></p></td>
<td style="text-align: left;"><p>long</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Set an explicit value for one of the time fields (such as ChronoField.YEAR).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>shift-by-seconds</code></p></td>
<td style="text-align: left;"><p>long</p></td>
<td style="text-align: left;"><p><code>0</code></p></td>
<td style="text-align: left;"><p>Configure a time-shift in seconds, to move the current time to past or future.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>time-zone</code></p></td>
<td style="text-align: left;"><p>ZoneId</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Override current time zone. The time will represent the SAME instant, in an explicit timezone.</p>
<p>If we are in a UTC time zone and you set the timezone to "Europe/Prague", the time will be shifted by the offset of Prague (e.g. if it is noon right now in UTC, you would get 14:00).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>year</code></p></td>
<td style="text-align: left;"><p>long</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Set an explicit value for one of the time fields (such as ChronoField.YEAR).</p></td>
</tr>
</tbody>
</table>
