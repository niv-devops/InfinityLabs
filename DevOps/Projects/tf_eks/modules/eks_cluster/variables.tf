variable "cluster_name" {
  description = "EKS cluster's name"
  type        = string
}

variable "subnet_ids" {
  description = "subnet IDs for EKS cluster nodes"
  type        = list(string)
  default     = []
}

variable "desired_capacity" {
  description = "Desired number of nodes in the node group"
  type        = number
  default     = 1
}

variable "max_capacity" {
  description = "Maximum number of nodes in the node group"
  type        = number
  default     = 3
}

variable "min_capacity" {
  description = "Minimum number of nodes in the node group"
  type        = number
  default     = 1
}
