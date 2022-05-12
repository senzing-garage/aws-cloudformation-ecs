# Cloudformation: senzing-demo-user-vpc-hosted-zone

## Synopsis

The `senzing-demo-user-vpc-hosted-zone` demonstrates a Senzing deployment using an AWS Cloudformation template.
In this formation, the user supplies the AWS VPC and Route53 Hosted Zone.

## Overview

The `senzing-demo-user-vpc-hosted-zone` demonstration is an AWS Cloudformation template that creates the following resources:

1. AWS infrastructure
    1. Subnets
    1. Internet Gateway
    1. Routes
    1. IAM Roles and Policies
    1. Logging
1. AWS services
    1. AWS Cognito
    1. AWS Elastic Container Service (ECS) Fargate
    1. AWS Elastic File System (EFS)
    1. AWS Relational Data Service (RDS) Aurora Postgres Serverless
    1. AWS Simple Queue Service (SQS)
1. Optional Senzing services
    1. Senzing API server
    1. Senzing Entity Search Web App
    1. Senzing Redoer
    1. Senzing SSH access
    1. Senzing Stream-Loader
    1. Senzing Stream-producer
    1. Senzing Xterm
    1. SwaggerUI

The following diagram shows the relationship of the docker containers in this docker composition.
Arrows represent data flow.

![Image of architecture](architecture.png)

This docker formation brings up the following docker containers:

1. *[senzing/entity-web-search-app](https://github.com/Senzing/entity-search-web-app)*
1. *[senzing/jupyter](https://github.com/Senzing/docker-jupyter)*
1. *[senzing/redoer](https://github.com/Senzing/redoer)*
1. *[senzing/senzing-api-server](https://github.com/Senzing/senzing-api-server)*
1. *[senzing/sshd](https://github.com/Senzing/docker-sshd)*
1. *[senzing/stream-loader](https://github.com/Senzing/stream-loader)*
1. *[senzing/stream-producer](https://github.com/Senzing/stream-producer)*
1. *[senzing/xterm](https://github.com/Senzing/docker-xterm)*

GitHub repository for
[aws-cloudformation-ecs-poc-simple](https://github.com/Senzing/aws-cloudformation-ecs-poc-simple).

### Contents

1. [Preamble](#preamble)
    1. [Legend](#legend)
1. [Expectations](#expectations)
1. [Demonstrate using AWS Console](#demonstrate-using-aws-console)
1. [Using deployment](#using-deployment)
1. [Additional topics](#additional-topics)
1. [Parameters](#parameters)
1. [Outputs](#outputs)

## Preamble

At [Senzing](http://senzing.com),
we strive to create GitHub documentation in a
"[don't make me think](https://github.com/Senzing/knowledge-base/blob/main/WHATIS/dont-make-me-think.md)" style.
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
  - [AWS Cloudformation](https://github.com/Senzing/knowledge-base/blob/main/WHATIS/aws-cloudformation.md)

## Demonstrate using AWS Console

### Prerequisites

1. AWS VPC
    1. [AWS VPC console](https://console.aws.amazon.com/vpc/home#vpcs:)
    1. The VPC must have "DNS hostnames" set to "Enabled"
1. AWS Route53 Hosted Zone
    1. [AWS Route53 Hosted Zone console](https://console.aws.amazon.com/route53/v2/hostedzones#)
1. Certificate
    1. [AWS Certificate Manager](https://console.aws.amazon.com/acm/home)
    1. Make sure the certificate is in the AWS region of the deployment.

### Launch AWS Cloudformation

1. :thinking: **Warning:** This Cloudformation deployment will accrue AWS costs.
   With appropriate permissions, the
   [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/)
   can help evaluate costs.
1. Visit [AWS Cloudformation with Senzing template](https://console.aws.amazon.com/cloudformation/home#/stacks/new?templateURL=https://s3.amazonaws.com/public-read-access/aws-cloudformation-ecs-user-vpc-hosted-zone/cloudformation.yaml).
1. In lower-right, click on "Next" button.
1. In **Specify stack details**
    1. In **Stack name**
        1. Enter an identifier of your choosing.
           Example: "senzing-demo"
    1. In **Parameters**
        1. In **Security responsibility**
            1. Understand the nature of the security in the deployment.
            1. Once understood, enter "I AGREE".
        1. In **Senzing installation**
            1. Accept the End User License Agreement
        1. In **Identify existing resources**
            1. Choose VPC.
               Must have an address range of `10.0.0.0/16` or larger.
               (e.g. `10.0.0.0/8`)
               See [AWS VPC console](https://console.aws.amazon.com/vpc/home#vpcs:)
               to create or manage VPCs.
            1. Choose AWS Route53 Hosted Zone.
               See [AWS Route53 Hosted Zone console](https://console.aws.amazon.com/route53/v2/hostedzones#)
               to create or manage Hosted Zones.
        1. In **Users**
            1. Enter your email address.  Example: `me@example.com`
    1. Other parameters are optional.
       The default values are fine.
    1. In lower-right, click "Next" button.
1. In **Configure stack options**
    1. In lower-right, click "Next" button.
1. In **Review {stack-name}**
    1. Near the bottom, in **Capabilities**
        1. Check ":ballot_box_with_check: I acknowledge that AWS CloudFormation might create IAM resources."
    1. In lower-right, click "Create stack" button.

## Using deployment

1. Visit [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/home).
    1. Make sure correct AWS region is selected.
1. Wait until "{stack-name}" status is `CREATE_COMPLETE`.
    1. Senzing formation takes about 20 minutes to fully deploy.
    1. May have to hit the refresh button a few times to get updated information.
1. Click on "{stack-name}" stack.
1. Click on "Outputs" tab.
1. Click on "0penFirst" value.
    1. You will be prompted for username and password,
       Use the `UserName` and `UserInitPassword` values found in the "Outputs" tab.

## Additional topics

1. [How to set AWS RDS force-scaling-capacity](https://github.com/Senzing/knowledge-base/blob/main/HOWTO/set-aws-rds-force-scaling-capacity.md)
1. [How to load AWS Cloudformation queue](https://github.com/Senzing/knowledge-base/blob/main/HOWTO/load-aws-cloudformation-queue.md)
1. [How to migrate Senzing in AWS Cloudformation](https://github.com/Senzing/knowledge-base/blob/main/HOWTO/migrate-senzing-in-cloudformation.md)
1. [How to update Senzing license](https://github.com/Senzing/knowledge-base/blob/main/HOWTO/update-senzing-license.md)

### Review AWS Cloudformation

The AWS resources created by the
[cloudformation.yaml](https://github.com/Senzing/aws-cloudformation-ecs-poc-simple/blob/main/cloudformation.yaml)
template can be see in the [AWS Management Console](https://console.aws.amazon.com).

1. CloudFormation
    1. [Stacks](https://console.aws.amazon.com/cloudformation/home?#/stacks)
1. CloudWatch
    1. [Log groups](https://console.aws.amazon.com/cloudwatch/home?#logsV2:log-groups)
1. Cognito
    1. [UserPool](https://console.aws.amazon.com/cognito/users/#/pool/u)
1. Elastic Compute Cloud (EC2)
    1. [Load Balancers](https://console.aws.amazon.com/ec2/v2/home?#LoadBalancers:)
    1. [Network interfaces](https://console.aws.amazon.com/ec2/v2/home?#NIC)
    1. [Target groups](https://console.aws.amazon.com/ec2/v2/home?#TargetGroups:)
1. Elastic Container Service (ECS)
    1. [Clusters](https://console.aws.amazon.com/ecs/home?#/clusters)
    1. [Task Definitions](https://console.aws.amazon.com/ecs/home?#/taskDefinitions)
1. Elastic File System (EFS)
    1. [File systems](https://console.aws.amazon.com/efs/home?#/filesystems)
1. Identity and Access Management (IAM)
    1. Certificates
    1. [Policies](https://console.aws.amazon.com/iam/home?#/policies)
    1. [Roles](https://console.aws.amazon.com/iam/home?#/roles)
1. Lambda
    1. [Functions](https://console.aws.amazon.com/lambda/home?#/functions)
1. Relational Data Service (RDS)
    1. [Databases](https://console.aws.amazon.com/rds/home?#databases:)
    1. [Parameter groups](https://console.aws.amazon.com/rds/home?#parameter-groups:)
    1. [Subnet groups](https://console.aws.amazon.com/rds/home?#db-subnet-groups-list:)
1. Route53
    1. [RecordSet](https://console.aws.amazon.com/route53/v2/hostedzones#)
1. Simple Queue Service (SQS)
    1. [Queues](https://console.aws.amazon.com/sqs/v2/home)
1. System Manager Agent (SSM)
    1. [Parameter store](https://console.aws.amazon.com/systems-manager/parameters)
1. Virtual Private Cloud (VPC)
    1. [Elastic IP addresses](https://console.aws.amazon.com/vpc/home?#Addresses:)
    1. [Endpoints](https://console.aws.amazon.com/vpc/home?#Endpoints:)
    1. [Internet gateways](https://console.aws.amazon.com/vpc/home?#igws)
    1. [NAT gateways](https://console.aws.amazon.com/vpc/home?#NatGateways:)
    1. [Network ACLs](https://console.aws.amazon.com/vpc/home?#acls)
    1. [Route Tables](https://console.aws.amazon.com/vpc/home?#RouteTables)
    1. [Security Groups](https://console.aws.amazon.com/vpc/home?#SecurityGroups)
    1. [Subnets](https://console.aws.amazon.com/vpc/home?#subnets)
    1. [VPCs](https://console.aws.amazon.com/vpc/home?#vpcs)

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
1. **Allowed values:** See [SENZING_ACCEPT_EULA](https://github.com/Senzing/knowledge-base/blob/main/lists/environment-variables.md#senzing_accept_eula).
1. **Default:** None

### CidrInbound

1. **Synopsis:** A Classless Inter-Domain Routing (CIDR) value used to limit access to the system.
   This restricts the inbound traffic to requests from specified IP ranges.
   Examples:
    1. A system with the value `0.0.0.0/0` allows access from anywhere.
    1. A system with the value `45.26.129.0/24` will allow access from IP addresses in the range `45.26.129.0` to `45.26.129.255`
    1. A system with the value `45.26.129.200/32` will allow access from a single IP address `45.26.129.200`.
1. **Required:** Yes
1. **Type:** String
1. **Allowed pattern:** Letters and numbers. Specifically: `'(?:\d{1,3}\.){3}\d{1,3}(?:/\d\d?)?'`
1. **Allowed values:** String in IPv4 [CIDR format](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing).
1. **Example:** 45.26.129.200/32
1. **Default:** 0.0.0.0/0

### CognitoAdminEmail

1. **Synopsis:**
   An email address of the person administrating this Cloudformation.
   The email address will be used when email is sent to additional users via the
   [AWS Cognito web console](https://console.aws.amazon.com/cognito/users/#/pool/u).
1. **Required:** Yes
1. **Type:** String
1. **Allowed values:**
    1. A string in email format.
    1. Example: `me@example.com`

### Route53HostedZoneId

1. **Synopsis:**
   An existing [AWS Route53 hosted zone](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/route-53-concepts.html#route-53-concepts-hosted-zone)
   to use when creating a hostname having the format:
   `{stack-name}.{hosted-zone-domain-name}`.
   To see available Hosted Zones, visit the
   [AWS Route53 Hosted Zone console](https://console.aws.amazon.com/route53/v2/hostedzones#).
1. **Required:** Yes
1. **Type:** List of `AWS::Route53::HostedZone::Id`

### RunApiServer

1. **Synopsis:**
   Optionally, run the
   [senzing-api-server](https://github.com/Senzing/senzing-api-server)
   which provides an HTTP REST API to the Senzing Engine.
1. **Required:** Yes
1. **Type:** Boolean
1. **Allowed values:**
   [ "Yes" | "No" ]
1. **Default:** Yes

### RunJupyter

1. **Synopsis:**
   Optionally, run the
   [Senzing Jupyter notebooks](https://github.com/Senzing/docker-jupyter)
   to view Jupyter notebooks showing Senzing code samples.
1. **Required:** Yes
1. **Type:** Boolean
1. **Allowed values:**
   [ "Yes" | "No" ]
1. **Default:** No

### RunRedoer

1. **Synopsis:**
   Optionally, run the
   [redoer](https://github.com/Senzing/redoer)
   to process "redo records"
1. **Required:** Yes
1. **Type:** Boolean
1. **Allowed values:**
   [ "Yes" | "No" ]
1. **Default:** Yes

### RunSshd

1. **Synopsis:**
   Optionally, run the
   [sshd](https://github.com/Senzing/docker-sshd)
   container that allows `ssh` and `scp` access.
   Can be used for debugging, copying files to the EFS, or the Senzing Exploratory Tools.
1. **Required:** Yes
1. **Type:** Boolean
1. **Allowed values:**
   [ "Yes" | "No" ]
1. **Default:** Yes

### RunStreamLoader

1. **Synopsis:**
   Optionally, run the
   [stream-loader](https://github.com/Senzing/stream-loader)'
   which reads records from the SQS queue and sends them to the Senzing Engine.
1. **Required:** Yes
1. **Type:** Boolean
1. **Allowed values:**
   [ "Yes" | "No" ]
1. **Default:** Yes

### RunStreamProducer

1. **Synopsis:**
   Optionally, run the
   [stream-producer](https://github.com/Senzing/stream-producer)
   container that fetches JSON lines from a file and pushes them to the SQS queue.
   If "Yes" is chosen,
   [SenzingInputUrl](#senzinginputurl),
   [SenzingRecordMin](#senzingrecordmin),
   and
   [SenzingRecordMax](#senzingrecordmax)
   need to be specified.
   If the JSON data in the [SenzingInputUrl](#senzinginputurl)
   has `DATA_SOURCE` and/or `ENTITY_TYPE` values,
   then [SenzingDataSource](#senzingdatasource)
   and [SenzingEntityType](#senzingentitytype)
   are required.
1. **Required:** Yes
1. **Type:** Boolean
1. **Allowed values:**
   [ "Yes" | "No" ]
1. **Default:** No

### RunSwagger

1. **Synopsis:**
   Optionally, run the
   [swaggerapi/swagger-ui](https://github.com/swagger-api/swagger-ui)
   container that hosts the SwaggerUI for viewing the
   [Senzing REST API OpenAPI document](https://github.com/Senzing/senzing-rest-api-specification).
1. **Required:** Yes
1. **Type:** Boolean
1. **Allowed values:**
   [ "Yes" | "No" ]
1. **Default:** Yes

### RunVpcFlowLogs

1. **Synopsis:**
   Optionally, capture information about the IP traffic going to and from network interfaces in your VPC.
1. **Required:** Yes
1. **Type:** Boolean
1. **Allowed values:**
   [ "Yes" | "No" ]
1. **Default:** No
1. **References:**
    1. [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html).

### RunWebApp

1. **Synopsis:**
   Optionally, run the
   [entity-search-web-app](https://github.com/Senzing/entity-search-web-app)
   which gives a web-based representation of data stored in the Senzing data model.
1. **Required:** Yes
1. **Type:** Boolean
1. **Allowed values:**
   [ "Yes" | "No" ]
1. **Example:**
1. **Default:** Yes

### RunXterm

1. **Synopsis:**
   Optionally, run the
   [Senzing Xterm](https://github.com/Senzing/docker-xterm)
   which gives a web-base terminal useful in running command line programs.
1. **Required:** Yes
1. **Type:** Boolean
1. **Allowed values:**
   [ "Yes" | "No" ]
1. **Example:**
1. **Default:** Yes

### SecurityResponsibility

1. **Synopsis:**
   The Senzing proof-of-concept AWS Cloudformation uses
   [AWS Cognito](https://aws.amazon.com/cognito/) for authentication,
   and HTTPS (using a self-signed certificate) for encrypted network traffic
   to expose services through a single, internet-facing AWS Elastic Load Balancer.
   With exception of the
   [senzing/sshd](https://github.com/Senzing/docker-sshd) container,
   no tasks in the AWS Elastic Container Service (ECS) have public IP addresses.

   To enable additional security measures for the deployment in your specific environment,
   you'll need to consult with your AWS administrator.
   Examples of additional security measures:
    - [AWS Route53](https://aws.amazon.com/route53/) with genuine X.509 certificate
    - [AWS Web Application Firewall (WAF)](https://aws.amazon.com/waf/)
    - [AWS Shield](https://aws.amazon.com/shield/)
    - [AWS Firewall Manager](https://aws.amazon.com/firewall-manager/)
    - [Amazon API Gateway](https://aws.amazon.com/api-gateway/)
    - Restrictive value for [CidrInbound](#cidrinbound)
1. **Required:** Yes
1. **Type:** String
1. **Allowed values:**
    1. "I AGREE"
1. **Default:** None

### SenzingDataSource

1. **Synopsis:**
   If using [RunStreamProducer](#runstreamproducer), supply the `DATA_SOURCE` value to be used.
1. **Required:** Yes
1. **Type:** String
1. **Default:** `TEST`

### SenzingEntityType

1. **Synopsis:**
   If using [RunStreamProducer](#runstreamproducer), supply the `ENTITY_TYPE` value to be used.
1. **Required:** Yes
1. **Type:** String
1. **Default:** `GENERIC`

### SenzingInputUrl

1. **Synopsis:**
   If using [RunStreamProducer](#runstreamproducer), supply the URL of a tar-gzipped file in JSON-lines format containing records to ingest into Senzing.
1. **Required:** Yes if running
   [Stream Producer](#runstreamproducer),
   otherwise no.
1. **Type:** String
1. **Allowed pattern:**  A URL starting with `http://` or `https://`.
1. **Example:** `https://www.example.com/my/records.json`
1. **Default:** `https://s3.amazonaws.com/public-read-access/TestDataSets/SenzingTruthSet/truth-set-3.0.0.jsonl`

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

### SenzingRecordMax

1. **Synopsis:**
   When using [SenzingInputUrl](#senzinginputurl), this indicates the number of the last line that will be
   read from the file.
   It is used to limit the number of records ingested into Senzing.
1. **Required:** Yes if using [SenzingInputUrl](#senzinginputurl), otherwise no.
1. **Type:** Number
1. **Allowed pattern:** Numbers. Specifically: `[0-9]*`
1. **Allowed values:** 0 = Read entire file;  Any positive integer.
1. **Example:** 15000000
1. **Default:** 0

### SenzingRecordMin

1. **Synopsis:**
   When using [SenzingInputUrl](#senzinginputurl), this indicates the number of the first line that will be
   read from the file.
   Used to skip lines at the beginning of the file.
   It is handy if the beginning of the file has already been ingested into Senzing.
1. **Required:** Yes if using [SenzingInputUrl](#senzinginputurl), otherwise no.
1. **Type:** Number
1. **Allowed pattern:** Numbers. Specifically: `[0-9]*`
1. **Allowed values:** 0 = Read from beginning;  Any positive integer.
1. **Example:** 100000
1. **Default:** 0

### VpcAvailabilityZones

1. **Synopsis:**
   When using [VpcId](#vpcid), list VPC availability zones in which to create subnets.
   Two availability zones need to be specified.
   Anything after two will be ignored.
1. **Required:** Yes if using [VpcId](#vpcid), otherwise no.
1. **Type:** CommaDelimitedList
1. **Allowed pattern:** Comma-delimited list of VPC availability zones in which to create subnets.
1. **Example:** us-east-1a,us-east-1e
1. **Default:** None - default availability zones used based on
   [Fn::GetAZs](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getavailabilityzones.html) and
   [AWS::Region](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/pseudo-parameter-reference.html#cfn-pseudo-param-region)
1. **References:**
    1. [Regions and Zones](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html)

### VpcId

1. **Synopsis:**
   VPC Id of existing VPC.
   If not specified, a new VPC will be created.
1. **Required:** No
1. **Type:** List of `AWS::EC2::VPC::Id`
1. **Default:** None - a new VPC will be created

## Outputs

### 0penFirst

1. **Synopsis:**
   An alias for [UrlWebApp](#urlwebapp).
   Since it's one of the first things to look at, it is listed first.
1. **Details:**
   It is listed first because the name "cheats" and uses a zero instead of a capital "o".

### AccountID

1. **Synopsis:**
   The AWS account ID used to create the AWS Cloudformation.

### CertificateArn

1. **Synopsis:**
   Amazon Resource Name (ARN) of certificate used for SSL support.
   More information at
   [AWS LoadBalancer Console](https://console.aws.amazon.com/ec2/v2/home#LoadBalancers).
   Select a load balancer, view the "Listeners" tab, then click "View/edit certificates".

### DatabaseHostCore

1. **Synopsis:**
   One of 3 Senzing database servers that hold the Senzing Model.
1. **Details:**
   More information at [AWS RDS Console](https://console.aws.amazon.com/rds/home).

### DatabaseHostLibfeat

1. **Synopsis:**
   Two of 3 Senzing database servers that hold the Senzing Model.
1. **Details:**
   More information at [AWS RDS Console](https://console.aws.amazon.com/rds/home)

### DatabaseHostRes

1. **Synopsis:**
   Three of 3 Senzing database servers that hold the Senzing Model.
1. **Details:**
   More information at [AWS RDS Console](https://console.aws.amazon.com/rds/home)

### DatabaseName

1. **Synopsis:**
   The name of the database.
   It is same name across all 3 database servers.
1. **Details:**
   Usually "G2".

### DatabasePassword

1. **Synopsis:**
   The randomly-generated administrative password for authenticating with the database.

### DatabasePortCore

1. **Synopsis:**
   The port used to access the [DatabaseHostCore](#databasehostcore) database.
1. **Details:**
   More information at [AWS RDS Console](https://console.aws.amazon.com/rds/home).

### DatabasePortLibfeat

1. **Synopsis:**
   The port used to access the [DatabaseHostLibfeat](#databasehostlibfeat) database.
1. **Details:**
   More information at [AWS RDS Console](https://console.aws.amazon.com/rds/home).

### DatabasePortRes

1. **Synopsis:**
      The port used to access the [DatabaseHostRes](#databasehostres) database.
1. **Details:**
   More information at [AWS RDS Console](https://console.aws.amazon.com/rds/home).

### DatabaseUsername

1. **Synopsis:**
   Username to access database in each of the three databases.
1. **Details:**
   More information at [AWS RDS Console](https://console.aws.amazon.com/rds/home).

### Ec2Vpc

1. **Synopsis:**
   The AWS Resource ID of the Virtual Private Cloud (VPC).
1. **Details:**
   More information at [AWS VPC Console](https://console.aws.amazon.com/vpc/home?#vpcs:).

### Host

1. **Synopsis:**
   The hostname of the loadbalancer that is a proxy to all of the services.
1. **Details:**
   More information at [AWS Load Balancers console](https://console.aws.amazon.com/ec2/v2/home?#LoadBalancers:).
   Also used as the `host` value when using [UrlSwagger](#urlswagger).

### Queue

1. **Synopsis:**
   The queue from which records are ingested into Senzing Engine.
   In otherwords, this is the queue where records are sent to be inserted into the Senzing Engine.
1. **Details:**
   More information at [AWS SQS Console](https://console.aws.amazon.com/sqs/v2/home?#/queues).

### QueueDeadLetter

1. **Synopsis:**
   The queue to which records that are not able to be ingested into Senzing Engine are sent.
   In otherwords, if the JSON message is malformed, or Senzing denied inserting into the Senzing Engine.
1. **Details:**
   More information at [AWS SQS Console](https://console.aws.amazon.com/sqs/v2/home?#/queues).

### QueueInfo

1. **Synopsis:**
   The queue that is populated with responses from inserting records into the Senzing Engine.
   This is commonly calls "WithInfo" information.
1. **Details:**
   More information at [AWS SQS Console](https://console.aws.amazon.com/sqs/v2/home?#/queues).

### SenzingVersion

1. **Synopsis:**
   The version of Senzing installed onto the AWS Elastic File System.
   More information at [Senzing API Version History](https://senzing.com/releases/#api-releases).

### SshPassword

1. **Synopsis:**
   Password to be used when logging into the
   [SSHD container](#runsshd).

### SshUsername

1. **Synopsis:**
   User ID to be used when logging into the
   [SSHD container](#runsshd).
1. **Details:**
   Usually "root".

### SubnetPrivate1

1. **Synopsis:**
   The first of two private subnets created.
1. **Details:**
   See the subnet having a Name in the form `{StackName}-ec2-subnet-private-1` in the
   [AWS Virtual Private Cloud console](https://console.aws.amazon.com/vpc/home?#subnets:).

### SubnetPrivate2

1. **Synopsis:**
   The second of two private subnets created.
1. **Details:**
   See the subnet having a Name in the form `{StackName}-ec2-subnet-private-2` in the
   [AWS Virtual Private Cloud console](https://console.aws.amazon.com/vpc/home?#subnets:).

### SubnetPublic1

1. **Synopsis:**
   The first of two public subnets created.
1. **Details:**
   See the subnet having a Name in the form `{StackName}-ec2-subnet-public-1` in the
   [AWS Virtual Private Cloud console](https://console.aws.amazon.com/vpc/home?#subnets:).

### SubnetPublic2

1. **Synopsis:**
   The second of two public subnets created.
1. **Details:**
   See the subnet having a Name in the form `{StackName}-ec2-subnet-public-2` in the
   [AWS Virtual Private Cloud console](https://console.aws.amazon.com/vpc/home?#subnets:).

### UrlApiServer

1. **Synopsis:**
   A URL showing how to reach the
   [Senzing API Server](https://github.com/Senzing/senzing-api-server)
   directly.

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
   [Swagger User Interface](https://github.com/swagger-api/swagger-ui).
1. **Usage:**
   To access the Senzing API server
    1. Using the URL, visit the `UrlSwagger` webpage.
    1. In **Servers**
        1. From the drop-down, select `{protocol}://{host}:{port}{path}`.
        1. **protocol:** https
        1. **host:** Enter the value of [Host](#host)
        1. **port:** 443
        1. **path:** /api
    1. The HTTP URIs will now access the deployed Senzing API server.

### UrlWebApp

1. **Synopsis:**
   A URL showing how to reach the
   [Senzing Entity Search Web App](https://github.com/Senzing/entity-search-web-app).

### UrlXterm

1. **Synopsis:**
   A URL showing how to reach the
   [Senzing Xterm](https://github.com/Senzing/docker-xterm).
1. **Usage:**
   From this Linux terminal, `G2Command.py`, `G2Explorer.py`, `G2ConfigTool.py`,
   can be run.

### UserInitPassword

1. **Synopsis:**
   The one-time password for the [UserName](#username).
1. **Details:**
   When the one-time password is used, the user is prompted for a new password.
   Once a new password is submitted, the one-time password has no value.

### UserName

1. **Synopsis:**
   The user name submitted for the [CognitoAdminEmail](#cognitoadminemail).
   It is the initial user created to access the system.
1. **Details:**
   To add users, see [UserPool](#userpool)

### UserPool

1. **Synopsis:**
   The specific [UserPool](https://console.aws.amazon.com/cognito/users/#/pool/u) URL.
   It can be used to add, manage, or delete users for this Cloudformation.
