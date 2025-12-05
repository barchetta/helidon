The [OpenAPI specification]({openapi-spec-url}) defines a standard way
to express the interface exposed by a REST service.

The [MicroProfile OpenAPI spec]({microprofile-open-api-spec-url})
explains how MicroProfile embraces OpenAPI, adding annotations,
configuration, and a service provider interface (SPI).

The OpenAPI support in Helidon {flavor-uc} performs two main tasks:

- Build an in-memory model of the REST API your service implements.

- Expose the model in text format (YAML or JSON) via the `/openapi`
  endpoint.

To construct the model, Helidon gathers information about the service
API from

\<dependency\> \<groupId\>io.helidon.microprofile.openapi\</groupId\>
\<artifactId\>helidon-microprofile-openapi\</artifactId\>
\<scope\>runtime\</scope\> \</dependency\>

# Furnish OpenAPI information about your endpoints

# Accessing the REST Endpoint

Once you have added the {flavor-uc} OpenAPI dependency to your your
application responds to the built-in endpoint — `/openapi` — and returns
the OpenAPI document describing the endpoints in your application.

default format of the OpenAPI document is YAML. There is not yet an
adopted IANA YAML media type, but a proposed one specifically for
OpenAPI documents that has some support is
`application/vnd.oai.openapi`. That is what Helidon returns by default.

In addition, a client can specify the HTTP header `Accept` as either
`application/vnd.oai.openapi+json` or `application/json` to request
JSON. Alternatively, the client can pass the query parameter `format` as
either `JSON` or `YAML` to receive `application/json` or
`application/vnd.oai.openapi` (YAML) output, respectively.

The [MicroProfile OpenAPI
JavaDocs]({microprofile-open-api-javadoc-base-url}) give full details of
the classes and interfaces you can use in your code.

# Building the Jandex index

A Jandex index stores information about the classes and methods in your
app and what annotations they have. It allows CDI to process annotations
faster during your application’s start-up, and OpenAPI uses the Jandex
index to discover details about the types in your resource method
signatures.

## Indexing your project

Add an invocation of the [Jandex maven
plug-in](https://github.com/smallrye/jandex/tree/main/maven-plugin) to
the `<build><plugins>` section of your `pom.xml` if it is not already
there:

``` xml
<plugin>
    <groupId>io.smallrye</groupId>
    <artifactId>jandex-maven-plugin</artifactId>
   <executions>
      <execution>
        <id>make-index</id>
      </execution>
    </executions>
</plugin>
```

When you build your app the plug-in generates the Jandex index
`META-INF/jandex.idx` and `maven` adds it to the application JAR.

## Indexing dependencies

Invoking the Jandex plug-in as described above indexes only the types in
your project. Some dependencies might include their own Jandex index
and, in that case, OpenAPI finds information about the types in the
dependency as well.

But if the signatures of your resource methods refer to types from
dependencies that do not have their own indexes then you should
customize how you use the plug-in.

The example below tailors the Jandex plug-in configuration to scan not
only the current project but another dependency and to index a specific
type from it.

``` xml
<execution>
    <id>make-index</id>
    <configuration> 
        <fileSets>
            <fileSet>
                <dependency> 
                    <groupId>jakarta.ws.rs</groupId>
                    <artifactId>jakarta.ws.rs-api</artifactId>
                </dependency>
                <includes> 
                    <include>**/MediaType.class</include>
                </includes>
            </fileSet>
        </fileSets>
    </configuration>
</execution>
```

- Augments the default configuration.

- Adds a `fileSet` in the form of a `dependency` that is already
  declared in your project.

- Selects the type or types from the `fileSet` you want to include in
  the generated index.

You can add more than one dependency and scan for more than a single
type. See the [Helidon MP OpenAPI expanded Jandex
example]({helidon-github-examples-url}/microprofile/openapi/expanded-jandex)
for more information and a complete project that indexes a dependency.

> [!NOTE]
> If your `pom.xml` *does not* create the Jandex index then the Helidon
> MP OpenAPI runtime automatically creates one in memory during app
> start-up. This slows down your app start-up and, depending on how CDI
> is configured, might inadvertently miss information.
>
> We *strongly recommend* using the Jandex plug-in to build the index
> into your app.
>
> Further, if your resource method signatures refer to types from
> outside your project we *strongly recommend* that you augment the
> Jandex plug-in invocation to include the dependencies and types your
> API uses. If you do not do so the resulting generated OpenAPI document
> is correct, but types that cannot be found are declared as `object` in
> the resulting OpenAPI model. This means your OpenAPI document contains
> less information about the types in your API than it otherwise could.
