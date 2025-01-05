resource "aws_dynamodb_table" "eks_api_table" {
  name         = var.table_name
  billing_mode = "PAY_PER_REQUEST"

  attribute {
    name = "id"
    type = "S"
  }

  hash_key = "id"

  tags = {
    Name = var.table_name
  }
}
