# IvfIndexConfig (integrations.langchain4j.providers.oracle) Configuration

Type: [io.helidon.integrations.langchain4j.providers.oracle.IvfIndexConfig](/apidocs/io.helidon.integrations.langchain4j.providers.oracle/io/helidon/integrations/langchain4j/providers/oracle/IvfIndexConfig.html)

This is a standalone configuration type, prefix from configuration root: `langchain4j.providers.oracle.ivf-index`

## Configuration options

| key | type | default value | description |
|----|----|----|----|
| `create-option` | CreateOption (CREATE_NONE, CREATE_IF_NOT_EXISTS, CREATE_OR_REPLACE) |   | Generated from dev.langchain4j.store.embedding.oracle.IndexBuilder.createOption(dev.langchain4j.store.embedding.oracle.CreateOption) |
| `degree-of-parallelism` | int |   | Generated from dev.langchain4j.store.embedding.oracle.IVFIndexBuilder.degreeOfParallelism(int) |
| `min-vectors-per-partition` | int |   | Generated from dev.langchain4j.store.embedding.oracle.IVFIndexBuilder.minVectorsPerPartition(int) |
| `name` | string |   | Generated from dev.langchain4j.store.embedding.oracle.IndexBuilder.name(java.lang.String) |
| `neighbor-partitions` | int |   | Generated from dev.langchain4j.store.embedding.oracle.IVFIndexBuilder.neighborPartitions(int) |
| `sample-per-partition` | int |   | Generated from dev.langchain4j.store.embedding.oracle.IVFIndexBuilder.samplePerPartition(int) |
| `target-accuracy` | int |   | Generated from dev.langchain4j.store.embedding.oracle.IVFIndexBuilder.targetAccuracy(int) |

Optional configuration options
