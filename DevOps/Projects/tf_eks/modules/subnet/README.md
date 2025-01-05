# Subnet Module

This module creates public and private subnets within a specified VPC, To define network segments for different availability zones.

## Inputs

| Variable               | Description                              | Type            | Default                                   |
|------------------------|------------------------------------------|-----------------|-------------------------------------------|
| `vpc_id`               | VPC's ID in which to create subnets      | `string`        | `""`                                      |
| `availability_zones`   | List of availability zones               | `list(string)`  | `["eu-central-1a", "eu-central-1b"]`      |
| `private_cidr_blocks`  | List of CIDR blocks for public subnets   | `list(string)`  | `["192.168.0.0/19", "192.168.32.0/19"]`   |
| `public_cidr_blocks`   | List of CIDR blocks for private subnets  | `list(string)`  | `["192.168.64.0/19", "192.168.96.0/19"]`  |

## Outputs

| Output                     | Description                            |
|----------------------------|----------------------------------------|
| `public_subnet_ids`        | The IDs of the created public subnets  |
| `private_subnet_ids`       | The IDs of the created private subnets |

## Usage

Include this module in your Terraform configuration and modify `terraform.tfvars`:

```hcl
availability_zones = ["eu-central-1a", "eu-central-1b"]

private_cidr_blocks = [
  "192.168.0.0/19",
  "192.168.32.0/19"
]

public_cidr_blocks = [
  "192.168.64.0/19",
  "192.168.96.0/19"
]
```
