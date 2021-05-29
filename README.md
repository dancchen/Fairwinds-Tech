# Fairwinds-Tech

Assumptions: 

1. It was decided to use Django as web application framework. 

2. The final deployment is not production ready.  Django is running in DEBUG mode and it has a light weight web server for testing and deveopment purpose.  ALLOWED_HOSTS = ['*'] is configured for easy testing also. 

3.  AMI is "Ubuntu Server 20.04 LTS (HVM), SSD Volume Type"   

4.  It is assumed the client pc is running Ubunto Desktop 20.04.  

Deployment Steps:

1. Copy the credential file to ~/fairwinds-tech and name it as file "cred". 

2. (optional) Run ~/fairwinds-tech/cleanup.sh to clean up.

3. Run ~/fairwinds-tech/fairwinds-deploy.sh Bash script.  This will setup AWS credentials to prepare the execution of deployEC2.py Python script and run it at the end.   

deployEC2.py will deploy EC2 instance and install docker to prepare ec2_django container run on the EC2 instance.  It will download an image from DockerHub called "danielcchen/ec2_django".  The address to connect to the django container will be provided when script exit.

Future Improvement:

It is assume keypair needs to be created each time the script is started. The deployEC2.py should check if the keypair exist and then create keypair if required. 
