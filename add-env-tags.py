import boto3

ec2_client = boto3.client('ec2')

instance_ids = []

reservations = ec2_client.describe_instances(
    Filters=[
    {
      'Name': 'instance-state-name',
      'Values': ['running']
    }
    ]
)['Reservations']
for res in reservations:
    instances = res['Instances']
    for ins in instances:
        instance_ids.append(ins['InstanceId'])

response = ec2_client.create_tags(
    Resources=instance_ids,
    Tags=[
        {
            'Key': 'environment',
            'Value': 'dev'
        }
    ]
)