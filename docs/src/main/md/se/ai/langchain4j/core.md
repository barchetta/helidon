# Overview

This module adds support for selected LangChain4j core components.

# Maven Coordinates

No additional dependencies are required beyond the [LangChain4j
integration core dependencies](langchain4j.xml#maven-coordinates).

# Components

## EmbeddingStoreContentRetriever

To automatically create and add `EmbeddingStoreContentRetriever` to the
service registry add the following lines to `application.yaml`:

``` yaml
langchain4j:
  rag:
    embedding-store-content-retriever:
      enabled: true
      embedding-model:
        service-registry.named: "@default"
      embedding-store:
        service-registry.named: "@default"
```

If `enabled` is set to `false`, the configuration is ignored, and the
component is not created.

Full list of configuration properties:

| Key | Type | Description |
|----|----|----|
| `display-name` | string | Display name. |
| `enabled` | boolean | If set to `false`, embedding store content retriever will be disabled even if configured. |
| `max-results` | int | Maximum number of results. |
| `min-score` | double | Minimum score threshold. |
| `embedding-model` | string | Service in the service registry that implements `dev.langchain4j.model.embedding.EmbeddingModel`. Use `embedding-model.service-registry.named: "serviceName"` to select a named service bean. Use `@default` (the default option) to refer to the unnamed service. |
| `embedding-store` | string | Name of the service in the service registry that implements `dev.langchain4j.model.embedding.EmbeddingStore<TextSegment>`. Use `embedding-model.service-registry.named: "serviceName"` to select a named service bean. Use `@default` (the default option) to refer to the unnamed service. |

# Additional Information

- [LangChain4j Integration](langchain4j.md)
