Type:
[io.helidon.integrations.langchain4j.EmbeddingStoreContentRetrieverConfig](/apidocs/io.helidon.integrations.langchain4j/io/helidon/integrations/langchain4j/EmbeddingStoreContentRetrieverConfig.html)

This is a standalone configuration type, prefix from configuration root:
`langchain4j.rag.embedding-store-content-retriever`

# Configuration options

| key | type | default value | description |
|----|----|----|----|
| `display-name` | string |   | The display name. |
| `embedding-model` | EmbeddingModel |   | Explicit embedding model to use in the content retriever. |
| `embedding-store` | EmbeddingStore |   | Embedding store to use in the content retriever. |
| `enabled` | boolean |   | If set to `false`, embedding store content retriever will be disabled even if configured. |
| `max-results` | int |   | The maximum number of results. |
| `min-score` | double |   | The minimum score threshold. |

Optional configuration options
