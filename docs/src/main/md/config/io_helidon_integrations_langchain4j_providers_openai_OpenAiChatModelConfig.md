Type:
[io.helidon.integrations.langchain4j.providers.openai.OpenAiChatModelConfig](/apidocs/io.helidon.integrations.langchain4j.providers.openai/io/helidon/integrations/langchain4j/providers/openai/OpenAiChatModelConfig.html)

This is a standalone configuration type, prefix from configuration root:
`langchain4j.open-ai.chat-model`

# Configuration options

| key | type | default value | description |
|----|----|----|----|
| `api-key` | string |   | Generated from dev.langchain4j.model.openai.OpenAiChatModel.OpenAiChatModelBuilder.apiKey(java.lang.String) |
| `base-url` | string |   | Generated from dev.langchain4j.model.openai.OpenAiChatModel.OpenAiChatModelBuilder.baseUrl(java.lang.String) |
| `custom-headers` | Map\<string, string\> |   | Generated from dev.langchain4j.model.openai.OpenAiChatModel.OpenAiChatModelBuilder.customHeaders(java.util.Map) |
| `default-request-parameters` | ChatRequestParameters |   | Generated from dev.langchain4j.model.openai.OpenAiChatModel.OpenAiChatModelBuilder.defaultRequestParameters(dev.langchain4j.model.chat.request.ChatRequestParameters) |
| `enabled` | boolean |   | If set to `false` (default), OpenAiChatModel will not be available even if configured. |
| `frequency-penalty` | double |   | Generated from dev.langchain4j.model.openai.OpenAiChatModel.OpenAiChatModelBuilder.frequencyPenalty(java.lang.Double) |
| `http-client-builder` | HttpClientBuilder |   | Generated from dev.langchain4j.model.openai.OpenAiChatModel.OpenAiChatModelBuilder.httpClientBuilder(dev.langchain4j.http.client.HttpClientBuilder) |
| `listeners` | ChatModelListener\[\] |   | Generated from dev.langchain4j.model.openai.OpenAiChatModel.OpenAiChatModelBuilder.listeners(java.util.List) |
| `log-requests` | boolean |   | Generated from dev.langchain4j.model.openai.OpenAiChatModel.OpenAiChatModelBuilder.logRequests(java.lang.Boolean) |
| `log-responses` | boolean |   | Generated from dev.langchain4j.model.openai.OpenAiChatModel.OpenAiChatModelBuilder.logResponses(java.lang.Boolean) |
| `logger` | Logger |   | Generated from dev.langchain4j.model.openai.OpenAiChatModel.OpenAiChatModelBuilder.logger(org.slf4j.Logger) |
| `logit-bias` | Map\<string, int\> |   | Generated from dev.langchain4j.model.openai.OpenAiChatModel.OpenAiChatModelBuilder.logitBias(java.util.Map) |
| `max-completion-tokens` | int |   | Generated from dev.langchain4j.model.openai.OpenAiChatModel.OpenAiChatModelBuilder.maxCompletionTokens(java.lang.Integer) |
| `max-retries` | int |   | Generated from dev.langchain4j.model.openai.OpenAiChatModel.OpenAiChatModelBuilder.maxRetries(java.lang.Integer) |
| `max-tokens` | int |   | Generated from dev.langchain4j.model.openai.OpenAiChatModel.OpenAiChatModelBuilder.maxTokens(java.lang.Integer) |
| `metadata` | Map\<string, string\> |   | Generated from dev.langchain4j.model.openai.OpenAiChatModel.OpenAiChatModelBuilder.metadata(java.util.Map) |
| `model-name` | string |   | Generated from dev.langchain4j.model.openai.OpenAiChatModel.OpenAiChatModelBuilder.modelName(java.lang.String) |
| `organization-id` | string |   | Generated from dev.langchain4j.model.openai.OpenAiChatModel.OpenAiChatModelBuilder.organizationId(java.lang.String) |
| `parallel-tool-calls` | boolean |   | Generated from dev.langchain4j.model.openai.OpenAiChatModel.OpenAiChatModelBuilder.parallelToolCalls(java.lang.Boolean) |
| `presence-penalty` | double |   | Generated from dev.langchain4j.model.openai.OpenAiChatModel.OpenAiChatModelBuilder.presencePenalty(java.lang.Double) |
| `project-id` | string |   | Generated from dev.langchain4j.model.openai.OpenAiChatModel.OpenAiChatModelBuilder.projectId(java.lang.String) |
| `return-thinking` | boolean |   | Generated from dev.langchain4j.model.openai.OpenAiChatModel.OpenAiChatModelBuilder.returnThinking(java.lang.Boolean) |
| `seed` | int |   | Generated from dev.langchain4j.model.openai.OpenAiChatModel.OpenAiChatModelBuilder.seed(java.lang.Integer) |
| `service-tier` | string |   | Generated from dev.langchain4j.model.openai.OpenAiChatModel.OpenAiChatModelBuilder.serviceTier(java.lang.String) |
| `stop` | string\[\] |   | Generated from dev.langchain4j.model.openai.OpenAiChatModel.OpenAiChatModelBuilder.stop(java.util.List) |
| `store` | boolean |   | Generated from dev.langchain4j.model.openai.OpenAiChatModel.OpenAiChatModelBuilder.store(java.lang.Boolean) |
| `strict-json-schema` | boolean |   | Generated from dev.langchain4j.model.openai.OpenAiChatModel.OpenAiChatModelBuilder.strictJsonSchema(java.lang.Boolean) |
| `strict-tools` | boolean |   | Generated from dev.langchain4j.model.openai.OpenAiChatModel.OpenAiChatModelBuilder.strictTools(java.lang.Boolean) |
| `supported-capabilities` | Capability\[\] (RESPONSE_FORMAT_JSON_SCHEMA) |   | Generated from dev.langchain4j.model.openai.OpenAiChatModel.OpenAiChatModelBuilder.supportedCapabilities(java.util.Set) |
| `temperature` | double |   | Generated from dev.langchain4j.model.openai.OpenAiChatModel.OpenAiChatModelBuilder.temperature(java.lang.Double) |
| `timeout` | Duration |   | Generated from dev.langchain4j.model.openai.OpenAiChatModel.OpenAiChatModelBuilder.timeout(java.time.Duration) |
| `top-p` | double |   | Generated from dev.langchain4j.model.openai.OpenAiChatModel.OpenAiChatModelBuilder.topP(java.lang.Double) |
| `user` | string |   | Generated from dev.langchain4j.model.openai.OpenAiChatModel.OpenAiChatModelBuilder.user(java.lang.String) |

Optional configuration options
