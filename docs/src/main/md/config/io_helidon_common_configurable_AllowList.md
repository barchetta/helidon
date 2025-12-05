Type:
[io.helidon.common.configurable.AllowList](/apidocs/io.helidon.common.configurable/io/helidon/common/configurable/AllowList.html)

# Configuration options

| key | type | default value | description |
|----|----|----|----|
| `allow.all` | boolean | `false` | Allows all strings to match (subject to "deny" conditions). An `allow.all` setting of `false` does not deny all strings but rather represents the absence of a universal match, meaning that other allow and deny settings determine the matching outcomes. |
| `allow.exact` | string\[\] |   | Exact strings to allow. |
| `allow.pattern` | Pattern\[\] |   | Patterns specifying strings to allow. |
| `allow.prefix` | string\[\] |   | Prefixes specifying strings to allow. |
| `allow.suffix` | string\[\] |   | Suffixes specifying strings to allow. |
| `deny.exact` | string\[\] |   | Exact strings to deny. |
| `deny.pattern` | Pattern\[\] |   | Patterns specifying strings to deny. |
| `deny.prefix` | string\[\] |   | Prefixes specifying strings to deny. |
| `deny.suffix` | string\[\] |   | Suffixes specifying strings to deny. |

Optional configuration options
