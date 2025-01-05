output "public_route_table_id" {
  description = "Public routing table's ID"
  value       = aws_route_table.public.id
}

output "private_route_table_id" {
  description = "Private routing table's ID"
  value       = aws_route_table.private.id
}
