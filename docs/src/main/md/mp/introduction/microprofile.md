Complete these tasks to get started with your MicroProfile application.

# Getting Started with Helidon MicroProfile

Helidon provides a MicroProfile server implementation
(`io.helidon.microprofile.server`) that encapsulates the Helidon
WebServer. You can either instantiate the server directly as is done in
the [Helidon MP Quickstart example](../guides/quickstart.md) or use its
built-in `main` as shown below.

## Maven Coordinates

The [Managing Dependencies](../../about/managing-dependencies.md) page
describes how you should declare dependency management for Helidon
applications. Then declare the following dependency in your project:

<div class="formalpara">

<div class="title">

Maven Dependency for full MicroProfile

</div>

``` xml
<dependency>
  <groupId>io.helidon.microprofile.bundles</groupId>
  <artifactId>helidon-microprofile</artifactId>
</dependency>
```

</div>

The above dependency adds all the features available in MicroProfile. If
you want to start with a smaller core set of features then you can use
the `core` bundle instead. This bundle includes the base feature in
MicroProfile (such as JAX-RS, CDI, JSON-P/B, and Config) and leaves out
some of the additional features such as Metrics and Tracing. You can add
those dependencies individually if you choose.

<div class="formalpara">

<div class="title">

Maven Dependency for MicroProfile core features only

</div>

``` xml
<dependency>
  <groupId>io.helidon.microprofile.bundles</groupId>
  <artifactId>helidon-microprofile-core</artifactId>
</dependency>
```

</div>

## Project files

Create a JAX-RS Resource class with at least one resource method.

<div class="formalpara">

<div class="title">

Sample JAX-RS Resource Class

</div>

``` java
@Path("/")
@RequestScoped
public class HelloWorldResource {
    @GET
    @Produces(MediaType.TEXT_PLAIN)
    public String message() {
        return "Hello World";
    }
}
```

</div>

And create a JAX-RS application.

<div class="formalpara">

<div class="title">

Sample JAX-RS Application

</div>

``` java
@ApplicationScoped
@ApplicationPath("/")
public class HelloWorldApplication extends Application {
    @Override
    public Set<Class<?>> getClasses() {
        return Set.of(
                HelloWorldResource.class
        );
    }
}
```

</div>

Add `beans.xml` in `src/main/resources/META-INF` so the CDI
implementation can pick up your classes.

<div class="formalpara">

<div class="title">

beans.xml

</div>

``` xml
<?xml version="1.0" encoding="UTF-8"?>
<beans/>
```

</div>

As a last step, add a main method to your application (or a dedicated
Main class) to start everything up.

<div class="formalpara">

<div class="title">

Sample JAX-RS Application

</div>

``` java
public static void main(String[] args) {
    io.helidon.microprofile.cdi.Main.main(args);
}
```

</div>

Run the main class. The server will start on port 7001 and serve your
resources.

## Adding Jandex

Jandex is an indexing tool for Weld (the CDI implementation used by
Helidon) that helps speed up the boot time of an application.

To use Jandex, configure a Maven plugin that adds the index to your JAR
file and a dependency on Jandex.

<div class="formalpara">

<div class="title">

jandex dependency

</div>

``` xml
<dependency>
    <groupId>io.smallrye</groupId>
    <artifactId>jandex</artifactId>
    <version>{version.plugin.jandex}</version>
</dependency>
```

</div>

<div class="formalpara">

<div class="title">

jandex plugin configuration

</div>

``` xml
<build>
    <plugins>
        <plugin>
            <groupId>io.smallrye</groupId>
            <artifactId>jandex-maven-plugin</artifactId>
            <version>3.1.2</version>
            <executions>
                <execution>
                    <id>make-index</id>
                    <goals>
                        <goal>jandex</goal>
                    </goals>
                    <phase>process-classes</phase>
                </execution>
            </executions>
        </plugin>
    </plugins>
</build>
```

</div>
