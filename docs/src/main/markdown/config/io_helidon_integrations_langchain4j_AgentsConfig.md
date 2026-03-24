# AgentsConfig (integrations.langchain4j) Configuration

Type: [io.helidon.integrations.langchain4j.AgentsConfig](/apidocs/io.helidon.integrations.langchain4j/io/helidon/integrations/langchain4j/AgentsConfig.html)

This is a standalone configuration type, prefix from configuration root: `langchain4j.agents`

## Configuration options

<table style="width:100%;">
<caption>Optional configuration options</caption>
<colgroup>
<col style="width: 23%" />
<col style="width: 23%" />
<col style="width: 15%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">key</th>
<th style="text-align: left;">type</th>
<th style="text-align: left;">default value</th>
<th style="text-align: left;">description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>async</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>If true, the agent will be invoked in an asynchronous manner, allowing the workflow to continue without waiting for the agent’s result.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>chat-memory</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Name of the dev.langchain4j.memory.ChatMemory service to use for this agent.</p>
<p>The value is resolved from the ServiceRegistry.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>chat-memory-provider</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Name of the dev.langchain4j.memory.chat.ChatMemoryProvider service to use for this agent.</p>
<p>The value is resolved from the ServiceRegistry.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>chat-model</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Name of the dev.langchain4j.model.chat.ChatModel service to use for this agent.</p>
<p>The value is resolved from the ServiceRegistry.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>content-retriever</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Name of the dev.langchain4j.rag.content.retriever.ContentRetriever service to use for this agent.</p>
<p>The value is resolved from the ServiceRegistry.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>description</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Description of the agent. It should be clear and descriptive to allow a language model to understand the agent’s purpose and its intended use.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>enabled</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>If set to <code>false</code>, agent will not be available even if configured.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>execute-tools-concurrently</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>If true, the agent’s tools can be invoked in a concurrent manner.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>input-guardrails</code></p></td>
<td style="text-align: left;"><p>Class[]</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Input guardrail classes to apply to the agent.</p>
<p>Each class is resolved from the ServiceRegistry.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>mcp-clients</code></p></td>
<td style="text-align: left;"><p>string[]</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Names of dev.langchain4j.mcp.client.McpClient services to use for MCP-backed tools.</p>
<p>Each name is resolved from the ServiceRegistry, the clients are then used to build an dev.langchain4j.mcp.McpToolProvider which is registered as the agent’s tool provider.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Agent identifier used to label the agent in workflows and/or agent registries.</p>
<p>If configured, this value is applied to the underlying agent builder via <code>agentBuilder.name(…​)</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>output-guardrails</code></p></td>
<td style="text-align: left;"><p>Class[]</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Output guardrail classes to apply to the agent.</p>
<p>Each class is resolved from the ServiceRegistry,</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>output-key</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Key of the output variable that will be used to store the result of the agent’s invocation.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>retrieval-augmentor</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Name of the dev.langchain4j.rag.RetrievalAugmentor service to use for this agent.</p>
<p>The value is resolved from the ServiceRegistry.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>tool-provider</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Name of the dev.langchain4j.service.tool.ToolProvider service to use for this agent.</p>
<p>The value is resolved from the ServiceRegistry.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>tools</code></p></td>
<td style="text-align: left;"><p>Class[]</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Tool service classes to register with the agent.</p>
<p>Each class is resolved from the ServiceRegistry, and the resulting service instances are registered using <code>agentBuilder.tools(…​)</code>.</p></td>
</tr>
</tbody>
</table>
