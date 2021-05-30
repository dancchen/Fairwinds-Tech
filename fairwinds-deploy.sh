#!/bin/bash 

# Install prerequisite for running Python script

sudo apt install -y git python3-pip

pip install awscli boto3

# Set up AWS access

[ ! -d ~/.aws ] && mkdir ~/.aws

export PATH=~/.local/bin:$PATH 

echo "[default]" > ~/.aws/config 

echo "output = json" >> ~/.aws/config
echo "region =" $(cat cred|grep -i region|awk -F: '{print $2}') >> ~/.aws/config

echo "[default]" > ~/.aws/credentials

echo "aws_secret_access_key =" $(cat cred|grep SecretAccessKey|awk -F: '{print $2}'|grep -o '".*"'|sed 's/"//g') >> ~/.aws/credentials

echo "aws_access_key_id =" $(cat cred|grep AccessKeyId|awk -F: '{print $2}'|grep -o '".*"'|sed 's/"//g') >> ~/.aws/credentials

chmod 600 ~/.aws/credentials ~/.aws/config

python3 ~/fairwinds-tech/deployEC2.py
