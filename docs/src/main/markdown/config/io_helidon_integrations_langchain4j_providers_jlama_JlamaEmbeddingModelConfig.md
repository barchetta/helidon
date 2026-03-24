# JlamaEmbeddingModelConfig (integrations.langchain4j.providers.jlama) Configuration

Type: [io.helidon.integrations.langchain4j.providers.jlama.JlamaEmbeddingModelConfig](/apidocs/io.helidon.integrations.langchain4j.providers.jlama/io/helidon/integrations/langchain4j/providers/jlama/JlamaEmbeddingModelConfig.html)

This is a standalone configuration type, prefix from configuration root: `langchain4j.providers.jlama`

## Configuration options

| key | type | default value | description |
|----|----|----|----|
| `auth-token` | string |   | Generated from dev.langchain4j.model.jlama.JlamaEmbeddingModel.JlamaEmbeddingModelBuilder.authToken(java.lang.String) |
| `enabled` | boolean | `true` | If set to `false`, JlamaEmbeddingModel will not be available even if configured. |
| `model-cache-path` | Path |   | Generated from dev.langchain4j.model.jlama.JlamaEmbeddingModel.JlamaEmbeddingModelBuilder.modelCachePath(java.nio.file.Path) |
| `pooling-type` | Generator.PoolingType (MODEL, AVG, MAX, SUM) |   | Generated from dev.langchain4j.model.jlama.JlamaEmbeddingModel.JlamaEmbeddingModelBuilder.poolingType(com.github.tjake.jlama.model.functions.Generator.PoolingType) |
| `quantize-model-at-runtime` | boolean |   | Generated from dev.langchain4j.model.jlama.JlamaEmbeddingModel.JlamaEmbeddingModelBuilder.quantizeModelAtRuntime(java.lang.Boolean) |
| `thread-count` | int |   | Generated from dev.langchain4j.model.jlama.JlamaEmbeddingModel.JlamaEmbeddingModelBuilder.threadCount(java.lang.Integer) |
| `working-directory` | Path |   | Generated from dev.langchain4j.model.jlama.JlamaEmbeddingModel.JlamaEmbeddingModelBuilder.workingDirectory(java.nio.file.Path) |

Optional configuration options
