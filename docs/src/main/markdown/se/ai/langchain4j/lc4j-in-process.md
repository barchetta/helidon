# In-Process Embedding Models

## Contents

- [Maven Coordinates](#_maven_coordinates)

- [In-Process Embedding Model](#_in_process_embedding_model)

- [Additional Information](#_additional_information)

## Maven Coordinates

In addition to the [LangChain4j integration core dependencies](langchain4j.md#maven-coordinates), add:

``` xml
<dependency>
    <groupId>io.helidon.integrations.langchain4j.providers</groupId>
    <artifactId>helidon-integrations-langchain4j-providers-lc4j-in-process</artifactId>
</dependency>
```

Depending on configured model `type`, add model artifact dependencies as follows:

- For `type: all_minilm_l6_v2`, add:

  ``` xml
  <dependency>
      <groupId>dev.langchain4j</groupId>
      <artifactId>langchain4j-embeddings-all-minilm-l6-v2</artifactId>
  </dependency>
  ```

- For `type: all_minilm_l6_v2_q`, add:

  ``` xml
  <dependency>
      <groupId>dev.langchain4j</groupId>
      <artifactId>langchain4j-embeddings-all-minilm-l6-v2-q</artifactId>
  </dependency>
  ```

- For `type: custom`, no additional model-specific dependency is required. Configure `path-to-model`, `path-to-tokenizer`, and `pooling-mode`.

## In-Process Embedding Model

Provider key: `lc4j-in-process`.

LangChain4j in-process embedding models run ONNX embedding inference locally in your process (see [LangChain4j documentation](https://docs.langchain4j.dev/integrations/embedding-models/in-process/)).

In Helidon, a named entry under `langchain4j.models` with `provider: lc4j-in-process` is created as a named singleton declarative service bean in the Helidon service registry. This is how `foo-bar-embedding-model` becomes available for content retrievers and direct injection.

``` yaml
langchain4j:

  models:
    foo-bar-embedding-model: 
      provider: lc4j-in-process
      type: all_minilm_l6_v2_q 

  content-retrievers:
    foo-bar-content-retriever:
      provider: lc4j-content-retriever
      embedding-model: foo-bar-embedding-model 
      embedding-store: foo-bar-inmemory-embedding-store
```

- Creates a named embedding model singleton bean (`foo-bar-embedding-model`) in Helidon.

- Sets provider defaults for in-process embedding model creation.

- Uses the named in-process embedding model from the service registry.

For `type: custom`, configure model and tokenizer paths and pooling mode:

``` yaml
langchain4j:
  models:
    foo-bar-content-retriever:
      provider: lc4j-in-process
      type: custom 
      path-to-model: "/models/custom-embeddings/model.onnx" 
      path-to-tokenizer: "/models/custom-embeddings/tokenizer.json" 
      pooling-mode: mean 
```

- Uses user-provided ONNX model.

- Required for custom type.

- Required for custom type.

- Required for custom type; maps to LangChain4j pooling mode.

If `type: custom` is selected but any of `path-to-model`, `path-to-tokenizer`, or `pooling-mode` is missing, Helidon fails startup with a configuration exception.

``` java
@Service.Singleton
public class EmbeddingModelConsumer {
    EmbeddingModelConsumer(@Service.Named("foo-bar-embedding-model") EmbeddingModel embeddingModel) { 
    }
}
```

- Injects the named in-process embedding model bean directly into another Helidon declarative service.

Configuration properties:

Type: [io.helidon.integrations.langchain4j.providers.lc4jinprocess.InProcessEmbeddingModelConfig](/apidocs/io.helidon.integrations.langchain4j.providers.lc4jinprocess/io/helidon/integrations/langchain4j/providers/lc4jinprocess/InProcessEmbeddingModelConfig.html)

This is a standalone configuration type, prefix from configuration root: `langchain4j.providers.lc4j-in-process`

### Configuration options

<table style="width:100%;">
<caption>Optional configuration options</caption>
<colgroup>
<col style="width: 23%" />
<col style="width: 23%" />
<col style="width: 15%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">key</th>
<th style="text-align: left;">type</th>
<th style="text-align: left;">default value</th>
<th style="text-align: left;">description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>enabled</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Whether the embedding model is enabled. If set to <code>false</code>, the model will not be available even if configured.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>executor</code></p></td>
<td style="text-align: left;"><p><a href="../../../se/ai/langchain4j/../../../config/io_helidon_common_configurable_ThreadPoolConfig.xml">ThreadPoolConfig</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Executor configuration used by the embedding model.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>path-to-model</code></p></td>
<td style="text-align: left;"><p>Path</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>The path to the modelPath file (e.g., "/path/to/model.onnx").</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>path-to-tokenizer</code></p></td>
<td style="text-align: left;"><p>Path</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>The path to the tokenizer file (e.g., "/path/to/tokenizer.json").</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>pooling-mode</code></p></td>
<td style="text-align: left;"><p>PoolingMode (CLS, MEAN)</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>The pooling model to use. Can be found in the "…​/1_Pooling/config.json" file on HuggingFace. Here is an <a href="https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/blob/main/1_Pooling/config.json"> example</a>. <code>"pooling_mode_mean_tokens": true</code> means that PoolingMode.MEAN should be used.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>type</code></p></td>
<td style="text-align: left;"><p>InProcessModelType (ALL_MINILM_L6_V2, ALL_MINILM_L6_V2_Q, CUSTOM)</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Which in-process ONNX model variant should be used.</p>
<p>Allowed values:</p>
<ul>
<li><p><code>ALL_MINILM_L6_V2</code>: The default "all-minilm-l6-v2" in-process embedding model.</p></li>
<li><p><code>ALL_MINILM_L6_V2_Q</code>: The quantized variant of the "all-minilm-l6-v2" in-process embedding model, typically offering reduced memory footprint and potentially faster inference at some quality cost.</p></li>
<li><p><code>CUSTOM</code>: A custom, user-provided in-process ONNX embedding model, when selected <code>path-to-model</code> and <code>path-to-tokenizer</code> needs to be provided.</p></li>
</ul></td>
</tr>
</tbody>
</table>

## Additional Information

- [LangChain4j Integration](langchain4j.md)

- [Lc4j Built-in Providers](lc4j-providers.md)

- [Retrieval-Augmented Generation (RAG)](rag.md)
