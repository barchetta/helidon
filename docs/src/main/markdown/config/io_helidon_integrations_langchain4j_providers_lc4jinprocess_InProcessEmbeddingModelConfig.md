# InProcessEmbeddingModelConfig (integrations.langchain4j.providers.lc4jinprocess) Configuration

Type: [io.helidon.integrations.langchain4j.providers.lc4jinprocess.InProcessEmbeddingModelConfig](/apidocs/io.helidon.integrations.langchain4j.providers.lc4jinprocess/io/helidon/integrations/langchain4j/providers/lc4jinprocess/InProcessEmbeddingModelConfig.html)

This is a standalone configuration type, prefix from configuration root: `langchain4j.providers.lc4j-in-process`

## Configuration options

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
<td style="text-align: left;"><p><a href="../config/../config/io_helidon_common_configurable_ThreadPoolConfig.xml">ThreadPoolConfig</a></p></td>
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
