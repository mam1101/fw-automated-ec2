####
# Author: Max Miller
# Last Modified: Sept 1st, 2020
# About:
#   This script launches a new AWS EC2 instance with a running base Django application.
####

import boto3 as bt
import botocore as bc
import paramiko
import time

client = bt.client('ec2')
resource = bt.resource('ec2')
key_name = 'ec2'
max_ssh_attempts = 5

# generate a new default VPC if none exists
try:
    client.create_default_vpc()
    print('New default VPC created')
except bc.exceptions.ClientError as e:
    print('Default VPC already exists')

# generate a new keypair to use with the ec2 instance if none exists
try:
    key = client.describe_key_pairs(KeyNames=[key_name])
except bc.exceptions.ClientError as e:
    key = client.create_key_pair(KeyName=key_name)
    rsa_key = key['KeyMaterial']
    f = open(f'{key_name}.pem', 'a')
    f.write(rsa_key)
    f.close()

ssh_key = paramiko.RSAKey.from_private_key_file(f'{key_name}.pem')
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

print('Creating a new EC2 instance')
create_instance = resource.create_instances(
    ImageId="ami-0dd005d3eb03f66e8",
    InstanceType='t1.micro',
    MinCount=1,
    MaxCount=1,
    KeyName=key_name
    )
instance = create_instance[0]

# wait for the instance to boot
print('Instance created. Waiting to connect...')
instance.wait_until_running()
instance.reload()
instance_ip = instance.public_ip_address
print(f'EC2 instance booted. Connecting to {instance_ip}...')

# try for ssh connection until one is established (usually take 1~2 tries)
for attempt in range(0, max_ssh_attempts):
    try:
        print(f'Connected to {instance_ip}')
        client.connect(hostname=instance_ip, username='ubuntu', pkey=ssh_key)

        # read the django setup script and load into memory
        with open('install_django.sh', 'r') as django_setup:
            lines = django_setup.readlines()
        commands = [command.strip() for command in lines]

        for cmd in commands:
            print(f'Running Command: {cmd}')
            stdin, stdout, stderr = client.exec_command(cmd)
            exit_status = stdout.channel.recv_exit_status()
            if exit_status == 0:
                print(stdout.read())
            else:
                print("Error:", exit_status, stderr)

        client.close()
        print('============================================')
        print(f'Web app is running at http://{instance_ip}')
        print('============================================')
        break

    except Exception as e:
        print('Retrying Connection...')
        time.sleep(10)
