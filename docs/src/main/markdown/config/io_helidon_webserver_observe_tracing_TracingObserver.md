# TracingObserver (webserver.observe.tracing) Configuration

Type: [io.helidon.webserver.observe.tracing.TracingObserver](/apidocs/io.helidon.webserver.observe.tracing/io/helidon/webserver/observe/tracing/TracingObserver.html)

*Config key*

``` text
tracing
```

This type provides the following service implementations:

- `io.helidon.webserver.observe.spi.ObserveProvider`

## Configuration options

| key | type | default value | description |
|----|----|----|----|
| `enabled` | boolean | `true` | Whether this observer is enabled. |
| `env-config` | TracingConfig | `TracingConfig.ENABLED` | Use the provided configuration as a default for any request. |
| `paths` | PathTracingConfig\[\] | `new @java.util.ArrayList@(@java.util.List@.of(PathTracingConfig.builder() .path("/metrics/") .tracingConfig(TracingConfig.DISABLED) .build(), PathTracingConfig.builder() .path("/observe/metrics/") .tracingConfig(TracingConfig.DISABLED) .build(), PathTracingConfig.builder() .path("/health/") .tracingConfig(TracingConfig.DISABLED) .build(), PathTracingConfig.builder() .path("/observe/health/") .tracingConfig(TracingConfig.DISABLED) .build(), PathTracingConfig.builder() .path("/openapi/") .tracingConfig(TracingConfig.DISABLED) .build(), PathTracingConfig.builder() .path("/observe/openapi/") .tracingConfig(TracingConfig.DISABLED) .build()))` | Path specific configuration of tracing. |
| `wait-tracing-enabled` | boolean | `false` | Whether waiting due to concurrency limit constraints should be traced. |
| `weight` | double | `900.0` | Weight of the feature registered with WebServer. Changing weight may cause tracing to be executed at a different time (such as after security, or even after all routes). Please understand feature weights before changing this order. |

Optional configuration options
