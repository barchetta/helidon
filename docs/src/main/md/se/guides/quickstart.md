This guide describes a basic example of an Helidon SE application using
Docker and Kubernetes.

# What You Need

For this 5 minute tutorial, you will need the following:

|  |  |
|----|----|
| [Java SE 21](https://www.oracle.com/technetwork/java/javase/downloads) ([Open JDK 21](http://jdk.java.net)) | Helidon requires Java 21+ (25+ recommended). |
| [Maven 3.8+](https://maven.apache.org/download.cgi) | Helidon requires Maven 3.8+. |
| [Docker 18.09+](https://docs.docker.com/install/) | If you want to build and run Docker containers. |
| [Kubectl 1.16.5+](https://kubernetes.io/docs/tasks/tools/install-kubectl/) | If you want to deploy to Kubernetes, you need `kubectl` and a Kubernetes cluster (you can [install one on your desktop](../../about/kubernetes.md). |

Prerequisite product versions for Helidon 4.4.0-SNAPSHOT

<div class="formalpara">

<div class="title">

Verify Prerequisites

</div>

``` bash
java -version
mvn --version
docker --version
kubectl version
```

</div>

<div class="formalpara">

<div class="title">

Setting JAVA_HOME

</div>

``` bash
# On Mac
export JAVA_HOME=`/usr/libexec/java_home -v 21`

# On Linux
# Use the appropriate path to your JDK
export JAVA_HOME=/usr/lib/jvm/jdk-21
```

</div>

# Generate The Project

Generate the project sources using the Helidon Maven archetype. The
result is a simple project that shows the basics of a Helidon SE
application using simple WebServer routing rules.

<div class="formalpara">

<div class="title">

Run the Maven archetype

</div>

``` bash
mvn -U archetype:generate -DinteractiveMode=false \
    -DarchetypeGroupId=io.helidon.archetypes \
    -DarchetypeArtifactId=helidon-quickstart-se \
    -DarchetypeVersion=4.4.0-SNAPSHOT \
    -DgroupId=io.helidon.examples \
    -DartifactId=helidon-quickstart-se \
    -Dpackage=io.helidon.examples.quickstart.se
```

</div>

> [!TIP]
> If you are using an earlier version of Helidon and the above command
> fails with `java.lang.NoSuchMethodError` then you can work-around the
> error by replacing `archetype:generate` with
> `org.apache.maven.plugins:maven-archetype-plugin:3.2.1:generate`. Or
> use the helidon CLI.

<div class="formalpara">

<div class="title">

Or alternatively run the helidon CLI

</div>

``` bash
helidon init --batch -Dflavor=mp -Dapp-type=quickstart
```

</div>

The archetype generates a Maven project in your current directory (for
example, `helidon-quickstart-se`). Change into this directory.

``` bash
cd helidon-quickstart-se
```

> [!TIP]
> If you want to use the generated project as a starter for your own
> application, then you can replace groupId, artifactId and package with
> values appropriate for your application.

<div class="formalpara">

<div class="title">

Build the Application

</div>

``` bash
mvn package
```

</div>

The project builds an application jar for the example and saves all
runtime dependencies in the `target/libs` directory. This means you can
easily start the application by running the application jar file:

<div class="formalpara">

<div class="title">

Run the application

</div>

``` bash
java -jar target/helidon-quickstart-se.jar
```

</div>

The example is a very simple "Hello World" greeting service. It supports
GET requests for generating a greeting message, and a PUT request for
changing the greeting itself. The response is encoded using JSON. For
example:

<div class="formalpara">

<div class="title">

Try the Application

</div>

``` bash
curl -X GET http://localhost:8080/greet
{"message":"Hello World!"}

curl -X GET http://localhost:8080/greet/Joe
{"message":"Hello Joe!"}

curl -X PUT -H "Content-Type: application/json" -d '{"greeting" : "Hola"}' http://localhost:8080/greet/greeting

curl -X GET http://localhost:8080/greet/Jose
{"message":"Hola Jose!"}
```

</div>

# Health and Metrics

Helidon provides built-in support for health and metrics endpoints.

<div class="formalpara">

<div class="title">

Health

</div>

``` bash
curl -sv -X GET http://localhost:8080/observe/health
```

</div>

Notice we use the `-v` option to curl so that you can see that the
health endpoint returns 204 (No Content) by default.

<div class="formalpara">

<div class="title">

Metrics in Prometheus Format

</div>

``` bash
curl -s -X GET http://localhost:8080/observe/metrics
```

</div>

<div class="formalpara">

<div class="title">

Metrics in JSON Format

</div>

``` bash
curl -H 'Accept: application/json' -X GET http://localhost:8080/observe/metrics
```

</div>

# Build a Docker Image

The project also contains a Dockerfile so that you can easily build and
run a Docker image. To build the Docker image, you need to have Docker
installed and running on your system.

<div class="formalpara">

<div class="title">

Docker build

</div>

``` bash
docker build -t helidon-quickstart-se .
```

</div>

<div class="formalpara">

<div class="title">

Run Docker Image

</div>

``` bash
docker run --rm -p 8080:8080 helidon-quickstart-se:latest
```

</div>

Then you can try the application as you did before.

# Deploy the application to Kubernetes

If you don’t have access to a Kubernetes cluster, you can [install one
on your desktop](../../about/kubernetes.md). Then deploy the example:

<div class="formalpara">

<div class="title">

Verify connectivity to cluster

</div>

``` bash
kubectl cluster-info
kubectl get nodes
```

</div>

<div class="formalpara">

<div class="title">

Deploy the application to Kubernetes

</div>

``` bash
kubectl create -f app.yaml
kubectl get pods # Wait for quickstart pod to be RUNNING
```

</div>

The step above created a service that is exposed into any node port.
Lookup the service to find the port.

<div class="formalpara">

<div class="title">

Lookup the service

</div>

``` bash
kubectl get service helidon-quickstart-se
```

</div>

Note the PORTs. You can now exercise the application as you did before
but use the second port number (the NodePort) instead of 8080. For
example:

``` bash
curl -X GET http://localhost:31431/greet
```

After you’re done, cleanup.

<div class="formalpara">

<div class="title">

Remove the application from Kubernetes

</div>

``` bash
kubectl delete -f app.yaml
```

</div>

# Building Native and Custom Runtime Images

Helidon also includes support for GraalVM Native Images and Java Custom
Runtime Images. For more information see:

- [GraalVM Native Images](graalnative.md)

- [Custom Runtime Images using `jlink`](jlink-image.md)

# The Helidon CLI

With the Helidon CLI you can create additional types of Helidon
applications and use the "dev loop" to do fast, iterative development.
[Try it now](../../about/cli.md).
