# aws-cloudformation-ecs

## Synopsis

In the demonstration Cloudformation templates,
some templates create AWS resources,
other templates require pre-existing AWS Resources.

1. :heavy_check_mark: - The Cloudformation creates the resource
1. :x: - A pre-existing AWS Resources is required.


|   | VPC | Route53 | RDS | Instructions | Launch |
|--:|:---:|:-------:|:---:|:------------:|:------:|
| 1 | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | [instructions](https://github.com/Senzing/aws-cloudformation-ecs-poc-simple) | [:arrow_forward:](https://console.aws.amazon.com/cloudformation/home#/stacks/new?stackName=senzing-poc&templateURL=https://s3.amazonaws.com/public-read-access/aws-cloudformation-ecs-poc-simple/cloudformation.yaml) |
| 2 | :x: | :heavy_check_mark: | :heavy_check_mark: | [instructions](docs/senzing-demo-full-stack) | [:arrow_forward:](https://console.aws.amazon.com/cloudformation/home#/stacks/new?templateURL=https://s3.amazonaws.com/public-read-access/aws-cloudformation-ecs-full-stack/cloudformation.yaml) |
| 3 | :heavy_check_mark: | :x: | :heavy_check_mark: | [instructions](docs/senzing-demo-hosted-zone) | [:arrow_forward:](https://console.aws.amazon.com/cloudformation/home#/stacks/new?templateURL=https://s3.amazonaws.com/public-read-access/aws-cloudformation-ecs-hosted-zone/cloudformation.yaml) |
| 4 | :x: | :x: | :heavy_check_mark: | [instructions](docs/senzing-demo-user-vpc-hosted-zone) | [:arrow_forward:](https://console.aws.amazon.com/cloudformation/home#/stacks/new?templateURL=https://s3.amazonaws.com/public-read-access/aws-cloudformation-ecs-user-vpc-hosted-zone/cloudformation.yaml) |


1. How to create AWS Resources:
    1. VPC
        1. [AWS VPC console](https://console.aws.amazon.com/vpc/home#vpcs:)
    1. Route53
        1. [AWS Route53 Hosted Zone console](https://console.aws.amazon.com/route53/v2/hostedzones#)

## Details

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
