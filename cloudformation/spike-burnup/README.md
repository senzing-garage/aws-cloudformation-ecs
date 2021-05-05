# Spike Burn up

## 0

1. A simple cloudformation that simply brings up `senzing/sshd`.
   This is to verify that that SSHD container can be reached via public IP address


## 1

1. Split up #0 to see if the VPC (1.1) can be separated from the application (1.2)

## 2


## 3

1. Add in the full Senzing stack.
1. It works, but you can't deploy 2 copies of the application:
    1. The subnets collide.
    1. **Ec2VpcGatewayAttachment**  Network vpc-0e3f12dc0e36aa701 already has an internet gateway attached (Service: AmazonEC2; Status Code: 400; Error Code: InvalidParameterValue; Request ID: 83b54b22-f2f2-42d9-ac7b-eadcafeee0bc; Proxy: null)

## 4

1. Move the Gateway to the "VPC" cloudformation
