# OciGenAiChatModelConfig (integrations.langchain4j.providers.oci.genai) Configuration

Type: [io.helidon.integrations.langchain4j.providers.oci.genai.OciGenAiChatModelConfig](/apidocs/io.helidon.integrations.langchain4j.providers.oraclegenai/io/helidon/integrations/langchain4j/providers/oci/genai/OciGenAiChatModelConfig.html)

This is a standalone configuration type, prefix from configuration root: `langchain4j.providers.oci-gen-ai`

## Configuration options

| key | type | default value | description |
|----|----|----|----|
| `default-request-parameters` | ChatRequestParameters |   | Generated from dev.langchain4j.community.model.oracle.oci.genai.BaseChatModel.Builder.defaultRequestParameters(dev.langchain4j.model.chat.request.ChatRequestParameters) |
| `enabled` | boolean | `true` | If set to `false`, OciGenAiChatModel will not be available even if configured. |
| `frequency-penalty` | double |   | Generated from dev.langchain4j.community.model.oracle.oci.genai.BaseChatModel.Builder.frequencyPenalty(java.lang.Double) |
| `listeners` | ChatModelListener\[\] |   | Generated from dev.langchain4j.community.model.oracle.oci.genai.BaseChatModel.Builder.listeners(java.util.List) |
| `log-probs` | int |   | Generated from dev.langchain4j.community.model.oracle.oci.genai.BaseGenericChatModel.Builder.logProbs(java.lang.Integer) |
| `max-tokens` | int |   | Generated from dev.langchain4j.community.model.oracle.oci.genai.BaseChatModel.Builder.maxTokens(java.lang.Integer) |
| `num-generations` | int |   | Generated from dev.langchain4j.community.model.oracle.oci.genai.BaseGenericChatModel.Builder.numGenerations(java.lang.Integer) |
| `presence-penalty` | double |   | Generated from dev.langchain4j.community.model.oracle.oci.genai.BaseChatModel.Builder.presencePenalty(java.lang.Double) |
| `seed` | int |   | Generated from dev.langchain4j.community.model.oracle.oci.genai.BaseChatModel.Builder.seed(java.lang.Integer) |
| `serving-type` | ServingMode.ServingType (OnDemand, Dedicated) |   | Generated from dev.langchain4j.community.model.oracle.oci.genai.BaseChatModel.Builder.servingType(com.oracle.bmc.generativeaiinference.model.ServingMode.ServingType) |
| `stop` | string\[\] |   | Generated from dev.langchain4j.community.model.oracle.oci.genai.BaseChatModel.Builder.stop(java.util.List) |
| `temperature` | double |   | Generated from dev.langchain4j.community.model.oracle.oci.genai.BaseChatModel.Builder.temperature(java.lang.Double) |
| `top-k` | int |   | Generated from dev.langchain4j.community.model.oracle.oci.genai.BaseChatModel.Builder.topK(java.lang.Integer) |
| `top-p` | double |   | Generated from dev.langchain4j.community.model.oracle.oci.genai.BaseChatModel.Builder.topP(java.lang.Double) |

Optional configuration options
