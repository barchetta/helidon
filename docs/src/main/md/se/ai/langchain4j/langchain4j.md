# Overview

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

## Features

- **Integration with Helidon Inject**

  Automatically creates and registers selected LangChain4j components in
  the Helidon service registry based on configuration.

- **Integration with CDI**

  Thanks to the **Helidon Inject to CDI Bridge**, LangChain4j components
  can be used in CDI environments, including Helidon MP applications.

- **Convention Over Configuration**

  Simplifies configuration by offering sensible defaults, reducing
  manual setup for common use cases.

- **Declarative AI Services**

  Supports [LangChain4j’s AI
  Services](https://docs.langchain4j.dev/tutorials/ai-services/) within
  the declarative programming model, allowing for clean, easy-to-manage
  code structures.

## Supported LangChain4j Components

- [**LangChain4j Core**](core.md)

  - [AI Services](#_ai_services)

  - [`EmbeddingStoreContentRetriever`](core.xml#_embeddingstorecontentretriever)

  - `MessageWindowChatMemory`

- [**Open AI**](open-ai.md)

  - [`OpenAiChatModel`](open-ai.xml#_openaichatmodel)

  - [`OpenAiStreamingChatModel`](open-ai.xml#_openaistreamingchatmodel)

  - [`OpenAiEmbeddingModel`](open-ai.xml#_openaiembeddingmodel)

  - [`OpenAiImageModel`](open-ai.xml#_openaiimagemodel)

  - [`OpenAiLanguageModel`](open-ai.xml#_openailanguagemodel)

  - [`OpenAiModerationModel`](open-ai.xml#_openaimoderationmodel)

- [**OCI GenAI**](oci-genai.md)

  - [`OciGenAiChatModel`](oci-genai.xml#_ocigenaichatmodel)

  - [`OciGenAiStreamingChatModel`](oci-genai.xml#_ocigenaistreamingchatmodel)

  - [`OciGenAiCohereChatModel`](oci-genai.xml#_ocigenaicoherechatmodel)

  - [`OciGenAiCohereStreamingChatModel`](oci-genai.xml#_ocigenaicoherestreamingchatmodel)

- [**Ollama**](ollama.md)

  - [`OllamaChatModel`](ollama.xml#_ollamachatmodel)

  - [`OllamaStreamingChatModel`](ollama.xml#_ollamastreamingchatmodel)

  - [`OllamaEmbeddingModel`](ollama.xml#_ollamaembeddingmodel)

  - [`OllamaLanguageModel`](ollama.xml#_ollamalanguagemodel)

- [**Cohere**](cohere.md)

  - [`CohereEmbeddingModel`](cohere.xml#_cohereembeddingmodel)

  - [`CohereScoringModel`](cohere.xml#_coherescoringmodel)

- [**Oracle**](oracle.md)

  - [`OracleEmbeddingStore`](oracle.xml#_oracleembeddingmodel)

- [**Coherence**](coherence.md)

  - [`CoherenceEmbeddingStore`](coherence.xml#_coherenceembeddingstore)

  - [`CoherenceChatMemoryStore`](coherence.xml#_coherencechatmemorystorestore)

- [**Jlama**](jlama.md)

  - [`JlamaChatModel`](jlama.xml#_jlamachatmodel)

  - [`JlamaStreamingChatModel`](jlama.xml#_jlamastreamingchatmodel)

  - [`JlamaEmbeddingModel`](jlama.xml#_jlamaembeddingmodel)

  - [`JlamaLanguageModel`](jlama.xml#_jlamalanguagemodel)

- [**LangChain4j Model Provider Generator**](codegen-provider.md)

> [!NOTE]
> This integration does not limit the use of other LangChain4j
> components in your application. The components listed above receive
> special treatment, meaning they can be automatically created based on
> configuration.

We will extend the number of supported components in future releases.

# Maven Coordinates

To enable LangChain4j Integration, add the following dependency to your
project’s `pom.xml` (see [Managing
Dependencies](../../../about/managing-dependencies.md)).

``` xml
<dependency>
    <groupId>io.helidon.integrations.langchain4j</groupId>
    <artifactId>helidon-integrations-langchain4j</artifactId>
</dependency>
```

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

Some features of the integration may require adding other dependencies.
Check the corresponding sections for additional information.

# General Concepts

## Creating Components

[Supported LangChain4j components](#_supported_langchain4j_components)
are automatically created and registered in service registry if exists
the corresponding configuration and `enabled` property is set to `true`.

For example, adding the following lines to `application.yaml` cause of
automatic creating and registering `OpenAiChatModel`, which later can be
injected in other classes of your application:

``` yaml
langchain4j:
  open-ai:
    chat-model:
      enabled: true
      api-key: "demo"
      base-url: "http://langchain4j.dev/demo/openai/v1"
      model-name: "gpt-4o-mini"
```

If `enabled` is set to `false`, the configuration is ignored, and the
component is not created. Configurable properties for each supported
component are listed in the corresponding documentation section below.

## Supplier Factory

Supplier Factory provide another way to create and register LangChain4j
components. It is useful for creating components that are not yet
natively supported by the integration. This method is not limited to
LangChain4j and suitable for creating and registering other classes.

Example below demonstrates a supplier factory for
`AllMiniLmL6V2EmbeddingModel`.

``` java
@Service.Singleton
class EmbeddingModelFactory implements Supplier<EmbeddingModel> {
    @Override
    public EmbeddingModel get() {
        return new AllMiniLmL6V2EmbeddingModel();
    }
}
```

By default, the **default** or **unnamed** Helidon bean is created. To
create a named service, you need to add `@Service.Named("name")`
annotation.

> [!NOTE]
> Supplier factories can be **standalone** or **static inner** classes.

## Injecting Components

You can inject Helidon services into another Helidon services using
constructor injection like this:

``` java
@Service.Singleton
public class Foo {
    private final Bar bar;

    @Service.Inject
    public Foo(Bar bar) {
        this.bar = bar;
    }
}
```

To inject a named service, annotate the constructor parameter with
`@Service.Named("name")`:

``` java
@Service.Singleton
public class Foo {
    private final Bar bar;

    @Service.Inject
    public Foo(@Service.Named("another-bar") Bar bar) {
        this.bar = bar;
    }
}
```

## Working in CDI Environment

In a CDI environment such as Helidon MP, Helidon Inject components are
exposed as CDI beans, allowing them to be injected into other CDI beans
without any restrictions.

# AI Services

LangChain4j AI Services provide a declarative and type-safe way to
define AI-powered functionality. It allows combining chat models,
retrieval-augmented generation (RAG), chat memory, and other building
blocks to create sophisticated AI-driven workflows. Read more about it
in [LangChain4j
documentation](https://docs.langchain4j.dev/tutorials/ai-services).

Helidon’s LangChain4j integration introduces a declarative Helidon
Inject-based approach for creating AI Services. It supports the
following components:

- **Chat Model**:

  - `dev.langchain4j.model.chat.ChatModel`

- **Streaming Chat Model**:

  - `dev.langchain4j.model.chat.StreamingChatModel`

- **Chat Memory** :

  - `dev.langchain4j.memory.ChatMemory`

- **Chat Memory Provider**:

  - `dev.langchain4j.memory.chat.ChatMemoryProvider`

- **Moderation Model**:

  - `dev.langchain4j.model.moderation.ModerationModel`

- **RAG**:

  - **Content Retriever**:
    `dev.langchain4j.rag.content.retriever.ContentRetriever`

  - **Retrieval Augmentor**: `dev.langchain4j.rag.RetrievalAugmentor`

- **Callback Functions**:

  - Methods annotated with `dev.langchain4j.agent.tool.Tool`

- **MCP Client**:

  - `dev.langchain4j.mcp.client.McpClient`

## Creating AI Service

AI Service is defined by a Java interface. It’s a pure LangChain4j
component. Refer to [LangChain4j
documentation](https://docs.langchain4j.dev/tutorials/ai-services) to
read more details about it.

Helidon’s LangChain4j integration provides a specialized set of
annotations for creating, configuring, and using LangChain4j AI Services
in Helidon applications.

To create an AI Service define an interface and annotate it with
`@AI.Service`.

``` java
@Ai.Service
public interface ChatAiService {
    String chat(String question);
}
```

In this scenario all LangChain4j components from the list above are
taken from the service registry. User still has an ability to manually
control the process by putting any of the following annotations which
specify a service name which must be used for this particular function
instead of discovering it automatically.

|  |  |
|----|----|
| Annotation | Description |
| `Ai.ChatModel` | Specifies the name of a service in the service registry that implements `ChatModel` to be used in the annotated AI Service. Mutually exclusive with `Ai.StreamingChatModel`. |
| `Ai.StreamingChatModel` | Specifies the name of a service in the service registry that implements `StreamingChatModel` to use in the annotated Ai Service. Mutually exclusive with `Ai.ChatModel`. |
| `Ai.ChatMemory` | Specifies the name of a service in the service registry that implements `ChatMemory` to use in the annotated Ai Service. Mutually exclusive with `Ai.ChatMemoryWindow` and `Ai.ChatMemoryProvider`. |
| `Ai.ChatMemoryWindow` | Adds a `MessageWindowChatModel` with the specified window size to the annotated AI Service. Mutually exclusive with `Ai.ChatMemory` and `Ai.ChatMemoryProvider`. |
| `Ai.ChatMemoryProvider` | Specifies the name of a service in the service registry that implements `ChatMemoryProvider` to use in the annotated Ai Service. Mutually exclusive with `Ai.ChatMemory` and `Ai.ChatMemoryWindow`. |
| `Ai.ModerationModel` | Specifies the name of a service in the service registry that implements `ModerationModel` to use in the annotated Ai Service. |
| `Ai.ContentRetriever` | Specifies the name of a service in the service registry that implements `ContentRetriever` to use in the annotated Ai Service. Mutually exclusive with `Ai.RetrievalAugmentor`. |
| `Ai.RetrievalAugmentor` | Specifies the name of a service in the service registry that implements `RetrievalAugmentor` to use in the annotated Ai Service. Mutually exclusive with `Ai.ContentRetriever`. |
| `Ai.ToolProvider` | Specifies the name of a service in the service registry that implements `ToolProvider` to use in the annotated Ai Service. Mutually exclusive with `Ai.McpClients`. |
| `Ai.McpClients` | Specifies the name/s of a `McpClient` in the service registry that implements `ToolProvider` to use in the annotated Ai Service. `McpToolProvider` is created from these clients. Mutually exclusive with `Ai.ToolProvider`. |

For example, in the snippet below a service with name
"myCustomChatMemory" will be used as chat memory and all other
components are discovered automatically.

``` java
@Ai.Service
@Ai.ChatMemory("myCustomChatMemory")
public interface ChatAiService {
    String chat(String question);
}
```

> [!NOTE]
> There is a possibility to switch off automatic discovery by using
> `@Ai.Service(autodicovery=false)`. In this case the service components
> are not discovered automatically and users must add components
> manually using annotations specified above. `@ChatModel` or
> `@StreamingChatModel` annotations are required.

Since `Ai.ToolProvider` and `Ai.McpClients` are mutually exclusive, some
clarification is needed regarding their functionality. Assume that
automatic discovery is set to true in this context:

- If neither annotation is present, a `ToolProvider` will be
  automatically discovered from the service registry.

- If the `Ai.McpClients` annotation is present, corresponding MCP client
  services will be discovered, and no `ToolProvider` will be discovered.

- If both annotations are present, an exception will be thrown.

## Tools (Callback Functions)

In LangChain4j, tools are callback functions that the language model can
invoke during a conversation to perform specific tasks, retrieve
information, or execute external logic. These tools extend the model’s
capabilities beyond simple text generation, allowing it to dynamically
interact with external systems. For instance, a tool might query a
database, call an external API, or perform calculations. Based on user
input, the model can decide to call a tool, interpret its response, and
incorporate it into the conversation for a more context-aware and
multi-step interaction.

To expose a method in a Helidon service as a tool, annotate it with the
`@Tool` annotation from `dev.langchain4j.agent.tool.Tool`, as shown in
the example below:

``` java
@Service.Singleton
public class OrderService {

    @Tool("Get order details for specified order number")
    public Order getOrderDetails(String orderNumber) {
        // ...
    }
}
```

> [!NOTE]
> If you are using Helidon MP, to enable `@Tool`-annotated methods in
> CDI beans, you must annotate the CDI bean with the `@Ai.Tool`
> qualifier.

For more details, read the [LangChain4j Documentation on
Tools](https://docs.langchain4j.dev/tutorials/tools#high-level-tool-api).

## MCP Client

In LangChain4j, an MCP (Model Context Protocol) client acts as a bridge
between the language model and external services or resources that
follow the MCP standard. Instead of directly embedding custom logic into
the application, the MCP client enables the model to discover, connect
to, and interact with external tools and data providers in a
standardized way.

To add MCP Clients to your AI Service, use the following:

``` java
@Ai.Service
@Ai.McpClients
public interface ChatAiService {
    String chat(String question);
}
```

If you want to have your MCP clients created from the configuration, it
should be placed under the `langchain4j.mcp-clients`. These are all the
MCP Client configuration options currently supported:

Type:
[io.helidon.integrations.langchain4j.McpClientConfig](/apidocs/io.helidon.integrations.langchain4j/io/helidon/integrations/langchain4j/McpClientConfig.html)

### Configuration options

| key | type | default value | description |
|----|----|----|----|
| `client-name` | string |   | Sets the name that the client will use to identify itself to the MCP server in the initialization message. Overwrites the default client name from langchain4j. |
| `client-version` | string |   | Sets the version string that the client will use to identify itself to the MCP server in the initialization message. Overwrites the default client version from langchain4j. |
| `initialization-timeout` | Duration |   | Sets the timeout for initializing the client. Overwrites the default timeout for initializing from langchain4j. |
| `key` | string |   | Sets a unique identifier for the client. If none is provided, a UUID will be automatically generated. This key is later used to identify the client in the service registry. |
| `log-requests` | boolean |   | Whether to log request traffic. |
| `log-responses` | boolean |   | Whether to log response traffic. |
| `ping-timeout` | Duration |   | The timeout to apply when waiting for a ping response. Overwrites the default timeout when waiting for a ping response from langchain4j. |
| `prompts-timeout` | Duration |   | The timeout for prompt-related operations (listing prompts as well as rendering the contents of a prompt). A value of zero means no timeout. Overwrites the default timeout for prompt-related operations from langchain4j. |
| `protocol-version` | string |   | Sets the protocol version that the client will advertise in the initialization message. Overwrites the default version from langchain4j. |
| `reconnect-interval` | Duration |   | The delay before attempting to reconnect after a failed connection. Overwrites the default reconnect interval from langchain4j. |
| `resources-timeout` | Duration |   | Sets the timeout for resource-related operations (listing resources as well as reading the contents of a resource). A value of zero means no timeout. Overwrites the default timeout for resource-related operations from langchain4j. |
| `sse-uri` | URI |   | The initial URI where to connect to the server and request a SSE channel. |
| `tool-execution-timeout` | Duration |   | Sets the timeout for tool execution. This value applies to each tool execution individually. A value of zero means no timeout. Overwrites the default timeout for tool execution from langchain4j. |
| `tool-execution-timeout-error-message` | string |   | The error message to return when a tool execution times out. Overwrites the default error message from langchain4j. |

Optional configuration options

## Observability (ChatModelListeners)

While LangChain4j doesn’t provide Observability out-of-box, it provides
for user to supplement it using `ChatModelListener`. For more details,
read the [LangChain4j Documentation on
Observability](https://docs.langchain4j.dev/tutorials/observability/).

Helidon provides `MetricsChatModelListener` which generates metrics that
follow the [OpenTelemetry Semantic Conventions for GenAI Metrics
v1.36.0](https://github.com/open-telemetry/semantic-conventions/blob/v1.36.0/docs/gen-ai/gen-ai-metrics.md).
This is done out-of-box for Chat API calls.

# Additional Information

- [LangChain4j documentation](https://docs.langchain4j.dev/)

- Components Reference

  - [Core LangChain4j Components](core.md)

  - [Open AI](open-ai.md)

  - [Ollama](ollama.md)

  - [Cohere](cohere.md)

  - [Oracle](oracle.md)

  - [Coherence](coherence.md)

  - [Jlama](jlama.md)

  - [Code generated Lc4j Provider](codegen-provider.md)
