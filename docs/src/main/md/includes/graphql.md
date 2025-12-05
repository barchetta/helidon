The following configuration keys can be used to set up integration with
WebServer:

| key | default value | description |
|----|----|----|
| `graphql.web-context` | `/graphql` | Context that serves the GraphQL endpoint. |
| `graphql.schema-uri` | `/schema.graphql` | URI that serves the schema (under web context) |
| `graphql.cors` |   | CORS configuration for this service |
| `graphql.executor-service` |   | Configuration of `ServerThreadPoolSupplier` used to set up executor service |

The following configuration keys can be used to set up GraphQL
invocation:

| key | default value | description |
|----|----|----|
| `graphql.default-error-message` | `Server Error` | Error message to send to caller in case of error |
| `graphql.exception-white-list` |   | Array of checked exception classes that should return default error message |
| `graphql.exception-black-list` |   | Array of unchecked exception classes that should return message to caller (instead of default error message) |
