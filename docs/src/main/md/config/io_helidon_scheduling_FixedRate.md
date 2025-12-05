Type:
[io.helidon.scheduling.FixedRate](/apidocs/io.helidon.scheduling/io/helidon/scheduling/FixedRate.html)

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
<td style="text-align: left;"><p><span
class="line-through"><code>delay</code></span></p></td>
<td style="text-align: left;"><p>long</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p><strong>Deprecated</strong> Fixed rate
delay between each invocation. Time unit is by default
java.util.concurrent.TimeUnit.SECONDS, can be specified with
io.helidon.scheduling.FixedRateConfig.Builder.timeUnit(java.util.concurrent.TimeUnit).</p>
<p>@deprecated use io.helidon.scheduling.FixedRateConfig.interval()
instead</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><span
class="line-through"><code>initial-delay</code></span></p></td>
<td style="text-align: left;"><p>long</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p><strong>Deprecated</strong> Initial
delay of the first invocation. Time unit is by default
java.util.concurrent.TimeUnit.SECONDS, can be specified with
io.helidon.scheduling.FixedRateConfig.Builder.timeUnit(java.util.concurrent.TimeUnit)
timeUnit().</p>
<p>@deprecated use io.helidon.scheduling.FixedRateConfig.delayBy()
instead</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>interval</code></p></td>
<td style="text-align: left;"><p>Duration</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Fixed interval between each
invocation.</p></td>
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
<td style="text-align: left;"><p><code>delay-by</code></p></td>
<td style="text-align: left;"><p>Duration</p></td>
<td style="text-align: left;"><p><code>PT0S</code></p></td>
<td style="text-align: left;"><p>Initial delay of the first
invocation.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>delay-type</code></p></td>
<td style="text-align: left;"><p>DelayType (SINCE_PREVIOUS_START,
SINCE_PREVIOUS_END)</p></td>
<td
style="text-align: left;"><p><code>DelayType.SINCE_PREVIOUS_START</code></p></td>
<td style="text-align: left;"><p>Configure whether the interval between
the invocations should be calculated from the time when previous task
started or ended. Delay type is by default
FixedRate.DelayType.SINCE_PREVIOUS_START.</p>
<p>Allowed values:</p>
<ul>
<li><p><code>SINCE_PREVIOUS_START</code>: Next invocation start is
measured from the previous invocation task start.</p></li>
<li><p><code>SINCE_PREVIOUS_END</code>: Next invocation start is
measured from the previous invocation task end.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>id</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Identification of the started task.
This can be used to later look up the instance, for example to cancel
it.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><span
class="line-through"><code>time-unit</code></span></p></td>
<td style="text-align: left;"><p>TimeUnit (NANOSECONDS, MICROSECONDS,
MILLISECONDS, SECONDS, MINUTES, HOURS, DAYS)</p></td>
<td
style="text-align: left;"><p><code>TimeUnit.TimeUnit.SECONDS</code></p></td>
<td style="text-align: left;"><p><strong>Deprecated</strong>
java.util.concurrent.TimeUnit TimeUnit used for interpretation of values
provided with io.helidon.scheduling.FixedRateConfig.Builder.delay(long)
and
io.helidon.scheduling.FixedRateConfig.Builder.initialDelay(long).</p>
<p>@deprecated as duration is used for new options, this option is not
needed</p></td>
</tr>
</tbody>
</table>
