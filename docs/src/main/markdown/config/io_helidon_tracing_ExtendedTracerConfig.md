# ExtendedTracerConfig (tracing) Configuration

Type: [io.helidon.tracing.ExtendedTracerConfig](/apidocs/io.helidon.tracing/io/helidon/tracing/ExtendedTracerConfig.html)

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
<td style="text-align: left;"><p><code>boolean-tags</code></p></td>
<td style="text-align: left;"><p>Map&lt;string, boolean&gt;</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Tracer-level tags with boolean values added to all reported spans.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>client-cert-pem</code></p></td>
<td style="text-align: left;"><p><a href="../config/../config/io_helidon_common_configurable_Resource.xml">Resource</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Client certificate for connecting securely to the tracing collector.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>enabled</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Whether to enable tracing. That is, whether to use a fully-featured tracing implementation on the path vs. a no-op implementation.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>export-timeout</code></p></td>
<td style="text-align: left;"><p>Duration</p></td>
<td style="text-align: left;"><p><code>PT10S</code></p></td>
<td style="text-align: left;"><p>Maximum time a transmission can be in progress before being cancelled.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>global</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Whether to create and register a tracer as the global tracer.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>host</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Host used in connecting to the tracing collector.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>int-tags</code></p></td>
<td style="text-align: left;"><p>Map&lt;string, int&gt;</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Tracer level tags with integer values added to all reported spans.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>max-export-batch-size</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p><code>512</code></p></td>
<td style="text-align: left;"><p>Maximum number of spans grouped for transmission together; typically does not exceed maxQueueSize() (batch processing).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>max-queue-size</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p><code>2048</code></p></td>
<td style="text-align: left;"><p>Maximum number of spans retained before discarding any not sent to the tracing collector (batch processing).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>path</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Path at the collector host and port used when sending trace data to the collector.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>port</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Port used in connecting to the tracing collector.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>private-key-pem</code></p></td>
<td style="text-align: left;"><p><a href="../config/../config/io_helidon_common_configurable_Resource.xml">Resource</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Private key for connecting securely to the tracing collector.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>protocol</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Protocol (such as <code>http</code> or <code>https</code>) used in connecting to the tracing collector.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>sampler-param</code></p></td>
<td style="text-align: left;"><p>double</p></td>
<td style="text-align: left;"><p><code>1.0</code></p></td>
<td style="text-align: left;"><p>Parameter value used by the selected sampler; interpretation depends on the sampler type..</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>sampler-type</code></p></td>
<td style="text-align: left;"><p>SamplerType (CONSTANT, RATIO)</p></td>
<td style="text-align: left;"><p><code>SamplerType.CONSTANT</code></p></td>
<td style="text-align: left;"><p>Type of sampler for collecting spans.</p>
<p>Allowed values:</p>
<ul>
<li><p><code>CONSTANT</code>: Sampling of every span.</p></li>
<li><p><code>RATIO</code>: Sampling of a proportion [0.0, 1.0] of spans.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>schedule-delay</code></p></td>
<td style="text-align: left;"><p>Duration</p></td>
<td style="text-align: left;"><p><code>PT5S</code></p></td>
<td style="text-align: left;"><p>Delay between consecutive transmissions to the tracing collector (batch processing).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>service</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Service name of the traced service.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>span-processor-type</code></p></td>
<td style="text-align: left;"><p>SpanProcessorType (SIMPLE, BATCH)</p></td>
<td style="text-align: left;"><p><code>SpanProcessorType.BATCH</code></p></td>
<td style="text-align: left;"><p>Type of span processor for accumulating spans before transmission to the tracing collector.</p>
<p>Allowed values:</p>
<ul>
<li><p><code>SIMPLE</code>: Simple Span Processor.</p></li>
<li><p><code>BATCH</code>: Batch Span Processor.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>tags</code></p></td>
<td style="text-align: left;"><p>Map&lt;string, string&gt;</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Tracer-level tags with <code>String</code> values added to all reported spans.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>trusted-cert-pem</code></p></td>
<td style="text-align: left;"><p><a href="../config/../config/io_helidon_common_configurable_Resource.xml">Resource</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Trusted certificates for connecting to the tracing collector.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>uri</code></p></td>
<td style="text-align: left;"><p>URI</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>URI for the collector to which to send tracing data.</p></td>
</tr>
</tbody>
</table>
