#!/bin/bash

# Export Terraform outputs to a file
terraform output -json > terraform_outputs.json

# Generate Ansible inventory file
./generate_inventory.sh

# Run the Ansible playbook
ansible-playbook -i inventory.yml cluster.yml --limit k8s_cluster