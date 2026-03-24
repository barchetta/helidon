# MCP

## Model Context Protocol (MCP)

The [Model Context Protocol (MCP)](https://modelcontextprotocol.io) is an open protocol designed to connect AI models with external tools, resources, and data sources in a standardized way. An MCP server exposes resources, prompts, and tools that AI clients can discover and invoke dynamically, enabling more powerful and context-aware applications.

## MCP Server

Helidon provides support for building Model Context Protocol (MCP) servers through a dedicated extension. The MCP Server feature is not part of the core Helidon Framework – it is delivered as a separate project hosted in the [helidon-mcp GitHub repository](https://github.com/helidon-io/helidon-mcp).

### Helidon MCP Server Extension

The Helidon MCP Server extension allows you to build and run MCP servers with Helidon.

Key points:

- Separate repository: [helidon-mcp](https://github.com/helidon-io/helidon-mcp)

- Independent lifecycle: Requires Helidon but has its own versioning and release cadence

- Dedicated documentation: Full usage guides, configuration details, and examples are provided directly in the [helidon-mcp documentation](https://github.com/helidon-io/helidon-mcp#documentation)

To get started:

1.  Visit the [helidon-mcp GitHub repository](https://github.com/helidon-io/helidon-mcp).

2.  Follow the setup and usage instructions in the repository’s documentation.

3.  Explore how to expose your Helidon resources as MCP tools, prompts, and data sources.

## MCP Client

Helidon includes support for an MCP client through its [integration with LangChain4j](../../se/ai/langchain4j/langchain4j.md). With this integration, you can set up the MCP client using Helidon configuration and plug it directly into your LangChain4j AI Services and Agents.

In LangChain4j, an MCP (Model Context Protocol) client acts as a bridge between the language model and external services or resources that follow the MCP standard. Instead of directly embedding custom logic into the application, the MCP client enables the model to discover, connect to, and interact with external tools and data providers in a standardized way.

To add MCP Clients to your AI Service, use `@Ai.McpClients` annotation to reference configured clients:

``` java
@Ai.Service
@Ai.ChatModel("expensive-model")
@Ai.McpClients(value = {"foo-mcp-server", "bar-mcp-server"})
public interface ChatAiService {
    String chat(String question);
}
```

If you want to have your MCP clients created from the configuration, it should be placed under the `langchain4j.mcp-clients`.

``` yaml
langchain4j:
  providers:
    open-ai:
      api-key: "${OPEN_AI_API_TOKEN}"

  models:
    expensive-model:
      provider: open-ai
      model-name: "openai.gpt-oss-120b"

  mcp-clients:
    foo-mcp-server:
      uri: http://foo-mcp-server
      initialization-timeout: PT15M
    bar-mcp-server:
      uri: http://bar-mcp-server
      tool-execution-timeout: PT10S
```

These are all the MCP Client configuration options currently supported:

Type: [io.helidon.integrations.langchain4j.McpClientConfig](/apidocs/io.helidon.integrations.langchain4j/io/helidon/integrations/langchain4j/McpClientConfig.html)

### Configuration options

| key | type | default value | description |
|----|----|----|----|
| <span class="line-through">`sse-uri`</span> | URI |   | **Deprecated** The initial URI where to connect to the server and request an SSE channel. |
| `uri` | URI |   | The URL of the MCP server. |

Required configuration options

| key | type | default value | description |
|----|----|----|----|
| `client-name` | string |   | Sets the name that the client will use to identify itself to the MCP server in the initialization message. Overwrites the default client name from langchain4j. |
| `client-version` | string |   | Sets the version string that the client will use to identify itself to the MCP server in the initialization message. Overwrites the default client version from langchain4j. |
| `initialization-timeout` | Duration |   | Sets the timeout for initializing the client. Overwrites the default timeout for initializing from langchain4j. |
| `key` | string |   | Sets a unique identifier for the client. If none is provided, a UUID will be automatically generated. This key is later used to identify the client in the service registry. |
| `log-requests` | boolean |   | Whether to log request traffic. |
| `log-responses` | boolean |   | Whether to log response traffic. |
| `ping-timeout` | Duration |   | The timeout to apply when waiting for a ping response. Overwrites the default timeout when waiting for a ping response from langchain4j. |
| `prompts-timeout` | Duration |   | The timeout for prompt-related operations (listing prompts as well as rendering the contents of a prompt). A value of zero seconds means no timeout. Overwrites the default timeout for prompt-related operations from langchain4j. |
| `protocol-version` | string |   | Sets the protocol version that the client will advertise in the initialization message. Overwrites the default version from langchain4j. |
| `reconnect-interval` | Duration |   | The delay before attempting to reconnect after a failed connection. Overwrites the default reconnect interval from langchain4j. |
| `resources-timeout` | Duration |   | Sets the timeout for resource-related operations (listing resources as well as reading the contents of a resource). A value of zero seconds means no timeout. Overwrites the default timeout for resource-related operations from langchain4j. |
| `tool-execution-timeout` | Duration |   | Sets the timeout for tool execution. This value applies to each tool execution individually. A value of zero seconds means no timeout. Overwrites the default timeout for tool execution from langchain4j. |
| `tool-execution-timeout-error-message` | string |   | The error message to return when a tool execution times out. Overwrites the default error message from langchain4j. |

Optional configuration options
