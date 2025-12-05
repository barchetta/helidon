In Helidon 4.x we have made some changes to APIs and runtime behavior.
This guide will help you upgrade a Helidon MP 3.x application to 4.x.

# Java 21 Runtime

Java 17 is no longer supported in Helidon 4. Java 21 or newer is
required (Java 25 or newer recommended). Please follow the instructions
in
[Prerequisites](../../about/prerequisites.md)
for proper installation.

Helidon 4 no longer uses Netty. Helidon MP is now running on Helidon
WebServer which is based on virtual threads technology, available in
Java 21.

# MicroProfile 6.0 support

MicroProfile 6.0 enables MicroProfile APIs to be used together with
Jakarta EE 10 Core Profile.

## MicroProfile specifications

Most of the MicroProfile specifications had relatively minor changes.
The exception is Metrics which had substantial changes.

- **MicroProfile Config 3.1**:

  Incompatible changes described in [MicroProfile Config 3.1
  Specification](https://download.eclipse.org/microprofile/microprofile-config-3.0.1/microprofile-config-spec-3.0.1.html#_incompatible_changes)

- **MicroProfile Fault Tolerance 4.0.2**:

  Incompatible changes described in [MicroProfile Fault Tolerance 4.0.2
  Specification](https://download.eclipse.org/microprofile/microprofile-fault-tolerance-4.0.2/microprofile-fault-tolerance-spec-4.0.2.html#_backward_incompatible_changes=)

- **MicroProfile Health 4.0**:

  Incompatible changes described in [MicroProfile Health 4.0
  Specification](https://download.eclipse.org/microprofile/microprofile-health-4.0/microprofile-health-spec-4.0.html#_incompatible_changes)

- **MicroProfile JWT Authentication 2.1**:

  Incompatible changes described in [MicroProfile JWT Authentication 2.1
  Specification](https://download.eclipse.org/microprofile/microprofile-jwt-auth-2.0/microprofile-jwt-auth-spec-2.0.html#_incompatible_changes)

- **MicroProfile Metrics 5.1.1**:

  Incompatible changes described in [MicroProfile Metrics 5.1.1
  Specification](https://download.eclipse.org/microprofile/microprofile-metrics-5.0.0/microprofile-metrics-spec-5.0.0.html#_incompatible_changes)

- **MicroProfile OpenAPI 3.1.1**:

  Incompatible changes described in [MicroProfile OpenAPI 3.1.1
  Specification](https://download.eclipse.org/microprofile/microprofile-open-api-3.1/microprofile-openapi-spec-3.1.html#incompatible_changes_30)

- **MicroProfile Rest Client 3.0**:

  Incompatible changes described in [MicroProfile Rest Client 3.0
  Specification](https://download.eclipse.org/microprofile/microprofile-rest-client-3.0/microprofile-rest-client-spec-3.0.html#_incompatible_changes)

- **MicroProfile Telemetry Tracing 1.1**:

  Incompatible changes described in [MicroProfile Telemetry Tracing 1.1
  Specification](https://download.eclipse.org/microprofile/microprofile-telemetry-1.0/tracing/microprofile-telemetry-tracing-spec-1.0.html#_incompatible_changes)

## Supported Jakarta EE specifications

- **CDI (Jakarta Contexts and Dependency Injection) 4.0**:

  Changes described in [CDI (Jakarta Contexts and Dependency Injection)
  4.0
  Specification](https://jakarta.ee/specifications/cdi/4.0/jakarta-cdi-spec-4.0.html#architecture)

- **JAX-RS (Jakarta RESTful Web Services) 3.1**:

  Changes described in [JAX-RS (Jakarta RESTful Web Services) 3.1
  Specification](https://download.eclipse.org/microprofile/microprofile-rest-client-3.0/microprofile-rest-client-spec-3.0.html#_incompatible_changes)

- **JSON-B (Jakarta JSON Binding) 3.0**:

  Changes described in [JSON-B (Jakarta JSON Binding) 3.0
  Specification](https://jakarta.ee/specifications/jsonb/2.0/jakarta-jsonb-spec-2.0.html#change-log)

- **JSON-P (Jakarta JSON Processing) 2.1**:

  Changes described in [JSON-P (Jakarta JSON Parsing) 2.1
  Specification](https://jakarta.ee/specifications/jsonp/2.1/apidocs/)

- **Jakarta Annotations 2.1.1**:

  Full information in [Jakarta Annotations 2.1.1
  Specification](https://jakarta.ee/specifications/annotations/2.0/annotations-spec-2.0.html)

- **Jakarta Persistence API 3.1**:

  Changes described in [Jakarta Persistence API 3.1
  Specification](https://jakarta.ee/specifications/persistence/3.0/jakarta-persistence-spec-3.0.html#revision-history)

- **Jakarta Transactions API 2.0**:

  Changes described in [Jakarta Transactions API 2.0
  Specification](https://jakarta.ee/specifications/transactions/2.0/jakarta-transactions-spec-2.0.html#revision-history)

- **Jakarta WebSocket API 2.1**:

  Changes described in [Jakarta WebSocket API 2.1
  Specification](https://jakarta.ee/specifications/websocket/2.0/websocket-spec-2.0.html#changes)

- **Jakarta Bean Validation 3.0**:

  Changes described in [Jakarta Bean Validation 3.0
  Specification](https://jakarta.ee/specifications/bean-validation/2.0/bean-validation_2.0.html#changelog)

> [!NOTE]
> Please, read each specification carefully for incompatible changes!

## Significant changes

### Jandex

Jandex group id was `org.jboss.jandex` and now is `io.smallrye`.

### Testing

Testing is now in a new package. It was:

``` xml
<dependency>
    <groupId>io.helidon.microprofile.tests</groupId>
    <artifactId>helidon-microprofile-tests-junit5</artifactId>
    <scope>test</scope>
</dependency>
```

Now is:

``` xml
<dependency>
    <groupId>io.helidon.microprofile.testing</groupId>
    <artifactId>helidon-microprofile-testing-junit5</artifactId>
    <scope>test</scope>
</dependency>
```

And the Java package has changed from
`io.helidon.microprofile.tests.junit5` to
`io.helidon.microprofile.testing.junit5`

## Logging

The Helidon console handler has changed from
`io.helidon.common.HelidonConsoleHandler` to
`io.helidon.logging.jul.HelidonConsoleHandler`.

If you use this handler in your `logging.properties` you will need to
update it and add the following dependency:

``` xml
<dependency>
    <groupId>io.helidon.logging</groupId>
    <artifactId>helidon-logging-jul</artifactId>
    <scope>runtime</scope>
</dependency>
```

# Conclusion

Please proceed to [Helidon MP Introduction](../introduction.md) to find
more information and documentation about each module.
