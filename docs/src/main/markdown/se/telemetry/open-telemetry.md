# OpenTelemetry Support in Helidon SE

## Contents

- [Overview](#_overview)

- [API](#_api)

- [Maven Coordinates](#maven-coordinates)

- [Configuration](#_configuration)

  - [Common Settings](#common-config)

  - [Tracing](#tracing-config)

  - [Metrics](#metrics-config)

  - [Logging](#logger-config)

- [Additional Information](#_additional_information)

## Overview

> [!NOTE]
> Helidon SE support for OpenTelemetry configuration and semantic conventions as described below is currently a [preview feature](/apidocs/io.helidon.common.features.api/io/helidon/common/features/api/Preview.html). We intend to support it going forward, but we might change its external API and behavior in backward-incompatible ways across dot releases.

Helidon SE supports OpenTelemetry in several important ways:

- Implements the [neutral Helidon tracing API](../../se/tracing.md) using OpenTelemetry

- Allows users to assign OpenTelemetry settings as follows:

  - Declaratively, using Helidon config under the top-level `telemetry` config key

  - Programmatically, using the OpenTelemetry SDK API and the Helidon OpenTelemetry API

- Conforms to the [OpenTelemetry semantic conventions](https://github.com/open-telemetry/semantic-conventions/blob/v1.58.0/docs/http/http-spans.md#http-server) for automatically-created spans and metrics for HTTP requests

- Allows [publishing Helidon metrics](../../se/metrics/metrics.md#usage-publishing) to backend systems using OTLP.

OpenTelemetry models observability as a set of [*signals*](https://opentelemetry.io/docs/concepts/signals/). Each signal—​for example metrics, tracing, and logging—​is an origin of monitoring data, and each has configurable settings which control its behavior.

Helidon’s config support for OpenTelemetry has certain config attributes which apply to OpenTelemetry as a whole, others which pertain to individual signals, and still more which describe lower-level elements within a signal.

The Helidon OpenTelemetry configuration format, the Helidon OpenTelemetry API, and this documentation all follow this hierarchy:

- [Top-level telemetry](#top-level-config)

  - Signals

    - [Tracing](#tracing-config)

    - [Metrics](#metrics-config)

    - [Logging](#logger-config)

This document describes how to configure each level in the hierarchy and covers general topics related to Helidon’s support of OpenTelemetry.

## API

There are *two* APIs that might be useful to developers working with OpenTelemetry:

- The Helidon OpenTelemetry API - useful for mapping configuration sources to Helidon builders and, ultimately, OpenTelemetry objects.

- The OpenTelemetry API - useful for creating OpenTelemetry objects apart from Helidon configuration sources.

The types in the Helidon OpenTelemetry API correspond closely to the configuration structures described in later sections of this document. Application code can use Helidon OpenTelemetry builders to prepare and construct each of the configurable entities to ultimately prepare an `OpenTelemetry` instance set up according to the application’s needs.

That said, application code can equally well use the OpenTelemetry API and its builders to prepare the `OpenTelemetry` instance.

Applications could even use both APIs together, reading configuration to construct a Helidon builder and then adding to that builder OpenTelemetry objects created separately using the OpenTelemetry API.

The [Helidon OpenTelemetry API Javadoc](/apidocs/io.helidon.telemetry.otelconfig/io/helidon/telemetry/otelconfig/package-summary.html) page lists the various types developers can use to prepare OpenTelemetry objects programmatically. As a starting point, the [`OpenTelemetryConfig`](/apidocs/io.helidon.telemetry.otelconfig/io/helidon/telemetry/otelconfig/OpenTelemetryConfig.html) interface and its [`Builder`](/apidocs/io.helidon.telemetry.otelconfig/io/helidon/telemetry/otelconfig/OpenTelemetryConfig.BuilderBase.html) represents the top-level configuration for OpenTelemetry. Their Javadoc contains links to other types that compose the top-level object, and so on.

Later sections in this document also describe the configuration settings available.

The [OpenTelemetry SDK documentation](https://opentelemetry.io/docs/languages/java/sdk/#sdk-components) explains its API.

> [!NOTE]
> Many applications do not need to use either the Helidon OpenTelemetry API or the OpenTelemetry API directly. They can instead rely completely on declarative Helidon configuration of OpenTelemetry.

### Managing the Global `OpenTelemetry` Instance

Typically, an application uses the same `OpenTelemetry` instance throughout its execution. OpenTelemetry offers a global `OpenTelemetry` instance to make it easy for application code to set and obtain the global instance.

Similarly, the Helidon tracing API has a global `Tracer`.

In most cases, an application that prepares OpenTelemetry programmatically should initialize both of those by including code as shown in the following example.

*Setting the global `OpenTelemetry` and `Tracer` instances in Helidon*

``` java
import java.util.Map;
import io.helidon.telemetry.otelconfig.HelidonOpenTelemetry;

import io.opentelemetry.api.GlobalOpenTelemetry;
import io.opentelemetry.api.OpenTelemetry;
import io.opentelemetry.api.trace.SpanKind;
import io.opentelemetry.api.trace.StatusCode;
import io.opentelemetry.context.Scope;
import io.opentelemetry.sdk.autoconfigure.AutoConfiguredOpenTelemetrySdk;

        // Application code using the OpenTelemetry API or the Helidon OpenTelemetry API or both.
        OpenTelemetry customOpenTelemetry = prepareOpenTelemetry();

        // App code to build any tags to be applied to every span.
        Map<String, String> tags = prepareTags();

        HelidonOpenTelemetry.global(customOpenTelemetry,
                                    "your-service-name",
                                    tags);
```

#### Assigning the Global Instance

Using Helidon to set the global `OpenTelemetry` instance has these effects:

- Assigns the instance as the OpenTelemetry global instance.

- Creates a Helidon `Tracer` using the OpenTelemetry instance and makes that the Helidon global `Tracer`.

> [!NOTE]
> Helidon is deprecating its use of "global" Helidon objects in favor of retrieving the correct instance from the Helidon service registry. Applications should migrate toward using, for example, `Services.get(Tracer.class)` instead of `Tracer.global()`.

## Maven Coordinates

To enable various aspects of OpenTelemetry Support add one or more of the following dependencies to your project’s `pom.xml` (see [Managing Dependencies](../../about/managing-dependencies.md)).

### Using the OpenTelemetry implementation of the Helidon Tracing API

Helidon offers an implementation of its [ neutral tracing API](../../se/tracing.md) that uses OpenTelemetry. Add the following dependency to use OpenTelemetry for tracing.

*Dependency to use the Helidon OpenTelemetry implementation of Helidon tracing*

``` xml
<dependency>
    <groupId>io.helidon.tracing.providers</groupId>
    <artifactId>helidon-tracing-providers-opentelemetry</artifactId>
    <scope>runtime</scope>
</dependency>
```

### Adding OpenTelemetry Configuration and Builder Support

To allow deployers and end users to set up Helidon configuration to control OpenTelemetry behavior, add the following dependency.

*Dependency to add Helidon OpenTelemetry config and programmatic builder support*

``` xml
<dependency>
    <groupId>io.helidon.telemetry</groupId>
    <artifactId>helidon-telemetry-opentelemetry-config</artifactId>
    <scope>runtime</scope> 
</dependency>
```

- To use the Helidon OpenTelemetry API in your application code, remove this line or change it to `<scope>compile</scope>`.

### Enabling Automatic Spans for HTTP Requests

Helidon’s tracing observability support automatically creates a new tracing span for each HTTP request if your project includes the following dependency.

*Dependency for automatic HTTP request tracing*

``` xml
<dependency>
    <groupId>io.helidon.webserver.observe</groupId>
    <artifactId>helidon-webserver-observe-tracing</artifactId>
    <scope>runtime</scope>
</dependency>
```

By default, when Helidon SE creates spans automatically for HTTP requests, it uses a set of rules—​semantic conventions—​for choosing the span name and adding tags to each span.

OpenTelemetry prescribes its own [semantic conventions](https://github.com/open-telemetry/semantic-conventions/blob/v1.58.0/docs/http/http-spans.md#http-server). If you add the following dependency, Helidon follows the OpenTelemetry semantic conventions for spans instead of its own.

*Dependency for Helidon support of the OpenTelemetry tracing semantic conventions*

``` xml
<dependency>
    <groupId>io.helidon.webserver.observe</groupId>
    <artifactId>helidon-webserver-observe-telemetry-tracing</artifactId>
    <scope>runtime</scope>
</dependency>
```

### Enabling Automatic Metrics for Incoming HTTP Requests

Helidon’s metrics observability support automatically registers and updates one or more meters (depending on configuration) and updates them accordingly as HTTP requests arrive.

*Dependency for automatic HTTP request measurements*

``` xml
<dependency>
    <groupId>io.helidon.webserver.observe</groupId>
    <artifactId>helidon-webserver-observe-metrics</artifactId>
    <scope>runtime</scope>
</dependency>
```

OpenTelemetry prescribes its own [semantic conventions](https://github.com/open-telemetry/semantic-conventions/blob/v1.58.0/docs/http/http-metrics.md#http-server) for metrics—​their names and tha attributes (tags) they have. If you add the following dependency, Helidon registers and updates meters according to the OpenTelemetry metrics semantic conventions.

*Dependency for Helidon support of the OpenTelemetry metrics semantic conventions for incoming HTTP requests*

``` xml
<dependency>
  <groupId>io.helidon.webserver.observe</groupId>
  <artifactId>helidon-webserver-observe-telemetry-metrics</artifactId>
  <scope>runtime</scope>
</dependency>
```

### Enabling OpenTelemetry for Outgoing Helidon Webclient Traffic

Helidon supports the OpenTelemetry semantic conventions for outgoing traffic which uses the Helidon WebClient. See the [Helidon WebClient documentation](../../se/webclient.md#_configuring_telemetry).

### Specifying Additional OpenTelemetry Dependencies

Most applications need to declare other runtime dependencies on OpenTelemetry artifacts because the configuration specifies—​or the application code uses—​particular OpenTelemetry types packaged in other artifacts. For example, OpenTelemetry exporters are packaged individually or as related groups. See [this section below](#note-about-exporter-dependencies) for some specific dependencies to consider adding for particular exporters.

These exporters transmit telemetry data using a different protocol. (See [this OpenTelemetry page](https://github.com/open-telemetry/opentelemetry-java/tree/v1.58.0/exporters).)

## Configuration

You can control almost all of OpenTelemetry’s overall, tracing, metrics, and logger runtime behavior using Helidon configuration settings. Helidon constructs an `OpenTelemetry` object using the configuration. The resulting `OpenTelemetry` instance reflects these settings from the Helidon configuration:

- Settings that pertain to [overall OpenTelemetry behavior](#top-level-config), apart from a particular signal.

- An OpenTelemetry tracer provider based on [tracing configuration](#tracing-config) in `signals.tracing`.

- An OpenTelemetry meter provider based on [metrics configuration](#metrics-config) in `signals.metrics`.

- An OpenTelemetry logger provider based on [logger configuration](#logger-config) in `signals.logging`.

### Controlling Overall OpenTelemetry Behavior

Several settings control the operation of OpenTelemetry as a whole, as shown in the next table.

Type: [io.helidon.telemetry.otelconfig.HelidonOpenTelemetry](/apidocs/io.helidon.telemetry.otelconfig/io/helidon/telemetry/otelconfig/HelidonOpenTelemetry.html)

This is a standalone configuration type, prefix from configuration root: `telemetry`

#### Configuration options

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
<td style="text-align: left;"><p>Whether the OpenTelemetry support is enabled.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>global</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Whether the io.opentelemetry.api.OpenTelemetry instance created from this configuration should be made the global one.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>propagators</code></p></td>
<td style="text-align: left;"><p>TextMapPropagator[]</p></td>
<td style="text-align: left;"><p><code>new java.util.ArrayList&lt;&gt;(io.helidon.telemetry.otelconfig.ContextPropagationType.DEFAULT_PROPAGATORS)</code></p></td>
<td style="text-align: left;"><p>OpenTelemetry io.opentelemetry.context.propagation.TextMapPropagator instances added explicitly by the app.</p>
<p>Default: <code>tracecontext,baggage</code>. See io.helidon.telemetry.otelconfig.ContextPropagationType</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>signals.logging</code></p></td>
<td style="text-align: left;"><p><a href="../../se/telemetry/../../config/io_helidon_telemetry_otelconfig_OpenTelemetryLoggingConfig.xml">OpenTelemetryLoggingConfig</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>OpenTelemetry logging settings.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>signals.metrics</code></p></td>
<td style="text-align: left;"><p><a href="../../se/telemetry/../../config/io_helidon_telemetry_otelconfig_OpenTelemetryMetricsConfig.xml">OpenTelemetryMetricsConfig</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>OpenTelemetry metrics settings.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>signals.tracing</code></p></td>
<td style="text-align: left;"><p><a href="../../se/telemetry/../../config/io_helidon_telemetry_otelconfig_OpenTelemetryTracingConfig.xml">OpenTelemetryTracingConfig</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>OpenTelemetry tracing settings.</p></td>
</tr>
</tbody>
</table>

Notes:

- OpenTelemetry uses default propagators of `tracecontext` and `baggage`. (See the `otel.propagators` property in [this OpenTelemetry guide](https://opentelemetry.io/docs/languages/java/configuration/#properties-general).)

- Setting `global` to `true` has the effect described in the [section](#effects-of-setting-global) about global instances.

### Common Configuration Across Signals

This section describes settings that apply to multiple signal types.

#### Assigning Attributes

Configured attributes are key/value pairs that OpenTelemetry attaches to each transmission of a signal. OpenTelemetry supports attributes of type `String`, `long`, `double`, and `boolean`. The Helidon configuration structure groups attributes by type so Helidon can indicate precisely to OpenTelemetry what type you intend for each attribute.

You can add attributes to the configuration for any of the signals under the signal’s `attributes` section.

Type: [io.helidon.telemetry.otelconfig.TypedAttributes](/apidocs/io.helidon.telemetry.otelconfig/io/helidon/telemetry/otelconfig/TypedAttributes.html)

##### Configuration options

| key        | type                   | default value | description         |
|------------|------------------------|---------------|---------------------|
| `booleans` | Map\<string, boolean\> |               | Boolean attributes. |
| `doubles`  | Map\<string, double\>  |               | Double attributes.  |
| `longs`    | Map\<string, long\>    |               | Long attributes.    |
| `strings`  | Map\<string, string\>  |               | String attributes.  |

Optional configuration options

The following example shows attribute settings for the tracing signal.

*Example attribute settings*

``` yaml
telemetry:
  service: my-helidon-service
  tracing:
    attributes:
      strings:
        attr1: 12
        attr5: "any old thing"
        attr7: something
      longs:
        attr2: 12
      doubles:
        attr3: 24.5
        attr6: 12
      booleans:
        attr4: true
```

#### Configuring Exporters and Processors/Readers

OpenTelemetry transmits the telemetry data it gathers to a backend system—​such as Grafana, Signoz, Prometheus, Jaeger, or others—​where you can view and query the data. OpenTelemetry goes through these distinct steps to gather and send data:

1.  OpenTelemetry tracing and log record *processors* and metrics *readers* gather and process data observations.

2.  OpenTelemetry *exporters* associated with each processor or reader then transmit\_ the data to one or more targets. Targets are typically backend systems but can be local ones for debugging. Each processor or reader uses one or more exporters to transmit telemetry data.

The processor settings determine when and how often each uses its exporters to deliver data. Each exporter’s settings prescribe where it should send the data, how to connect to a backend, etc.

##### Configuring Processors (and readers)

An OpenTelemetry span or log record processor or metric reader is one of the following types:

- simple - The processor sends each telemetry observation to its exporters for transmission as soon as it receives the observation.

- batch - The processor groups observations into batches and sends a batch at a time to its exporters for transmission.

In the table below only the `type` and `exporters` setting apply to `simple` processors; the other settings are for batch processors.

Type: [io.helidon.telemetry.otelconfig.BatchProcessorConfig](/apidocs/io.helidon.telemetry.otelconfig/io/helidon/telemetry/otelconfig/BatchProcessorConfig.html)

##### Configuration options

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
<td style="text-align: left;"><p>ProcessorType (SIMPLE, BATCH)</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Processor type.</p>
<p>Allowed values:</p>
<ul>
<li><p><code>SIMPLE</code>: Simple Processor.</p></li>
<li><p><code>BATCH</code>: Batch Processor.</p></li>
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
<td style="text-align: left;"><p>Name(s) of the exporter(s) this processor should use; specifying no names uses all configured exporters (or if no exporters are configured, the default OpenTelemetry exporter(s)).</p>
<p>Each name must be the name of one of the configured OpenTelemetryTracingConfig.exporterConfigs().</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>max-export-batch-size</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Maximum number of items batched for export together. OpenTelemetry requires this value to not exceed the maxQueueSize().</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>max-queue-size</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Maximum number of items retained before discarding excess unexported ones.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>schedule-delay</code></p></td>
<td style="text-align: left;"><p>Duration</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Delay between consecutive exports.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>timeout</code></p></td>
<td style="text-align: left;"><p>Duration</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Maximum time an export can run before being cancelled.</p></td>
</tr>
</tbody>
</table>

##### Configuring Exporters

Exporter objects in OpenTelemetry are specific to both *how* they transmit telemetry data and *what* signal they work with. Even so, many exporter settings are very similar across different signals. This section describes the behavior and configuration that is common among exporters. Refer to the sections below that describe each signal to see what additional exporter settings, if any, each signal adds.

Helidon configuration supports several of the most popular exporters, discussed below.

###### Setting Up OTLP Exporters

Most users choose an `Otlp` exporter which has two variations—​one using gRPC and one using HTTP with protocol buffers—​as indicated by the `protocol` setting.

*Common Configuration for OTLP exporters*

Type: [io.helidon.telemetry.otelconfig.OtlpExporterConfig](/apidocs/io.helidon.telemetry.otelconfig/io/helidon/telemetry/otelconfig/OtlpExporterConfig.html)

##### Configuration options

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
<td style="text-align: left;"><p><a href="../../se/telemetry/../../config/io_helidon_common_configurable_Resource.xml">Resource</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Trusted certificates.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>client.certificate</code></p></td>
<td style="text-align: left;"><p><a href="../../se/telemetry/../../config/io_helidon_common_configurable_Resource.xml">Resource</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>TLS certificate.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>client.key</code></p></td>
<td style="text-align: left;"><p><a href="../../se/telemetry/../../config/io_helidon_common_configurable_Resource.xml">Resource</a></p></td>
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
<td style="text-align: left;"><p><code>connect-timeout</code></p></td>
<td style="text-align: left;"><p>Duration</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Connection timeout.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>endpoint</code></p></td>
<td style="text-align: left;"><p>URI</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Endpoint of the collector to which the exporter should transmit.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>headers</code></p></td>
<td style="text-align: left;"><p>Map&lt;string, string&gt;</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Headers added to each export message.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>internal-telemetry-version</code></p></td>
<td style="text-align: left;"><p>InternalTelemetryVersion (LEGACY, LATEST)</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Self-monitoring telemetry OpenTelemetry should collect.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>memory-mode</code></p></td>
<td style="text-align: left;"><p>MemoryMode (REUSABLE_DATA, IMMUTABLE_DATA)</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Memory mode.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>protocol</code></p></td>
<td style="text-align: left;"><p>OtlpExporterProtocolType (HTTP_PROTO, GRPC)</p></td>
<td style="text-align: left;"><p><code>OtlpExporterProtocolType.DEFAULT</code></p></td>
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

<table>
<caption>OpenTelemetry OTLP exporter defaults</caption>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Setting</th>
<th style="text-align: left;">OpenTelemetry default</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>compression</code></p></td>
<td style="text-align: left;"><p><code>none</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>endpoint</code></p></td>
<td style="text-align: left;"><p><code>grpc</code> protocol: <a href="http://localhost:4317">http://localhost:4317</a></p>
<p><code>http/proto</code> protocol: <a href="http://localhost:4318">http://localhost:4318</a></p></td>
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

###### OTLP Retry Policy

You can control how each exporter retries if a transmission to a backend fails.

Type: [io.helidon.telemetry.otelconfig.RetryPolicyConfig](/apidocs/io.helidon.telemetry.otelconfig/io/helidon/telemetry/otelconfig/RetryPolicyConfig.html)

###### Configuration options

| key | type | default value | description |
|----|----|----|----|
| `initial-backoff` | Duration |   | Initial backoff time. |
| `max-attempts` | int |   | Maximum number of retry attempts. |
| `max-backoff` | Duration |   | Maximum backoff time. |
| `max-backoff-multiplier` | double |   | Maximum backoff multiplier. |

Optional configuration options

OpenTelemetry also supports a Zipkin exporter which it has recently deprecated.

###### Zipkin Exporter

*Configuration for Zipkin exporters*

Type: [io.helidon.telemetry.otelconfig.ZipkinExporterConfig](/apidocs/io.helidon.telemetry.otelconfig/io/helidon/telemetry/otelconfig/ZipkinExporterConfig.html)

##### Configuration options

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
<td style="text-align: left;"><p>SpanBytesEncoder (JSON_V1, THRIFT, JSON_V2, PROTO3)</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Encoder type.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>endpoint</code></p></td>
<td style="text-align: left;"><p>URI</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Collector endpoint to which this exporter should transmit.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>timeout</code></p></td>
<td style="text-align: left;"><p>Duration</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Exporter timeout.</p></td>
</tr>
</tbody>
</table>

The [OpenTelemetry documentation](https://opentelemetry.io/docs/languages/java/configuration/#properties-exporters) describes the defaults; see the "Properties for Zipkin span exporters" section there.

| Setting       | OpenTelemetry default value          |
|---------------|--------------------------------------|
| `compression` | `none`                               |
| `encoder`     | `JSON_V2`                            |
| `endpoint`    | <http://localhost:9411/api/v2/spans> |
| `timeout`     | 10 seconds                           |

OpenTelemetry defaults for Zipkin exporters

OpenTelemetry provides other exporters, often used for debugging:

- `console`

  Writes telemetry data at the `INFO` level using the `java.util.logging.Logger` for `io.opentelemetry.exporter.logging.Logging{signal}Expoerter`

- `logging-otlp`

  Writes telemetry data in JSON format to the logger for the particular OpenTelemetry implementation class (e.g., `OtlpJsonLoggingMetricExporter`).

The `console` and `logging-otlp` have no configuration that is common across all signals.

> [!NOTE]
> You need to add dependencies to your project for the exporters your application uses, even ones supported by Helidon config.

The table below describes the exporter types that Helidon configuration supports and what dependency your project needs to support them.

If you need to use an exporter that is *not* in the table:

- Add a dependency on the OpenTelemetry artifact that contains that exporter type.

- Add application code that prepares the exporter instance.

- Prepare the Helidon OpenTelemetry builders programmatically and add your exporter instance to the builder.

In the table below, the Maven artifacts are all in the `io.opentelemetry` group.

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
<th style="text-align: left;">Artifact ID to add - <code>see</code>also the <a href="https://opentelemetry.io/docs/languages/java/sdk/#spanexporter">OpenTelemetry documentation</a></th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="2" style="text-align: left;"><p><a href="#otlp-exporter-config"><code>otlp</code></a><br />
(see <code>protocol</code> setting below)</p></td>
<td style="text-align: left;"><p><code>OtlpGrpc{signal}Exporter</code></p></td>
<td rowspan="2" style="text-align: left;"><p><code>opentelemetry-exporter-otlp</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>OtlpHttp{signal}Exporter</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><a href="../../se/telemetry/../../config/io_helidon_telemetry_otelconfig_ZipkinExporterConfig.xml"><code>zipkin</code></a></p></td>
<td style="text-align: left;"><p><code>ZipkinSpanExporter</code></p></td>
<td style="text-align: left;"><p><code>opentelemetry-exporter-zipkin</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>console</code></p></td>
<td style="text-align: left;"><p><code>Logging{signal}Exporter</code></p></td>
<td rowspan="2" style="text-align: left;"><p><code>opentelemetry-exporter-logging</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>logging_otlp</code></p></td>
<td style="text-align: left;"><p><code>OtlpJsonLogging{signal}Exporter</code></p>
<p><code>SystemOutLogRecordExporeter</code></p></td>
</tr>
</tbody>
</table>

##### Associating Each Processor and Reader with its Exporters

In configuration, you link processors and readers with the exporters you want each to use as follows:

- For clarity, name each exporter if you have more than one.

- Optionally specify for each processor or reader the names of the exporters it should use.

  If you omit the exporter names for a processor or reader, Helidon associates it with all configured exporters. If you configure no exporters explicitly, Helidon associates the OpenTelemetry default exporter with the processor or reader.

The following examples show increasingly-complicated scenarios using tracing as the signal:

- Default

- Minimal configuration

- Maximum flexibility

For many applications the default and minimal scenarios work well.

##### Default

This scenario includes no configuration at all for either processors or exporters.

OpenTelemetry uses its default processor (`batch`) with its default exporter (`otlp` using `grpc`). \|

``` yaml
telemetry:
  service: "inventory"
  tracing:
    sampler: "always_off"
```

##### Minimal configuration

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

##### Maximum flexibility

The user configures possibly multiple processors and possibly multiple named exporters. Each processor’s configuration lists the names of the exporters it should use; no names means all exporters.

The first processor (type `batch`) uses both exporters because it does not specify any exporter names. The second processor uses only the `alternate-otlp` exporter.\|

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

### Controlling OpenTelemetry Tracing Behavior

The settings under `signals.tracing` prepare an OpenTelemetry `TracerProvider`. When your application uses the Helidon tracing API to obtain a `Tracer`, Helidon uses the `TracerProvider` prepared from this config to create the tracer.

The next table describes the OpenTelemetry tracing settings.

Type: [io.helidon.telemetry.otelconfig.OpenTelemetryTracingConfig](/apidocs/io.helidon.telemetry.otelconfig/io/helidon/telemetry/otelconfig/OpenTelemetryTracingConfig.html)

#### Configuration options

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
<td style="text-align: left;"><p><code>attributes</code></p></td>
<td style="text-align: left;"><p>AttributesBuilder</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Name/value pairs passed to OpenTelemetry.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>exporters</code></p></td>
<td style="text-align: left;"><p>Map&lt;string, SpanExporter&gt;</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Span exporters.</p>
<p>The key in the map is a unique name—​of the user’s choice—​for the exporter config settings. The ProcessorConfig.exporters() config setting for a processor config specifies zero or more of these names to associate the exporters built from the exporter configs with the processor built from the processor config.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>processors</code></p></td>
<td style="text-align: left;"><p><a href="../../se/telemetry/../../config/io_helidon_telemetry_otelconfig_ProcessorConfig.xml">ProcessorConfig[]</a></p></td>
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

Refer to the earlier sections about [configuring attributes](#attributes-config) and [configuring processors and exporters](#exporters-and-processors).

Sections below describe how to set up the tracing signal configuration:

- [Configuring the Span Sampler](#span-sampler-config)

- [Configuring the Span Limits](#span-limits-config)

#### Configuring the Span Sampler

OpenTelemetry offers different ways of sampling data—​deciding which tracing spans tp capture and send to the backend. The [OpenTelemetry documentation](https://opentelemetry.io/docs/languages/java/sdk/#sampler) describes sampling in more detail.

Helidon configuration supports the sampler implementations that reside in the `opentelemetry-sdk` as listed in the table below. Other samplers are in other components. If you need to use one of those:

- Add the relevant OpenTelemetry dependency to your project.

- Instantiate the span sample you need.

- Prepare the sampler and the OpenTelemetry-related builders programmatically and use your sampler to assign the sampler the `OpenTelemetryTracer.Builder` should use.

Type: [io.helidon.telemetry.otelconfig.SamplerConfig](/apidocs/io.helidon.telemetry.otelconfig/io/helidon/telemetry/otelconfig/SamplerConfig.html)

#### Configuration options

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
<td style="text-align: left;"><p>SamplerType (ALWAYS_ON, ALWAYS_OFF, TRACEIDRATIO, PARENTBASED_ALWAYS_ON, PARENTBASED_ALWAYS_OFF, PARENTBASED_TRACEIDRATIO)</p></td>
<td style="text-align: left;"><p><code>SamplerType.DEFAULT</code></p></td>
<td style="text-align: left;"><p>Sampler type.</p>
<p>Allowed values:</p>
<ul>
<li><p><code>ALWAYS_ON</code>: Always on sampler.</p></li>
<li><p><code>ALWAYS_OFF</code>: Always off sampler.</p></li>
<li><p><code>TRACEIDRATIO</code>: Trace ID ratio-based sampler.</p></li>
<li><p><code>PARENTBASED_ALWAYS_ON</code>: Parent-based always-on sampler.</p></li>
<li><p><code>PARENTBASED_ALWAYS_OFF</code>: Parent-based always-off sampler.</p></li>
<li><p><code>PARENTBASED_TRACEIDRATIO</code>: Parent-based trace ID ration-based sampler.</p></li>
</ul></td>
</tr>
</tbody>
</table>

#### Configuring Span Limits

OpenTelemetry allows you to constrain certain aspects of the data it gathers in tracing spans. By assigning the settings in the table below, you can apply the span limits you want.

Type: [io.helidon.telemetry.otelconfig.SpanLimitsConfig](/apidocs/io.helidon.telemetry.otelconfig/io/helidon/telemetry/otelconfig/SpanLimitsConfig.html)

#### Configuration options

| key | type | default value | description |
|----|----|----|----|
| `max-attribute-value-length` | int |   | Maximum attribute value length. |
| `max-attributes` | int |   | Maximum number of attributes. |
| `max-attributes-per-event` | int |   | Maximum number of attributes per event. |
| `max-attributes-per-link` | int |   | Maximum number of attributes per link. |
| `max-events` | int |   | Maximum number of events. |
| `max-links` | int |   | Maximum number of links. |

Optional configuration options

The [OpenTelemetry documentation](https://opentelemetry.io/docs/languages/java/sdk/#sampler) describes the defaults; see the "Properties for span limits" section there.

| Setting                      | OpenTelemetry Default |
|------------------------------|-----------------------|
| `max-attribute-value-length` | no limit              |
| `max-attributes`             | 128                   |
| `max-attributes-per-event`   | 128                   |
| `max-events`                 | 128                   |
| `max-links`                  | 128                   |

OpenTelemetry defaults for span limits

### Controlling OpenTelemetry Metrics Behavior

The settings under `signals.metrics` prepare an OpenTelemetry `MeterProvider`. If your code uses the OpenTelemetry API to obtain an OpenTelemetry meter, meter provider, or meter builder, OpenTelemetry uses the `MeterProvider` prepared from this configuration.

The sections below describe Helidon config settings that correspond very directly to OpenTelemetry builders for the relevant OpenTelemetry type. Refer to the relevant OpenTelemetry documentation or Javadoc to understand the effect each setting has.

See the earlier sections about [configuring attributes](#attributes-config) and [configuring processors and exporters](#exporters-and-processors). A [later section below](#metric-exporters-config) describes some additional attributes on metrics exporters.

The next table describes the OpenTelemetry metrics settings.

Type: [io.helidon.telemetry.otelconfig.OpenTelemetryMetricsConfig](/apidocs/io.helidon.telemetry.otelconfig/io/helidon/telemetry/otelconfig/OpenTelemetryMetricsConfig.html)

#### Configuration options

| key | type | default value | description |
|----|----|----|----|
| `attributes` | AttributesBuilder |   | Name/value pairs passed to OpenTelemetry. |
| `exporters` | Map\<string, MetricExporter\> |   | Metric exporter configurations, configurable using io.helidon.telemetry.otelconfig.MetricExporterConfig. |
| `readers` | [MetricReaderConfig\[\]](../../se/telemetry/../../config/io_helidon_telemetry_otelconfig_MetricReaderConfig.md) |   | Settings for metric readers. |
| `views` | OpenTelemetryMetricsConfigSupport.ViewRegistration\[\] |   | Metric view information, configurable using io.helidon.telemetry.otelconfig.ViewRegistrationConfig. |

Optional configuration options

OpenTelemetry applies the defaults described in the next table.

| Setting | OpenTelemetry default (and OpenTelemetry doc link) |
|----|----|
| `exporters` | [`otlp` with `grpc` protocol](https://opentelemetry.io/docs/languages/java/configuration/#properties-exporters) - see that web page’s "Properties: exporters, `otel.metrics.exporter` property"\] section. |
| `readers` | [`PeriodicMetricReader`](https://opentelemetry.io/docs/languages/java/configuration/#properties-metrics) with an interval of one minute |

Default metric settings applied by OpenTelemetry

Sections below describe how to set up the configuration that is specific to the metrics signal:

- [Configuring Metric Exporters](#metric-exporters-config)

- [Configuring Metric Readers](#metric-readers-config)

- [Configuring Metric Views](#metric-views-config)

The following example illustrates some of the ways you can configure OpenTelemetry metrics behavior. It is neither complete nor typical.

*Example OpenTelemetry Metrics Configuration*

``` yaml
telemetry:
  service: "test-telemetry"
  signals:
    metrics:                                          
      exporters:
        - name: exp-1                                 
          type: otlp
          endpoint: "http://host:1234"
          temporality-preference: cumulative          
          default-histogram-aggregation:              
            type: base2-exponential-bucket-histogram
            max-buckets: 152
            max-scale: 19
        - name: exp-2                                 
          type: otlp
          protocol: grpc
          temporality-preference: delta               
          default-histogram-aggregation:              
            type: explicit-bucket-histogram
            bucket-boundaries: [3,5,7]
      readers:
        - type: periodic                              
          exporter: exp-1
          interval: PT6S
      views:
        - name: sum-view                              
          aggregation:
            type: sum
          description: "Sum view"
          instrument-selector:
            name: counter-selector
            type: counter
            meter-name: my-counter
```

- Introduces the metrics configuration.

- Introduces the first metric exporter (with name `exp-1`).

- Indicates to accumulate measurement values since the previous transmission.

- Prescribes to aggregate histograms for transmission using the OpenTelemetry `BASE2_EXPONENTIAL_BUCKET_HISTOGRAM` technique with the specified maximum number of buckets and maximum scale.

- Introduces the second metric exporter (with name `exp-2`).

- Indicates to transmit deltas since the last transmission.

- Prescribes to aggregate histograms using a histogram with the given explicit bucket boundary values.

- Declares a single metric reader of the OpenTelemetry `PERIODIC` types gathering data each 6 seconds.

- Declares a single view to influence influence the transmission of the `my-counter` counter data.

#### Metric Exporters

The configuration for metrics exporters has several additional settings beyond those described earlier for exporters in general.

Type: [io.helidon.telemetry.otelconfig.MetricExporterConfig](/apidocs/io.helidon.telemetry.otelconfig/io/helidon/telemetry/otelconfig/MetricExporterConfig.html)

#### Configuration options

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
<td style="text-align: left;"><p><a href="../../se/telemetry/../../config/io_helidon_common_configurable_Resource.xml">Resource</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Trusted certificates.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>client.certificate</code></p></td>
<td style="text-align: left;"><p><a href="../../se/telemetry/../../config/io_helidon_common_configurable_Resource.xml">Resource</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>TLS certificate.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>client.key</code></p></td>
<td style="text-align: left;"><p><a href="../../se/telemetry/../../config/io_helidon_common_configurable_Resource.xml">Resource</a></p></td>
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
<td style="text-align: left;"><p><code>connect-timeout</code></p></td>
<td style="text-align: left;"><p>Duration</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Connection timeout.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>default-histogram-aggregation</code></p></td>
<td style="text-align: left;"><p>DefaultAggregationSelector</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Preferred default histogram aggregation technique, configurable as io.helidon.telemetry.otelconfig.MetricDefaultHistogramAggregationConfig.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>endpoint</code></p></td>
<td style="text-align: left;"><p>URI</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Endpoint of the collector to which the exporter should transmit.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>headers</code></p></td>
<td style="text-align: left;"><p>Map&lt;string, string&gt;</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Headers added to each export message.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>internal-telemetry-version</code></p></td>
<td style="text-align: left;"><p>InternalTelemetryVersion (LEGACY, LATEST)</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Self-monitoring telemetry OpenTelemetry should collect.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>memory-mode</code></p></td>
<td style="text-align: left;"><p>MemoryMode (REUSABLE_DATA, IMMUTABLE_DATA)</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Memory mode.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>protocol</code></p></td>
<td style="text-align: left;"><p>OtlpExporterProtocolType (HTTP_PROTO, GRPC)</p></td>
<td style="text-align: left;"><p><code>OtlpExporterProtocolType.DEFAULT</code></p></td>
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
<td style="text-align: left;"><p><code>temporality-preference</code></p></td>
<td style="text-align: left;"><p>AggregationTemporalitySelector</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Preferred output aggregation technique (how transmitted values reflect the values recorded locally), configurable as a io.helidon.telemetry.otelconfig.MetricTemporalityPreferenceType value: <code>CUMULATIVE, DELTA, LOWMEMORY</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>timeout</code></p></td>
<td style="text-align: left;"><p>Duration</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Exporter timeout.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>type</code></p></td>
<td style="text-align: left;"><p>MetricExporterType (OTLP, CONSOLE, LOGGING_OTLP)</p></td>
<td style="text-align: left;"><p><code>MetricExporterType.OTLP</code></p></td>
<td style="text-align: left;"><p>Metric exporter type.</p>
<p>Allowed values:</p>
<ul>
<li><p><code>OTLP</code>: OpenTelemetry Protocol io.opentelemetry.exporter.otlp.http.metrics.OtlpHttpMetricExporter and io.opentelemetry.exporter.otlp.metrics.OtlpGrpcMetricExporter.</p></li>
<li><p><code>CONSOLE</code>: Console (io.opentelemetry.exporter.logging.LoggingMetricExporter.</p></li>
<li><p><code>LOGGING_OTLP</code>: JSON logging to console io.opentelemetry.exporter.logging.otlp.OtlpJsonLoggingMetricExporter.</p></li>
</ul></td>
</tr>
</tbody>
</table>

##### Metric Aggregation

OpenTelemetry allows control over how each exporter aggregates histogram data prior to transmission to a backend.

Type: [io.helidon.telemetry.otelconfig.MetricDefaultHistogramAggregationConfig](/apidocs/io.helidon.telemetry.otelconfig/io/helidon/telemetry/otelconfig/MetricDefaultHistogramAggregationConfig.html)

#### Configuration options

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
<td style="text-align: left;"><p><code>type</code></p></td>
<td style="text-align: left;"><p>MetricDefaultHistogramAggregationType (EXPLICIT_BUCKET_HISTOGRAM, BASE2_EXPONENTIAL_BUCKET_HISTOGRAM)</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Type of aggregation default.</p>
<p>Allowed values:</p>
<ul>
<li><p><code>EXPLICIT_BUCKET_HISTOGRAM</code>: Explicit buckets.</p></li>
<li><p><code>BASE2_EXPONENTIAL_BUCKET_HISTOGRAM</code>: Base 2 exponential bucket.</p></li>
</ul></td>
</tr>
</tbody>
</table>

You can configure the explicit bucket boundaries for `EXPLICIT_BUCKET_HISTOGRAM` aggregation.

Type: [io.helidon.telemetry.otelconfig.ExplicitBucketHistogramAggregationConfig](/apidocs/io.helidon.telemetry.otelconfig/io/helidon/telemetry/otelconfig/ExplicitBucketHistogramAggregationConfig.html)

#### Configuration options

| key                 | type       | default value | description                 |
|---------------------|------------|---------------|-----------------------------|
| `bucket-boundaries` | double\[\] |               | Explicit bucket boundaries. |

Optional configuration options

You can configure the exponential histogram aggregation behavior.

Type: [io.helidon.telemetry.otelconfig.Base2ExponentialHistogramAggregationConfig](/apidocs/io.helidon.telemetry.otelconfig/io/helidon/telemetry/otelconfig/Base2ExponentialHistogramAggregationConfig.html)

#### Configuration options

| key           | type | default value | description                |
|---------------|------|---------------|----------------------------|
| `max-buckets` | int  |               | Maximum number of buckets. |
| `max-scale`   | int  |               | Maximum scale.             |

Optional configuration options

#### Metric Readers

An OpenTelemetry metric reader collects metric data in the server and then uses the associated metric exporter to send that data to the endpoint configured.

Type: [io.helidon.telemetry.otelconfig.MetricReaderConfig](/apidocs/io.helidon.telemetry.otelconfig/io/helidon/telemetry/otelconfig/MetricReaderConfig.html)

#### Configuration options

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
<td style="text-align: left;"><p><code>exporter</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Name of the configured metric exporter to use for this metric reader.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>type</code></p></td>
<td style="text-align: left;"><p>MetricReaderType (PERIODIC)</p></td>
<td style="text-align: left;"><p><code>MetricReaderType.PERIODIC</code></p></td>
<td style="text-align: left;"><p>Metric reader type.</p>
<p>Allowed values:</p>
<ul>
<li><p><code>PERIODIC</code>: Periodic metric reader type.</p></li>
</ul></td>
</tr>
</tbody>
</table>

The periodic reader supports the following settings.

Type: [io.helidon.telemetry.otelconfig.PeriodicMetricReaderConfig](/apidocs/io.helidon.telemetry.otelconfig/io/helidon/telemetry/otelconfig/PeriodicMetricReaderConfig.html)

#### Configuration options

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
<td style="text-align: left;"><p><code>exporter</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Name of the configured metric exporter to use for this metric reader.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>interval</code></p></td>
<td style="text-align: left;"><p>Duration</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Metric reader read interval.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>type</code></p></td>
<td style="text-align: left;"><p>MetricReaderType (PERIODIC)</p></td>
<td style="text-align: left;"><p><code>MetricReaderType.PERIODIC</code></p></td>
<td style="text-align: left;"><p>Metric reader type.</p>
<p>Allowed values:</p>
<ul>
<li><p><code>PERIODIC</code>: Periodic metric reader type.</p></li>
</ul></td>
</tr>
</tbody>
</table>

#### Metric Views

OpenTelemetry metric views allow you to influence how meters are aggregated for reporting to backend systems.

Type: [io.helidon.telemetry.otelconfig.ViewRegistrationConfig](/apidocs/io.helidon.telemetry.otelconfig/io/helidon/telemetry/otelconfig/ViewRegistrationConfig.html)

#### Configuration options

| key | type | default value | description |
|----|----|----|----|
| `aggregation` | Aggregation |   | Aggregation for the metric view, configurable as an io.helidon.telemetry.otelconfig.AggregationType: `DROP, DEFAULT, SUM, LAST_VALUE, EXPLICIT_BUCKET_HISTOGRAM, BASE2_EXPONENTIAL_BUCKET_HISTOGRAM`. |
| `attribute-filter` | Predicate |   | Attribute name filter, configurable as a string compiled as a regular expression using java.util.regex.Pattern. |
| `cardinality-limit` | int |   | Cardinality limit. |
| `description` | string |   | Metric view description. |
| `instrument-selector` | InstrumentSelector |   | Instrument selector, configurable using io.helidon.telemetry.otelconfig.InstrumentSelectorConfig. |
| `name` | string |   | Metrics view name. |

Optional configuration options

The instrument selector controls which meters this view reflects.

Type: [io.helidon.telemetry.otelconfig.InstrumentSelectorConfig](/apidocs/io.helidon.telemetry.otelconfig/io/helidon/telemetry/otelconfig/InstrumentSelectorConfig.html)

#### Configuration options

| key | type | default value | description |
|----|----|----|----|
| `meter-name` | string |   | Meter name. |
| `meter-schema-url` | string |   | Meter schema URL. |
| `meter-version` | string |   | Meter version. |
| `name` | string |   | Instrument name. |
| `type` | InstrumentType (COUNTER, UP_DOWN_COUNTER, HISTOGRAM, OBSERVABLE_COUNTER, OBSERVABLE_UP_DOWN_COUNTER, OBSERVABLE_GAUGE, GAUGE) |   | Instrument type. |
| `unit` | string |   | Instrument unit. |

Optional configuration options

### Controlling OpenTelemetry Logger Behavior

The settings under `signal.logging` prepare an OpenTelemetry \`LoggerProvider.

The sections below describe Helidon config settings that correspond directly to OpenTelemetry builders for the relevant OpenTelemetry type. Refer to the relevant OpenTelemetry documentation or Javadoc to understand the effect each setting has.

The next table describes the OpenTelemetry logging settings.

Type: [io.helidon.telemetry.otelconfig.OpenTelemetryLoggingConfig](/apidocs/io.helidon.telemetry.otelconfig/io/helidon/telemetry/otelconfig/OpenTelemetryLoggingConfig.html)

#### Configuration options

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
<td style="text-align: left;"><p><code>attributes</code></p></td>
<td style="text-align: left;"><p>AttributesBuilder</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Name/value pairs passed to OpenTelemetry.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>enabled</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Whether the OpenTelemetry logger should be enabled. (Passed to OpenTelemetry.)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>exporters</code></p></td>
<td style="text-align: left;"><p>Map&lt;string, LogRecordExporter&gt;</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Log record exporters.</p>
<p>The key in the map is a unique name—​of the user’s choice—​for the exporter config settings. The ProcessorConfig.exporters() config setting for a processor config specifies zero or more of these names to associate the exporters built from the exporter configs with the processor built from the processor config.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>log-limits</code></p></td>
<td style="text-align: left;"><p>LogLimits</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Log limits to apply to log transmission.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>minimum-severity</code></p></td>
<td style="text-align: left;"><p>Severity (UNDEFINED_SEVERITY_NUMBER, TRACE, TRACE2, TRACE3, TRACE4, DEBUG, DEBUG2, DEBUG3, DEBUG4, INFO, INFO2, INFO3, INFO4, WARN, WARN2, WARN3, WARN4, ERROR, ERROR2, ERROR3, ERROR4, FATAL, FATAL2, FATAL3, FATAL4)</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Minimum severity level of log records to process.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>processors</code></p></td>
<td style="text-align: left;"><p><a href="../../se/telemetry/../../config/io_helidon_telemetry_otelconfig_ProcessorConfig.xml">ProcessorConfig[]</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Settings for logging processors.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>trace-based</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Whether to include &lt;em&gt;only&lt;/em&gt; log records from traces which are sampled. Defaults to the OpenTelemetry default.</p></td>
</tr>
</tbody>
</table>

OpenTelemetry uses the following defaults:

| Setting            | OpenTelemetry default     |
|--------------------|---------------------------|
| `exporters`        | none                      |
| `minimum-severity` | undefined severity number |
| `processors`       | no-op processor           |
| `trace-based`      | `false`                   |

Default logging settings applied by OpenTelemetry

Refer to the earlier sections about [configuring attributes](#attributes-config) and [configuring processors and exporters](#exporters-and-processors).

Sections below explain how to set up the configuration that is specific to the logging signal:

- [Configuring Log Limits](#configuring-log-limits)

#### Configuring Log Limits

For defaults, Helidon defers to the OpenTelemetry defaults, listed below.

Type: [io.helidon.telemetry.otelconfig.LogLimitsConfig](/apidocs/io.helidon.telemetry.otelconfig/io/helidon/telemetry/otelconfig/LogLimitsConfig.html)

##### Configuration options

| key | type | default value | description |
|----|----|----|----|
| `max-attribute-value-length` | int |   | Maximum length of an attribute value. |
| `max-number-of-attributes` | int |   | Maximum number of attributes allowed. |

Optional configuration options

OpenTelemetry applies the following defaults:

| Setting | OpenTelemetry default |
|----|----|
| `max-attribute-value-length` | `Integer.MAX_VALUE` |
| `max-number-of-attributes` | 128 |
| `exporters` | [`otlp` with `grpc` protocol](https://opentelemetry.io/docs/languages/java/configuration/#properties-exporters) - see that web page’s "Properties: exporters, `otel.logger.exporter` property" section. |
| `log-limits` | \`max- |
| `processors` | [`otlp`](https://opentelemetry.io/docs/languages/java/configuration/#properties-logs) - see that web page’s "Properties: logs" section. |

Default log limit settings applied by OpenTelemetry

The following example illustrates some of the ways you can configure OpenTelemetry logger behavior. It is neither complete nor typical.

*Example OpenTelemetry Logger Configuration*

``` yaml
telemetry:
  service: test-tel-logging
  global: false
  signals:
    logging:                              
      minimum-severity: TRACE             
      log-limits:                         
        max-attribute-value-length: 20
        max-number-of-attributes: 14
      processors:                         
        - type: batch
          schedule-delay: PT10S
          max-queue-size: 15
          max-export-batch-size: 5
          timeout: PT30S
        - type: simple
      exporters:                          
        - name: exp-1
          endpoint: "http://host:1234"
```

- Introduces the logger configuration.

- Sets the minimum log level severity to of log messages to send to the backend system.

- Configures limits related to attributes that accompany log messages.

- Prescribes the logger processors.

- Prescribes the logger exporters.

#### Logger Exporters and Processors

You associate each logger processor with a logger exporter using the exporter’s name. See the [earlier section](#exporters-and-processors) for more information.

## Additional Information

### Helidon Documentation

- [Helidon Tracing](../../se/tracing.md)

### OpenTelemetry Documentation

- [Settings and defaults](https://opentelemetry.io/docs/languages/java/configuration/#properties-exporters)

- [OpenTelemetry Java SDK reference](https://opentelemetry.io/docs/languages/java/sdk)

- [HTTP semantic conventions](https://github.com/open-telemetry/semantic-conventions/blob/v1.58.0/docs/http/http-spans.md#http-server)

- [Intro to OpenTelemetry Java](https://opentelemetry.io/docs/languages/java/intro/)
