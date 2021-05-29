import boto3
import os
import time
import subprocess
import paramiko


ec2 = boto3.resource('ec2', region_name='us-west-1')

# create a file to store the key locally
outfile = open('ec2-keypair.pem','w')

# call the boto ec2 function to create a key pair
key_pair = ec2.create_key_pair(KeyName='ec2-keypair')

# capture the key and store it in a file
KeyPairOut = str(key_pair.key_material)
print(KeyPairOut)
outfile.write(KeyPairOut)
outfile.close()

os.chmod("ec2-keypair.pem", 0o400)

# Create ec2 and use SubnetId to associate VPC.
instances = ec2.create_instances(
     ImageId='ami-0d382e80be7ffdae5',
     MinCount=1,
     MaxCount=1,
     InstanceType='t2.micro',
     KeyName='ec2-keypair',
     SubnetId='subnet-00f10fc4d76c44151'
 )

instance = instances[0]

instance.wait_until_running()

# Associate Security Group to the instance to allow access to instance VPC 
instance.modify_attribute(Groups=['sg-040cfb330480cad0f'])

# Reload to get the DNS name after EC2 is up and running
instance.load()
hostname = instance.public_dns_name

key = paramiko.RSAKey.from_private_key_file('ec2-keypair.pem')

client = paramiko.SSHClient()

client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect/ssh to an instance

try:

    # Here 'ubuntu' is user name and 'hostname' is public DNS name 

    client.connect(hostname=hostname, username="ubuntu", pkey=key)

    # Execute a command(cmd) after connecting/ssh to an instance

    cmds = ["sudo apt update",  
            "sudo apt install -y apt-transport-https ca-certificates curl software-properties-common",
            "curl -fsSL https:\/\/download.docker.com\/linux/ubuntu/gpg | sudo apt-key add -",  
            "sudo add-apt-repository \"deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable\"",  
            "sudo apt update",  
            "apt-cache policy docker-ce",  
            "sudo apt install -y docker-ce", 
            "sudo docker run -d -p 8000:8000 danielcchen\/ec2_django"]

    for cmd in cmds:
        print(cmd) 
        stdin,stdout,stderr=client.exec_command(cmd)
        outlines=stdout.readlines()
        result=''.join(outlines)
        print (result)        

    client.close()


except Exception as e:

    print(e)

print(hostname)
print("ssh -i ec2-keypair.pem ubuntu@{}".format(hostname))
print("Please use this address to access the website http://{}:8000".format(hostname))


