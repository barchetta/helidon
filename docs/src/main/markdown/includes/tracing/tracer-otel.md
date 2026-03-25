# Configuring OpenTelemetry Tracing

Helidon supports configuration of OpenTelemetry and OpenTelemetry tracing in two primary ways: using tracing or using telemetry.

> [!NOTE]
> If you provide settings under both `telemetry` and `tracing`, Helidon uses the `telemetry` settings. Specifying both does not confuse Helidon but it might confuse users.

*Dependency for OpenTelemetry support using tracing*

``` xml
<dependency>
    <groupId>io.helidon.tracing.providers</groupId>
    <artifactId>helidon-tracing-providers-opentelemetry</artifactId>
</dependency>
```

## Configuring OpenTelemetry Tracing

## Configuration options

| Key | Kind | Type | Default Value | Description |
|----|----|----|----|----|
| <span id="aec0bf-exporter-type"></span> [`exporter-type`](../../config/io_helidon_tracing_providers_opentelemetry_OtlpExporterProtocolType.md) | `VALUE` | `i.h.t.p.o.OtlpExporterProtocolType` | `GRPC` | Type of OTLP exporter to use for pushing span data |
| <span id="a0fe59-propagators"></span> `propagators` | `LIST` | `i.h.t.p.o.O.CustomMethods` |   | Context propagators |

- Specifies the OpenTelemetry service name.

- Indicates the configured tracer *should not* be made the global tracer (defaults to `true`).

- Assigns an integer-valued tag `example` the value `1`.

- Assigns a string-valued tag `direction` the value `north`.

By default, Helidon tracing support for OpenTelemetry uses OpenTelemetry’s OTLP gRPC exporter. Alternatively, you can choose to use OpenTelemetry’s HTTP exporter using protobuf by setting `exporter-type` to `http/proto`. To use other exporters OpenTelemetry offers, use the Helidon `telemetry` configuration instead of `tracing`.
