resource "aws_eip" "eip_nat_gtw" {
  vpc = true

  tags = {
    Name = var.eip_name
  }
}

resource "aws_nat_gateway" "nat_gtw" {
  allocation_id = aws_eip.eip_nat_gtw.id
  subnet_id     = var.public_subnet_id

  tags = {
    Name = var.nat_name
  }

  depends_on = [aws_internet_gateway.eks_igw]
}

