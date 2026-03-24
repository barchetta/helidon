# HTTP Signatures Provider

Support for HTTP Signatures.

### Setup

*Maven dependency*

``` xml
<dependency>
    <groupId>io.helidon.security.providers</groupId>
    <artifactId>helidon-security-providers-http-sign</artifactId>
</dependency>
```

### Overview

HTTP header signature provider.

Type: [io.helidon.security.providers.httpsign.HttpSignProvider]({javadoc-base-url}/io.helidon.security.providers.httpsign/io/helidon/security/providers/httpsign/HttpSignProvider.md)

*Config key*

``` text
http-signatures
```

This type provides the following service implementations:

- `io.helidon.security.spi.AuthenticationProvider`

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
<td style="text-align: left;"><p><code>backward-compatible-eol</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>false</code></p></td>
<td style="text-align: left;"><p>Enable support for Helidon versions before 3.0.0 (exclusive).</p>
<p>Until version 3.0.0 (exclusive) there was a trailing end of line added to the signed data. To be able to communicate cross versions, we must configure this when talking to older versions of Helidon. Default value is <code>false</code>. In Helidon 2.x, this switch exists as well and the default is <code>true</code>, to allow communication between versions as needed.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>headers</code></p></td>
<td style="text-align: left;"><p>HttpSignHeader[] (SIGNATURE, AUTHORIZATION, CUSTOM)</p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Add a header that is validated on inbound requests. Provider may support more than one header to validate.</p>
<p>Allowed values:</p>
<ul>
<li><p><code>SIGNATURE</code>: Creates (or validates) a "Signature" header.</p></li>
<li><p><code>AUTHORIZATION</code>: Creates (or validates) an "Authorization" header, that contains "Signature" as the beginning of its content (the rest of the header is the same as for SIGNATURE.</p></li>
<li><p><code>CUSTOM</code>: Custom provided using a io.helidon.security.util.TokenHandler.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>inbound.keys</code></p></td>
<td style="text-align: left;"><p><a href="../../../includes/security/providers/../../../config/io_helidon_security_providers_httpsign_InboundClientDefinition.xml">InboundClientDefinition[]</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Add inbound configuration. This is used to validate signature and authenticate the party.</p>
<p>The same can be done through configuration:</p>
<pre><code>{
 name = &quot;http-signatures&quot;
 class = &quot;HttpSignProvider&quot;
 http-signatures {
     inbound {
         # This configures the InboundClientDefinition
         keys: [
         {
             key-id = &quot;service1&quot;
             hmac.secret = &quot;${CLEAR=password}&quot;
         }]
     }
 }
}</code></pre></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>optional</code></p></td>
<td style="text-align: left;"><p>boolean</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"><p>Set whether the signature is optional. If set to true (default), this provider will SecurityResponse.SecurityStatus.ABSTAIN from this request if signature is not present. If set to false, this provider will SecurityResponse.SecurityStatus.FAILURE fail if signature is not present.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>outbound</code></p></td>
<td style="text-align: left;"><p><a href="../../../includes/security/providers/../../../config/io_helidon_security_providers_common_OutboundConfig.xml">OutboundConfig</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Add outbound targets to this builder. The targets are used to chose what to do for outbound communication. The targets should have OutboundTargetDefinition attached through OutboundTarget.Builder.customObject(Class, Object) to tell us how to sign the request.</p>
<p>The same can be done through configuration:</p>
<pre><code>{
 name = &quot;http-signatures&quot;
 class = &quot;HttpSignProvider&quot;
 http-signatures {
     targets: [
     {
         name = &quot;service2&quot;
         hosts = [&quot;localhost&quot;]
         paths = [&quot;/service2/.*&quot;]
&#10;         # This configures the OutboundTargetDefinition
         signature {
             key-id = &quot;service1&quot;
             hmac.secret = &quot;${CLEAR=password}&quot;
         }
     }]
 }
}</code></pre></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>realm</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p><code>helidon</code></p></td>
<td style="text-align: left;"><p>Realm to use for challenging inbound requests that do not have "Authorization" header in case header is HttpSignHeader.AUTHORIZATION and singatures are not optional.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>sign-headers</code></p></td>
<td style="text-align: left;"><p><a href="../../../includes/security/providers/../../../config/io_helidon_security_providers_httpsign_SignedHeadersConfig_HeadersConfig.xml">SignedHeadersConfig.HeadersConfig[]</a></p></td>
<td style="text-align: left;"><p> </p></td>
<td style="text-align: left;"><p>Override the default inbound required headers (e.g. headers that MUST be signed and headers that MUST be signed IF present).</p>
<p>Defaults:</p>
<ul>
<li><p>get, head, delete methods: date, (request-target), host are mandatory; authorization if present (unless we are creating/validating the HttpSignHeader.AUTHORIZATION ourselves</p></li>
<li><p>put, post: same as above, with addition of: content-length, content-type and digest if present</p></li>
<li><p>for other methods: date, (request-target)</p></li>
</ul>
<p>Note that this provider DOES NOT validate the "Digest" HTTP header, only the signature.</p></td>
</tr>
</tbody>
</table>

### Example code

See the [example]({helidon-github-examples-url}/security/webserver-signatures) on GitHub.

*Configuration example*

``` yaml
security:
  providers:
    - http-signatures:
        inbound:
          keys:
            - key-id: "service1-hmac"
              principal-name: "Service1 - HMAC signature"
              hmac.secret: "${CLEAR=changeit}"
            - key-id: "service1-rsa"
              principal-name: "Service1 - RSA signature"
              public-key:
                keystore:
                  resource.path: "src/main/resources/keystore.p12"
                  passphrase: "changeit"
                  cert.alias: "service_cert"
        outbound:
          - name: "service2-hmac"
            hosts: ["localhost"]
            paths: ["/service2"]
            signature:
              key-id: "service1-hmac"
              hmac.secret: "${CLEAR=changeit}"
          - name: "service2-rsa"
            hosts: ["localhost"]
            paths: ["/service2-rsa.*"]
            signature:
              key-id: "service1-rsa"
              private-key:
                keystore:
                  resource.path: "src/main/resources/keystore.p12"
                  passphrase: "changeit"
                  key.alias: "myPrivateKey"
```

### Signature basics

- standard: based on <https://tools.ietf.org/html/draft-cavage-http-signatures-03>

- key-id: an arbitrary string used to locate signature configuration - when a request is received the provider locates validation configuration based on this id (e.g. HMAC shared secret or RSA public key). Commonly used meanings are: key fingerprint (RSA); API Key

### How does it work?

**Inbound Signatures** We act as a server and another party is calling us with a signed HTTP request. We validate the signature and assume identity of the caller.

**Outbound Signatures** We act as a client and we sign our outgoing requests. If there is a matching `outbound` target specified in configuration, its configuration will be applied for signing the outgoing request, otherwise there is no signature added
