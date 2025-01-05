# Routing Table Module

This module creates public and private routing tables and associates them with corresponding subnets, to control the routing of network traffic within the VPC.

## Inputs

| Variable                    | Description                                           | Type     | Default                 |
|-----------------------------|-------------------------------------------------------|----------|-------------------------|
| `vpc_id`                    | The ID of the VPC to which the route tables belong    | `string` | `""`                    |
| `public_subnet_id_a`        | The ID of the first public subnet                     | `string` | `""`                    |
| `public_subnet_id_b`        | The ID of the second public subnet                    | `string` | `""`                    |
| `private_subnet_id_a`       | The ID of the first private subnet                    | `string` | `""`                    |
| `private_subnet_id_b`       | The ID of the second private subnet                   | `string` | `""`                    |
| `public_route_table_name`   | The name tag for the public route table               | `string` | `"public_route_table"`  |
| `private_route_table_name`  | The name tag for the private route table              | `string` | `"private_route_table"` |

## Outputs

| Output                    | Description                        |
|---------------------------|------------------------------------|
| `public_route_table_id`   | The ID of the public route table   |
| `private_route_table_id`  | The ID of the private route table  |

## Usage

Include this module in your Terraform configuration and modify the public and private RT names in `variables.tf`:

```hcl
variable "public_route_table_name" {
  description = "The name tag for the public route table"
  type        = string
  default     = "public_route_table"
}

variable "private_route_table_name" {
  description = "The name tag for the private route table"
  type        = string
  default     = "private_route_table"
}
```
