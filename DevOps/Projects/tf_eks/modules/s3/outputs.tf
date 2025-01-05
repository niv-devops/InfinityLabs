output "bucket_name" {
  value       = aws_s3_bucket.eks_api_bucket.id
  description = "S3 bucket's name for EKS API"
}
