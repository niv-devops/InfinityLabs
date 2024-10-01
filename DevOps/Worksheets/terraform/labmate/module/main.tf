data "http" "my_ip" {
  url = "http://checkip.amazonaws.com/"
}

locals {
  inbound_ports = [80, 443]
  my_ip = "${chomp(data.http.my_ip.response_body)}/32"
}

resource "aws_security_group" "tf_sg" {
  name        = "tf-sg"
  dynamic "ingress" {
    for_each = local.inbound_ports
     content {
       from_port   = ingress.value
       to_port     = ingress.value
       protocol    = "tcp"
       cidr_blocks = ["0.0.0.0/0"]
     }
  }

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = [local.my_ip]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
