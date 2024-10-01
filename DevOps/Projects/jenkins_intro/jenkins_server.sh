#!/bin/bash

# Connect to Ec2 Instance
cd InfinityLabs/DevOps/jenkins_project/
chmod 400 "goofy.pem"
ssh -i "goofy.pem" ubuntu@ec2-52-29-192-147.eu-central-1.compute.amazonaws.com

# Install Jenkins on Ubuntu: Long Term Support release
sudo apt update -y
sudo wget -O /usr/share/keyrings/jenkins-keyring.asc \
  https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key
echo "deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc]" \
  https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt-get update
sudo apt-get install jenkins

# Installation of Java
sudo apt install fontconfig openjdk-17-jre
sudo snap install openjdk
java -version

# Enable and start Jenkins
sudo systemctl enable jenkins
sudo systemctl start jenkins
sudo systemctl status jenkins

# Get password for initial admin configuration
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
