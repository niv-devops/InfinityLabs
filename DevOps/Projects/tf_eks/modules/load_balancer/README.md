# Load Balancer Module

This module creates public and internal Application Load Balancers (ALB) to distribute incoming traffic to the REST API running on EKS.

## Features

- Creates a public Application Load Balancer for internet-facing applications.
- Creates an internal Application Load Balancer for private applications.
- Configurable security groups for access control.
- Outputs the DNS names of both load balancers.

### Inputs

| Name                | Description                                             | Type             | Default  |
|---------------------|---------------------------------------------------------|------------------|----------|
| `security_group_id` | Security group's ID associated with the load balancers  | `string`         | `null`   |
| `public_subnets`    | Public subnet IDs for the load balancer                 | `list(string)`   | `[]`     |
| `private_subnets`   | Private subnet IDs for the internal load balancer       | `list(string)`   | `[]`     |

### Outputs

| Name                   | Description                       |
|------------------------|-----------------------------------|
| `public_lb_dns_name`   | Public load balancer's DNS name   |
| `internal_lb_dns_name` | Internal load balancer's DNS name |

## Usage

Include this module in your Terraform configuration and modify SG in `terraform.tfvars`:

```hcl
security_group_id = "sg-#################"
```
