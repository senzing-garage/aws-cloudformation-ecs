# aws-cloudformation-ecs-private

## Synopsis

In these demonstration Cloudformation templates (CFT),
we show the deploying of Senzing into a pre-existing, private VPC.

There are three CFTs:

1. cloudformation-VPC.yaml - a test harness and exemplar VPC.
2. cloudformation-database.yaml - installs the database into it's own stack.
3. cloudformation-basic.yaml - installs Senzing and other services.

## Test harness VPC (cloudformation-VPC.yaml)

The purpose of this CFT is two-fold.  It sets up a VPC in order to test installation
of the other CFTs.  It also shows what infrastructure is necessary in order to
install Senzing using the other CFTs.  There are redundant private subnets created and
a single public subnet.  None of the Senzing resources are installed on the public
subnets it is created to allow the other CFTs to pull images from Senzing's public
ECR and S3 via an internet gateway.

Note:  if your VPC does not allow egress to the public internet, then [look here](#gapped-vpc).

## Database installation (cloudformation-database.yaml)

The purpose of this CFT is to create the database or databases for Senzing.  There
are several necessary parameters needed for this step:  a VPC, the VPC CIDR block,
2 private subnets, and a security group that allows internet egress.  This CFT
also outputs necessary details for the basic CFT so that it doesn't have to ask
for the same parameters.

The rationale behind having a database CFT and a Senzing basic CFT
is to allow you to easily save your database.  You can bring down the basic
stack, munge it, and bring up new ones as you see fit, while your database
remains.  This is especially useful if you have lots of data and don't want
to pay the price for reloading.

## Senzing basic installation (cloudformation-basic.yaml)

The purpose of this CFT is to install Senzing and all the associated services.
In it we have selected commonly used services.  However, just like all our CFTs,
you are encouraged to tune and tweak as you see fit.  In particular, if you'd like
to turn on and off services you'll find a block in the CFT that makes this easy:

```
    Run:
      ApiServer: Yes
      Jupyter: No
      Redoer: Yes
      Sshd: Yes
      SshdMax: No
      StreamLoader: Yes
      StreamProducer: Yes
      Swagger: No
      VpcFlowLogs: No
      WebApp: Yes
      Xterm: Yes
```

## Gapped VPC

The CFTs included here will not work in a VPC that does not have any internet access.
There are a couple of commented out sections in the cloudformation-VPC.yaml
file that show an approach the problem of a gapped VPC using VPC endpoints.
There are several VPC endpoints in the VPC CFT, all of which are required to pull
images from a private ECR.  Similarly, the 443 ingress is required in the security
group.

However, it's not a complete implementation, just a starter.  The VPC endpoints work
to allow access to a private ECR, but do not address issues of how to install the
Senzing installation archive.  Furthermore, a private ECR requires that the user
create repositories and pull the images from the public ECR to their private ECR.
These private repos may need a policy like this one:

```
{
    "Version": "2008-10-17",
    "Statement": [
        {
            "Sid": "AllowPull",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::<account number>:root"
            },
            "Action": [
                "ecr:GetDownloadUrlForLayer",
                "ecr:BatchGetImage",
                "ecr:BatchCheckLayerAvailability"
            ]
        }
    ]
}
```

applied to each repo if the installation account is different than the ECR account
or perhaps for other permissions reasons.  Generally, there is a great deal of
variability to provide all the answers for such an environment.

