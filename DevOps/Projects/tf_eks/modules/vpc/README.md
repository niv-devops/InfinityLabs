# VPC Module

This module creates an Amazon Virtual Private Cloud (VPC) for secure and isolated environment to AWS resources.

## Inputs

| Name              | Description                  | Type      | Default             |
|-------------------|------------------------------|-----------|---------------------|
| `vpc_cidr`        | CIDR block for the VPC       | `string`  | `192.168.0.0/16`    |
| `tags`            | Tags to assign to the VPC    | `map`     | `Name = "eks_vpc"`  |

## Outputs

| Name           | Description                    |
|----------------|--------------------------------|
| `vpc_id`       | The ID of the created VPC      |
| `vpc_cidr`     | The CIDR block of the VPC      |

## Usage

Include this module in your Terraform configuration and modify `terraform.tfvars`:

```hcl
vpc_cidr_block = "192.168.0.0/16"

vpc_tags = {
  Name = "eks_vpc"
}
```
