**Root Certificate: Acts as a Certificate Authority (CA) to sign other certificates.**
**Server Certificate: Used by Logstash server to secure communication.**
**Client Certificate: Used by clients (Filebeat) to authenticate and secure their connections to the server.**

$ openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout client.key -out client.crt -CA ca.crt -CAkey ca.key

1. **Generate a Root Certificate (Certificate Authority)**

# Create a Private Key for the Root Certificate:
$ openssl genpkey -algorithm RSA -out rootCA.key -aes256
- *rootCA.key: File to store the root certificate private key.*
- *aes256: Encrypts the private key with AES-256 encryption for added security.*

# Create a Root Certificate:
$ openssl req -x509 -new -nodes -key rootCA.key -sha256 -days 1024 -out rootCA.crt
- *rootCA.crt: File to store the root certificate.*
- *x509: Create a self-signed certificate.*
- *days 1024: Specifies the validity period of the certificate in days.*

2. **Generate a Certificate for Logstash Server**

# Generate a Private Key for the Server Certificate:
$ openssl genpkey -algorithm RSA -out server.key -aes256
- *server.key: File to store the server private key.*

# Create a Certificate Signing Request (CSR):
$ openssl req -new -key server.key -out server.csr
- *server.csr: File to store the certificate signing request.*

# Generate the Server Certificate Using the Root Certificate:
$ openssl x509 -req -in server.csr -CA rootCA.crt -CAkey rootCA.key -CAcreateserial -out server.crt -days 1024 -sha256
- *server.crt: File to store the server certificate.*
- *-CA: Specifies the root certificate.*
- *-CAkey: Specifies the root certificate's private key.*
- *-CAcreateserial: Creates a serial number file for the root certificate.*
- *-days 1024: Specifies the validity period of the server certificate in days.*

3. **Generate a Certificate for Filebeat (Client Certificate)**

# Generate a Private Key for the Client Certificate:
$ openssl genpkey -algorithm RSA -out client.key -aes256
- *client.key: File to store the client private key.*

# Create a Certificate Signing Request (CSR):
$ openssl req -new -key client.key -out client.csr
- *client.csr: File to store the certificate signing request.*

# Generate the Client Certificate Using the Root Certificate:
$ openssl x509 -req -in client.csr -CA rootCA.crt -CAkey rootCA.key -CAcreateserial -out client.crt -days 1024 -sha256
- *client.crt: File to store the client certificate.*

4. **Verify the Certificates**
# Verify the Root Certificate:
$ openssl x509 -in rootCA.crt -text -noout
# Verify the Server Certificate:
$ openssl x509 -in server.crt -text -noout
# Verify the Client Certificate:
$ openssl x509 -in client.crt -text -noout
