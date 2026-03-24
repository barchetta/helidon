# ContentRetrieverConfig (integrations.langchain4j) Configuration

Type: [io.helidon.integrations.langchain4j.ContentRetrieverConfig](/apidocs/io.helidon.integrations.langchain4j/io/helidon/integrations/langchain4j/ContentRetrieverConfig.html)

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
<td style="text-align: left;"><p><code>display-name</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Display name for this content retriever configuration.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>embedding-model</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Explicit embedding model to use in the content retriever.</p>
<p>If empty, the default embedding model is used (as resolved by the service registry). If set, the value identifies a named service that provides embedding model bean.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>embedding-store</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Embedding store to use in the content retriever.</p>
<p>The value identifies a named service that provides embedding store implementation used to retrieve relevant content.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>enabled</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>If set to <code>false</code>, component will be disabled even if configured.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>max-results</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Maximum number of results to return from the retriever.</p>
<p>If empty, the retriever implementation default is used.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>min-score</code></p></td>
<td style="text-align: left;"><p>double</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Minimum score threshold for retrieved results.</p>
<p>If empty, the retriever implementation default is used.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>type</code></p></td>
<td style="text-align: left;"><p>ContentRetrieverType (EMBEDDING_STORE_CONTENT_RETRIEVER, WEB_SEARCH_CONTENT_RETRIEVER)</p></td>
<td style="text-align: left;"><p><code>ContentRetrieverType.EMBEDDING_STORE_CONTENT_RETRIEVER</code></p></td>
<td style="text-align: left;"><p>Type of content retriever to create.</p>
<p>Allowed values:</p>
<ul>
<li><p><code>EMBEDDING_STORE_CONTENT_RETRIEVER</code>: Embedding store-backed content retriever.</p></li>
<li><p><code>WEB_SEARCH_CONTENT_RETRIEVER</code>: Web search-backed content retriever.</p></li>
</ul></td>
</tr>
</tbody>
</table>
