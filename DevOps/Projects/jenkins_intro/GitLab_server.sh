# Setting up a GitLab server on an Amazon EC2 instance:
ssh -i "gitlab key.pem" ubuntu@ec-public-ip.eu-central-1.compute.amazonaws.com
sudo apt update && sudo apt upgrade -y
sudo apt install -y curl openssh-server ca-certificates tzdata perl
curl https://packages.gitlab.com/install/repositories/gitlab/gitlab-ce/script.deb.sh | sudo bash

sudo EXTERNAL_URL="http://<ec2-public-ip>" apt-get install gitlab-ce
sudo nano /etc/gitlab/gitlab.rb   -->   external_url 'http://<ec2-public-ip>'
sudo gitlab-ctl reconfigure

# Open URL: http://<ec2-public-ip>
# user: root     password: /etc/gitlab/init_pass

# Generate SSH Key:pair and add it to GitLab account (User Settings --> SSH Keys)
ssh-keygen

# Config local repo
git remote add <remote-name> git@<ec2-public-ip>:username/projectname.git
git remote -v
git push -u <remote-name> <branch-name>

access token: glpat-47G6fSHhbZZsfMvyEPR8
glpat-zCduXXxdb1Fnz4s4LmZB
https://goofy.servebeer.com

##################################################################################################

# Setting up a GitLab server on an EC2 instance using a Docker image
ssh -i /path/to/your-key-pair.pem ubuntu@<ec2-public-ip>
sudo apt update && sudo apt upgrade -y
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker (ubuntu)
sudo systemctl start docker
sudo systemctl enable docker
sudo mkdir -p /srv/gitlab/config /srv/gitlab/logs /srv/gitlab/data

# Pull gitlab repo
sudo docker run --detach \
  --hostname 54.93.195.23 \
  --publish 443:443 --publish 80:80 --publish 2424:22 \
  --name gitlab \
  --restart always \
  --volume /srv/gitlab/config:/etc/gitlab \
  --volume /srv/gitlab/logs:/var/log/gitlab \
  --volume /srv/gitlab/data:/var/opt/gitlab \
  gitlab/gitlab-ce:latest
  
  
services:
  gitlab:
    image: gitlab/gitlab-ce:latest
    container_name: gitlab
    restart: always
    hostname: 'goofy.servebeer.com' / '3.122.61.221'
    environment:
      GITLAB_OMNIBUS_CONFIG: |
        external_url 'https://goofy.servebeer.com' / '3.122.61.221'
    ports:
      - '80:80'
      - '443:443'
      - '2424:22'
    volumes:
      - '/srv/gitlab/config:/etc/gitlab'
      - '/srv/gitlab/logs:/var/log/gitlab'
      - '/srv/gitlab/data:/var/opt/gitlab'
    shm_size: '256m'


# Open URL: http://<ec2-public-ip>
goofy.servebeer.com


##################################################################################################


create a new user
1. Click on your profile picture in the top-right corner and select "Admin Area."
2. In the Admin Area, navigate to "Users."
3. Click on the "Invite user" button(Enter the user’s email address, name, role, specific group or project they should be added to.
4. Click "Invite" to send the invitation.
5. Go to the project’s page on your GitLab instance.
6. Click on "Settings" in the left sidebar and select "Members" or "Access".
   - Click on the "Invite member" button.
   - Enter the user’s email address (if they’re not already part of the project) or username.
   - Choose the appropriate role for the user. Here are common roles and their permissions:
     - **Guest:** Can view the project and create issues.
     - **Reporter:** Can view and pull code, create issues and leave comments.
     - **Developer:** Can push code, merge requests, and manage their own branches.
     - **Maintainer:** Can manage the project, including adding/removing members and merging code.
     - **Owner:** Full control over the project (usually reserved for project admins or owners).
Click "Invite" or "Add to project" to confirm.**

Ensure that the user has the necessary access by:
Go to the "Members" page in your project settings to verify the user’s role and access level.
Ask the user to log in and verify that they can access the project and perform the tasks you’ve assigned to them.



##################################################################################################


Upload a project to GitLab server according to GitLab flow

git checkout -b main
git checkout -b develop

git add .
git commit -m "Initializing branches"
git push -u origin main
git push -u origin develop
git push origin feature/new-feature_name

change branch: git checkout main

1. Create a Merge Request --> Go to the "Merge Requests" section
2. Click on the "New merge request" button
3. Select your feature branch as the source branch and `main` as the target branch.
4. Provide a title and description for the merge request.
5. Click "Create merge request."
6. Approve merge request.

# Create .gitlab-ci.yml file on root branch:

stages:
  - build
  - test
  - deploy

build:
  stage: build
  script:
    - echo "Building the project..."

test:
  stage: test
  script:
    - echo "Running tests..."

deploy:
  stage: deploy
  script:
    - echo "Deploying the application..."

# Commit and push changes:
git add .
git commit -m "Add CI/CD configuration"
git push origin main

# Monitor pipeline status under the "CI/CD" section of the project.


#######################################################################################################################################


# Adding a new feature to weather webapp:
git checkout -b feature/new-feature_name

# Update webapp with new feature, commit and push:
git add .
git commit -m "new feature description"
git push origin feature/new-feature_name

# Create a Merge Request
# Deploy Changes with CI/CD pipeline

ssh
cd /path/to/your/weather-web-app
git pull origin main
sudo systemctl restart gunicorn
sudo systemctl restart nginx
