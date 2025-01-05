## "Hello World" Simple REST API

This repo contains a simple REST API written in python using flask, which can also be deployed to docker containers.
Based on - https://github.com/alankrantas/hello-world-rest-apis/tree/main/python_api

## "Hello World" REST API Deployment with Terraform on EKS

This project deploys a simple "Hello World" REST API using Python on an Amazon EKS (Elastic Kubernetes Service) cluster through Terraform.

## Structure

The cluster alongside its AWS components are organized into several Terraform modules to build the whole infrastructure:

- **VPC Module**: Creates a Virtual Private Cloud (VPC) for isolating resources.
- **Subnet Module**: Configures subnets for the VPC.
- **Routing Table Module**: Sets up routing tables for directing traffic.
- **Internet Gateway Module**: Provides internet access to the VPC.
- **NAT Gateway Module**: Enables instances in a private subnet to initiate outbound traffic to the internet.
- **Load Balancer Module**: Configures an application load balancer to distribute traffic to the API.
- **EKS Cluster Module**: Deploys an EKS cluster for running containerized applications.
- **State Locking**: Configures S3 backend using DynamoDB as a locking mechanism for Terraform's state locking features.

## Prerequisites

- Terraform installed on your local machine
- AWS CLI configured with appropriate permissions
- kubectl installed for managing the EKS cluster

## Getting Started

1. Partial clone for Python REST API repository:
   ```bash
   git clone --filter=blob:none --no-checkout https://github.com/alankrantas/hello-world-rest-apis.git
   cd hello-world-rest-apis
   git sparse-checkout init --cone
   git sparse-checkout set python_api
   git checkout
   ```

2. Navigate to each module directory and configure `variables.tf` or `terraform.tfvars` files. Follow the instructions in the individual module READMEs for specific configurations and outputs.

3. For more configurations, refer to [Terraform's AWS Provider documentation](https://registry.terraform.io/providers/hashicorp/aws/latest/docs).

4. Test your configurations, refer to `Tests` section.

5. Initialize and apply the Terraform configuration:
   ```bash
   terraform init
   terraform apply
   ```

## Tests

1. Run `terraform validate` to check whether the configuration is syntactically valid and internally consistent.

2. Run `terraform plan` to see what changes will be made to your infrastructure without actually applying them.

3. Integrate testing with Terraform using tools like `Terratest` to write tests that apply your Terraform code and then verify the infrastructure it creates.

## Usage

Once the deployment is complete, you can access the REST API through the Load Balancer URL provided in the output.

## Cleanup

To destroy the resources created, run `terraform destroy`.
