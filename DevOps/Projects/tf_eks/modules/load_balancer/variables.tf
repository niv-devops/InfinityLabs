variable "security_group_id" {
  description = "Security group's ID associated with the load balancers"
  type        = string
}

variable "public_subnets" {
  description = "Public subnet's IDs associated with the load balancer"
  type        = list(string)
}

variable "private_subnets" {
  description = "Private subnet's IDs associated with the load balancer"
  type        = list(string)
}
