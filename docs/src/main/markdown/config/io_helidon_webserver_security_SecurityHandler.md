# SecurityHandler (webserver.security) Configuration

Type: [io.helidon.webserver.security.SecurityHandler](/apidocs/io.helidon.webserver.security/io/helidon/webserver/security/SecurityHandler.html)

## Configuration options

| key | type | default value | description |
|----|----|----|----|
| `audit` | boolean |   | Whether to audit this request - defaults to false, if enabled, request is audited with event type "request". |
| `audit-event-type` | string |   | Override for event-type, defaults to `request`. |
| `audit-message-format` | string |   | Override for audit message format, defaults to `%3$s %1$s "%2$s" %5$s %6$s requested by %4$s`. |
| `authenticate` | boolean |   | If called, request will go through authentication process - defaults to false (even if authorize is true). |
| `authentication-optional` | boolean |   | If called, authentication failure will not abort request and will continue as anonymous (defaults to false). |
| `authenticator` | string |   | Use a named authenticator (as supported by security - if not defined, default authenticator is used). Will enable authentication. |
| `authorize` | boolean |   | Enable authorization for this route. |
| `authorizer` | string |   | Use a named authorizer (as supported by security - if not defined, default authorizer is used, if none defined, all is permitted). Will enable authorization. |
| `roles-allowed` | string\[\] |   | An array of allowed roles for this path - must have a security provider supporting roles (either authentication or authorization provider). This method enables authentication and authorization (you can disable them again by calling SecurityHandler.skipAuthorization() and authenticationOptional() if needed). |
| `sockets` | string\[\] |   | List of sockets this configuration should be applied to. If empty, the configuration is applied to all configured sockets. |

Optional configuration options
