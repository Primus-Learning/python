import boto3

ec2_client = boto3.client('ec2')

ec2_client.create_vpc(
    CidrBlock="172.31.0.0/16"
)

all_available_vpcs = ec2_client.describe_vpcs()
vpcs = all_available_vpcs["Vpcs"]

for vpc in vpcs:
    print(vpc["VpcId"])
    cidr_block_assoc_sets = vpc["CidrBlockAssociationSet"]
    for assoc_set in cidr_block_assoc_sets:
        print(assoc_set["CidrBlockState"])