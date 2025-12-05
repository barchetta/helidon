Type:
[io.helidon.common.configurable.ThreadPoolSupplier](/apidocs/io.helidon.common.configurable/io/helidon/common/configurable/ThreadPoolSupplier.html)

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
<td style="text-align: left;"><p><code>core-pool-size</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p><code>10</code></p></td>
<td style="text-align: left;"><p>Core pool size of the thread pool
executor. Defaults to DEFAULT_CORE_POOL_SIZE.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>growth-rate</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p><code>0</code></p></td>
<td style="text-align: left;"><p>The percentage of task submissions that
should result in adding threads, expressed as a value from 1 to 100. The
rate applies only when all of the following are true:</p>
<ul>
<li><p>the pool size is below the maximum, and</p></li>
<li><p>there are no idle threads, and</p></li>
<li><p>the number of tasks in the queue exceeds the
<code>growthThreshold</code></p></li>
</ul>
<p>For example, a rate of 20 means that while these conditions are met
one thread will be added for every 5 submitted tasks.</p>
<p>Defaults to DEFAULT_GROWTH_RATE</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>growth-threshold</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p><code>1000</code></p></td>
<td style="text-align: left;"><p>The queue size above which pool growth
will be considered if the pool is not fixed size. Defaults to
DEFAULT_GROWTH_THRESHOLD.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>is-daemon</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Is daemon of the thread pool executor.
Defaults to DEFAULT_IS_DAEMON.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>keep-alive</code></p></td>
<td style="text-align: left;"><p>Duration</p></td>
<td style="text-align: left;"><p><code>PT3M</code></p></td>
<td style="text-align: left;"><p>Keep alive of the thread pool executor.
Defaults to DEFAULT_KEEP_ALIVE.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>max-pool-size</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p><code>50</code></p></td>
<td style="text-align: left;"><p>Max pool size of the thread pool
executor. Defaults to DEFAULT_MAX_POOL_SIZE.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Name of this thread pool
executor.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>queue-capacity</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p><code>10000</code></p></td>
<td style="text-align: left;"><p>Queue capacity of the thread pool
executor. Defaults to DEFAULT_QUEUE_CAPACITY.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>should-prestart</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Whether to prestart core threads in
this thread pool executor. Defaults to DEFAULT_PRESTART.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>thread-name-prefix</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Name prefix for threads in this thread
pool executor. Defaults to DEFAULT_THREAD_NAME_PREFIX.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>virtual-threads</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>When configured to <code>true</code>,
an unbounded virtual executor service (project Loom) will be used.</p>
<p>If enabled, all other configuration options of this executor service
are ignored!</p></td>
</tr>
</tbody>
</table>
