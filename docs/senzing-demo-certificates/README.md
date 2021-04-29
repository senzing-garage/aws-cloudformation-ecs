# Cloudformation: senzing-demo-certificates

## Synopsis

The `senzing-demo-certificates` demonstrates a Senzing deployment using an AWS Cloudformation template
using an X.509 certificate and private key.

## Overview

The `senzing-demo-certificates` demonstration is an AWS Cloudformation template that creates the following resources:

1. AWS infrastructure
    1. VPC
    1. Subnets
    1. Internet Gateway
    1. Routes
    1. IAM Roles and Policies
    1. Logging
1. AWS services
    1. AWS Elastic File System (EFS)
    1. AWS Simple Queue Service (SQS)
    1. AWS Relational Data Service (RDS) Aurora Postgres Serverless
    1. AWS Elastic Container Service (ECS) Fargate
1. Senzing services
    1. Senzing Stream-Loader
    1. Senzing Redoer
    1. Senzing API server
    1. Senzing Entity Search Web App
1. Optional services:
    1. SwaggerUI
    1. Senzing Stream-producer
    1. Senzing SSH access
    1. AWS VPC Flow Logs

The following diagram shows the relationship of the docker containers in this docker composition.
Arrows represent data flow.

![Image of architecture](architecture.png)

This docker formation brings up the following docker containers:

1. *[senzing/entity-web-search-app](https://github.com/Senzing/entity-search-web-app)*
1. *[senzing/redoer](https://github.com/Senzing/redoer)*
1. *[senzing/senzing-api-server](https://github.com/Senzing/senzing-api-server)*
1. *[senzing/sshd](https://github.com/Senzing/docker-sshd)*
1. *[senzing/stream-loader](https://github.com/Senzing/stream-loader)*
1. *[senzing/stream-producer](https://github.com/Senzing/stream-producer)*

Help for
[senzing-demo-certificates](https://github.com/Senzing/aws-cloudformation-ecs/tree/main/cloudformation/senzing-demo-certificates).

### Contents

1. [Preamble](#preamble)
    1. [Legend](#legend)
1. [Expectations](#expectations)
1. [Demonstrate using AWS Console](#demonstrate-using-aws-console)
1. [Parameters](#parameters)
1. [Outputs](#outputs)

## Preamble

At [Senzing](http://senzing.com),
we strive to create GitHub documentation in a
"[don't make me think](https://github.com/Senzing/knowledge-base/blob/master/WHATIS/dont-make-me-think.md)" style.
For the most part, instructions are copy and paste.
Whenever thinking is needed, it's marked with a "thinking" icon :thinking:.
Whenever customization is needed, it's marked with a "pencil" icon :pencil2:.
If the instructions are not clear, please let us know by opening a new
[Documentation issue](https://github.com/Senzing/aws-cloudformation-ecs/issues/new?template=documentation_request.md)
describing where we can improve.   Now on with the show...

### Legend

1. :thinking: - A "thinker" icon means that a little extra thinking may be required.
   Perhaps there are some choices to be made.
   Perhaps it's an optional step.
1. :pencil2: - A "pencil" icon means that the instructions may need modification before performing.
1. :warning: - A "warning" icon means that something tricky is happening, so pay attention.

## Expectations

- **Space:** This repository and demonstration require 6 GB free disk space.
- **Time:** Budget 40 minutes to get the demonstration up-and-running.
- **Background knowledge:** This repository assumes a working knowledge of:
  - [AWS Cloudformation](https://github.com/Senzing/knowledge-base/blob/master/WHATIS/aws-cloudformation.md)

## Demonstrate using AWS Console

### Launch AWS Cloudformation

1. Visit [AWS Cloudformation with Senzing template](https://console.aws.amazon.com/cloudformation/home#/stacks/new?templateURL=https://public-read-access.s3.amazonaws.com/aws-cloudformation-ecs-hosted-zone/cloudformation.yaml).
1. In lower-right, click on "Next" button.
1. In **Specify stack details**
    1. In **Stack name**
        1. Enter an identifier of your choosing.
           Example: "senzing-demo"
    1. In **Parameters**
        1. In **Acknowledge insecure system**
            1. Understand the nature of the security in the deployment.
            1. Once understood, enter "I AGREE".
        1. In **Senzing installation**
            1. Accept the End User License Agreement
        1. In **Security**
            1. Enter your email address.
            1. Choose a hosted zone from the list.
    1. Other parameters are optional.
    1. In lower-right, click "Next" button.
1. In **Configure stack options**
    1. In lower-right, click "Next" button.
1. In **Review {stack-name}**
    1. Near the bottom, in **Capabilities**
        1. Check ":ballot_box_with_check: I acknowledge that AWS CloudFormation might create IAM resources."
    1. In lower-right, click "Create stack" button.
1. Senzing formation takes about 20 minutes to fully deploy.

### View results

1. Visit [AWS Cloudformation console](https://console.aws.amazon.com/cloudformation/home).
1. Choose appropriate "Stack name"
1. Choose "Outputs" tab.
    1. For descriptions of outputs, click on the value for `ADescriptionOfOutputs`,
       which links to [Outputs](#outputs) further down this page.

## Parameters

Technical information on AWS Cloudformation parameters can be seen at
[Parameters](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html).

### AcceptEula

1. **Synopsis:**
   To use the Senzing code, you must agree to the End User License Agreement (EULA).
   This step is intentionally tricky to ensure that you make a conscious effort to accept the EULA.
1. **Required:** Yes
1. **Type:** String
1. **Allowed values:** See [SENZING_ACCEPT_EULA](https://github.com/Senzing/knowledge-base/blob/master/lists/environment-variables.md#senzing_accept_eula).
1. **Default:** None

### CertificateBody

1. **Synopsis:**
   The X.509 certificate
1. **Required:** Yes
1. **Type:** String
1. **Example:**

   ```console
   -----BEGIN CERTIFICATE-----
   MIIEHTCCAwWgAwIBAgIDAJojMA0GCSqGSIb3DQEBCwUAMIGLMQswCQYDVQQGEwJV
   UzETMBEGA1UECAwKQ2FsaWZvcm5pYTEWMBQGA1UEBwwNU2FuIEZyYW5jaXNjbzEX
   MBUGA1UECgwOTXlPcmdhbml6YXRpb24xHTAbBgNVBAsMFE15T3JnYW5pemF0aW9u
   YWxVbml0MRcwFQYDVQQDDA5NeSBvd24gUm9vdCBDQTAeFw0yMTAzMTExNTAwNDla
   Fw0zMDAzMDkxNTAwNDlaMIGIMQswCQYDVQQGEwJVUzETMBEGA1UECAwKQ2FsaWZv
   cm5pYTEWMBQGA1UEBwwNU2FuIEZyYW5jaXNjbzEXMBUGA1UECgwOTXlPcmdhbml6
   YXRpb24xHTAbBgNVBAsMFE15T3JnYW5pemF0aW9uYWxVbml0MRQwEgYDVQQDDAtl
   eGFtcGxlLmNvbTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAMnKQhQG
   pRuxcO5RF8VMyAmWe4rs4XWeodVQflYtJVY+mCg/JidmgYe1EYXvE2Qqf1Xzi2O2
   oEJJSAs/s+Wb91yzunnoHVR/5uTHdjN2e6HRhEmUFlJuconjlmBxVKe1LG4Ra8yr
   JA+E0tS2kzrGCLNcFpghQ982GJjuvRWm9nAAsCJPm7N8a/Gm1opMdUkiH1b/3d47
   0wugisz6fYRHQ61UIYfjNUWlg/tV1thGOScAB2RyusQJdTB422BQAlpD4TTX8uj8
   Wd0GhYjpM8DWWpSUOFsoYOHBc3bPr7ctpOoIG8gZcs56zDwZi9CVda4viS/8HPnC
   r8jXaQW1pqwP8ekCAwEAAaOBijCBhzAJBgNVHRMEAjAAMB0GA1UdDgQWBBTaOaPu
   XmtLDTJVv++VYBiQr9gHCTAfBgNVHSMEGDAWgBTaOaPuXmtLDTJVv++VYBiQr9gH
   CTATBgNVHSUEDDAKBggrBgEFBQcDATALBgNVHQ8EBAMCB4AwGAYDVR0RBBEwD4IN
   Ki5leGFtcGxlLmNvbTANBgkqhkiG9w0BAQsFAAOCAQEAWIZu4sma7MmWTXSMwKSP
   stQDWdIvcwthD8ozHkLsNdl5eKqOEndAc0wb7mSk1z8rRkSsd0D0T2zaKyduCYrs
   eBAMhS2+NnHWcXxhn0VOkmXhw5kO8Un14KIptRH0y8FIqHMJ8LrSiK9g9fWCRlI9
   g7eBipu43hzGyMiBP3K0EQ4m49QXlIEwG3OIWak5hdR29h3cD6xXMXaUtlOswsAN
   3PDG/gcjZWZpkwPlaVzwjV8MRsYLmQIYdHPr/qF1FWddYPvK89T0nzpgiuFdBOTY
   W6I1TeTAXFXG2Qf4trXsh5vsFNAisxlRF3mkpixYP5OmVXTOyN7cCOSPOUh6Uctv
   eg==
   -----END CERTIFICATE-----
   ```

### CidrInbound

1. **Synopsis:** The password used to access the AWS Aurora Postgres Serverless databases.
1. **Required:** Yes
1. **Type:** String
1. **Allowed pattern:** Letters and numbers. Specifically: `'(?:\d{1,3}\.){3}\d{1,3}(?:/\d\d?)?'`
1. **Allowed values:** String in IPv4 [CIDR format](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing).
1. **Example:** 45.26.129.200/32
1. **Default:** 0.0.0.0/0

### CognitoAdminEmail

1. **Synopsis:** An email address that will be used as a username to access the system via AWS Cognito.
1. **Required:** Yes
1. **Type:** String
1. **Allowed pattern:** A valid email address
1. **Example:** me@example.com
1. **Default:** None

### PrivateKey

1. **Synopsis:**
   Private key
1. **Required:** Yes
1. **Type:** String
1. **Example:**

   ```console
   -----BEGIN PRIVATE KEY-----
   MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDJykIUBqUbsXDu
   URfFTMgJlnuK7OF1nqHVUH5WLSVWPpgoPyYnZoGHtRGF7xNkKn9V84tjtqBCSUgL
   P7Plm/dcs7p56B1Uf+bkx3Yzdnuh0YRJlBZSbnKJ45ZgcVSntSxuEWvMqyQPhNLU
   tpM6xgizXBaYIUPfNhiY7r0VpvZwALAiT5uzfGvxptaKTHVJIh9W/93eO9MLoIrM
   +n2ER0OtVCGH4zVFpYP7VdbYRjknAAdkcrrECXUweNtgUAJaQ+E01/Lo/FndBoWI
   6TPA1lqUlDhbKGDhwXN2z6+3LaTqCBvIGXLOesw8GYvQlXWuL4kv/Bz5wq/I12kF
   taasD/HpAgMBAAECggEAKePgBdI/UllqrT6OZboDyOHBcdytDULKK8NTBsbGenny
   EmDRpdpEx4xSP/CaoO+lkY1GgYO3DyuxVgx6Zw8Ssd7ptkb2V8VZhGLX6eUN01Dw
   WmnwnForUu65F/pO7aXRvGPHciyRBtu2/MuOEuRrh/h1BE3bjinnv0/IVwdbH3LW
   pLiJoxzlSJDDomaIAOtB3u6Lw1/6kXiYT9lvXnUpBzR+1uMApTPQN0NJuxLiA0Rs
   es2kBTZ/weEQW+GeJaSYmEXX9zCKGMVCq5EZfS3sH0TrkDENVqW40J+OF3Ee6r12
   CoWLWkC+DPtfHvwh1zp89HFYZ7I6lyycBb31yHb1kQKBgQDuURbpgWxP7XaSgPuI
   6rv2ApjZQav58kNj1K1pRIcnoZsfz3LX3xfft0PKyoKDmndN8nS9KKL9T//XIBaO
   PeD3XzlSvQQ/SvNdaBHqOzkkwldGng3swR3c8RELoaKU9yBdhlMFYXkZsIp5hZgG
   MPVdihamFfUk9J/sdYAr9vjnVQKBgQDYw1TWyBi4UTkMox62hqSUgWw3llaliHkP
   tEinMKF3i0oZzGzWDIHV9YoPPuu2L5cy+j2wLe8r6DWvsKd0dqeNS/yXYj7eIDVz
   fff9SmP25RdtV8h6fkAiLD708G7P0w94G+LhakuVpeTpMNSDPWUk6bl+K81ZRvm6
   DKS7aOM4RQKBgEhQFrG38dO27Fm8BZcgEvStCRAzWym2lzg9mnjssE4YPWfDnMdg
   DHB3vXxVQpEIV9cxELctE3flxG3UcMOshwzIui4e6KED7yCSqYz3d3lt9umYoAUM
   /DDEfTWYUCr/abS3Q43Ia+SdqwcAwIZwaKN/eSvgUchq6fPoG4I7qH8ZAoGBAMRS
   ndtuHZ2Kyw3cC6wrZJKwabAq9M02PtdvZMIwdH3OZU3abdSsPUfo/KL0TQ6UKfBc
   31RbNhzhUwaODAyajwSVhvAhZmlOaLryo5IAN2vdcAtzjzsKb9HDmz3DKcoHEiKp
   tyKMYGrodtyRglhfWeVF3uAckf9DHllYrDalN+61AoGAP9OrCgoDnjtTasFzibZ8
   jb+xYG9E42smB2gep03Jj8l5gqnWTFh0TyA1Z7+RJNvSzkqK8bU/uAH/TgJAqviE
   7XA7a2yuaf/Ww4vToy5bo1HqhQBak1PP2wzuWiUkJcyTRTGryLvnIR9fDonJ9TAd
   0GsjqdfyAqjsvycLNvwR0wk=
   -----END PRIVATE KEY-----
   ```

### RunStreamProducer

1. **Synopsis:**
   Optionally, run the
   [stream-producer](https://github.com/Senzing/stream-producer)
   container that fetches JSON lines from a file and pushes them to the SQS queue.
1. **Required:** Yes
1. **Type:** Boolean
1. **Allowed values:**
   [ "Yes" | "No" ]
1. **Default:** Yes

### SecurityResponsibility

1. **Synopsis:**
   Acknowledgement of the security level of the system.
1. **Required:** Yes
1. **Type:** String
1. **Allowed values:** "I AGREE"
1. **Default:** None

### SenzingLicenseAsBase64

1. **Synopsis:**
   To ingest more than 100,000 records, a Senzing license is required.
   A binary version of the Senzing license, `g2.lic`, is not usable as a parameter in the text entry field.
   Instead, a [Base64](https://en.wikipedia.org/wiki/Base64) representation of the information is needed.
   An example of how to produce base64 from `g2.lic` on Linux and macOS:

   ```console
   base64 /opt/senzing/etc/g2.lic
   ```

   Copy the entire output from the command and paste into the text entry field.
1. **Required:** Yes if ingesting more than 100,000 records, otherwise no.
1. **Type:** String
1. **Allowed pattern:** Empty or Base64 characters. Specifically `^$|[^-A-Za-z0-9+/=]|=[^=]|={3,}$`
1. **Allowed values:** Base64 encoded string
1. **Example:**

   ```console
   AQAAADgCAAAAAAAAU2VuemluZwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
   AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
   AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
   AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
   AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAARGVtbyBFeHBpcmVkAAAAAAAA
   AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADIwMjAtMTItMTYA
   AAAAAAAAAAAARVZBTAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
   AAAAAAAAAAAAAAAAAAAAAFNUQU5EQVJEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
   AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKCGAQAAAAAAMTk3Ni0wMS0wMQAAAAAAAAAAAABN
   T05USExZAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
   AAAAAAAARkdIST5XYOZ90kbyAbU7wM7XvPCwq/FgORZIekwFMg8zi3tCD0V5+12q72aqk0E6JOct
   +cPAq/T50N5Pf5nvJZ6TaW3TzQbnH/z5f/ALsWLydE2DPNvq3HuAjkjZpg2h7mb4OUqorGxDI9RX
   TX8hPjzYrBfMdOgl1DlRBVG36WwdpB8AnSfaegbYU+U/vfof+ff6mJk8gzPg+OGPwg21/S6i2TT4
   RbTCSYP/TpfXyJGE6dbQWEC9rFhYuWq3mFF3z7zFEcmxpNfZuBtYsxni8P3sDZ706RA+wcQF7TVg
   giJoK03W8kd6mk3X+fvc4ARJo9RarYInsAvSHKlr1KpxeebuirfqgSz+uEW6pqOD1fV0oHnFncdf
   jV2k2CqmIfThB/ONQcn/4/EIlhdzXqxSlXAGz6C7ApHq6xUCdLILx/NfdUEypHIfyabrpXKOKOPx
   zekhGztEzB0gSJNebEa++EKxHDOc1Sc0YD9q9KvcaGSPTjlCJeaNhufg9Sz/iXZMP+d4Vkp+Bn6p
   mfUPG7tKharEoRChUNfRms8wVyNxmz6LRw5Uy14Dlodd0LyBQRB9Tx8FVYMh5AElwjbQOoDOIRvi
   IQIGsUNp/ZkP7PdBxc/b9o3rjUsZCzyCtP+jflZSqMenzXCsTI1Xay6On2wSVwQdJ1/2eIwKEfCF
   hj4DZlY5+jSo
   ```

1. **Default:** None

## Outputs

### 0penFirst

### AccountID

1. **Synopsis:**
   AWS account from which Cloudformation was deployed.

### DatabaseHostCore

1. **Synopsis:**
   One of three Senzing databases.
   More information at
   [AWS RDS Console](https://console.aws.amazon.com/rds/home).

### DatabaseHostLibfeat

1. **Synopsis:**
   Two of three Senzing databases.
   More information at
   [AWS RDS Console](https://console.aws.amazon.com/rds/home).

### DatabaseHostRes

1. **Synopsis:**
   Three of three Senzing databases.
   More information at
   [AWS RDS Console](https://console.aws.amazon.com/rds/home).

### DatabaseName

1. **Synopsis:**
   Name of database in each of the three databases.
   More information at
   [AWS RDS Console](https://console.aws.amazon.com/rds/home).

### DatabasePassword

1. **Synopsis:**
   Password to access database in each of the three databases.
   More information at
   [AWS RDS Console](https://console.aws.amazon.com/rds/home).

### DatabasePortCore

1. **Synopsis:**
   The port used to access the [DatabaseHostCore](#databasehostcore) database.
   More information at
   [AWS RDS Console](https://console.aws.amazon.com/rds/home).

### DatabasePortLibfeat

1. **Synopsis:**
   The port used to access the [DatabaseHostLibfeat](#databasehostlibfeat) database.
   More information at
   [AWS RDS Console](https://console.aws.amazon.com/rds/home).

### DatabasePortRes

1. **Synopsis:**
   The port used to access the [DatabaseHostRes](#databasehostres) database.
   More information at
   [AWS RDS Console](https://console.aws.amazon.com/rds/home).

### DatabaseUsername

1. **Synopsis:**
   Username to access database in each of the three databases.
   More information at
   [AWS RDS Console](https://console.aws.amazon.com/rds/home).

### Ec2Vpc

1. **Synopsis:**
   Identifier of the Virtual Private Cloud (VPC).
   More information at
   [AWS VPC Console](https://console.aws.amazon.com/vpc/home#vpcs:).

### Host

   More information at
   [AWS Load Balancers Console](https://console.aws.amazon.com/ec2/v2/home?region=us-east-1#LoadBalancers).
   Select a load balancer, view the "Description" tab, view **DNS name**.

### QueueDeadLetter

1. **Synopsis:**
   The queue to which records that are not able to be ingested into Senzing Engine are sent.
   In otherwords, if the JSON message is malformed, or Senzing d into the Senzing Engine.
   More information at [AWS SQS Console](https://console.aws.amazon.com/sqs/v2/home?#/queues).

### QueueInput

1. **Synopsis:**
   The queue from which records are ingested into Senzing Engine.
   In otherwords, this is the queue where records are sent to be inserted into the Senzing Engine.
   More information at [AWS SQS Console](https://console.aws.amazon.com/sqs/v2/home?#/queues).

### QueueOutput

1. **Synopsis:**
   The queue to which "WithInfo" results are sent by the
   [stream-loader](https://github.com/Senzing/stream-loader)
   after ingesting records from the [QueueInput](#queueinput).
   More information at [AWS SQS Console](https://console.aws.amazon.com/sqs/v2/home?#/queues).

### QueueRedoerInput

### QueueRedoerOutput

### SenzingVersion

1. **Synopsis:**
   The version of Senzing installed onto the AWS Elastic File System.
   More information at [Senzing API Version History](https://senzing.com/releases/#api-releases).

### SshPassword

1. **Synopsis:**
   Password to be used when logging into the SSHD container.

### SshUsername

1. **Synopsis:**
   User ID to be used when logging into the SSHD container.

### SubnetPrivate1

### SubnetPrivate2

### SubnetPublic1

### SubnetPublic2

### UrlApiServer

1. **Synopsis:**
   A URL showing how to reach the
   [Senzing API Server](https://github.com/Senzing/senzing-api-server).

### UrlApiServerHeartbeat

1. **Synopsis:**
   A URL showing how to reach the
   [Senzing API Server](https://github.com/Senzing/senzing-api-server)
   directly.
   The `/heartbeat` URI path simply demonstrates that the API server is responding.
   For more URIs, see
   [SwaggerUrl output value](#urlswagger).

### UrlJupyter

1. **Synopsis:**
   A URL showing how to reach the
   [Senzing Jupyter notebooks](https://github.com/Senzing/docker-jupyter).

### UrlSwagger

1. **Synopsis:**
   A URL showing how to reach the
   [swaggerapi/swagger-ui](https://github.com/swagger-api/swagger-ui)
   for viewing the
   [Senzing REST API OpenAPI document](https://github.com/Senzing/senzing-rest-api-specification).

### UrlWebApp

1. **Synopsis:**
   A URL showing how to reach the
   [Senzing Entity Search Web App](https://github.com/Senzing/entity-search-web-app).

### UrlXterm

1. **Synopsis:**
   A URL showing how to reach the
   [Senzing Xterm](https://github.com/Senzing/docker-xterm).

### UserInitPassword

1. **Synopsis:**
   A one-time password for logging into AWS Cognito.
   More information at
   [AWS User Pools](https://console.aws.amazon.com/cognito/users/).
   Select User Pool, select Users and Groups.

### UserName

1. **Synopsis:**
   The initial AWS Cognito user defined by the CloudFormation deployment.
   Additional users can be created by viewing
   more information at
   [AWS User Pools](https://console.aws.amazon.com/cognito/users/).
   Select User Pool, select "Users and Groups", select "Create user"

### UserPool
