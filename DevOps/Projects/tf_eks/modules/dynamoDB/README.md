# DynamoDB Module

This module creates an Amazon DynamoDB table to use with S3 for Terraform's state locking feature.

## Inputs

| Name        | Description             | Type   | Default |
|-------------|-------------------------|--------|---------|
| `table_name` | DynamoDB table's name  | string | ""      |

## Outputs

| Name         | Description                    |
|--------------|--------------------------------|
| `table_name` | Created DynamoDB table's name  |

## Usage

Include this module in your Terraform configuration and modify `terraform.tfvars` in root dir:

```hcl
module "dynamodb" {
  source      = "./modules/dynamodb"
  table_name  = "DynamoDB-table-name"
}
```