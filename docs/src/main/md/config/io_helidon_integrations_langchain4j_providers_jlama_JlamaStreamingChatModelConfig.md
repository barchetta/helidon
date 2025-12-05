Type:
[io.helidon.integrations.langchain4j.providers.jlama.JlamaStreamingChatModelConfig](/apidocs/io.helidon.integrations.langchain4j.providers.jlama/io/helidon/integrations/langchain4j/providers/jlama/JlamaStreamingChatModelConfig.html)

This is a standalone configuration type, prefix from configuration root:
`langchain4j.jlama.streaming-chat-model`

# Configuration options

| key | type | default value | description |
|----|----|----|----|
| `auth-token` | string |   | Generated from dev.langchain4j.model.jlama.JlamaStreamingChatModel.JlamaStreamingChatModelBuilder.authToken(java.lang.String) |
| `enabled` | boolean |   | If set to `false` (default), JlamaStreamingChatModel will not be available even if configured. |
| `max-tokens` | int |   | Generated from dev.langchain4j.model.jlama.JlamaStreamingChatModel.JlamaStreamingChatModelBuilder.maxTokens(java.lang.Integer) |
| `model-cache-path` | Path |   | Generated from dev.langchain4j.model.jlama.JlamaStreamingChatModel.JlamaStreamingChatModelBuilder.modelCachePath(java.nio.file.Path) |
| `quantize-model-at-runtime` | boolean |   | Generated from dev.langchain4j.model.jlama.JlamaStreamingChatModel.JlamaStreamingChatModelBuilder.quantizeModelAtRuntime(java.lang.Boolean) |
| `temperature` | float |   | Generated from dev.langchain4j.model.jlama.JlamaStreamingChatModel.JlamaStreamingChatModelBuilder.temperature(java.lang.Float) |
| `thread-count` | int |   | Generated from dev.langchain4j.model.jlama.JlamaStreamingChatModel.JlamaStreamingChatModelBuilder.threadCount(java.lang.Integer) |
| `working-directory` | Path |   | Generated from dev.langchain4j.model.jlama.JlamaStreamingChatModel.JlamaStreamingChatModelBuilder.workingDirectory(java.nio.file.Path) |
| `working-quantized-type` | DType (BOOL, U8, I8, I16, U16, F16, BF16, I32, U32, F32, F64, I64, U64, Q4, Q5) |   | Generated from dev.langchain4j.model.jlama.JlamaStreamingChatModel.JlamaStreamingChatModelBuilder.workingQuantizedType(com.github.tjake.jlama.safetensors.DType) |

Optional configuration options
