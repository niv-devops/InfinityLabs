resource "aws_lb" "public_lb" {
  name               = "public-lb"
  internal           = false
  load_balancer_type = "application"
  security_groups    = [var.security_group_id]
  subnets            = var.public_subnets

  enable_deletion_protection = false

  tags = {
    Name = "public-lb"
  }
}

resource "aws_lb" "internal_lb" {
  name               = "internal-lb"
  internal           = true
  load_balancer_type = "application"
  security_groups    = [var.security_group_id]
  subnets            = var.private_subnets

  enable_deletion_protection = false

  tags = {
    Name = "internal-lb"
  }
}
