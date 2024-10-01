output "sg_id" {
  description = "EC2 instance security group"
  value       = aws_security_group.tf_sg.id
}
