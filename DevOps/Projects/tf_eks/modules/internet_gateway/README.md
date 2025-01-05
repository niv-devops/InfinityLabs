# Internet Gateway Module

This module creates an Internet Gateway and attaches it to the VPC, to provide internet access for its resources.

## Inputs

| Variable   | Description                              | Type     | Default     |
|------------|------------------------------------------|----------|-------------|
| `vpc_id`   | VPC's ID to attach the Internet Gateway  | `string` | `""`        |
| `igw_name` | The name tag for the Internet Gateway    | `string` | `"eks-igw"` |

## Outputs

| Output                 | Description                        |
|------------------------|------------------------------------|
| `internet_gateway_id`  | ID of the created Internet Gateway |

## Usage

Include this module in your Terraform configuration and modify `igw_name` var in `variables.tf`:

```hcl
variable "igw_name" {
  description = "Name tag for the Internet Gateway"
  type        = string
  default     = "eks_igw"
}
```
