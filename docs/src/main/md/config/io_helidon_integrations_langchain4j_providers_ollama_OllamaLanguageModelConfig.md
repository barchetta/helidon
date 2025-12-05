Type:
[io.helidon.integrations.langchain4j.providers.ollama.OllamaLanguageModelConfig](/apidocs/io.helidon.integrations.langchain4j.providers.ollama/io/helidon/integrations/langchain4j/providers/ollama/OllamaLanguageModelConfig.html)

This is a standalone configuration type, prefix from configuration root:
`langchain4j.ollama.language-model`

# Configuration options

| key | type | default value | description |
|----|----|----|----|
| `base-url` | string |   | Generated from dev.langchain4j.model.ollama.OllamaLanguageModel.OllamaLanguageModelBuilder.baseUrl(java.lang.String) |
| `custom-headers` | Map\<string, string\> |   | Generated from dev.langchain4j.model.ollama.OllamaLanguageModel.OllamaLanguageModelBuilder.customHeaders(java.util.Map) |
| `enabled` | boolean |   | If set to `false` (default), OllamaLanguageModel will not be available even if configured. |
| `http-client-builder` | HttpClientBuilder |   | Generated from dev.langchain4j.model.ollama.OllamaLanguageModel.OllamaLanguageModelBuilder.httpClientBuilder(dev.langchain4j.http.client.HttpClientBuilder) |
| `log-requests` | boolean |   | Generated from dev.langchain4j.model.ollama.OllamaLanguageModel.OllamaLanguageModelBuilder.logRequests(java.lang.Boolean) |
| `log-responses` | boolean |   | Generated from dev.langchain4j.model.ollama.OllamaLanguageModel.OllamaLanguageModelBuilder.logResponses(java.lang.Boolean) |
| `max-retries` | int |   | Generated from dev.langchain4j.model.ollama.OllamaLanguageModel.OllamaLanguageModelBuilder.maxRetries(java.lang.Integer) |
| `model-name` | string |   | Generated from dev.langchain4j.model.ollama.OllamaLanguageModel.OllamaLanguageModelBuilder.modelName(java.lang.String) |
| `num-ctx` | int |   | Generated from dev.langchain4j.model.ollama.OllamaLanguageModel.OllamaLanguageModelBuilder.numCtx(java.lang.Integer) |
| `num-predict` | int |   | Generated from dev.langchain4j.model.ollama.OllamaLanguageModel.OllamaLanguageModelBuilder.numPredict(java.lang.Integer) |
| `repeat-penalty` | double |   | Generated from dev.langchain4j.model.ollama.OllamaLanguageModel.OllamaLanguageModelBuilder.repeatPenalty(java.lang.Double) |
| `response-format` | ResponseFormat |   | Generated from dev.langchain4j.model.ollama.OllamaLanguageModel.OllamaLanguageModelBuilder.responseFormat(dev.langchain4j.model.chat.request.ResponseFormat) |
| `seed` | int |   | Generated from dev.langchain4j.model.ollama.OllamaLanguageModel.OllamaLanguageModelBuilder.seed(java.lang.Integer) |
| `stop` | string\[\] |   | Generated from dev.langchain4j.model.ollama.OllamaLanguageModel.OllamaLanguageModelBuilder.stop(java.util.List) |
| `temperature` | double |   | Generated from dev.langchain4j.model.ollama.OllamaLanguageModel.OllamaLanguageModelBuilder.temperature(java.lang.Double) |
| `timeout` | Duration |   | Generated from dev.langchain4j.model.ollama.OllamaLanguageModel.OllamaLanguageModelBuilder.timeout(java.time.Duration) |
| `top-k` | int |   | Generated from dev.langchain4j.model.ollama.OllamaLanguageModel.OllamaLanguageModelBuilder.topK(java.lang.Integer) |
| `top-p` | double |   | Generated from dev.langchain4j.model.ollama.OllamaLanguageModel.OllamaLanguageModelBuilder.topP(java.lang.Double) |

Optional configuration options
