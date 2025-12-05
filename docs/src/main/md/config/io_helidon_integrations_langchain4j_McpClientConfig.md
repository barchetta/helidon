Type:
[io.helidon.integrations.langchain4j.McpClientConfig](/apidocs/io.helidon.integrations.langchain4j/io/helidon/integrations/langchain4j/McpClientConfig.html)

# Configuration options

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
