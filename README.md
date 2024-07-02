# aws-cloudformation-ecs

## :no_entry: Deprecated

[![No Maintenance Intended](http://unmaintained.tech/badge.svg)](http://unmaintained.tech/)

If you are beginning your journey with [Senzing],
please start with [Senzing Quick Start guides].

You are in the [Senzing Garage] where projects are "tinkered" on.
Although this GitHub repository may help you understand an approach to using Senzing,
it's not considered to be "production ready" and is not considered to be part of the Senzing product.
Heck, it may not even be appropriate for your application of Senzing!

## Synopsis

In the demonstration Cloudformation templates,
some templates create AWS resources,
other templates require pre-existing AWS Resources.

1. :heavy_check_mark: - The Cloudformation creates the resource
1. :x: - A pre-existing AWS Resources is required.

|   | VPC | Route53 | RDS | Instructions | Launch |
|--:|:---:|:-------:|:---:|:------------:|:------:|
| 1 | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | [aws-cloudformation-ecs-poc-simple] | [:arrow_forward:](https://console.aws.amazon.com/cloudformation/home#/stacks/new?stackName=senzing-poc&templateURL=https://s3.amazonaws.com/public-read-access/aws-cloudformation-ecs-poc-simple/cloudformation.yaml) |
| 2 | :heavy_check_mark: | :x: | :heavy_check_mark: | [senzing-demo-hosted-zone] | [:arrow_forward:](https://console.aws.amazon.com/cloudformation/home#/stacks/new?templateURL=https://s3.amazonaws.com/public-read-access/aws-cloudformation-ecs-hosted-zone/cloudformation.yaml) |
| 3 | :x: | :heavy_check_mark: | :heavy_check_mark: | [senzing-demo-full-stack] | [:arrow_forward:](https://console.aws.amazon.com/cloudformation/home#/stacks/new?templateURL=https://s3.amazonaws.com/public-read-access/aws-cloudformation-ecs-full-stack/cloudformation.yaml) |
| 4 | :x: | :x: | :heavy_check_mark: | [senzing-demo-user-vpc-hosted-zone] | [:arrow_forward:](https://console.aws.amazon.com/cloudformation/home#/stacks/new?templateURL=https://s3.amazonaws.com/public-read-access/aws-cloudformation-ecs-user-vpc-hosted-zone/cloudformation.yaml) |

1. How to create AWS Resources:
    1. VPC
        1. [AWS VPC console]
    1. Route53
        1. [AWS Route53 Hosted Zone console]

## Warning

1. :warning: **Warning:**
   This Cloudformation deployment will accrue AWS costs.
   With appropriate permissions, the [AWS Cost Explorer]
   can help evaluate costs.
1. :warning: **Warning:**
   This Cloudformation deployment only runs in [supported AWS Regions].

## Details

1. [aws-cloudformation-ecs-certificates]
    1. User specifies X.590 certificate and private-key.
1. [aws-cloudformation-ecs-full-stack]
    1. User specifies VPC.
    1. User specifies which services are started.
1. [aws-cloudformation-ecs-hosted-zone]
    1. User specifies AWS Route53 Hosted Zone.
1. [aws-cloudformation-ecs-staging]
    1. Pulls Senzing API from staging server.
    1. User specifies VPC.
    1. User specifies which services are started.
1. [aws-cloudformation-ecs-staging-simple]
    1. Pulls Senzing API from staging server.
1. [aws-cloudformation-ecs-staging-simple-100M]
    1. Pulls Senzing API from staging server.
    1. Reads gzipped input file.
    1. User specifies Senzing API version.
1. [aws-cloudformation-ecs-user-vpc-hosted-zone]
    1. User specifies AWS Route53 Hosted Zone.
    1. User specifies VPC.
    1. User specifies which services are started.

## Analysis

1. Variations among Cloudformation templates

    | VPC | Route53 | Phase | Name | Comments |
    |:---:|:-------:|:-----:|------|----------|
    | D   | N       | P     | senzing-demo-full-stack | |
    | D   | N       | T     | senzing-demo-staging | Used to test releases |
    | D   | Y       | P     | senzing-demo-user-vpc-hosted-zone |
    | S   | N       | P     | senzing-demo-poc-simple | A "no user options" formation |
    | S   | N       | T     | senzing-demo-staging-simple | Used to test releases |
    | S   | U       | T     | senzing-demo-certificates | Input: certificate, private key |
    | S   | Y       | P     | senzing-demo-hosted-zone | |

1. VPC
    1. 'S' = Static. User cannot specify VPC.
    1. 'D' = Dynamic. User can specify existing VPC.
1. Route53
    1. 'Y' = Existing Route53 Hosted Zone specified by user.
    1. 'N' = Self-signed certificate used.
    1. 'U' = User-supplied certificate.
1. Phase
    1. 'P' - For Public use
    1. 'T' - For Testing purposes

[AWS Cost Explorer]: https://aws.amazon.com/aws-cost-management/aws-cost-explorer/
[AWS Route53 Hosted Zone console]: https://console.aws.amazon.com/route53/v2/hostedzones#
[AWS VPC console]: https://console.aws.amazon.com/vpc/home#vpcs:
[aws-cloudformation-ecs-certificates]: cloudformation/aws-cloudformation-ecs-certificates
[aws-cloudformation-ecs-full-stack]: cloudformation/aws-cloudformation-ecs-full-stack
[aws-cloudformation-ecs-hosted-zone]: cloudformation/aws-cloudformation-ecs-hosted-zone
[aws-cloudformation-ecs-poc-simple]: https://github.com/senzing-garage/aws-cloudformation-ecs-poc-simple
[aws-cloudformation-ecs-staging]: cloudformation/aws-cloudformation-ecs-staging
[aws-cloudformation-ecs-staging-simple]: cloudformation/aws-cloudformation-ecs-staging-simple
[aws-cloudformation-ecs-staging-simple-100M]: cloudformation/aws-cloudformation-ecs-staging-simple-100M
[aws-cloudformation-ecs-user-vpc-hosted-zone]: cloudformation/aws-cloudformation-ecs-vpc-hosted-zone
[Senzing]: https://senzing.com/
[Senzing Garage]: https://github.com/senzing-garage
[Senzing Quick Start guides]: https://docs.senzing.com/quickstart/
[senzing-demo-full-stack]: docs/senzing-demo-full-stack
[senzing-demo-hosted-zone]: docs/senzing-demo-hosted-zone
[senzing-demo-user-vpc-hosted-zone]: docs/senzing-demo-user-vpc-hosted-zone
[supported AWS Regions]: https://github.com/senzing-garage/knowledge-base/blob/main/lists/aws-supported-regions.md
