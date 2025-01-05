# NAT Gateway Module

This module creates a NAT Gateway in a specified public subnet and associates it with an Elastic IP, to enable outbound internet traffic for resources in private subnets.

## Inputs

| Variable           | Description                                        | Type     | Default         |
|--------------------|----------------------------------------------------|----------|-----------------|
| `public_subnet_id` | Public subnet's ID to deploy the NAT Gateway       | `string` | `""`            |
| `eip_name`         | Elastic IP's name associated with the NAT Gateway  | `string` | `"eip_nat_gtw"` |
| `nat_name`         | NAT Gateway's name tag                             | `string` | `"nat_gtw"`     |

## Outputs

| Output              | Description                                     |
|---------------------|-------------------------------------------------|
| `nat_gateway_id`    | Created NAT Gateway's ID                        |
| `eip_id`            | Elastic IP's ID associated with the NAT Gateway |

## Usage

Include this module in your Terraform configuration and modify `eip_name` and `nat_name` vars in `variables.tf`:

```hcl
variable "eip_name" {
  description = "Elastic IP's name tag associated with the NAT Gateway"
  type        = string
  default     = "eip_nat_gtw"
}

variable "nat_name" {
  description = "NAT Gateway's name tag"
  type        = string
  default     = "nat_gtw"
}
}
```
