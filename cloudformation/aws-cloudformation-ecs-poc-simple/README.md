# aws-cloudformation-ecs-poc-simple

## Synopsis

The `aws-cloudformation-ecs-poc-simple` demonstrates a Senzing deployment using an AWS Cloudformation template.

Detailed instructions at
[hub.senzing.com/aws-cloudformation-ecs-poc-simple](http://senzing.github.io/aws-cloudformation-ecs-poc-simple)

## How to deploy without much thinking

1. :warning: **Warning:** This Cloudformation deployment will accrue AWS costs.
   With appropriate permissions, the
   [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/)
   can help evaluate costs.
1. Download the appropriate [AWS Cloudformation template example](https://raw.githubusercontent.com/Senzing/aws-cloudformation-ecs-poc-simple/main/cloudformation.yaml) from this repository to your local device.  Example:
    ```
    curl -X GET \
        --output ~/cloudformation.yaml \
        https://raw.githubusercontent.com/Senzing/aws-cloudformation-ecs-poc-simple/main/cloudformation.yaml
    ```
3. It is highly suggested to take a look at the AWS Cloudformation Template that has been downloaded.  This template is an example that deploys and configures a number of services and facilities.  While it is a working and complete example, each business may have different requirements and their account may not have all the privledges required to deploy it.  Furthermore, the examples change over time and these files are meant to be treated as code files so they should be put under source control.
1. Visit the [AWS Cloudformation home](https://console.aws.amazon.com/cloudformation/home).
1. At the upper-right, click the "Create stack" drop-down and choose "With new resources (standard)".
1. In the "Specify template" area choose the "Upload a template file" radio button.
1. Select the "Choose file" button and choose the AWS Cloudformation template that was downloaded previously.
1. At lower-right, click on "Next" button.
1. In **Specify stack details**
    1. In **Stack name**
        1. Choose a stack name that is unique to you and 21 characters or less.  (Several resource types have a limit of 32 character names. The CFT uses the stack name and an 11 character suffix to name resources uniquely.)
    1. In **Parameters**
        1. In **Senzing installation**
            1. Accept the End User License Agreement.
            1. Optionally, add a license string.
        1. In **Security**
            1. Provide the email address for the administrative user.  Example: `me@example.com`
            1. Provide the permitted IP address block allowed to connect using CIDR notation.  Note: to open the installation to any IP address use: `0.0.0.0/0`.  For more on CIDR, see [Classless Inter-Domain Routing](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing)
        1. In **Optional: Initial data load**
            1. If "Yes" is chosen, the default truth set will be loaded.
        1. In **Security responsibility**
            1. Understand the nature of the security in the deployment.
            1. Once understood, enter "I AGREE".
    1. At lower-right, click "Next" button.
1. In **Configure stack options**
    1. At lower-right, click "Next" button.
1. In **Review senzing-poc**
    1. Near the bottom, in **Capabilities**
        1. Check ":ballot_box_with_check: I acknowledge that AWS CloudFormation might create IAM resources."
    1. At lower-right, click "Create stack" button.

## Using deployment

1. Visit [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/home).
    1. Make sure correct AWS region is selected.
1. Wait until "senzing-poc" status is `CREATE_COMPLETE`.
    1. Senzing formation takes about 20 minutes to fully deploy.
    1. May have to hit the refresh button a few times to get updated information.
1. Click on "senzing-poc" stack.
1. Click on "Outputs" tab.
1. Open the "0penFirst" value in a new web browser tab or window.
    1. Because this uses a self-signed certificate, a warning will come up in your browser.  Simply continue.
    1. In the "Sign in with your email and password" dialog box, enter the *UserName* and *UserInitPassword*
       values seen in the "Output" tab of the "senzing-poc" stack.  This is a one-time password.
    1. In **Change Password**, enter a new password.

## Additional topics

1. [How to load AWS Cloudformation queue](https://github.com/senzing-garage/knowledge-base/blob/main/HOWTO/load-aws-cloudformation-queue.md)
1. [How to set AWS RDS force-scaling-capacity](https://github.com/senzing-garage/knowledge-base/blob/main/HOWTO/set-aws-rds-force-scaling-capacity.md)
1. [How to migrate Senzing in AWS Cloudformation](https://github.com/senzing-garage/knowledge-base/blob/main/HOWTO/migrate-senzing-in-cloudformation.md)
1. [How to update Senzing license](https://github.com/senzing-garage/knowledge-base/blob/main/HOWTO/update-senzing-license.md)
1. [How to migrate an AWS RDS database](https://github.com/senzing-garage/knowledge-base/blob/main/HOWTO/migrate-aws-rds-database.md)

## Behind the scenes

### What Cloudformation does

1. Provisions:
    1. AWS infrastructure: VPC, subnets, Internet Gateway, Routes, IAM Roles and Policies, Logging
    1. AWS: EFS, 3 SQS queues, 3 AWS Aurora Postgres Serverless databases, ECS, Cognito
    1. Senzing: Stream-loader, Redoer, API Server, Entity Search Web App

### What is not supported

1. What this doesn't support (i.e. what you don't get):
    1. Specification of existing AWS resources
        1. VPC, Subnets, RDS, SQS
