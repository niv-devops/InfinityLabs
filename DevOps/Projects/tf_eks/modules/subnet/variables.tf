variable "availability_zones" {
  description = "Availability Zones list"
  type        = list(string)
}

variable "public_cidr_blocks" {
  description = "Public subnets CIDR blocks"
  type        = list(string)
}

variable "private_cidr_blocks" {
  description = "Private subnets CIDR blocks"
  type        = list(string)
}
