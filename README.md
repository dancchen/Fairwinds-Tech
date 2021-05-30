# Fairwinds-Tech

Overview:

The fairwinds-deploy.sh is a simple bash script to setup AWS credentials and kickoff deployEC2.py script to initiate an AWS deployment.  The deployEC2.py will deploy EC2 instance and install docker to prepare ec2_django container run on the EC2 instance.  It will download an image from DockerHub called "danielcchen/ec2_django".  The address to connect to the django web server will be provided when the script exits.

Assumptions: 

1. Django is the web application framework for this deployment.

2. The final deployment is not production ready.  Django is running in DEBUG mode and it has a light weight web server for testing and deveopment purpose.  ALLOWED_HOSTS = ['*'] is configured for easy testing also. 

3.  EC2 uses AMI "Ubuntu Server 20.04 LTS (HVM), SSD Volume Type"   

4.  It is assumed that the user starts the command from a Ubunto Desktop.  

5.  Deployment is assumed to be in the AWS us-west-1 region. The region, AMI and Security Group of the EC2 instance won't change and is hard coded in the Python/Configuration Management script. 


Deployment Steps:

0. mkdir fairwinds-tech and git clone from github.

1. Copy the credential file to ~/fairwinds-tech and name it as file "cred". 

2. (optional) Run ~/fairwinds-tech/cleanup.sh to clean up.

3. Run ~/fairwinds-tech/fairwinds-deploy.sh Bash script.  This will setup AWS credentials to prepare the execution of deployEC2.py at the end.   


Future Improvement:

It is assumed keypair needs to be created each time the script is started. The deployEC2.py should check if the keypair exists and create keypair if it doesn't exist. 

For production ready deployment, Nginx or Apache can be deployed as web server.


Reason to pick Django:

It's a robust and popular web framework and easy to deploy.  It's highly compatible with popular OS and databases.  It's easy to extend and scale.  For Development purpose, it has light weight web server for testing purpose.
