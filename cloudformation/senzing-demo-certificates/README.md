
### spike-certificate-with-node

1. Spike status: failed
    1. Although Node.js
       [crypto](https://nodejs.org/api/crypto.html)
       can create public/private keys,
       it cannot generate a full X509 certificate.

1. References:
    1. Node.js [crypto](https://nodejs.org/api/crypto.html)
    1. [using node-forge](https://stackoverflow.com/questions/31624143/using-nodes-crypto-library-to-create-a-self-signed-certificate/31624843)

### spike-certificate-certificate-manager

1. Spike status: failed
    1. Requires a domain name hosted by AWS

### spike certificate-self-signed

1. Spike uses **Parameters:** to input a X509 certificate and private key.
   Defaults are provided.
1. Spike status:  Works, but not the function needed

### spike-certificate-create.py

1. In python, create an X509 certificate using OpenSSL.crypto
1. Spike status:
    1. Although python works, the python cannot easily be made into an AWS lambda because of the OpenSSL library.
