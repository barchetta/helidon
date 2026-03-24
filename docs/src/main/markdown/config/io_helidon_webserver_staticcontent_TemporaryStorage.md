# TemporaryStorage (webserver.staticcontent) Configuration

Type: [io.helidon.webserver.staticcontent.TemporaryStorage](/apidocs/io.helidon.webserver.staticcontent/io/helidon/webserver/staticcontent/TemporaryStorage.html)

## Configuration options

| key | type | default value | description |
|----|----|----|----|
| `delete-on-exit` | boolean | `true` | Whether temporary files should be deleted on JVM exit. This is enabled by default, yet it may be useful for debugging purposes to keep the files in place. |
| `directory` | Path |   | Location of the temporary storage, defaults to temporary storage configured for the JVM. |
| `enabled` | boolean | `true` | Whether the temporary storage is enabled, defaults to `true`. If disabled, nothing is stored in temporary directory (may have performance impact, as for example a file may be extracted from a zip file on each request). |
| `file-prefix` | string | `helidon-ws` | Prefix of the files in temporary storage. |
| `file-suffix` | string | `.je` | Suffix of the files in temporary storage. |

Optional configuration options
