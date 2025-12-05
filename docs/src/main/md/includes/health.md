# Built-In Health Checks

You can use Helidon-provided health checks to report various common
health check statuses:

<table style="width:100%;">
<colgroup>
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 13%" />
<col style="width: 65%" />
<col style="width: 13%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Built-in health check</th>
<th style="text-align: left;">Health check name</th>
<th style="text-align: left;">JavaDoc</th>
<th style="text-align: left;">Config properties (within
<code>server.features.observe.observers.health</code>)</th>
<th style="text-align: left;">Default config value</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>deadlock detection †</p></td>
<td style="text-align: left;"><p><code>deadlock</code></p></td>
<td style="text-align: left;"><p><a
href="{health-javadoc-base-url}/io/helidon/health/checks/DeadlockHealthCheck.html"><code>DeadlockHealthCheck</code></a></p></td>
<td style="text-align: left;"><p>n/a</p></td>
<td style="text-align: left;"><p>n/a</p></td>
</tr>
<tr>
<td rowspan="2" style="text-align: left;"><p>available disk space
†</p></td>
<td rowspan="2"
style="text-align: left;"><p><code>diskSpace</code></p></td>
<td rowspan="2" style="text-align: left;"><p><a
href="{health-javadoc-base-url}/io/helidon/health/checks/DiskSpaceHealthCheck.html"><code>DiskSpaceHealthCheck</code></a></p></td>
<td
style="text-align: left;"><p><code>helidon.health.diskSpace.thresholdPercent</code></p></td>
<td style="text-align: left;"><p><code>99.999</code></p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>helidon.health.diskSpace.path</code></p></td>
<td style="text-align: left;"><p><code>/</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>available heap memory</p></td>
<td style="text-align: left;"><p><code>heapMemory</code></p></td>
<td style="text-align: left;"><p><a
href="{health-javadoc-base-url}/io/helidon/health/checks/HeapMemoryHealthCheck.html"><code>HeapMemoryHealthCheck</code></a></p></td>
<td
style="text-align: left;"><p><code>helidon.health.heapMemory.thresholdPercent</code></p></td>
<td style="text-align: left;"><p><code>98</code></p></td>
</tr>
</tbody>
</table>

† Helidon cannot support the indicated health checks in the GraalVM
native image environment, so with native image those health checks do
not appear in the health output.

Simply adding the built-in health check dependency is sufficient to
register all the built-in health checks automatically. If you want to
use only some of the built-in checks in your application, you can
disable automatic discovery of the built-in health checks and register
only the ones you want.

Further, you can suppress one or more health checks by setting the
configuration item `server.features.observe.observers.health.exclude` to
a comma-separated list of the health check names you want to exclude.
