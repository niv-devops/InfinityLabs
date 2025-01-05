output "public_lb_dns_name" {
  description = "Public load balancer's DNS name"
  value       = aws_lb.public_lb.dns_name
}

output "internal_lb_dns_name" {
  description = "Internal load balancer's DNS name"
  value       = aws_lb.internal_lb.dns_name
}
