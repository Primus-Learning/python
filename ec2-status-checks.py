import boto3
import schedule

ec2_client = boto3.client('ec2')

def check_instance_status():
    statuses = ec2_client.describe_instance_status(
        # IncludeAllInstances=True
    )
    for status in statuses['InstanceStatuses']:
        state = status['InstanceState']['Name']
        ins_status = status['InstanceStatus']['Status']
        sys_status = status['SystemStatus']['Status']
        instance_id = status['InstanceId']
        print(f"Instance {instance_id} is {state} status is {ins_status} and system status is {sys_status}")
    print("##################################\n")

schedule.every(5).seconds.do(check_instance_status)

while True:
    schedule.run_pending()