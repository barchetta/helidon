# ABAC Provider

Attribute based access control authorization provider.

### Setup

*Maven dependency*

``` xml
<dependency>
    <groupId>io.helidon.security.providers</groupId>
    <artifactId>helidon-security-providers-abac</artifactId>
</dependency>
```

### Overview

Attribute Based Access Control provider

Type: [io.helidon.security.providers.abac.AbacProvider](/apidocs/io.helidon.security.providers.abac/io/helidon/security/providers/abac/AbacProvider.html)

*Config key*

``` text
abac
```

This type provides the following service implementations:

- `io.helidon.security.spi.SecurityProvider`

- `io.helidon.security.spi.AuthorizationProvider`

### Configuration options

| key | type | default value | description |
|----|----|----|----|
| `fail-if-none-validated` | boolean | `true` | Whether to fail if NONE of the attributes is validated. |
| `fail-on-unvalidated` | boolean | `true` | Whether to fail if any attribute is left unvalidated. |

Optional configuration options

### Example code

See the [example](https://github.com/helidon-io/helidon-examples/tree/helidon-4.x/examples/security/attribute-based-access-control) on GitHub.

*Configuration example*

``` yaml
security:
  providers:
    - abac:
```

### Configuration options

The following table shows all configuration options of the provider and their default values

| key | default value | description |
|----|----|----|
| `fail-on-unvalidated` | `true` | "Unvalidated" means: an attribute is defined, but there is no validator available for it |
| `fail-if-none-validated` | `true` | "None validated" means: there was not a single attribute that was validated |

### How does it work?

ABAC uses available validators and validates them against attributes of the authenticated user.

Combinations of `fail-on-unvalidated` and `fail-if-none-validated`:

1.  `true` & `true`: Will fail if any attribute is not validated and if any has failed validation

2.  `false` & `true`: Will fail if there is one or more attributes present and NONE of them is validated or if any has failed validation, Will NOT fail if there is at least one validated attribute and any number of not validated attributes (and NONE failed)

3.  `false` & `false`: Will fail if there is any attribute that failed validation, Will NOT fail if there are no failed validation or if there are NONE validated

Any attribute of the following objects can be used:

- environment (such as time of request) - e.g. env.time.year

- subject (user) - e.g. subject.principal.id

- subject (service) - e.g. service.principal.id

- object (must be explicitly invoked by developer in code, as object cannot be automatically added to security context) - e.g. object.owner

This provider checks that all defined ABAC validators are validated. If there is a definition for a validator that is not checked, the request is denied (depending on configuration as mentioned above).

ABAC provider also allows an object to be used in authorization process, such as when evaluating if an object’s owner is the current user. The following example uses the Expression language validator to demonstrate the point in a JAX-RS resource:

*Example of using an object*

``` java
@Authenticated
@Path("/abac")
public class AbacResource {
    @GET
    @Authorized(explicit = true)
    @PolicyStatement("${env.time.year >= 2017 && object.owner == subject.principal.id}")
    public Response process(@Context SecurityContext context) {
        // probably looked up from a database
        SomeResource res = new SomeResource("user");
        AuthorizationResponse atzResponse = context.authorize(res);

        if (atzResponse.isPermitted()) {
            //do the update
            return Response.ok().entity("fine, sir").build();
        } else {
            return Response.status(Response.Status.FORBIDDEN)
                    .entity(atzResponse.description().orElse("Access not granted"))
                    .build();
        }
    }
}
```

**The following validators are implemented:**

- [Roles](#_role_validator)

- [Scopes](#_scope_validator)

- [EL Policy](#_expression_language_policy_validator)

### Role Validator

Checks whether user/service is in either of the required role(s).

Configuration Key: `role-validator`

Annotations: `@RolesAllowed`, `@RoleValidator.Roles`

*Configuration example for `WebServer`*

``` yaml
security:
  web-server.paths:
    - path: "/user/*"
      roles-allowed: ["user"]
```

*JAX-RS example*

``` java
@RolesAllowed("user")
@RoleValidator.Roles(value = "service_role", subjectType = SubjectType.SERVICE)
@Authenticated
@Path("/abac")
public class AbacResource {
}
```

#### Interaction with JAX-RS sub-resource locators

When using sub-resource locators in JAX-RS, the roles allowed are collected from each "level" of execution: - Application class annotations - Resource class annotations + resource method annotations - Sub-resource class annotations + sub-resource method annotations - Sub-resource class annotations + sub-resource method annotations (for every sub-resource on the path)

The `RolesAllowed` or `Roles` annotation to be used is the last one in the path as defined above.

*Example 1:* There is a `RolesAllowed("admin")` defined on a sub-resource locator resource class. In this case the required role is `admin`.

*Example 2:* There is a `RolesAllowed("admin")` defined on a sub-resource locator resource class and a `RolesAllowed("user")` defined on the method of the sub-resource that provides the response. In this case the required role is `user`.

### Scope Validator

Checks whether user has all the required scopes.

Configuration Key: `scope-validator`

Annotations: `@Scope`

*Configuration example for `WebServer`*

``` yaml
security:
  web-server.paths:
    - path: "/user/*"
      abac.scopes:
        ["calendar_read", "calendar_edit"]
```

*JAX-RS example*

``` java
@Scope("calendar_read")
@Scope("calendar_edit")
@Authenticated
@Path("/abac")
public class AbacResource {
}
```

### Expression Language Policy Validator

Policy executor using Java EE policy expression language (EL)

Configuration Key: `policy-javax-el`

Annotations: `@PolicyStatement`

Example of a policy statement: `${env.time.year >= 2017}`

*Configuration example for `WebServer`*

``` yaml
security:
  web-server.paths:
    - path: "/user/*"
      policy:
        statement: "hasScopes('calendar_read','calendar_edit') AND timeOfDayBetween('8:15', '17:30')"
```

*JAX-RS example*

``` java
@PolicyStatement("${env.time.year >= 2017}")
@Authenticated
@Path("/abac")
public class AbacResource {
}
```

*Configuration example for `JAX-RS` over the configuration*

``` yaml
server:
  features:
    security:
      endpoints:
        - path: "/somePath"
          config:
            abac.policy-validator.statement: "\\${env.time.year >= 2017}"
```
