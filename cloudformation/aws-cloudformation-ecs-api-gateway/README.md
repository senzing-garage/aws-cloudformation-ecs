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
1. Visit [AWS Cloudformation with Senzing template](https://console.aws.amazon.com/cloudformation/home#/stacks/new?stackName=senzing-poc&templateURL=https://s3.amazonaws.com/public-read-access/aws-cloudformation-ecs-poc-simple/cloudformation.yaml)
1. At lower-right, click on "Next" button.
1. In **Specify stack details**
    1. In **Parameters**
        1. In **Security responsibility**
            1. Understand the nature of the security in the deployment.
            1. Once understood, enter "I AGREE".
        1. In **Senzing installation**
            1. Accept the End User License Agreement
        1. In **Security**
            1. Enter your email address.  Example: `me@example.com`
    1. Other parameters are optional.
       The default values are fine.
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

1. [How to load AWS Cloudformation queue](https://github.com/Senzing/knowledge-base/blob/main/HOWTO/load-aws-cloudformation-queue.md)
1. [How to set AWS RDS force-scaling-capacity](https://github.com/Senzing/knowledge-base/blob/main/HOWTO/set-aws-rds-force-scaling-capacity.md)
1. [How to migrate Senzing in AWS Cloudformation](https://github.com/Senzing/knowledge-base/blob/main/HOWTO/migrate-senzing-in-cloudformation.md)
1. [How to update Senzing license](https://github.com/Senzing/knowledge-base/blob/main/HOWTO/update-senzing-license.md)
1. [How to migrate an AWS RDS database](https://github.com/Senzing/knowledge-base/blob/main/HOWTO/migrate-aws-rds-database.md)

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

## Programmatic access to the Api Server

Set Environment Variables
```
export AWS_COGNITO_USERNAME="<replace-with-username>"
export AWS_COGNITO_PASSWORD="<replace-with-password>"
export AWS_COGNITO_CLIENT_ID="<replace-with-appclient-id>"
export AWS_COGNITO_POOL_ID="<replace-with-userpool-id>"
export HTTP_API_URL="<replace-with-http-api-url>"
export WEBSOCKET_API_URL="<replace-with-websocket-api-url>"
export AWS_REGION="<replace-with-aws-region>"
```

Confirm password of new user
```
aws cognito-idp admin-set-user-password \
  --user-pool-id ${AWS_COGNITO_POOL_ID} \
  --username ${AWS_COGNITO_USERNAME} \
  --password ${AWS_COGNITO_PASSWORD} \
  --permanent
```

Get access token
```
SENZING_COGNITO_ACCESS_TOKEN=$( curl -X POST \
  --header 'X-Amz-Target: AWSCognitoIdentityProviderService.InitiateAuth' \
  --header 'Content-Type: application/x-amz-json-1.1' \
  --data "
    {
      \"AuthParameters\" : {
        \"USERNAME\" : \"${AWS_COGNITO_USERNAME}\",
        \"PASSWORD\" : \"${AWS_COGNITO_PASSWORD}\"
      },
      \"AuthFlow\" : \"USER_PASSWORD_AUTH\",
      \"ClientId\" : \"${AWS_COGNITO_CLIENT_ID}\"
    }
    " \
    https://cognito-idp.${AWS_REGION}.amazonaws.com/ | jq \
    --raw-output ".AuthenticationResult.AccessToken" )
```

Here a sample heartbeat request is made to the HTTP API server

```
curl -H "Authorization: Bearer ${SENZING_COGNITO_ACCESS_TOKEN}" ${HTTP_API_URL}/api/heartbeat
```

Here a sample analyze websocket request is made to the API server

```
wscat -H "token: ${SENZING_COGNITO_ACCESS_TOKEN}" -H "accept: application/json; charset=UTF-8" -H "Content-Type: application/x-jsonlines; charset=UTF-8" -c "${WEBSOCKET_API_URL}?progressPeriod=3000&eofSendTimeout=3"
```
