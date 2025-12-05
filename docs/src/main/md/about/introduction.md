# What is Helidon?

- [What is Helidon?](#_what_is_helidon)

- [Helidon Flavors](#_helidon_flavors)

  - [What flavor shall I use?](#_what_flavor_shall_i_use)

- [Prerequisites](#_prerequisites)

- [Next Steps](#_next_steps)

# What is Helidon?

[Helidon](https://helidon.io) is a collection of Java libraries for
writing microservices.

Helidon is open source under the Apache license. Sources are available
on [GitHub](https://github.com/oracle/helidon/tree/main).

Helidon is cloud-native ready. It provides fast start-up time and has
low memory consumption and a small disk footprint. It also comes with a
full observability stack out of the box including health checks,
metrics, tracing and logging.

Helidon fully supports GraalVM native image allowing you to build a
native executable from your Java application.

Helidon applications are stand-alone Java applications running in their
own JVM and powered by the Helidon WebServer.

# Helidon Flavors

Helidon comes in two flavors: **Helidon SE** and **Helidon MP**. Think
about these flavors as frameworks providing similar functionality but
offering different developer experiences.

| **Helidon SE** | **Helidon MP** |
|----|----|
| Gives you full transparency and puts you in control. | Built on top of the Helidon SE libraries and provides a platform that is familiar to enterprise Java developers. |
| Microframework model with a very small footprint and limited functionality (~7 MB). | [MicroProfile](https://projects.eclipse.org/proposals/eclipse-microprofile) implementation; slightly larger footprint than SE (~13 MB). |
| Helidon SE is Helidon’s foundational set of APIs. As of Helidon 4, virtual threads have enabled these APIs to change from asynchronous to blocking. This results in much simpler code that is easier to write, maintain, debug and understand.. | Declarative style with dependency injection. |
| Transparent "no magic" development experience; pure java application development with no annotations and no dependency injections. | Developer experience similar to that of Spring Boot, Jakarta EE and MicroProfile; layers on some Jakarta EE components (CDI, JAX-RS, JSON-P, JSON-B). |
| Learn more about [Helidon SE](../se/introduction.md). | Learn more about [Helidon MP](../mp/introduction.md). |

To help illustrate the differences, below are two samples implementing a
simple RESTful service. One uses Helidon SE, the other Helidon MP.

<div class="formalpara">

<div class="title">

Helidon SE sample

</div>

``` java
WebServer.builder()
        .addRouting(HttpRouting.builder()
                            .get("/greet", (req, res)
                                    -> res.send("Hello World!")))
        .build()
        .start();
```

</div>

<div class="formalpara">

<div class="title">

Helidon MP sample

</div>

``` java
@Path("hello")
public class HelloWorld {
    @GET
    public String hello() {
        return "Hello World";
    }
}
```

</div>

Even though Helidon MP supports Jakarta EE APIs it does not require an
application server. Helidon MP applications are stand-alone Java
applications running in their own JVM powered by Helidon WebServer.

## What flavor shall I use?

Use Helidon SE if

- Performance is your main goal.

- Your application is heavily using concurrency.

- You are not planning to use any CDI-based components.

- You want to use a minimum number of third-party dependencies.

Use Helidon MP if

- You want to base your application on modern enterprise Java standards
  such as Jakarta EE and MicroProfile.

- You are familiar with Java EE, Jakarta EE or Spring Boot and would
  like to have a similar development experience.

- You are migrating existing Java EE/Jakarta EE application to
  microservices.

- You are planning to use CDI components or extensions.

- You are planning to use JPA for data access and Jersey (JAX-RS) for
  RESTful services.

> [!NOTE]
> If you don’t know which Helidon flavor to use – use **Helidon MP**.

# Prerequisites

Helidon requires Java and Maven. You might also need Docker and
Kubernetes depending on how you plan to deploy your services.

|  |  |
|----|----|
| [Java SE 21](https://www.oracle.com/technetwork/java/javase/downloads) ([Open JDK 21](http://jdk.java.net)) | Helidon requires Java 21+ (25+ recommended). |
| [Maven 3.8+](https://maven.apache.org/download.cgi) | Helidon requires Maven 3.8+. |
| [Docker 18.09+](https://docs.docker.com/install/) | If you want to build and run Docker containers. |
| [Kubectl 1.16.5+](https://kubernetes.io/docs/tasks/tools/install-kubectl/) | If you want to deploy to Kubernetes, you need `kubectl` and a Kubernetes cluster (you can [install one on your desktop](../about/kubernetes.md). |

Prerequisite product versions for Helidon 4.4.0-SNAPSHOT

We also strongly suggest installing the [Helidon CLI](cli.md) (command
line interface) which helps in generating and building Helidon projects.

# Upgrade

To upgrade your current version of Helidon, follow the `Upgrade Guides`:

To upgrade from Helidon 3.x to 4.x:

- [Helidon SE 4x Upgrade
  Guide](../se/guides/upgrade_4x.md)

- [Helidon MP 4x Upgrade
  Guide](../mp/guides/upgrade_4x.md)

To upgrade from Helidon 2.x to 3.x:

- [Helidon SE 3x Upgrade
  Guide](../se/guides/upgrade_3x.md)

- [Helidon MP 3x Upgrade
  Guide](../mp/guides/upgrade_3x.md)

To upgrade from Helidon 1.x to 2.x:

- [Helidon SE 2x Upgrade
  Guide](../se/guides/upgrade.md)

- [Helidon MP 2x Upgrade
  Guide](../mp/guides/upgrade.md)

# Next Steps

Choose a Helidon flavor to explore and start using it. Check out the
following:

- [Helidon SE
  Documentation](../se/introduction.md)

- [Helidon MP
  Documentation](../mp/introduction.md)
