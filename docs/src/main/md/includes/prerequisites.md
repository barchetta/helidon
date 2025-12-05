# Prerequisites

|  |  |
|----|----|
| [Java SE 21](https://www.oracle.com/technetwork/java/javase/downloads) ([Open JDK 21](http://jdk.java.net)) | Helidon requires Java 21+ (25+ recommended). |
| [Maven 3.8+](https://maven.apache.org/download.cgi) | Helidon requires Maven 3.8+. |
| [Docker 18.09+](https://docs.docker.com/install/) | If you want to build and run Docker containers. |
| [Kubectl 1.16.5+](https://kubernetes.io/docs/tasks/tools/install-kubectl/) | If you want to deploy to Kubernetes, you need `kubectl` and a Kubernetes cluster (you can [install one on your desktop](../about/kubernetes.md). |

Prerequisite product versions for Helidon {helidon-version}

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

|  |  |
|----|----|
| [Java SE 21](https://www.oracle.com/technetwork/java/javase/downloads) ([Open JDK 21](http://jdk.java.net)) | Helidon requires Java 21+ (25+ recommended). |
| [Maven 3.8+](https://maven.apache.org/download.cgi) | Helidon requires Maven 3.8+. |
| [Docker 18.09+](https://docs.docker.com/install/) | If you want to build and run Docker containers. |
| [Kubectl 1.16.5+](https://kubernetes.io/docs/tasks/tools/install-kubectl/) | If you want to deploy to Kubernetes, you need `kubectl` and a Kubernetes cluster (you can [install one on your desktop](../about/kubernetes.md). |
| [Helidon CLI](../about/cli.md) | If you want to use the Helidon CLI to create and build your application |

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

|  |  |
|----|----|
| [Java SE 21](https://www.oracle.com/technetwork/java/javase/downloads) ([Open JDK 21](http://jdk.java.net)) | Helidon requires Java 21+ (25+ recommended). |
| [Maven 3.8+](https://maven.apache.org/download.cgi) | Helidon requires Maven 3.8+. |
| [Docker 18.09+](https://docs.docker.com/install/) | If you want to build and run Docker containers. |
| [Kubectl 1.16.5+](https://kubernetes.io/docs/tasks/tools/install-kubectl/) | If you want to deploy to Kubernetes, you need `kubectl` and a Kubernetes cluster (you can [install one on your desktop](../about/kubernetes.md). |
| [Helm](https://github.com/helm/helm) | To manage Kubernetes applications. |

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

|  |  |
|----|----|
| [Java SE 21](https://www.oracle.com/technetwork/java/javase/downloads) ([Open JDK 21](http://jdk.java.net)) | Helidon requires Java 21+ (25+ recommended). |
| [Maven 3.8+](https://maven.apache.org/download.cgi) | Helidon requires Maven 3.8+. |
| [Docker 18.09+](https://docs.docker.com/install/) | If you want to build and run Docker containers. |
| [Kubectl 1.16.5+](https://kubernetes.io/docs/tasks/tools/install-kubectl/) | If you want to deploy to Kubernetes, you need `kubectl` and a Kubernetes cluster (you can [install one on your desktop](../about/kubernetes.md). |
| [curl](https://curl.se/download.html) | (Optional) for testing |

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

|  |  |
|----|----|
| [Java SE 21](https://www.oracle.com/technetwork/java/javase/downloads) ([Open JDK 21](http://jdk.java.net)) | Helidon requires Java 21+ (25+ recommended). |
| [Maven 3.8+](https://maven.apache.org/download.cgi) | Helidon requires Maven 3.8+. |
| [Docker 18.09+](https://docs.docker.com/install/) | If you want to build and run Docker containers. |
| [Kubectl 1.16.5+](https://kubernetes.io/docs/tasks/tools/install-kubectl/) | If you want to deploy to Kubernetes, you need `kubectl` and a Kubernetes cluster (you can [install one on your desktop](../about/kubernetes.md). |
| [GraalVM for JDK 21](https://www.graalvm.org/release-notes/JDK_21/) | `native-image` support requires GraalVM for JDK 21. When running in the Graal JVM (not native-image) Helidon supports GraalVM for JDK 21 or newer. |

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

|  |  |
|----|----|
| Linux/x64 or Linux/ARM64 | While CRaC snapshotting can be simulated on MacOS or Windows, full CRaC functionality is only available on Linux/x64 and Linux/ARM64. |
| [Maven 3.8+](https://maven.apache.org/download.cgi) | Helidon requires Maven 3.8+. |
| [Azul Zulu JDK CRaC 21+](https://www.azul.com/downloads/?version=java-21-lts&package=jdk-crac#zulu) | Zulu Warp CRaC engine allows snapshotting without elevated privileges |
