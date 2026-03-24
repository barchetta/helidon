# MockChatRule (integrations.langchain4j.providers.mock) Configuration

Type: [io.helidon.integrations.langchain4j.providers.mock.MockChatRule](/apidocs/io.helidon.integrations.langchain4j.providers.mock/io/helidon/integrations/langchain4j/providers/mock/MockChatRule.html)

## Configuration options

| key | type | default value | description |
|----|----|----|----|
| `pattern` | Pattern |   | The regular expression pattern that this rule matches. |
| `response` | string |   | Static text response that will be returned when the pattern matches. |
| `template` | string |   | Response template (e.g., using placeholders ex.: '\$1' for regex pattern group 1) used when the pattern matches. |

Optional configuration options
