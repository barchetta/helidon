# OllamaChatModelConfig (integrations.langchain4j.providers.ollama) Configuration

Type: [io.helidon.integrations.langchain4j.providers.ollama.OllamaChatModelConfig](/apidocs/io.helidon.integrations.langchain4j.providers.ollama/io/helidon/integrations/langchain4j/providers/ollama/OllamaChatModelConfig.html)

This is a standalone configuration type, prefix from configuration root: `langchain4j.providers.ollama`

## Configuration options

| key | type | default value | description |
|----|----|----|----|
| `base-url` | string |   | Generated from dev.langchain4j.model.ollama.OllamaBaseChatModel.Builder.baseUrl(java.lang.String) |
| `custom-headers` | Map\<string, string\> |   | Generated from dev.langchain4j.model.ollama.OllamaBaseChatModel.Builder.customHeaders(java.util.Map) |
| `default-request-parameters` | ChatRequestParameters |   | Generated from dev.langchain4j.model.ollama.OllamaBaseChatModel.Builder.defaultRequestParameters(dev.langchain4j.model.chat.request.ChatRequestParameters) |
| `enabled` | boolean | `true` | If set to `false`, OllamaChatModel will not be available even if configured. |
| `http-client-builder` | HttpClientBuilder |   | Generated from dev.langchain4j.model.ollama.OllamaBaseChatModel.Builder.httpClientBuilder(dev.langchain4j.http.client.HttpClientBuilder) |
| `listeners` | ChatModelListener\[\] |   | Generated from dev.langchain4j.model.ollama.OllamaBaseChatModel.Builder.listeners(java.util.List) |
| `log-requests` | boolean |   | Generated from dev.langchain4j.model.ollama.OllamaBaseChatModel.Builder.logRequests(java.lang.Boolean) |
| `log-responses` | boolean |   | Generated from dev.langchain4j.model.ollama.OllamaBaseChatModel.Builder.logResponses(java.lang.Boolean) |
| `logger` | Logger |   | Generated from dev.langchain4j.model.ollama.OllamaBaseChatModel.Builder.logger(org.slf4j.Logger) |
| `max-retries` | int |   | Generated from dev.langchain4j.model.ollama.OllamaChatModel.OllamaChatModelBuilder.maxRetries(java.lang.Integer) |
| `min-p` | double |   | Generated from dev.langchain4j.model.ollama.OllamaBaseChatModel.Builder.minP(java.lang.Double) |
| `mirostat` | int |   | Generated from dev.langchain4j.model.ollama.OllamaBaseChatModel.Builder.mirostat(java.lang.Integer) |
| `mirostat-eta` | double |   | Generated from dev.langchain4j.model.ollama.OllamaBaseChatModel.Builder.mirostatEta(java.lang.Double) |
| `mirostat-tau` | double |   | Generated from dev.langchain4j.model.ollama.OllamaBaseChatModel.Builder.mirostatTau(java.lang.Double) |
| `model-name` | string |   | Generated from dev.langchain4j.model.ollama.OllamaBaseChatModel.Builder.modelName(java.lang.String) |
| `num-ctx` | int |   | Generated from dev.langchain4j.model.ollama.OllamaBaseChatModel.Builder.numCtx(java.lang.Integer) |
| `num-predict` | int |   | Generated from dev.langchain4j.model.ollama.OllamaBaseChatModel.Builder.numPredict(java.lang.Integer) |
| `repeat-last-n` | int |   | Generated from dev.langchain4j.model.ollama.OllamaBaseChatModel.Builder.repeatLastN(java.lang.Integer) |
| `repeat-penalty` | double |   | Generated from dev.langchain4j.model.ollama.OllamaBaseChatModel.Builder.repeatPenalty(java.lang.Double) |
| `response-format` | ResponseFormat |   | Generated from dev.langchain4j.model.ollama.OllamaBaseChatModel.Builder.responseFormat(dev.langchain4j.model.chat.request.ResponseFormat) |
| `return-thinking` | boolean |   | Generated from dev.langchain4j.model.ollama.OllamaBaseChatModel.Builder.returnThinking(java.lang.Boolean) |
| `seed` | int |   | Generated from dev.langchain4j.model.ollama.OllamaBaseChatModel.Builder.seed(java.lang.Integer) |
| `stop` | string\[\] |   | Generated from dev.langchain4j.model.ollama.OllamaBaseChatModel.Builder.stop(java.util.List) |
| `supported-capabilities` | Capability\[\] (RESPONSE_FORMAT_JSON_SCHEMA) |   | Generated from dev.langchain4j.model.ollama.OllamaBaseChatModel.Builder.supportedCapabilities(java.util.Set) |
| `temperature` | double |   | Generated from dev.langchain4j.model.ollama.OllamaBaseChatModel.Builder.temperature(java.lang.Double) |
| `think` | boolean |   | Generated from dev.langchain4j.model.ollama.OllamaBaseChatModel.Builder.think(java.lang.Boolean) |
| `timeout` | Duration |   | Generated from dev.langchain4j.model.ollama.OllamaBaseChatModel.Builder.timeout(java.time.Duration) |
| `top-k` | int |   | Generated from dev.langchain4j.model.ollama.OllamaBaseChatModel.Builder.topK(java.lang.Integer) |
| `top-p` | double |   | Generated from dev.langchain4j.model.ollama.OllamaBaseChatModel.Builder.topP(java.lang.Double) |

Optional configuration options
