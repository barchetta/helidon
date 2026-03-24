# Tracer (tracing) Configuration

Jaeger tracer configuration.

Type: [io.helidon.tracing.Tracer](/apidocs/io.helidon.tracing/io/helidon/tracing/Tracer.html)

This is a standalone configuration type, prefix from configuration root: `tracing`

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
<td style="text-align: left;"><p><code>client-cert-pem</code></p></td>
<td style="text-align: left;"><p><a href="../config/../config/io_helidon_common_configurable_Resource.xml">Resource</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Certificate of client in PEM format.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>exporter-timeout</code></p></td>
<td style="text-align: left;"><p>Duration</p></td>
<td style="text-align: left;"><p><code>PT10S</code></p></td>
<td style="text-align: left;"><p>Timeout of exporter requests.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>max-export-batch-size</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p><code>512</code></p></td>
<td style="text-align: left;"><p>Maximum Export Batch Size of exporter requests.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>max-queue-size</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p><code>2048</code></p></td>
<td style="text-align: left;"><p>Maximum Queue Size of exporter requests.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>private-key-pem</code></p></td>
<td style="text-align: left;"><p><a href="../config/../config/io_helidon_common_configurable_Resource.xml">Resource</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Private key in PEM format.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>propagation</code></p></td>
<td style="text-align: left;"><p>JaegerTracerBuilder.PropagationFormat[] (B3, B3_SINGLE, JAEGER, W3C)</p></td>
<td style="text-align: left;"><p><code>JAEGER</code></p></td>
<td style="text-align: left;"><p>Add propagation format to use.</p>
<p>Allowed values:</p>
<ul>
<li><p><code>B3</code>: The Zipkin B3 trace context propagation format using multiple headers.</p></li>
<li><p><code>B3_SINGLE</code>: B3 trace context propagation using a single header.</p></li>
<li><p><code>JAEGER</code>: The Jaeger trace context propagation format.</p></li>
<li><p><code>W3C</code>: The W3C trace context propagation format.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>sampler-param</code></p></td>
<td style="text-align: left;"><p>Number</p></td>
<td style="text-align: left;"><p><code>1</code></p></td>
<td style="text-align: left;"><p>The sampler parameter (number).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>sampler-type</code></p></td>
<td style="text-align: left;"><p>JaegerTracerBuilder.SamplerType (CONSTANT, RATIO)</p></td>
<td style="text-align: left;"><p><code>CONSTANT</code></p></td>
<td style="text-align: left;"><p>Sampler type.</p>
<p>See <a href="https://www.jaegertracing.io/docs/latest/sampling/#client-sampling-configuration">Sampler types</a>.</p>
<p>Allowed values:</p>
<ul>
<li><p><code>CONSTANT</code>: Constant sampler always makes the same decision for all traces. It either samples all traces <code>1</code> or none of them <code>0</code>.</p></li>
<li><p><code>RATIO</code>: Ratio of the requests to sample, double value.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>schedule-delay</code></p></td>
<td style="text-align: left;"><p>Duration</p></td>
<td style="text-align: left;"><p><code>PT5S</code></p></td>
<td style="text-align: left;"><p>Schedule Delay of exporter requests.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>span-processor-type</code></p></td>
<td style="text-align: left;"><p>JaegerTracerBuilder.SpanProcessorType (SIMPLE, BATCH)</p></td>
<td style="text-align: left;"><p><code>batch</code></p></td>
<td style="text-align: left;"><p>Span Processor type used.</p>
<p>Allowed values:</p>
<ul>
<li><p><code>SIMPLE</code>: Simple Span Processor.</p></li>
<li><p><code>BATCH</code>: Batch Span Processor.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>trusted-cert-pem</code></p></td>
<td style="text-align: left;"><p><a href="../config/../config/io_helidon_common_configurable_Resource.xml">Resource</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Trusted certificates in PEM format.</p></td>
</tr>
</tbody>
</table>
