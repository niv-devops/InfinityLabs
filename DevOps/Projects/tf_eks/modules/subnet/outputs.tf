output "public_subnet_id" {
  description = "Public subnets IDs"
  value       = aws_subnet.public[*].id
}

output "private_subnet_id" {
  description = "Private subnets IDs"
  value       = aws_subnet.private[*].id
}
