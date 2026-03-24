# OpenAiLanguageModelConfig (integrations.langchain4j.providers.openai) Configuration

Type: [io.helidon.integrations.langchain4j.providers.openai.OpenAiLanguageModelConfig](/apidocs/io.helidon.integrations.langchain4j.providers.openai/io/helidon/integrations/langchain4j/providers/openai/OpenAiLanguageModelConfig.html)

This is a standalone configuration type, prefix from configuration root: `langchain4j.providers.open-ai`

## Configuration options

| key | type | default value | description |
|----|----|----|----|
| `api-key` | string |   | Generated from dev.langchain4j.model.openai.OpenAiLanguageModel.OpenAiLanguageModelBuilder.apiKey(java.lang.String) |
| `base-url` | string |   | Generated from dev.langchain4j.model.openai.OpenAiLanguageModel.OpenAiLanguageModelBuilder.baseUrl(java.lang.String) |
| `custom-headers` | Map\<string, string\> |   | Generated from dev.langchain4j.model.openai.OpenAiLanguageModel.OpenAiLanguageModelBuilder.customHeaders(java.util.Map) |
| `custom-query-params` | Map\<string, string\> |   | Generated from dev.langchain4j.model.openai.OpenAiLanguageModel.OpenAiLanguageModelBuilder.customQueryParams(java.util.Map) |
| `enabled` | boolean | `true` | If set to `false`, OpenAiLanguageModel will not be available even if configured. |
| `http-client-builder` | HttpClientBuilder |   | Generated from dev.langchain4j.model.openai.OpenAiLanguageModel.OpenAiLanguageModelBuilder.httpClientBuilder(dev.langchain4j.http.client.HttpClientBuilder) |
| `log-requests` | boolean |   | Generated from dev.langchain4j.model.openai.OpenAiLanguageModel.OpenAiLanguageModelBuilder.logRequests(java.lang.Boolean) |
| `log-responses` | boolean |   | Generated from dev.langchain4j.model.openai.OpenAiLanguageModel.OpenAiLanguageModelBuilder.logResponses(java.lang.Boolean) |
| `logger` | Logger |   | Generated from dev.langchain4j.model.openai.OpenAiLanguageModel.OpenAiLanguageModelBuilder.logger(org.slf4j.Logger) |
| `max-retries` | int |   | Generated from dev.langchain4j.model.openai.OpenAiLanguageModel.OpenAiLanguageModelBuilder.maxRetries(java.lang.Integer) |
| `model-name` | string |   | Generated from dev.langchain4j.model.openai.OpenAiLanguageModel.OpenAiLanguageModelBuilder.modelName(java.lang.String) |
| `organization-id` | string |   | Generated from dev.langchain4j.model.openai.OpenAiLanguageModel.OpenAiLanguageModelBuilder.organizationId(java.lang.String) |
| `project-id` | string |   | Generated from dev.langchain4j.model.openai.OpenAiLanguageModel.OpenAiLanguageModelBuilder.projectId(java.lang.String) |
| `temperature` | double |   | Generated from dev.langchain4j.model.openai.OpenAiLanguageModel.OpenAiLanguageModelBuilder.temperature(java.lang.Double) |
| `timeout` | Duration |   | Generated from dev.langchain4j.model.openai.OpenAiLanguageModel.OpenAiLanguageModelBuilder.timeout(java.time.Duration) |

Optional configuration options
