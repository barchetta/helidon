# Overview

> [!NOTE]
> Micrometer integration is deprecated beginning in Helidon 4.1 and is planned for removal in a future major release. Please use the [Helidon neutral metrics API](../../se/metrics/metrics.md).

Helidon {h1-prefix} simplifies how you can use Micrometer for application-specific metrics:

- The endpoint `/micrometer`: A configurable endpoint that exposes metrics according to which Micrometer meter registry responds to the HTTP request.

- The `MicrometerSupport` class: A convenience class for enrolling Micrometer meter registries your application creates explicitly or for selecting which built-in Micrometer meter registries to use.

- Configuration to tailor the Prometheus and other Micrometer meter registries.

In Helidon {helidon-version}, Micrometer support is separate from the Helidon {h1-prefix} metrics API and the built-in Helidon metrics.

## Maven Coordinates

To enable Micrometer support, add the following dependency to your project’s `pom.xml` (see [Managing Dependencies](../../about/managing-dependencies.md)).

``` xml
<dependency>
    <groupId>io.helidon.integrations.micrometer</groupId>
    <artifactId>helidon-integrations-micrometer</artifactId>
</dependency>
```

Micrometer supports different types of meter registries which have different output styles and formats. Helidon provides built-in support for the Prometheus meter registry. To use other meter registry types, you will need to add dependencies for them to your `pom.xml` and, optionally, add code to your application or add configuration to set them up as you wish.

### Overriding Defaults for Built-in Meter Registry Types

Unless you specify otherwise, Helidon uses defaults for any built-in Micrometer meter registry. For example, Helidon configures the built-in Prometheus registry using `PrometheusConfig.DEFAULT`.

To use configuration to control the selection and behavior of Helidon’s built-in Micrometer meter registries, include in your configuration (such as `application.yaml`) a `micrometer.builtin-registries` section.

*Enroll Prometheus built-in meter registry using default configuration*

``` yaml
micrometer:
  builtin-registries:
    - type: prometheus
```

*Enroll Prometheus built-in meter registry with non-default configuration*

``` yaml
micrometer:
  builtin-registries:
    - type: prometheus
      prefix: myPrefix
```

Note that the first config example is equivalent to the default Helidon Micrometer behavior; Helidon by default supports the Prometheus meter registry.

The configuration keys that are valid for the `builtin-registries` child entries depend on the type of Micrometer meter registry. For example, support in Helidon for the [Prometheus meter registry]({micrometer-javadoc-registry-prometheus-base-url}/PrometheusConfig.md) respects the `prefix` configuration setting but other meter registries might not and might support other settings. Refer to the documentation for the meter registry you want to configure to find out what items apply to that registry type.

Helidon does not validate the configuration keys you specify for meter registries.

### Accessing the Helidon Micrometer Endpoint

Your application can easily have Helidon create a REST endpoint which clients can access to retrieve Micrometer metrics, by default at the `/micrometer` endpoint.

Within Helidon, each type of meter registry is paired with some code that examines the incoming HTTP request to `/micrometer` and decides whether the request matches up with the associated meter registry. The first pairing that accepts the request returns the response. You will need to take advantage of this if your application uses additional meter registries beyond what Helidon automatically provides *and* you want those meter registries reflected in the output from the `/micrometer` REST endpoint.

## Configuration

You can configure the Helidon Micrometer REST service as you can other built-in Helidon services by adding configuration settings under the `micrometer` top-level key.

### Configuration options

By default, Helidon Micrometer integration exposes the `/micrometer` endpoint. You can override the path using the [`Builder`]({micrometer-javadoc-base-url}/MicrometerSupport.Builder.md) or the `micrometer.web-context` configuration key.

*Overriding the default Micrometer path*

``` yaml
micrometer:
  web-context: my-micrometer
```

can create, look up, and update metrics programmatically using the Micrometer `MeterRegistry` API. The [Micrometer concepts document]({micrometer-api-url}) provides a good starting point for learning how to use Micrometer’s interfaces and classes.

Helidon {flavor-uc} includes an [example application]({helidon-github-examples-url}/integrations/micrometer/se) which uses Micrometer support.
