This guide describes how to create a sample AI powered Helidon
{flavor-uc} project with LangChain4j integration.

# Introduction

[LangChain4j](https://github.com/langchain4j/langchain4j) is a Java
framework for building AI-powered applications using Large Language
Models (LLMs). It provides seamless integration with multiple LLM
providers, including OpenAI, Cohere, Hugging Face, and others. Key
features include AI Services for easy model interaction, support for
Retrieval-Augmented Generation (RAG) to enhance responses with external
data, and tools for working with embeddings and knowledge retrieval.

Helidon provides a LangChain4j integration module that simplifies the
use of LangChain4j in Helidon applications.

> [!NOTE]
> LangChain4j integration is a preview feature. The APIs shown here are
> subject to change. These APIs will be finalized in a future release of
> Helidon.

# What you need

For this 15 minute tutorial, you will need the following:

|  |  |
|----|----|
| [Java SE 21](https://www.oracle.com/technetwork/java/javase/downloads) ([Open JDK 21](http://jdk.java.net)) | Helidon requires Java 21+ (25+ recommended). |
| [Maven 3.8+](https://maven.apache.org/download.cgi) | Helidon requires Maven 3.8+. |
| [Docker 18.09+](https://docs.docker.com/install/) | If you want to build and run Docker containers. |
| [Kubectl 1.16.5+](https://kubernetes.io/docs/tasks/tools/install-kubectl/) | If you want to deploy to Kubernetes, you need `kubectl` and a Kubernetes cluster (you can [install one on your desktop](../../about/kubernetes.md). |

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

# Generate the Project

Generate the project using the Helidon {flavor-uc} Quickstart Maven
archetype.

<div class="formalpara">

<div class="title">

Run the Maven archetype:

</div>

``` bash
mvn -U archetype:generate -DinteractiveMode=false \
    -DarchetypeGroupId=io.helidon.archetypes \
    -DarchetypeArtifactId=helidon-quickstart-{flavor-lc} \
    -DarchetypeVersion={helidon-version} \
    -DgroupId=io.helidon.examples \
    -DartifactId=helidon-quickstart-{project-tag}-{flavor-lc} \
    -Dpackage=io.helidon.examples.quickstart.{project-tag}
```

</div>

The archetype generates a Maven project in your current directory, (for
example, `helidon-quickstart-{project-tag}-{flavor-lc}`). Change into
this directory and build.

``` bash
cd helidon-quickstart-{project-tag}-{flavor-lc}
```

# Dependencies

Add necessary dependencies for LangChain4j integration and OpenAI
provider in the project POM.

``` xml
<dependency>
    <groupId>io.helidon.integrations.langchain4j</groupId>
    <artifactId>helidon-integrations-langchain4j</artifactId>
</dependency>
<dependency>
    <groupId>io.helidon.integrations.langchain4j.providers</groupId>
    <artifactId>helidon-integrations-langchain4j-providers-open-ai</artifactId>
</dependency>
```

You will also need extra annotation processors as LangChain4j AI
services are handled as superfast build time beans.

Include the following annotation processors in the `<build><plugins>`
section of `pom.xml`:

``` xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-compiler-plugin</artifactId>
    <configuration>
        <annotationProcessorPaths>
            <path>
                <groupId>io.helidon.codegen</groupId>
                <artifactId>helidon-codegen-apt</artifactId>
                <version>${helidon.version}</version>
            </path>
            <path>
                <groupId>io.helidon.integrations.langchain4j</groupId>
                <artifactId>helidon-integrations-langchain4j-codegen</artifactId>
                <version>${helidon.version}</version>
            </path>
            <path>
                <groupId>io.helidon.service</groupId>
                <artifactId>helidon-service-codegen</artifactId>
                <version>${helidon.version}</version>
            </path>
        </annotationProcessorPaths>
    </configuration>
</plugin>
```

# Configuration

Add to the configuration file following LangChain4j configuration for
OpenAI provider.

> [!TIP]
> Don’t forget to enable your model with `enabled` set to `true`

# Ai Service

Next we need to create LangChain4j [Ai
service](https://docs.langchain4j.dev/tutorials/ai-services) and
annotate it with `@Ai.Service` so Helidon can make a superfast build
time bean from it.

``` java
Unresolved directive in langchain4j.adoc - include::{sourcedir}/{flavor-lc}/guides/LangChain4jSnippets.java[tag=base_ai_service, indent=0]
```

When we build and run our Helidon AI-powered quickstart:

    mvn package -DskipTests && java -jar ./target/*.jar

We can test our pirate service with curl:

    echo "Who are you?" | curl -d @- localhost:8080/chat

# Prompt Template Arguments

Ofcourse all the features from LangChain4j Ai services are going to
work, let’s try to expand the example with [template
arguments](https://docs.langchain4j.dev/tutorials/ai-services#usermessage).

``` java
Unresolved directive in langchain4j.adoc - include::{sourcedir}/{flavor-lc}/guides/LangChain4jSnippets.java[tag=template_ai_service, indent=0]
```

Remember to fix the code calling the service.

``` java
Unresolved directive in langchain4j.adoc - include::{sourcedir}/{flavor-lc}/guides/LangChain4jSnippets.java[tag=template_resource, indent=0]
```

When we build and run our Helidon AI-powered quickstart:

    mvn package -DskipTests && java -jar ./target/*.jar

We can test our pirate service with curl:

    echo "Who was your captain?" | curl -d @- localhost:8080/chat

# Custom Memory Provider

We can also extend the pirate example with [conversation
memory](https://docs.langchain4j.dev/tutorials/chat-memory). First, we
need to create a memory provider so our memory works per conversation
ID.

``` java
Unresolved directive in langchain4j.adoc - include::{sourcedir}/{flavor-lc}/guides/LangChain4jSnippets.java[tag=memory_provider, indent=0]
```

Now we can extend Ai service with an extra argument so we can supply
identifier of our conversation with the pirate.

``` java
Unresolved directive in langchain4j.adoc - include::{sourcedir}/{flavor-lc}/guides/LangChain4jSnippets.java[tag=memory_ai_service, indent=0]
```

We will expect conversation id as a header on the webserver.

``` java
Unresolved directive in langchain4j.adoc - include::{sourcedir}/{flavor-lc}/guides/LangChain4jSnippets.java[tag=memory_resource, indent=0]
```

    mvn package -DskipTests && java -jar ./target/*.jar

We can test our pirate service with curl:

    echo "Hi, I am John."          | curl -d @- -H "conversation-id: 123" localhost:8080/chat
    Ahoy there, John

    echo "Do you remeber my name?" | curl -d @- -H "conversation-id: 123" localhost:8080/chat
    Aye, John! The name be etched in me memory like a ship’s anchor in the sand.
