variable "vpc_id" {
  description = "VPC's ID to associate routing tables"
  type        = string
}

variable "private_subnet_id_a" {
  description = "First private subnet's ID"
  type        = string
}

variable "private_subnet_id_b" {
  description = "Second private subnet's ID"
  type        = string
}

variable "public_subnet_id_a" {
  description = "First public subnet's ID"
  type        = string
}

variable "public_subnet_id_b" {
  description = "Second public subnet's ID"
  type        = string
}

variable "public_route_table_name" {
  description = "Public routing table's name tag"
  type        = string
  default     = "public_route_table"
}

variable "private_route_table_name" {
  description = "Private routing table's name tag"
  type        = string
  default     = "private_route_table"
}

