#! /usr/bin/env python3

from netaddr import IPNetwork


def as_cidr(cidr_decimal, cidr_prefix):
    octals = '.'.join([str(cidr_decimal >> (i << 3) & 0xFF) for i in range(4)[::-1]])
    return "{0}/{1}".format(octals, cidr_prefix)


def find_cidr_decimal(cidr):
    (octets, prefix) = cidr.split('/')
    octet = octets.split(".")
    return int(octet[0]) << 24 | int(octet[1]) << 16 | int(octet[2]) << 8 | int(octet[3])


def find_cidr_prefix(cidr):
    (octets, prefix) = cidr.split('/')
    return int(prefix)


def highest_cidr(cidrs):
    result = "0.0.0.0/0"
    result_decimal = find_cidr_decimal(result)
    for cidr in cidrs:
        cidr_decimal = find_cidr_decimal(cidr)
        if cidr_decimal > result_decimal:
            result = cidr
            result_decimal = find_cidr_decimal(result)
    return result


def adjust_cidr(cidr, next_cidr_prefix=None):
    last_cidr_decimal = find_cidr_decimal(cidr)
    last_cidr_prefix = find_cidr_prefix(cidr)
    stride = 2 << (31 - last_cidr_prefix)
    mask = 0xffffffff - (stride - 1)
    next_cidr_decimal = last_cidr_decimal & mask
    next_cidr_decimal = next_cidr_decimal + stride - 1
    return as_cidr(next_cidr_decimal, next_cidr_prefix)


def next_cidr(cidr):
    last_cidr_decimal = find_cidr_decimal(cidr)
    last_cidr_prefix = find_cidr_prefix(cidr)
    stride = 2 << (31 - last_cidr_prefix)
    mask = 0xffffffff - (stride - 1)
    next_cidr_decimal = (last_cidr_decimal + stride) & mask
    return as_cidr(next_cidr_decimal, last_cidr_prefix)


x = {
        'Subnets': [
            {
                'AvailabilityZone': 'us-east-1b',
                'AvailabilityZoneId': 'use1-az1',
                'AvailableIpAddressCount': 248,
                'CidrBlock': '10.0.2.0/24',
                'DefaultForAz': False,
                'MapPublicIpOnLaunch': False,
                'MapCustomerOwnedIpOnLaunch': False,
                'State': 'available',
                'SubnetId': 'subnet-0851e7e6aeb79035e',
                'VpcId': 'vpc-020079e3d81c9a3f7',
                'OwnerId': '488776654093',
                'AssignIpv6AddressOnCreation': False,
                'Ipv6CidrBlockAssociationSet': [],
                'Tags': [
                    {
                        'Key': 'aws:cloudformation:stack-name',
                        'Value': 'mjd-5001'
                    }, {
                        'Key': 'Name',
                        'Value': 'mjd-5001-ec2-subnet-private-2'
                    }, {
                        'Key': 'aws:cloudformation:logical-id',
                        'Value': 'Ec2SubnetPrivate2'
                    }, {
                        'Key': 'aws:cloudformation:stack-id',
                        'Value': 'arn:aws:cloudformation:us-east-1:488776654093:stack/mjd-5001/2a641d60-b1a0-11eb-9112-0a029b5a039d'
                    }
                ],
                'SubnetArn': 'arn:aws:ec2:us-east-1:488776654093:subnet/subnet-0851e7e6aeb79035e'
            }, {
                'AvailabilityZone': 'us-east-1a',
                'AvailabilityZoneId': 'use1-az6',
                'AvailableIpAddressCount': 248,
                'CidrBlock': '10.0.1.0/24',
                'DefaultForAz': False,
                'MapPublicIpOnLaunch': False,
                'MapCustomerOwnedIpOnLaunch': False,
                'State': 'available',
                'SubnetId': 'subnet-0b4669f0334891bb7',
                'VpcId': 'vpc-020079e3d81c9a3f7',
                'OwnerId': '488776654093',
                'AssignIpv6AddressOnCreation': False,
                'Ipv6CidrBlockAssociationSet': [],
                'Tags': [
                    {
                        'Key': 'aws:cloudformation:stack-name',
                        'Value': 'mjd-5001'
                    }, {
                        'Key': 'aws:cloudformation:stack-id',
                        'Value': 'arn:aws:cloudformation:us-east-1:488776654093:stack/mjd-5001/2a641d60-b1a0-11eb-9112-0a029b5a039d'
                    }, {
                        'Key': 'Name',
                        'Value': 'mjd-5001-ec2-subnet-private-1'
                    }, {
                        'Key': 'aws:cloudformation:logical-id', 'Value': 'Ec2SubnetPrivate1'
                    }
                ],
                'SubnetArn': 'arn:aws:ec2:us-east-1:488776654093:subnet/subnet-0b4669f0334891bb7'
            }, {
                'AvailabilityZone': 'us-east-1a',
                'AvailabilityZoneId': 'use1-az6',
                'AvailableIpAddressCount': 248,
                'CidrBlock': '10.1.1.255/24',
                'DefaultForAz': False,
                'MapPublicIpOnLaunch': False,
                'MapCustomerOwnedIpOnLaunch': False,
                'State': 'available',
                'SubnetId': 'subnet-0b4669f0334891bb7',
                'VpcId': 'vpc-020079e3d81c9a3f7',
                'OwnerId': '488776654093',
                'AssignIpv6AddressOnCreation': False,
                'Ipv6CidrBlockAssociationSet': [],
                'Tags': [
                    {
                        'Key': 'aws:cloudformation:stack-name',
                        'Value': 'mjd-5001'
                    }, {
                        'Key': 'aws:cloudformation:stack-id',
                        'Value': 'arn:aws:cloudformation:us-east-1:488776654093:stack/mjd-5001/2a641d60-b1a0-11eb-9112-0a029b5a039d'
                    }, {
                        'Key': 'Name',
                        'Value': 'mjd-5001-ec2-subnet-private-1'
                    }, {
                        'Key': 'aws:cloudformation:logical-id', 'Value': 'Ec2SubnetPrivate1'
                    }
                ],
                'SubnetArn': 'arn:aws:ec2:us-east-1:488776654093:subnet/subnet-0b4669f0334891bb7'
            }
        ],
        'ResponseMetadata': {
            'RequestId': 'fe3f3397-ecea-42ca-ac90-943554c1cba0',
            'HTTPStatusCode': 200,
            'HTTPHeaders': {
                'x-amzn-requestid': 'fe3f3397-ecea-42ca-ac90-943554c1cba0',
                'cache-control': 'no-cache, no-store',
                'strict-transport-security':
                'max-age=31536000; includeSubDomains',
                'content-type': 'text/xml;charset=UTF-8',
                'content-length': '3443',
                'vary': 'accept-encoding',
                'date': 'Mon, 10 May 2021 18:44:53 GMT',
                'server': 'AmazonEC2'
            },
            'RetryAttempts': 0
        }
    }

subnets = x.get("Subnets")
cidr = highest_cidr(p["CidrBlock"] for p in subnets)
print("Highest CIDR: {}".format(cidr))

#  Using IPNetwork

next_range = IPNetwork(cidr)
result = []
for x in range(2):
    next_range = next_range.next()
    result.append(str(next_range))
print(result)

# Using home brew.

cidr = adjust_cidr(cidr, 24)
result = []
for x in range(2):
    cidr = next_cidr(cidr)
    result.append(cidr)
print(result)
