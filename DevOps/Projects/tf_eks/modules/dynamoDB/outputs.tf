output "table_name" {
  value       = aws_dynamodb_table.eks_api_table.name
  description = "DynamoDB's table name for EKS API"
}
