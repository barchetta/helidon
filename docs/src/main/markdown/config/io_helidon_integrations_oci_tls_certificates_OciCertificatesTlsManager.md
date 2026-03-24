# OciCertificatesTlsManager (integrations.oci.tls.certificates) Configuration

Type: [io.helidon.integrations.oci.tls.certificates.OciCertificatesTlsManager](/apidocs/io.helidon.integrations.oci.tls.certificates/io/helidon/integrations/oci/tls/certificates/OciCertificatesTlsManager.html)

## Configuration options

| key | type | default value | description |
|----|----|----|----|
| `ca-ocid` | string |   | The Certificate Authority OCID. |
| `cert-ocid` | string |   | The Certificate OCID. |
| `compartment-ocid` | string |   | The OCID of the compartment the services are in. |
| `key-ocid` | string |   | The Key OCID. |
| `key-password` | Supplier |   | The Key password. |
| `schedule` | string |   | The schedule for trigger a reload check, testing whether there is a new io.helidon.common.tls.Tls instance available. |
| `vault-crypto-endpoint` | URI |   | The address to use for the OCI Key Management Service / Vault crypto usage. Each OCI Vault has public crypto and management endpoints. We need to specify the crypto endpoint of the vault we are rotating the private keys in. The implementation expects both client and server to store the private key in the same vault. |
| `vault-management-endpoint` | URI |   | The address to use for the OCI Key Management Service / Vault management usage. The crypto endpoint of the vault we are rotating the private keys in. |

Optional configuration options
