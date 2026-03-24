# EvictableCache (security.providers.common) Configuration

Type: [io.helidon.security.providers.common.EvictableCache](/apidocs/io.helidon.security.providers.common/io/helidon/security/providers/common/EvictableCache.html)

## Configuration options

| key | type | default value | description |
|----|----|----|----|
| `cache-enabled` | boolean | `true` | If the cacheEnabled is set to false, no caching will be done. Otherwise (default behavior) evictable caching will be used. |
| `cache-evict-delay-millis` | long | `60000` | Delay from the creation of the cache to first eviction |
| `cache-evict-period-millis` | long | `300000` | How often to evict records |
| `cache-overall-timeout-millis` | long | `3600000` | Configure record timeout since its creation. |
| `cache-timeout-millis` | long | `3600000` | Configure record timeout since last access. |
| `evictor-class` | Class |   | Configure evictor to check if a record is still valid. This should be a fast way to check, as it is happening in a ConcurrentHashMap.forEachKey(long, Consumer). This is also called during all get and remove operations to only return valid records. |
| `max-size` | long | `100000` | Configure maximal cache size. |
| `parallelism-threshold` | long | `10000` | Configure parallelism threshold. |

Optional configuration options
