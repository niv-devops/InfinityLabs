variable "vpc_id" {
  description = "VPC's ID to attach the Internet Gateway"
  type        = string
}

variable "igw_name" {
  description = "Name tag for the Internet Gateway"
  type        = string
  default     = "eks_igw"
}

