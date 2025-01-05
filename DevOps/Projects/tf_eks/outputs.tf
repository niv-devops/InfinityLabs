output "vpc_id" {
  description = "ID of the VPC"
  value       = module.vpc.id
}

output "cluster_name" {
  description = "The name of the EKS cluster"
  value       = module.eks_cluster.cluster_name
}

output "cluster_endpoint" {
  description = "The endpoint of the EKS cluster"
  value       = module.eks_cluster.cluster_endpoint
}
