# aws-cloudformation-ecs

1. Checkmarks represent where you supply pre-existing AWS Resources:

    |   | VPC | Route53 | RDS | Instructions | Launch |
    |--:|:---:|:-------:|:---:|:------------:|:------:|
    | 1 | | | | [instructions](https://github.com/Senzing/aws-cloudformation-ecs-poc-simple) | [:arrow_forward:](https://console.aws.amazon.com/cloudformation/home#/stacks/new?stackName=senzing-poc&templateURL=https://s3.amazonaws.com/public-read-access/aws-cloudformation-ecs-poc-simple/cloudformation.yaml) |
    | 2 | :heavy_check_mark: | :heavy_check_mark: | | [instructions](docs/senzing-demo-user-vpc-hosted-zone) | [:arrow_forward:](https://console.aws.amazon.com/cloudformation/home#/stacks/new?templateURL=https://s3.amazonaws.com/public-read-access/aws-cloudformation-ecs-user-vpc-hosted-zone/cloudformation.yaml) |

1. How to create AWS Resources:
    1. VPC
        1. [AWS VPC console](https://console.aws.amazon.com/vpc/home#vpcs:)
    1. Route53
        1. [AWS Route53 Hosted Zone console](https://console.aws.amazon.com/route53/v2/hostedzones#)

## Details

1. Variations among Cloudformation templates

    | VPC | Route53 | Name | Comments |
    |:---:|:-------:|------|----------|
    | D   | N       | senzing-demo-full-stack | |
    | D   | N       | senzing-demo-staging | Used to test releases |
    | D   | Y       | senzing-demo-user-vpc-hosted-zone |
    | S   | N       | senzing-demo-poc-simple | A "no user options" formation |
    | S   | N       | senzing-demo-staging-simple | Used to test releases |
    | S   | U       | senzing-demo-certificates | Input: certificate, private key |
    | S   | Y       | senzing-demo-hosted-zone | |

1. VPC
    1. 'S' = Static. User cannot specify.
    1. 'D' = Dynamic. User can specify.
1. Route53
    1. 'Y' = Route53 Hosted Zone specified by user.
    1. 'N' = Self-signed certificate used.
    1. 'U' = User-supplied certificate.
