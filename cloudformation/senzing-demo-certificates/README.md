# Senzing Demo Certificates

## Spikes

### spike-certificate-with-ec2

### spike-certificate-with-node

1. **Approach:**
    1. Create an AWS Lambda written in Node.js.
1. **Spike status:**
    1. Failed
    1. Although Node.js
       [crypto](https://nodejs.org/api/crypto.html)
       can create public/private keys,
       it cannot generate a full X509 certificate.
1. **References:**
    1. Node.js [crypto](https://nodejs.org/api/crypto.html)
    1. [using node-forge](https://stackoverflow.com/questions/31624143/using-nodes-crypto-library-to-create-a-self-signed-certificate/31624843)

### spike-certificate-certificate-manager

1. **Approach:**
    1. Use `AWS::CertificateManager::Certificate`.
1. **Spike status:**
    1. Failed
    1. Requires a domain name hosted by AWS.

### spike certificate-self-signed

1. **Approach:**
    1. Spike uses **Parameters:** to input a X509 certificate and private key.
       Defaults are provided.
1. **Spike status:**
    1. Works, but not the function needed.
    1. Certificate is passed in as a parameter;  needs to be generate by Cloudformation template.

### spike-certificate-create.py

1. **Approach:**
    1. In python script, create an X509 certificate using OpenSSL.crypto
1. **Spike status:**
    1. Although python works, the python cannot easily be made into an AWS lambda because of the OpenSSL library.

### spike-certificate-with-python

1. **Approach:**
    1. Create an AWS Lambda written in python.
1. **Spike status:**
    1. Stalled on requirement for `OpenSSL` package being publicly available
