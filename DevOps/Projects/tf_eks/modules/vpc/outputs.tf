output "vpc_id" {
  description = "VPC's ID"
  value       = aws_vpc.eks_vpc.id
}
