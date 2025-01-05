output "cluster_name" {
  description = "EKS cluster's name"
  value       = aws_eks_cluster.eks_cluster.name
}

output "cluster_endpoint" {
  description = "EKS cluster's endpoint for control plane"
  value       = aws_eks_cluster.eks_cluster.endpoint
}

output "kubeconfig" {
  description = "Kubeconfig file for accessing the cluster"
  value       = aws_eks_cluster.eks_cluster.kubeconfig
}
