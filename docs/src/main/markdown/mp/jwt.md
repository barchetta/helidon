# JWT Authentication

## Contents

- [Overview](#_overview)

- [Maven Coordinates](#maven-coordinates)

- [Usage](#_usage)

- [API](#_api)

- [Configuration](#_configuration)

- [Examples](#_examples)

- [Additional Information](#_additional_information)

- [Reference](#_reference)

## Overview

JSON Web Tokens (JWT) are an open, industry standard [(RFC 7519)](https://datatracker.ietf.org/doc/html/rfc7519) method for representing claims securely between two parties.

JSON Web Token defines a compact and self-contained way for securely transmitting information between parties as a JSON object. With JWT Auth you can integrate security features such as single sign on into your Helidon MP applications.

## Maven Coordinates

To enable JWT Authentication, either add a dependency on the [helidon-microprofile bundle](../mp/introduction/microprofile.md) or add the following dependency to your project’s `pom.xml` (see [Managing Dependencies](../about/managing-dependencies.md)).

``` xml
<dependency>
    <groupId>io.helidon.microprofile.jwt</groupId>
    <artifactId>helidon-microprofile-jwt-auth</artifactId>
</dependency>
```

## Usage

The main configuration point for JWT Auth is a JAX-RS Application class. As this class is discovered using CDI, it must have a bean defining annotation.

Minimal required setup is done using `@LoginConfig(authMethod = "MP-JWT")`:

``` java
@LoginConfig(authMethod = "MP-JWT")
@ApplicationScoped
public class ProtectedApplication extends Application {
}
```

## API

The following interfaces and annotations are used to work with JWT in Helidon MP:

- `JsonWebToken` - an interface used in CDI beans *(@RequestScoped)* dependency injection to obtain the JWT of the currently executing caller.

- `@Claim` - an annotation used by CDI bean *(@RequestScoped)* dependency injection to obtain individual claims from the caller’s JWT.

- `ClaimValue` - a proxy interface used with `@Claim` annotation to оbtain the value of a claim by calling `getValue()`.

## Configuration

MP-JWT Auth configuration is defined by the spec (options prefixed with \`mp.jwt.\`), and we add a few configuration options for the security provider (options prefixed with \`security.providers.mp-jwt-auth.\`)

Type: [io.helidon.microprofile.jwt.auth.JwtAuthProvider](/apidocs/io.helidon.microprofile.jwt.auth/io/helidon/microprofile/jwt/auth/JwtAuthProvider.html)

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
<td style="text-align: left;"><p><code>mp.jwt.decrypt.key.algorithm</code></p></td>
<td style="text-align: left;"><p>string (RSA-OAEP, RSA-OAEP-256)</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Expected key management algorithm supported by the MP JWT endpoint. Supported algorithms are either <code>RSA-OAEP</code> or <code>RSA-OAEP-256</code>. If no algorithm is set, both algorithms must be accepted.</p>
<p>Allowed values:</p>
<ul>
<li><p><code>RSA-OAEP</code>: RSA-OAEP Algorithm</p></li>
<li><p><code>RSA-OAEP-256</code>: RSA-OAEP-256 Algorithm</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>mp.jwt.decrypt.key.location</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Private key for decryption of encrypted claims. The value may be a relative path or a URL.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>mp.jwt.token.cookie</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p><code>Bearer</code></p></td>
<td style="text-align: left;"><p>Specific cookie property name where we should search for JWT property.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>mp.jwt.token.header</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p><code>Authorization</code></p></td>
<td style="text-align: left;"><p>Name of the header expected to contain the token.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>mp.jwt.verify.audiences</code></p></td>
<td style="text-align: left;"><p>string[]</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Expected audiences of incoming tokens.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>mp.jwt.verify.clock.skew</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p><code>5</code></p></td>
<td style="text-align: left;"><p>Clock skew to be accounted for in token expiration and max age validations in seconds.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>mp.jwt.verify.issuer</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Expected issuer in incoming requests.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>mp.jwt.verify.publickey</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>String representation of the public key.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>mp.jwt.verify.publickey.location</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Path to public key. The value may be a relative path or a URL.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>mp.jwt.verify.token.age</code></p></td>
<td style="text-align: left;"><p>int</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Maximal expected token age in seconds. If this value is set, <code>iat</code> claim needs to be present in the JWT.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>security.providers.mp-jwt-auth.allow-impersonation</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>false</code></p></td>
<td style="text-align: left;"><p>Whether to allow impersonation by explicitly overriding username from outbound requests using io.helidon.security.EndpointConfig.PROPERTY_OUTBOUND_ID property. By default this is not allowed and identity can only be propagated.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>security.providers.mp-jwt-auth.atn-token.default-key-id</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Default JWT key ID which should be used.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>security.providers.mp-jwt-auth.atn-token.handler</code></p></td>
<td style="text-align: left;"><p><a href="../mp/../config/io_helidon_security_util_TokenHandler.xml">TokenHandler</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Token handler to extract username from request. Uses <code>Authorization</code> header with `bearer ` prefix by default.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>security.providers.mp-jwt-auth.atn-token.jwk.resource</code></p></td>
<td style="text-align: left;"><p><a href="../mp/../config/io_helidon_common_configurable_Resource.xml">Resource</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>JWK resource for authenticating the request</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>security.providers.mp-jwt-auth.atn-token.jwt-audience</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Audience expected in inbound JWTs.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>security.providers.mp-jwt-auth.atn-token.verify-key</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Path to public key. The value may be a relative path or a URL.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>security.providers.mp-jwt-auth.authenticate</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Whether to authenticate requests.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>security.providers.mp-jwt-auth.load-on-startup</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>false</code></p></td>
<td style="text-align: left;"><p>Whether to load JWK verification keys on server startup Default value is <code>false</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>security.providers.mp-jwt-auth.optional</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>false</code></p></td>
<td style="text-align: left;"><p>Whether authentication is required. By default, request will fail if the username cannot be extracted. If set to false, request will process and this provider will abstain.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>security.providers.mp-jwt-auth.principal-type</code></p></td>
<td style="text-align: left;"><p>SubjectType (USER, SERVICE)</p></td>
<td style="text-align: left;"><p><code>USER</code></p></td>
<td style="text-align: left;"><p>Principal type this provider extracts (and also propagates).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>security.providers.mp-jwt-auth.propagate</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Whether to propagate identity.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>security.providers.mp-jwt-auth.sign-token</code></p></td>
<td style="text-align: left;"><p><a href="../mp/../config/io_helidon_security_providers_common_OutboundConfig.xml">OutboundConfig</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Configuration of outbound rules.</p></td>
</tr>
</tbody>
</table>

A configuration example in `microprofile-config.properties`:

``` properties
mp.jwt.verify.issuer=https://{PublicIssuerDomain}/oauth2/default
mp.jwt.verify.publickey.location=${mp.jwt.verify.issuer}/v1/keys
```

## Examples

``` java
@Path("/hello")
public class HelloResource {

    @GET
    @Produces(TEXT_PLAIN)
    public String hello(@Context SecurityContext context) {
        Optional<Principal> userPrincipal = context.userPrincipal();
        return "Hello, " + userPrincipal.get().getName() + "!";
    }
}
```

Do not forget to annotate the `HelloApplication` class to enable JWT:

``` java
@LoginConfig(authMethod = "MP-JWT")
@ApplicationScoped
public class HelloApplication extends Application {

    @Override
    public Set<Class<?>> getClasses() {
        return Set.of(HelloResource.class);
    }
}
```

Add the following configuration in `microprofile-config.properties`:

``` properties
mp.jwt.verify.issuer=https://{IssuerPublicDomain}/oauth2/default
mp.jwt.verify.publickey.location=${mp.jwt.verify.issuer}/v1/keys
```

Obtain the Security Token from external issuer:

``` bash
TOKEN=sdf4dDSWFcswdsffDSasEgv...
```

Run the application and execute an http request against it:

``` bash
curl -X GET -I -H "Authorization: Bearer $TOKEN" http://localhost:8080/hello
```

*Curl output*

``` bash
HTTP/1.1 200 OK
Date: 08.06.2022 10:33:47 EEST
connection: keep-alive
content-length: 28

Hello, secure@helidon.io!
```

which means that the request successfully passed authentication.

## Additional Information

Learn more about JWT authentication at:  
[Eclipse MicroProfile Interoperable JWT RBAC](https://download.eclipse.org/microprofile/microprofile-jwt-auth-2.1#_introduction)

## Reference

- [MicroProfile JWT Auth Spec](https://download.eclipse.org/microprofile/microprofile-jwt-auth-2.1/microprofile-jwt-auth-spec-2.1.html)

- [MicroProfile JWT Auth GitHub Repository](https://github.com/eclipse/microprofile-jwt-auth)
