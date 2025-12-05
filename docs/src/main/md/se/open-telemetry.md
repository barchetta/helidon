# Overview

> [!NOTE]
> Helidon SE support for OpenTelemetry configuration and semantic
> conventions as described below is currently an [incubating
> feature](/apidocs/io.helidon.common.features.api/io/helidon/common/features/api/Incubating.html).
> We intend to support it going forward, but we might withdraw the
> feature entirely or change its external API and behavior in
> backward-incompatible ways across dot releases.

Helidon SE supports OpenTelemetry in several important ways:

- Implements the [neutral Helidon tracing
  API](tracing.md)
  using OpenTelemetry

- Allows users to assign OpenTelemetry settings as follows:

  - Declaratively, using Helidon config under the top-level `telemetry`
    config key

  - Programmatically, using the OpenTelemetry SDK API and the Helidon
    OpenTelemetry API

- Conforms to the [OpenTelemetry semantic
  conventions](https://github.com/open-telemetry/semantic-conventions/blob/v1.29.0/docs/http/http-spans.md#http-server)
  for automatically-created spans

OpenTelemetry models observability as a set of
[*signals*](https://opentelemetry.io/docs/concepts/signals/). Each
signal—​for example metrics, tracing, and logging—​is an origin of
monitoring data, and each has configurable settings which control its
behavior.

Helidon’s config support for OpenTelemetry has certain config attributes
which apply to OpenTelemetry as a whole, others which pertain to
individual signals, and still more which describe lower-level elements
within a signal.

The Helidon OpenTelemetry configuration format, the Helidon
OpenTelemetry API, and this documentation all follow this hierarchy:

- [Top-level telemetry](#top-level-config)

  - Signals

    - [Tracing](#tracing-config)

      - [Attributes](#attributes-config)

      - [Span exporters](#span-exporters-config)

      - [Span processors](#span-processors-config)

      - [Span sampler](#span-sampler-config)

      - [Span limits](#span-limits-config)

This document describes how to configure each level in the hierarchy and
covers general topics related to Helidon’s support of OpenTelemetry.

# API

There are *two* APIs that might be useful to developers working with
OpenTelemetry:

- The Helidon OpenTelemetry API - useful for mapping configuration
  sources to Helidon builders and, ultimately, OpenTelemetry objects.

- The OpenTelemetry API - useful for creating OpenTelemetry objects
  apart from Helidon configuration sources.

The types of the Helidon OpenTelemetry API correspond closely to the
configuration structures described in later sections of this document.
Application code can use Helidon OpenTelemetry builders to prepare and
construct each of the configurable entities to ultimately prepare an
`OpenTelemetry` instance set up according to the application’s needs.

That said, application code can equally well use the OpenTelemetry API
and its builders to prepare the `OpenTelemetry` instance.

Applications could even use both APIs together, reading configuration to
construct a Helidon builder and then adding to that builder
OpenTelemetry objects created separately using the OpenTelemetry API.

The [Helidon OpenTelemetry API
Javadoc](/apidocs/io.helidon.telemetry.otelconfig/io/helidon/telemetry/otelconfig/package-summary.html)
page lists the various types developers can use to prepare OpenTelemetry
objects programmatically. As a starting point, the
[`OpenTelemetryConfig`](/apidocs/io.helidon.telemetry.otelconfig/io/helidon/telemetry/otelconfig/OpenTelemetryConfig.html)
interface and its
[`Builder`](/apidocs/io.helidon.telemetry.otelconfig/io/helidon/telemetry/otelconfig/OpenTelemetryConfig.BuilderBase.html)
represents the top-level configuration for OpenTelemetry. Their Javadoc
contains links to other types that compose the top-level object, and so
on.

Later sections in this document also describe the configuration settings
available.

The [OpenTelemetry SDK
documentation](https://opentelemetry.io/docs/languages/java/sdk/#sdk-components)
explains its API.

> [!NOTE]
> Many applications do not need to use either the Helidon OpenTelemetry
> API or the OpenTelemetry API directly. They can instead rely
> completely on declarative Helidon configuration of OpenTelemetry.

## Managing the Global `OpenTelemetry` Instance

Typically, an application uses the same `OpenTelemetry` instance
throughout its execution. OpenTelemetry offers a global `OpenTelemetry`
instance to make it easy for application code to set and obtain the
global instance.

Similarly, the Helidon tracing API has a global `Tracer`.

In most cases, an application that prepares OpenTelemetry
programmatically should initialize both of those by including code as
shown in the following example.

<div class="formalpara">

<div class="title">

Setting the global `OpenTelemetry` and `Tracer` instances in Helidon

</div>

``` java
import java.util.Map;
import io.helidon.telemetry.otelconfig.HelidonOpenTelemetry;
import io.opentelemetry.api.OpenTelemetry;

        // Application code using the OpenTelemetry API or the Helidon OpenTelemetry API or both.
        OpenTelemetry customOpenTelemetry = prepareOpenTelemetry();

        // App code to build any tags to be applied to every span.
        Map<String, String> tags = prepareTags();

        HelidonOpenTelemetry.global(customOpenTelemetry,
                                    "your-service-name",
                                    tags);
```

</div>

### Assigning the Global Instance

Using Helidon to set the global `OpenTelemetry` instance has these
effects:

- Assigns the instance as the OpenTelemetry global instance.

- Creates a Helidon `Tracer` using the OpenTelemetry instance and makes
  that the Helidon global `Tracer`.

# Maven Coordinates

To enable various aspects of OpenTelemetry Support add one or more of
the following dependencies to your project’s `pom.xml` (see [Managing
Dependencies](../about/managing-dependencies.md)).

## Using the OpenTelemetry implementation of the Helidon Tracing API

Helidon offers an implementation of its [ neutral tracing
API](tracing.md) that uses OpenTelemetry. Add the following dependency
to use OpenTelemetry for tracing.

<div class="formalpara">

<div class="title">

Dependency to use the Helidon OpenTelemetry implementation of Helidon
tracing

</div>

``` xml
<dependency>
    <groupId>io.helidon.tracing.providers</groupId>
    <artifactId>helidon-tracing-providers-opentelemetry</artifactId>
    <scope>runtime</scope>
</dependency>
```

</div>

## Adding OpenTelemetry Configuration and Builder Support

To allow deployers and end users to set up Helidon configuration to
control OpenTelemetry behavior, add the following dependency.

<div class="formalpara">

<div class="title">

Dependency to add Helidon OpenTelemetry config and programmatic builder
support

</div>

``` xml
<dependency>
    <groupId>io.helidon.telemetry</groupId>
    <artifactId>helidon-telemetry-opentelemetry-config</artifactId>
    <scope>runtime</scope> 
</dependency>
```

</div>

- To use the Helidon OpenTelemetry API in your application code, remove
  this line or change it to `<scope>compile</scope>`.

## Enabling Automatic Spans for HTTP Requests

Helidon’s tracing observability support automatically creates a new
tracing span for each HTTP request if your project includes the
following dependency.

<div class="formalpara">

<div class="title">

Dependency for automatic HTTP request tracing

</div>

``` xml
<dependency>
    <groupId>io.helidon.webserver.observe</groupId>
    <artifactId>helidon-webserver-observe-tracing</artifactId>
    <scope>runtime</scope>
</dependency>
```

</div>

By default, when Helidon SE creates spans automatically for HTTP
requests, it uses a set of rules—​semantic conventions—​for choosing the
span name and adding tags to each span.

OpenTelemetry prescribes its own [semantic
conventions](https://github.com/open-telemetry/semantic-conventions/blob/v1.29.0/docs/http/http-spans.md#http-server).
If you add the following dependency, Helidon follows the OpenTelemetry
semantic conventions for spans instead of its own.

<div class="formalpara">

<div class="title">

Dependency for Helidon support of the OpenTelemetry semantic conventions

</div>

``` xml
<dependency>
    <groupId>io.helidon.webserver.observe</groupId>
    <artifactId>helidon-webserver-observe-telemetry-tracing</artifactId>
    <scope>runtime</scope>
</dependency>
```

</div>

## Specifying Additional OpenTelemetry Dependencies

Most applications need to declare other runtime dependencies on
OpenTelemetry artifacts because the configuration specifies—​or the
application code uses—​particular OpenTelemetry types packaged in other
artifacts. For example, OpenTelemetry packages various span exporters
individually. (See [this OpenTelemetry
page](https://github.com/open-telemetry/opentelemetry-java/tree/v1.29.0/exporters)
on span exporters in particular.)

# Configuration

You can control almost all of OpenTelemetry’s overall and tracing
runtime behavior using Helidon configuration settings. Helidon
constructs an `OpenTelemetry` object using the configuration. The
resulting `OpenTelemetry` instance includes an OpenTelemetry
`TracerProvider` if the config specifies settings for it under
`signals.tracing`.

## Controlling Overall OpenTelemetry Behavior

Several settings control the operation of OpenTelemetry as a whole, as
shown in the next table.

Type:
[io.helidon.telemetry.otelconfig.HelidonOpenTelemetry](/apidocs/io.helidon.telemetry.otelconfig/io/helidon/telemetry/otelconfig/HelidonOpenTelemetry.html)

This is a standalone configuration type, prefix from configuration root:
`telemetry`

## Configuration options

| key | type | default value | description |
|----|----|----|----|
| `service` | string |   | Service name used in sending telemetry data to the collector. |

Required configuration options

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
<td style="text-align: left;"><p><code>enabled</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Whether the OpenTelemetry support is
enabled.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>global</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Whether the
io.opentelemetry.api.OpenTelemetry instance created from this
configuration should be made the global one.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>propagators</code></p></td>
<td style="text-align: left;"><p>TextMapPropagator[]</p></td>
<td
style="text-align: left;"><p><code>new java.util.ArrayList&lt;&gt;(io.helidon.telemetry.otelconfig.ContextPropagationType.DEFAULT_PROPAGATORS)</code></p></td>
<td style="text-align: left;"><p>OpenTelemetry
io.opentelemetry.context.propagation.TextMapPropagator instances added
explicitly by the app.</p>
<p>Default: ContextPropagationType.DEFAULT_NAMES. See
io.helidon.telemetry.otelconfig.ContextPropagationType</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>signals.tracing</code></p></td>
<td style="text-align: left;"><p><a
href="../config/io_helidon_telemetry_otelconfig_OpenTelemetryTracingConfig.xml">OpenTelemetryTracingConfig</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>OpenTelemetry tracing
settings.</p></td>
</tr>
</tbody>
</table>

Notes:

- OpenTelemetry uses default propagators of `tracecontext` and
  `baggage`. (See the `otel.propagators` property in [this OpenTelemetry
  guide](https://opentelemetry.io/docs/languages/java/configuration/#properties-general).)

- Setting `global` to `true` has the effect described in the
  [section](#effects-of-setting-global) about global instances.

## Controlling OpenTelemetry Tracing Behavior

The settings under `settings.tracing` prepare an OpenTelemetry
`TracerProvider`. When your application uses the Helidon tracing API to
obtain a `Tracer`, Helidon uses the `TracerProvider` prepared from this
config to create the tracer.

The next table describes the OpenTelemetry tracing settings.

Type:
[io.helidon.telemetry.otelconfig.OpenTelemetryTracingConfig](/apidocs/io.helidon.telemetry.otelconfig/io/helidon/telemetry/otelconfig/OpenTelemetryTracingConfig.html)

### Configuration options

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
<td
style="text-align: left;"><p><code>attributes.booleans</code></p></td>
<td style="text-align: left;"><p>Map&lt;string, boolean&gt;</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Boolean attributes.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>attributes.doubles</code></p></td>
<td style="text-align: left;"><p>Map&lt;string, double&gt;</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Double attributes.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>attributes.longs</code></p></td>
<td style="text-align: left;"><p>Map&lt;string, long&gt;</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Long attributes.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>attributes.strings</code></p></td>
<td style="text-align: left;"><p>Map&lt;string, string&gt;</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>String attributes.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>exporters</code></p></td>
<td style="text-align: left;"><p>Map&lt;string,
SpanExporter&gt;</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Span exporters.</p>
<p>The key in the map is a unique name—​of the user’s choice—​for the
exporter config settings. The SpanProcessorConfig.exporters() config
setting for a processor config specifies zero or more of these names to
associate the exporters built from the exporter configs with the
processor built from the processor config.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>processors</code></p></td>
<td style="text-align: left;"><p><a
href="../config/io_helidon_telemetry_otelconfig_SpanProcessorConfig.xml">SpanProcessorConfig[]</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Settings for span processors.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>sampler</code></p></td>
<td style="text-align: left;"><p>Sampler</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Tracing sampler.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>span-limits</code></p></td>
<td style="text-align: left;"><p>SpanLimits</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Tracing span limits.</p></td>
</tr>
</tbody>
</table>

OpenTelemetry applies the defaults described in the next table.

| Setting | OpenTelemetry default (and OpenTelemetry doc link) |
|----|----|
| `exporters` | [`otlp` with `grpc` protocol](https://opentelemetry.io/docs/languages/java/configuration/#properties-exporters) - see "Properties: exporters, `otel.traces.exporter` property" |
| `processors` | [`batch` with defaults](https://opentelemetry.io/docs/languages/java/configuration/#properties-traces) - see "Properties for batch span processor(s)" |
| `sampler` | [`parentbased_always_on`](https://opentelemetry.io/docs/languages/java/configuration/#properties-traces) - see "Properties for sampler" |
| `span-limits` | See [tracing](https://opentelemetry.io/docs/languages/java/configuration/#properties-traces) "Properties for span limits" |

Default tracing settings applied by OpenTelemetry

Sections below describe how to set up the tracing signal configuration:

- [Assigning attributes](#attributes-config)

- [Associating Exporters and
  Processors](#associating-exporters-and-processors)

- [Configuring Span Exporters](#span-exporters-config)

- [Configuring Span Processors](#span-processors-config)

- [Configuring the Span Sampler](#span-sampler-config)

- [Configuring the Span Limits](#span-limits-config)

### Assigning Attributes

Configured attributes are key/value pairs that OpenTelemetry attaches to
each tracing span. OpenTelemetry supports attributes of type `String`,
`long`, `double`, and `boolean`. The configuration stricture groups
attributes by type so Helidon knows precisely what type you intend for
each attribute.

### Associating Exporters and Processors

Ultimately, OpenTelemetry transmits the telemetry data it gathers to a
backend system—​such as Grafana, Prometheus, Jaeger, or others—​where you
can view and query the data. OpenTelemetry tracing first *processes*
each data observation within the JVM and then *exports* the processed
data to one or more backends. Each span processor uses one or more span
exporters to transmit telemetry data.

You link processors and exporters in config selectively as follows:

- Name each exporter if you have more than one.

- List, for each processor, the names of exporters it should use.
  Omitting a processor’s list of exporter names causes the processor to
  use all configured exporters.

The following examples show increasingly-complicated scenarios:

- Default

- Minimal configuration

- Maximum flexibility

For many applications the default and minimal scenarios work well.

#### Default

This scenario includes no configuration at all for either processors or
exporters.

OpenTelemetry uses its default processor (`batch`) with its default
exporter (`otlp` using `grpc`). \|

``` yaml
telemetry:
  service: "inventory"
  tracing:
    sampler: "always_off"
```

#### Minimal configuration

The user configures at most one processor and at most one exporter.

The single processor uses the single exporter.

No exporter name is declared or referenced.

``` yaml
telemetry:
  service: "inventory"
  tracing:
    sampler: "always_off"
    exporters:
      - type: zipkin
        compression: gzip
    processors:
      - type: batch
        max-queue-size: 50
```

#### Maximum flexibility

The user configures possibly multiple processors and possibly multiple
named exporters. Each processor’s configuration lists the names of the
exporters it should use; no names means all exporters.

The first processor (type `batch`) uses both exporters because it does
not specify any exporter names. The second processor uses only the
`alternate-otlp` exporter.\|

``` yaml
telemetry:
  service: "inventory"
  tracing:
    sampler: "always_off"
    exporters:
      - type: zipkin
        compression: gzip
        name: "compressed-zipkin"
      - endpoint: "http://collect.com:4317"
        name: "alternate-otlp""
    processors:
      - type: batch
        max-queue-size: 50
      - type: simple
        exporters: ["alternate-otlp"]
```

### Configuring Span Processors

An OpenTelemetry span processor is one of the following types:

- simple - The processor sends each telemetry observation to its
  exporters for transmission as soon as it receives the observation.

- batch - The processor groups observations into batches and sends a
  batch at a time to its exporters for transmission.

In the table below only the `type` and `exporters` setting apply to
`simple` span processors; the other settings are for batch processors.

Type:
[io.helidon.telemetry.otelconfig.BatchSpanProcessorConfig](/apidocs/io.helidon.telemetry.otelconfig/io/helidon/telemetry/otelconfig/BatchSpanProcessorConfig.html)

#### Configuration options

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
<td style="text-align: left;"><p><code>type</code></p></td>
<td style="text-align: left;"><p>SpanProcessorType (SIMPLE,
BATCH)</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Span processor type.</p>
<p>Allowed values:</p>
<ul>
<li><p><code>SIMPLE</code>: Simple Span Processor.</p></li>
<li><p><code>BATCH</code>: Batch Span Processor.</p></li>
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
<td style="text-align: left;"><p><code>exporters</code></p></td>
<td style="text-align: left;"><p>string[]</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Name(s) of the span exporter(s) this
span processor should use; specifying no names uses all configured
exporters (or if no exporters are configured, the default OpenTelemetry
exporter(s)).</p>
<p>Each name must be the name of one of the configured
OpenTelemetryTracingConfig.exporterConfigs().</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>max-export-batch-size</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Maximum number of spans batched for
export together. OpenTelemetry requires this value to not exceed the
maxQueueSize().</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>max-queue-size</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Maximum number of spans retained before
discarding excess unexported ones.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>schedule-delay</code></p></td>
<td style="text-align: left;"><p>Duration</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Delay between consecutive
exports.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>timeout</code></p></td>
<td style="text-align: left;"><p>Duration</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Maximum time an export can run before
being cancelled.</p></td>
</tr>
</tbody>
</table>

### Configuring Span Exporters

OpenTelemetry supports many types of exporters, each with its own
configurable settings. Helidon configuration supports several of the
most popular exporters, listed in the table below.

> [!NOTE]
> You need to add dependencies to your project for the exporters your
> application uses, even ones supported by Helidon config.

If you need to use an exporter that is *not* in the table:

- Add a dependency on the OpenTelemetry artifact that contains that
  exporter type.

- Add application code that prepares the exporter instance.

- Prepare the Helidon OpenTelemetry builders programmatically and add
  your exporter instance to the builder.

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 25%" />
<col style="width: 62%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Exporter type</th>
<th style="text-align: left;">OpenTelemetry Java Type</th>
<th style="text-align: left;">Dependency to add - see also the <a
href="https://opentelemetry.io/docs/languages/java/sdk/#spanexporter">OpenTelemetry
documentation</a></th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="2" style="text-align: left;"><p><a
href="#otlp-exporter-config"><code>otlp</code></a><br />
(see <code>protocol</code> setting below)</p></td>
<td
style="text-align: left;"><p><code>OtlpGrpcSpanExporter</code></p></td>
<td rowspan="2" style="text-align: left;"><div class="sourceCode"
id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">dependency</span>&gt;</span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">groupId</span>&gt;io.opentelemetry&lt;/<span class="kw">groupId</span>&gt;</span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">artifactId</span>&gt;opentelemetry-exporter-otlp&lt;/<span class="kw">artifactId</span>&gt;</span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">dependency</span>&gt;</span></code></pre></div></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>OtlpHttpSpanExporter</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><a
href="#zipkin-exporter-config"><code>zipkin</code></a></p></td>
<td
style="text-align: left;"><p><code>ZipkinSpanExporter</code></p></td>
<td style="text-align: left;"><div class="sourceCode" id="cb2"><pre
class="sourceCode xml"><code class="sourceCode xml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">dependency</span>&gt;</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">groupId</span>&gt;io.opentelemetry&lt;/<span class="kw">groupId</span>&gt;</span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">artifactId</span>&gt;opentelemetry-exporter-zipkin&lt;/<span class="kw">artifactId</span>&gt;</span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">dependency</span>&gt;</span></code></pre></div></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>console</code></p></td>
<td
style="text-align: left;"><p><code>LoggingSpanExporter</code></p></td>
<td style="text-align: left;"><p>included</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>logging_otlp</code></p></td>
<td
style="text-align: left;"><p><code>OtlpJsonLoggingSpanExporter</code></p></td>
<td style="text-align: left;"><p>included</p></td>
</tr>
</tbody>
</table>

#### Configuring an OTLP Exporter

The configuration for OTLP exporters is the same, regardless of which
protocol you choose: `grpc` (the default) or `http/proto`. OpenTelemetry
applies some different default values depending on the protocol.

Type:
[io.helidon.telemetry.otelconfig.OtlpExporterConfig](/apidocs/io.helidon.telemetry.otelconfig/io/helidon/telemetry/otelconfig/OtlpExporterConfig.html)

### Configuration options

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
<td style="text-align: left;"><p><code>certificate</code></p></td>
<td style="text-align: left;"><p><a
href="../config/io_helidon_common_configurable_Resource.xml">Resource</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Trusted certificates.</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p><code>client.certificate</code></p></td>
<td style="text-align: left;"><p><a
href="../config/io_helidon_common_configurable_Resource.xml">Resource</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>TLS certificate.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>client.key</code></p></td>
<td style="text-align: left;"><p><a
href="../config/io_helidon_common_configurable_Resource.xml">Resource</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>TLS client key.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>compression</code></p></td>
<td style="text-align: left;"><p>CompressionType (GZIP, NONE)</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Compression the exporter uses.</p>
<p>Allowed values:</p>
<ul>
<li><p><code>GZIP</code>: GZIP compression.</p></li>
<li><p><code>NONE</code>: No compression.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>endpoint</code></p></td>
<td style="text-align: left;"><p>URI</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Endpoint of the collector to which the
exporter should transmit.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>headers</code></p></td>
<td style="text-align: left;"><p>Map&lt;string, string&gt;</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Headers added to each export
message.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>protocol</code></p></td>
<td style="text-align: left;"><p>OtlpExporterProtocolType (HTTP_PROTO,
GRPC)</p></td>
<td
style="text-align: left;"><p><code>OtlpExporterProtocolType.DEFAULT</code></p></td>
<td style="text-align: left;"><p>Exporter protocol type.</p>
<p>Allowed values:</p>
<ul>
<li><p><code>HTTP_PROTO</code>: http/proto protocol type.</p></li>
<li><p><code>GRPC</code>: grpc protocol type.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>retry-policy</code></p></td>
<td style="text-align: left;"><p>RetryPolicy</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Retry policy.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>timeout</code></p></td>
<td style="text-align: left;"><p>Duration</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Exporter timeout.</p></td>
</tr>
</tbody>
</table>

The [OpenTelemetry
documentation](https://opentelemetry.io/docs/languages/java/configuration/#properties-exporters)
describes the defaults; see the "Properties for \`otlp \`span, metric,
and log exporters" section there.

<table>
<caption>OpenTelemetry defaults for tracing</caption>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Setting</th>
<th style="text-align: left;">OpenTelemetry default (and OpenTelemetry
doc link)</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>compression</code></p></td>
<td style="text-align: left;"><p><code>none</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>endpoint</code></p></td>
<td style="text-align: left;"><p><code>grpc</code> protocol: <a
href="http://localhost:4317">http://localhost:4317</a></p>
<p><code>http/proto</code> protocol: <a
href="http://localhost:4318">http://localhost:4318</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>protocol</code></p></td>
<td style="text-align: left;"><p><code>grpc</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>retry-policy</code></p></td>
<td style="text-align: left;"><p>none</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>timeout</code></p></td>
<td style="text-align: left;"><p>10 seconds</p></td>
</tr>
</tbody>
</table>

#### Configuring a Zipkin Exporter

Type:
[io.helidon.telemetry.otelconfig.ZipkinExporterConfig](/apidocs/io.helidon.telemetry.otelconfig/io/helidon/telemetry/otelconfig/ZipkinExporterConfig.html)

### Configuration options

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
<td style="text-align: left;"><p><code>compression</code></p></td>
<td style="text-align: left;"><p>CompressionType (GZIP, NONE)</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Compression type.</p>
<p>Allowed values:</p>
<ul>
<li><p><code>GZIP</code>: GZIP compression.</p></li>
<li><p><code>NONE</code>: No compression.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>encoder</code></p></td>
<td style="text-align: left;"><p>SpanBytesEncoder (JSON_V1, THRIFT,
JSON_V2, PROTO3)</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Encoder type.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>endpoint</code></p></td>
<td style="text-align: left;"><p>URI</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Collector endpoint to which this
exporter should transmit.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>timeout</code></p></td>
<td style="text-align: left;"><p>Duration</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Exporter timeout.</p></td>
</tr>
</tbody>
</table>

The [OpenTelemetry
documentation](https://opentelemetry.io/docs/languages/java/configuration/#properties-exporters)
describes the defaults; see the "Properties for Zipkin span exporters"
section there.

| Setting       | OpenTelemetry default value          |
|---------------|--------------------------------------|
| `compression` | `none`                               |
| `encoder`     | `JSON_V2`                            |
| `endpoint`    | <http://localhost:9411/api/v2/spans> |
| `timeout`     | 10 seconds                           |

OpenTelemetry defaults for Zipkin exporters

### Configuring the Span Sampler

OpenTelemetry offers different ways of sampling data—​deciding which
tracing spans tp capture and send to the backend. The [OpenTelemetry
documentation](https://opentelemetry.io/docs/languages/java/sdk/#sampler)
describes sampling in more detail.

Helidon configuration supports the sampler implementations that reside
in the `opentelemetry-sdk` as listed in the table below. Other samplers
are in other components. If you need to use one of those:

- Add the relevant OpenTelemetry dependency to your project.

- Instantiate the span sample you need.

- Prepare the sampler and the OpenTelemetry-related builders
  programmatically and use your sampler to assign the sampler the
  `OpenTelemetryTracer.Builder` should use.

Type:
[io.helidon.telemetry.otelconfig.SamplerConfig](/apidocs/io.helidon.telemetry.otelconfig/io/helidon/telemetry/otelconfig/SamplerConfig.html)

### Configuration options

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
<td style="text-align: left;"><p><code>param</code></p></td>
<td style="text-align: left;"><p>double</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Sampler parameter.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>type</code></p></td>
<td style="text-align: left;"><p>SamplerType (ALWAYS_ON, ALWAYS_OFF,
TRACEIDRATIO, PARENTBASED_ALWAYS_ON, PARENTBASED_ALWAYS_OFF,
PARENTBASED_TRACEIDRATIO)</p></td>
<td
style="text-align: left;"><p><code>SamplerType.DEFAULT</code></p></td>
<td style="text-align: left;"><p>Sampler type.</p>
<p>Allowed values:</p>
<ul>
<li><p><code>ALWAYS_ON</code>: Always on sampler.</p></li>
<li><p><code>ALWAYS_OFF</code>: Always off sampler.</p></li>
<li><p><code>TRACEIDRATIO</code>: Trace ID ratio-based sampler.</p></li>
<li><p><code>PARENTBASED_ALWAYS_ON</code>: Parent-based always-on
sampler.</p></li>
<li><p><code>PARENTBASED_ALWAYS_OFF</code>: Parent-based always-off
sampler.</p></li>
<li><p><code>PARENTBASED_TRACEIDRATIO</code>: Parent-based trace ID
ration-based sampler.</p></li>
</ul></td>
</tr>
</tbody>
</table>

### Configuring Span Limits

OpenTelemetry allows you to constrain certain aspects of the data it
gathers in tracing spans. By assigning the settings in the table below,
you can apply the span limits you want.

Type:
[io.helidon.telemetry.otelconfig.SpanLimitsConfig](/apidocs/io.helidon.telemetry.otelconfig/io/helidon/telemetry/otelconfig/SpanLimitsConfig.html)

### Configuration options

| key | type | default value | description |
|----|----|----|----|
| `max-attribute-value-length` | int |   | Maximum attribute value length. |
| `max-attributes` | int |   | Maximum number of attributes. |
| `max-attributes-per-event` | int |   | Maximum number of attributes per event. |
| `max-attributes-per-link` | int |   | Maximum number of attributes per link. |
| `max-events` | int |   | Maximum number of events. |
| `max-links` | int |   | Maximum number of links. |

Optional configuration options

The [OpenTelemetry
documentation](https://opentelemetry.io/docs/languages/java/sdk/#sampler)
describes the defaults; see the "Properties for span limits" section
there.

| Setting                      | OpenTelemetry Default |
|------------------------------|-----------------------|
| `max-attribute-value-length` | no limit              |
| `max-attributes`             | 128                   |
| `max-attributes-per-event`   | 128                   |
| `max-events`                 | 128                   |
| `max-links`                  | 128                   |

OpenTelemetry defaults for span limits

# Additional Information

## Helidon Documentation

- [Helidon Tracing](tracing.md)

## OpenTelemetry Documentation

- [Settings and
  defaults](https://opentelemetry.io/docs/languages/java/configuration/#properties-exporters)

- [OpenTelemetry Java SDK
  reference](https://opentelemetry.io/docs/languages/java/sdk)

- [HTTP semantic
  conventions](https://github.com/open-telemetry/semantic-conventions/blob/v1.29.0/docs/http/http-spans.md#http-server)

- [Intro to OpenTelemetry
  Java](https://opentelemetry.io/docs/languages/java/intro/)
