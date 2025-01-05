#!/bin/bash

# echo 8 | kubeContext 
# delete previous secret
kubectl delete secret -n argocd aws-eu-central-1-helm-ecr
# get ecr token
TOKEN=$(aws ecr get-login-password --region eu-central-1 | base64 | tr -d '[:space:]')
# create a new file out of the template file
cp ecr-credentials-template.yml ecr-new.yml
# create a new secret manifest file with the token
sed -i "s/<ECR-TOKEN>/$TOKEN/g" ecr-new.yml
# apply secret to the cluster
kubectl apply -f ecr-new.yml
# delete file
rm ecr-new.yml
