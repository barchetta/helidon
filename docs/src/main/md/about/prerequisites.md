Everything you need to get started with Helidon is listed here.

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

# Setting `JAVA_HOME`

<div class="formalpara">

<div class="title">

Setting `JAVA_HOME`

</div>

``` bash
# On Mac
export JAVA_HOME=`/usr/libexec/java_home -v 21`

# On Linux
# Use the appropriate path to your JDK
export JAVA_HOME=/usr/lib/jvm/jdk-21
```

</div>

# Try the Quickstart Examples

Now you are ready to try the Quickstart Examples:

1.  [Helidon MP Quickstart Example](../mp/guides/quickstart.md)

2.  [Helidon SE Quickstart Example](../se/guides/quickstart.md)

> [!TIP]
> See [About Helidon](introduction.md) for more information on the
> differences between Helidon MP and SE.

> [!TIP]
> See [Helidon on Windows](windows.md) for some tips on using Helidon
> on Windows.
