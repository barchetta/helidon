# OciGenAiCohereStreamingChatModelConfig (integrations.langchain4j.providers.oci.genai) Configuration

Type: [io.helidon.integrations.langchain4j.providers.oci.genai.OciGenAiCohereStreamingChatModelConfig](/apidocs/io.helidon.integrations.langchain4j.providers.oraclegenai/io/helidon/integrations/langchain4j/providers/oci/genai/OciGenAiCohereStreamingChatModelConfig.html)

This is a standalone configuration type, prefix from configuration root: `langchain4j.providers.oci-gen-ai-cohere`

## Configuration options

| key | type | default value | description |
|----|----|----|----|
| `citation-quality` | CohereChatRequest.CitationQuality (Accurate, Fast) |   | Generated from dev.langchain4j.community.model.oracle.oci.genai.BaseCohereChatModel.Builder.citationQuality(com.oracle.bmc.generativeaiinference.model.CohereChatRequest.CitationQuality) |
| `default-request-parameters` | ChatRequestParameters |   | Generated from dev.langchain4j.community.model.oracle.oci.genai.BaseChatModel.Builder.defaultRequestParameters(dev.langchain4j.model.chat.request.ChatRequestParameters) |
| `documents` | Object\[\] |   | Generated from dev.langchain4j.community.model.oracle.oci.genai.BaseCohereChatModel.Builder.documents(java.util.List) |
| `enabled` | boolean | `true` | If set to `false`, OciGenAiCohereStreamingChatModel will not be available even if configured. |
| `frequency-penalty` | double |   | Generated from dev.langchain4j.community.model.oracle.oci.genai.BaseChatModel.Builder.frequencyPenalty(java.lang.Double) |
| `is-raw-prompting` | boolean |   | Generated from dev.langchain4j.community.model.oracle.oci.genai.BaseCohereChatModel.Builder.isRawPrompting(java.lang.Boolean) |
| `is-search-queries-only` | boolean |   | Generated from dev.langchain4j.community.model.oracle.oci.genai.BaseCohereChatModel.Builder.isSearchQueriesOnly(java.lang.Boolean) |
| `listeners` | ChatModelListener\[\] |   | Generated from dev.langchain4j.community.model.oracle.oci.genai.BaseChatModel.Builder.listeners(java.util.List) |
| `max-input-tokens` | int |   | Generated from dev.langchain4j.community.model.oracle.oci.genai.BaseCohereChatModel.Builder.maxInputTokens(java.lang.Integer) |
| `max-tokens` | int |   | Generated from dev.langchain4j.community.model.oracle.oci.genai.BaseChatModel.Builder.maxTokens(java.lang.Integer) |
| `preamble-override` | string |   | Generated from dev.langchain4j.community.model.oracle.oci.genai.BaseCohereChatModel.Builder.preambleOverride(java.lang.String) |
| `presence-penalty` | double |   | Generated from dev.langchain4j.community.model.oracle.oci.genai.BaseChatModel.Builder.presencePenalty(java.lang.Double) |
| `prompt-truncation` | CohereChatRequest.PromptTruncation (Off, AutoPreserveOrder) |   | Generated from dev.langchain4j.community.model.oracle.oci.genai.BaseCohereChatModel.Builder.promptTruncation(com.oracle.bmc.generativeaiinference.model.CohereChatRequest.PromptTruncation) |
| `seed` | int |   | Generated from dev.langchain4j.community.model.oracle.oci.genai.BaseChatModel.Builder.seed(java.lang.Integer) |
| `serving-type` | ServingMode.ServingType (OnDemand, Dedicated) |   | Generated from dev.langchain4j.community.model.oracle.oci.genai.BaseChatModel.Builder.servingType(com.oracle.bmc.generativeaiinference.model.ServingMode.ServingType) |
| `stop` | string\[\] |   | Generated from dev.langchain4j.community.model.oracle.oci.genai.BaseChatModel.Builder.stop(java.util.List) |
| `temperature` | double |   | Generated from dev.langchain4j.community.model.oracle.oci.genai.BaseChatModel.Builder.temperature(java.lang.Double) |
| `top-k` | int |   | Generated from dev.langchain4j.community.model.oracle.oci.genai.BaseChatModel.Builder.topK(java.lang.Integer) |
| `top-p` | double |   | Generated from dev.langchain4j.community.model.oracle.oci.genai.BaseChatModel.Builder.topP(java.lang.Double) |

Optional configuration options
