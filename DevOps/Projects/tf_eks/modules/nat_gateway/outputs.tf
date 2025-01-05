output "nat_gateway_id" {
  description = "Created NAT Gateway's ID"
  value       = aws_nat_gateway.nat_gtw.id
}

output "eip_id" {
  description = "Elastic IP's ID associated with the NAT Gateway"
  value       = aws_eip.eip_nat_gtw.id
}

