Proxies and reverse proxies between an HTTP client and your Helidon
application mask important information (for example `Host` header,
originating IP address, protocol) about the request the client sent.
Fortunately, many of these intermediary network nodes set or update
either the [standard HTTP `Forwarded`
header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Forwarded)
or the [non-standard `X-Forwarded-*` family of
headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-For)
to preserve information about the original client request.

Helidon’s requested URI discovery feature allows your application—​and
Helidon itself—​to reconstruct information about the original request
using the `Forwarded` header and the `X-Forwarded-*` family of headers.

When you prepare the connections in your server you can include the
following optional requested URI discovery settings:

- enabled or disabled

- which type or types of requested URI discovery to use:

  - `FORWARDED` - uses the `Forwarded` header

  - `X_FORWARDED` - uses the `X-Forwarded-*` headers

  - `HOST` - uses the `Host` header

- what intermediate nodes to trust

When your application invokes `request.requestedUri()` Helidon iterates
through the discovery types you set up for the receiving connection,
gathering information from the corresponding header(s) for that type. If
the request does not have the corresponding header(s), or your settings
do not trust the intermediate nodes reflected in those headers, then
Helidon tries the next discovery type you set up. Helidon uses the
`HOST` discovery type if you do not set up discovery yourself or if, for
a particular request, it cannot assemble the request information using
any discovery type you did set up for the socket.

To obtain the requested URI information, your handler or service invokes
`ServerRequest.requestedUri()` which returns a `UriInfo` record

You can also use configuration to set up the requested URI discovery
behavior. The following example replicates the settings assigned
programmatically in the earlier code example:
