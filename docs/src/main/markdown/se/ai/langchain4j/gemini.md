# Google Gemini

## Contents

- [Overview](#_overview)

- [Maven Coordinates](#_maven_coordinates)

- [Components](#_components)

  - [GoogleAiGeminiChatModel](#_googleaigeminichatmodel)

  - [GoogleAiGeminiStreamingChatModel](#_googleaigeministreamingchatmodel)

- [Additional Information](#_additional_information)

## Overview

This module adds support for selected [Google Gemini](https://ai.google.dev/gemini-api/docs/models) models.

## Maven Coordinates

In addition to the [Helidon integration with LangChain4j core dependencies](langchain4j.md#maven-coordinates), you must add the following:

``` xml
<dependency>
    <groupId>io.helidon.integrations.langchain4j.providers</groupId>
    <artifactId>helidon-integrations-langchain4j-providers-google-gemini</artifactId>
</dependency>
```

## Components

### GoogleAiGeminiChatModel

To automatically create and add `GoogleAiGeminiChatModel` to the service registry add the following lines to `application.yaml`:

``` yaml
langchain4j:
  providers:
    google-gemini:
      api-key: "${GEMINI_TOKEN}"

  models:
    gemini-chat-model:
      provider: google-gemini
      model-name: "gemini-2.0-flash"
```

If `enabled` is set to `false`, the configuration is ignored, and the component is not created.

Type: [io.helidon.integrations.langchain4j.providers.gemini.GoogleAiGeminiChatModelConfig](/apidocs/io.helidon.integrations.langchain4j.providers.google.gemini/io/helidon/integrations/langchain4j/providers/gemini/GoogleAiGeminiChatModelConfig.html)

This is a standalone configuration type, prefix from configuration root: `langchain4j.providers.google-gemini`

### Configuration options

| key | type | default value | description |
|----|----|----|----|
| `allow-code-execution` | boolean |   | Generated from dev.langchain4j.model.googleai.BaseGeminiChatModel.GoogleAiGeminiChatModelBaseBuilder.allowCodeExecution(java.lang.Boolean) |
| `allow-google-maps` | boolean |   | Generated from dev.langchain4j.model.googleai.BaseGeminiChatModel.GoogleAiGeminiChatModelBaseBuilder.allowGoogleMaps(java.lang.Boolean) |
| `allow-google-search` | boolean |   | Generated from dev.langchain4j.model.googleai.BaseGeminiChatModel.GoogleAiGeminiChatModelBaseBuilder.allowGoogleSearch(java.lang.Boolean) |
| `allow-url-context` | boolean |   | Generated from dev.langchain4j.model.googleai.BaseGeminiChatModel.GoogleAiGeminiChatModelBaseBuilder.allowUrlContext(java.lang.Boolean) |
| `api-key` | string |   | Generated from dev.langchain4j.model.googleai.BaseGeminiChatModel.GoogleAiGeminiChatModelBaseBuilder.apiKey(java.lang.String) |
| `base-url` | string |   | Generated from dev.langchain4j.model.googleai.BaseGeminiChatModel.GoogleAiGeminiChatModelBaseBuilder.baseUrl(java.lang.String) |
| `default-request-parameters` | ChatRequestParameters |   | Generated from dev.langchain4j.model.googleai.BaseGeminiChatModel.GoogleAiGeminiChatModelBaseBuilder.defaultRequestParameters(dev.langchain4j.model.chat.request.ChatRequestParameters) |
| `enable-enhanced-civic-answers` | boolean |   | Generated from dev.langchain4j.model.googleai.BaseGeminiChatModel.GoogleAiGeminiChatModelBaseBuilder.enableEnhancedCivicAnswers(java.lang.Boolean) |
| `enabled` | boolean | `true` | If set to `false`, GoogleAiGeminiChatModel will not be available even if configured. |
| `frequency-penalty` | double |   | Generated from dev.langchain4j.model.googleai.BaseGeminiChatModel.GoogleAiGeminiChatModelBaseBuilder.frequencyPenalty(java.lang.Double) |
| `http-client-builder` | HttpClientBuilder |   | Generated from dev.langchain4j.model.googleai.BaseGeminiChatModel.GoogleAiGeminiChatModelBaseBuilder.httpClientBuilder(dev.langchain4j.http.client.HttpClientBuilder) |
| `include-code-execution-output` | boolean |   | Generated from dev.langchain4j.model.googleai.BaseGeminiChatModel.GoogleAiGeminiChatModelBaseBuilder.includeCodeExecutionOutput(java.lang.Boolean) |
| `listeners` | ChatModelListener\[\] |   | Generated from dev.langchain4j.model.googleai.BaseGeminiChatModel.GoogleAiGeminiChatModelBaseBuilder.listeners(java.util.List) |
| `log-requests` | boolean |   | Generated from dev.langchain4j.model.googleai.BaseGeminiChatModel.GoogleAiGeminiChatModelBaseBuilder.logRequests(java.lang.Boolean) |
| `log-requests-and-responses` | boolean |   | Generated from dev.langchain4j.model.googleai.BaseGeminiChatModel.GoogleAiGeminiChatModelBaseBuilder.logRequestsAndResponses(java.lang.Boolean) |
| `log-responses` | boolean |   | Generated from dev.langchain4j.model.googleai.BaseGeminiChatModel.GoogleAiGeminiChatModelBaseBuilder.logResponses(java.lang.Boolean) |
| `logger` | Logger |   | Generated from dev.langchain4j.model.googleai.BaseGeminiChatModel.GoogleAiGeminiChatModelBaseBuilder.logger(org.slf4j.Logger) |
| `logprobs` | int |   | Generated from dev.langchain4j.model.googleai.BaseGeminiChatModel.GoogleAiGeminiChatModelBaseBuilder.logprobs(java.lang.Integer) |
| `max-output-tokens` | int |   | Generated from dev.langchain4j.model.googleai.BaseGeminiChatModel.GoogleAiGeminiChatModelBaseBuilder.maxOutputTokens(java.lang.Integer) |
| `max-retries` | int |   | Generated from dev.langchain4j.model.googleai.GoogleAiGeminiChatModel.GoogleAiGeminiChatModelBuilder.maxRetries(java.lang.Integer) |
| `media-resolution` | GeminiMediaResolutionLevel (MEDIA_RESOLUTION_UNSPECIFIED, MEDIA_RESOLUTION_LOW, MEDIA_RESOLUTION_MEDIUM, MEDIA_RESOLUTION_HIGH, MEDIA_RESOLUTION_ULTRA_HIGH) |   | Generated from dev.langchain4j.model.googleai.BaseGeminiChatModel.GoogleAiGeminiChatModelBaseBuilder.mediaResolution(dev.langchain4j.model.googleai.GeminiMediaResolutionLevel) |
| `media-resolution-per-part-enabled` | boolean |   | Generated from dev.langchain4j.model.googleai.BaseGeminiChatModel.GoogleAiGeminiChatModelBaseBuilder.mediaResolutionPerPartEnabled(java.lang.Boolean) |
| `model-name` | string |   | Generated from dev.langchain4j.model.googleai.BaseGeminiChatModel.GoogleAiGeminiChatModelBaseBuilder.modelName(java.lang.String) |
| `presence-penalty` | double |   | Generated from dev.langchain4j.model.googleai.BaseGeminiChatModel.GoogleAiGeminiChatModelBaseBuilder.presencePenalty(java.lang.Double) |
| `response-format` | ResponseFormat |   | Generated from dev.langchain4j.model.googleai.BaseGeminiChatModel.GoogleAiGeminiChatModelBaseBuilder.responseFormat(dev.langchain4j.model.chat.request.ResponseFormat) |
| `response-logprobs` | boolean |   | Generated from dev.langchain4j.model.googleai.BaseGeminiChatModel.GoogleAiGeminiChatModelBaseBuilder.responseLogprobs(java.lang.Boolean) |
| `retrieve-google-maps-widget-token` | boolean |   | Generated from dev.langchain4j.model.googleai.BaseGeminiChatModel.GoogleAiGeminiChatModelBaseBuilder.retrieveGoogleMapsWidgetToken(java.lang.Boolean) |
| `return-thinking` | boolean |   | Generated from dev.langchain4j.model.googleai.BaseGeminiChatModel.GoogleAiGeminiChatModelBaseBuilder.returnThinking(java.lang.Boolean) |
| `seed` | int |   | Generated from dev.langchain4j.model.googleai.BaseGeminiChatModel.GoogleAiGeminiChatModelBaseBuilder.seed(java.lang.Integer) |
| `send-thinking` | boolean |   | Generated from dev.langchain4j.model.googleai.BaseGeminiChatModel.GoogleAiGeminiChatModelBaseBuilder.sendThinking(java.lang.Boolean) |
| `stop-sequences` | string\[\] |   | Generated from dev.langchain4j.model.googleai.BaseGeminiChatModel.GoogleAiGeminiChatModelBaseBuilder.stopSequences(java.util.List) |
| `supported-capabilities` | Capability\[\] (RESPONSE_FORMAT_JSON_SCHEMA) |   | Generated from dev.langchain4j.model.googleai.GoogleAiGeminiChatModel.GoogleAiGeminiChatModelBuilder.supportedCapabilities(java.util.Set) |
| `temperature` | double |   | Generated from dev.langchain4j.model.googleai.BaseGeminiChatModel.GoogleAiGeminiChatModelBaseBuilder.temperature(java.lang.Double) |
| `thinking-config` | GeminiThinkingConfig |   | Generated from dev.langchain4j.model.googleai.BaseGeminiChatModel.GoogleAiGeminiChatModelBaseBuilder.thinkingConfig(dev.langchain4j.model.googleai.GeminiThinkingConfig) |
| `timeout` | Duration |   | Generated from dev.langchain4j.model.googleai.BaseGeminiChatModel.GoogleAiGeminiChatModelBaseBuilder.timeout(java.time.Duration) |
| `tool-config` | GeminiFunctionCallingConfig |   | Generated from dev.langchain4j.model.googleai.BaseGeminiChatModel.GoogleAiGeminiChatModelBaseBuilder.toolConfig(dev.langchain4j.model.googleai.GeminiFunctionCallingConfig) |
| `top-k` | int |   | Generated from dev.langchain4j.model.googleai.BaseGeminiChatModel.GoogleAiGeminiChatModelBaseBuilder.topK(java.lang.Integer) |
| `top-p` | double |   | Generated from dev.langchain4j.model.googleai.BaseGeminiChatModel.GoogleAiGeminiChatModelBaseBuilder.topP(java.lang.Double) |

Optional configuration options

### GoogleAiGeminiStreamingChatModel

To automatically create and add `GoogleAiGeminiStreamingChatModel` to the service registry add the following lines to `application.yaml`:

``` yaml
langchain4j:
  providers:
    google-gemini:
      api-key: "${GEMINI_TOKEN}"

  models:
    gemini-streaming-chat-model:
      provider: google-gemini
      model-name: "gemini-2.0-flash"
```

If `enabled` is set to `false`, the configuration is ignored, and the component is not created.

Type: [io.helidon.integrations.langchain4j.providers.gemini.GoogleAiGeminiStreamingChatModelConfig](/apidocs/io.helidon.integrations.langchain4j.providers.google.gemini/io/helidon/integrations/langchain4j/providers/gemini/GoogleAiGeminiStreamingChatModelConfig.html)

This is a standalone configuration type, prefix from configuration root: `langchain4j.providers.google-gemini`

### Configuration options

| key | type | default value | description |
|----|----|----|----|
| `allow-code-execution` | boolean |   | Generated from dev.langchain4j.model.googleai.BaseGeminiChatModel.GoogleAiGeminiChatModelBaseBuilder.allowCodeExecution(java.lang.Boolean) |
| `allow-google-maps` | boolean |   | Generated from dev.langchain4j.model.googleai.BaseGeminiChatModel.GoogleAiGeminiChatModelBaseBuilder.allowGoogleMaps(java.lang.Boolean) |
| `allow-google-search` | boolean |   | Generated from dev.langchain4j.model.googleai.BaseGeminiChatModel.GoogleAiGeminiChatModelBaseBuilder.allowGoogleSearch(java.lang.Boolean) |
| `allow-url-context` | boolean |   | Generated from dev.langchain4j.model.googleai.BaseGeminiChatModel.GoogleAiGeminiChatModelBaseBuilder.allowUrlContext(java.lang.Boolean) |
| `api-key` | string |   | Generated from dev.langchain4j.model.googleai.BaseGeminiChatModel.GoogleAiGeminiChatModelBaseBuilder.apiKey(java.lang.String) |
| `base-url` | string |   | Generated from dev.langchain4j.model.googleai.BaseGeminiChatModel.GoogleAiGeminiChatModelBaseBuilder.baseUrl(java.lang.String) |
| `default-request-parameters` | ChatRequestParameters |   | Generated from dev.langchain4j.model.googleai.BaseGeminiChatModel.GoogleAiGeminiChatModelBaseBuilder.defaultRequestParameters(dev.langchain4j.model.chat.request.ChatRequestParameters) |
| `enable-enhanced-civic-answers` | boolean |   | Generated from dev.langchain4j.model.googleai.BaseGeminiChatModel.GoogleAiGeminiChatModelBaseBuilder.enableEnhancedCivicAnswers(java.lang.Boolean) |
| `enabled` | boolean | `true` | If set to `false`, GoogleAiGeminiStreamingChatModel will not be available even if configured. |
| `frequency-penalty` | double |   | Generated from dev.langchain4j.model.googleai.BaseGeminiChatModel.GoogleAiGeminiChatModelBaseBuilder.frequencyPenalty(java.lang.Double) |
| `http-client-builder` | HttpClientBuilder |   | Generated from dev.langchain4j.model.googleai.BaseGeminiChatModel.GoogleAiGeminiChatModelBaseBuilder.httpClientBuilder(dev.langchain4j.http.client.HttpClientBuilder) |
| `include-code-execution-output` | boolean |   | Generated from dev.langchain4j.model.googleai.BaseGeminiChatModel.GoogleAiGeminiChatModelBaseBuilder.includeCodeExecutionOutput(java.lang.Boolean) |
| `listeners` | ChatModelListener\[\] |   | Generated from dev.langchain4j.model.googleai.BaseGeminiChatModel.GoogleAiGeminiChatModelBaseBuilder.listeners(java.util.List) |
| `log-requests` | boolean |   | Generated from dev.langchain4j.model.googleai.BaseGeminiChatModel.GoogleAiGeminiChatModelBaseBuilder.logRequests(java.lang.Boolean) |
| `log-requests-and-responses` | boolean |   | Generated from dev.langchain4j.model.googleai.BaseGeminiChatModel.GoogleAiGeminiChatModelBaseBuilder.logRequestsAndResponses(java.lang.Boolean) |
| `log-responses` | boolean |   | Generated from dev.langchain4j.model.googleai.BaseGeminiChatModel.GoogleAiGeminiChatModelBaseBuilder.logResponses(java.lang.Boolean) |
| `logger` | Logger |   | Generated from dev.langchain4j.model.googleai.BaseGeminiChatModel.GoogleAiGeminiChatModelBaseBuilder.logger(org.slf4j.Logger) |
| `logprobs` | int |   | Generated from dev.langchain4j.model.googleai.BaseGeminiChatModel.GoogleAiGeminiChatModelBaseBuilder.logprobs(java.lang.Integer) |
| `max-output-tokens` | int |   | Generated from dev.langchain4j.model.googleai.BaseGeminiChatModel.GoogleAiGeminiChatModelBaseBuilder.maxOutputTokens(java.lang.Integer) |
| `media-resolution` | GeminiMediaResolutionLevel (MEDIA_RESOLUTION_UNSPECIFIED, MEDIA_RESOLUTION_LOW, MEDIA_RESOLUTION_MEDIUM, MEDIA_RESOLUTION_HIGH, MEDIA_RESOLUTION_ULTRA_HIGH) |   | Generated from dev.langchain4j.model.googleai.BaseGeminiChatModel.GoogleAiGeminiChatModelBaseBuilder.mediaResolution(dev.langchain4j.model.googleai.GeminiMediaResolutionLevel) |
| `media-resolution-per-part-enabled` | boolean |   | Generated from dev.langchain4j.model.googleai.BaseGeminiChatModel.GoogleAiGeminiChatModelBaseBuilder.mediaResolutionPerPartEnabled(java.lang.Boolean) |
| `model-name` | string |   | Generated from dev.langchain4j.model.googleai.BaseGeminiChatModel.GoogleAiGeminiChatModelBaseBuilder.modelName(java.lang.String) |
| `presence-penalty` | double |   | Generated from dev.langchain4j.model.googleai.BaseGeminiChatModel.GoogleAiGeminiChatModelBaseBuilder.presencePenalty(java.lang.Double) |
| `response-format` | ResponseFormat |   | Generated from dev.langchain4j.model.googleai.BaseGeminiChatModel.GoogleAiGeminiChatModelBaseBuilder.responseFormat(dev.langchain4j.model.chat.request.ResponseFormat) |
| `response-logprobs` | boolean |   | Generated from dev.langchain4j.model.googleai.BaseGeminiChatModel.GoogleAiGeminiChatModelBaseBuilder.responseLogprobs(java.lang.Boolean) |
| `retrieve-google-maps-widget-token` | boolean |   | Generated from dev.langchain4j.model.googleai.BaseGeminiChatModel.GoogleAiGeminiChatModelBaseBuilder.retrieveGoogleMapsWidgetToken(java.lang.Boolean) |
| `return-thinking` | boolean |   | Generated from dev.langchain4j.model.googleai.BaseGeminiChatModel.GoogleAiGeminiChatModelBaseBuilder.returnThinking(java.lang.Boolean) |
| `seed` | int |   | Generated from dev.langchain4j.model.googleai.BaseGeminiChatModel.GoogleAiGeminiChatModelBaseBuilder.seed(java.lang.Integer) |
| `send-thinking` | boolean |   | Generated from dev.langchain4j.model.googleai.BaseGeminiChatModel.GoogleAiGeminiChatModelBaseBuilder.sendThinking(java.lang.Boolean) |
| `stop-sequences` | string\[\] |   | Generated from dev.langchain4j.model.googleai.BaseGeminiChatModel.GoogleAiGeminiChatModelBaseBuilder.stopSequences(java.util.List) |
| `temperature` | double |   | Generated from dev.langchain4j.model.googleai.BaseGeminiChatModel.GoogleAiGeminiChatModelBaseBuilder.temperature(java.lang.Double) |
| `thinking-config` | GeminiThinkingConfig |   | Generated from dev.langchain4j.model.googleai.BaseGeminiChatModel.GoogleAiGeminiChatModelBaseBuilder.thinkingConfig(dev.langchain4j.model.googleai.GeminiThinkingConfig) |
| `timeout` | Duration |   | Generated from dev.langchain4j.model.googleai.BaseGeminiChatModel.GoogleAiGeminiChatModelBaseBuilder.timeout(java.time.Duration) |
| `tool-config` | GeminiFunctionCallingConfig |   | Generated from dev.langchain4j.model.googleai.BaseGeminiChatModel.GoogleAiGeminiChatModelBaseBuilder.toolConfig(dev.langchain4j.model.googleai.GeminiFunctionCallingConfig) |
| `top-k` | int |   | Generated from dev.langchain4j.model.googleai.BaseGeminiChatModel.GoogleAiGeminiChatModelBaseBuilder.topK(java.lang.Integer) |
| `top-p` | double |   | Generated from dev.langchain4j.model.googleai.BaseGeminiChatModel.GoogleAiGeminiChatModelBaseBuilder.topP(java.lang.Double) |

Optional configuration options

## Additional Information

- [LangChain4j Integration](langchain4j.md)

- [LangChain4j Google AI Gemini Documentation](https://docs.langchain4j.dev/integrations/language-models/google-ai-gemini)

- [Google AI Gemini Website](https://ai.google.dev/gemini-api/docs)
