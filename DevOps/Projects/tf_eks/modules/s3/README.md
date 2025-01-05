# S3 Module

This module creates an Amazon S3 bucket to use with Amazon DynamoDB for Terraform's state locking feature.

## Inputs

| Name          | Description       | Type   | Default |
|---------------|-------------------|--------|---------|
| `bucket_name` | S3 bucket's name  | string | ""      |

## Outputs

| Name          | Description              |
|---------------|--------------------------|
| `bucket_name` | Created S3 bucket's name |

## Usage

Include this module in your Terraform configuration and modify `terraform.tfvars` in root dir:

```hcl
module "s3" {
  source      = "./modules/s3"
  bucket_name = "S3-bucket-name"
}
```