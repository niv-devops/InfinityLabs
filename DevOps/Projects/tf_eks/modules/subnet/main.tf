resource "aws_subnet" "private_subnet" {
  count                  = 2
  vpc_id                 = aws_vpc.eks_vpc.id
  cidr_block             = element(var.private_cidr_blocks, count.index)
  availability_zone      = element(var.availability_zones, count.index)

  tags = {
    Name                              = "private_${element(var.availability_zones, count.index)}"
    "kubernetes.io/role/internal-elb" = "1"
    "kubernetes.io/cluster/eks_cluster" = "owned"
  }
}

resource "aws_subnet" "public_subnet" {
  count                  = 2
  vpc_id                 = aws_vpc.eks_vpc.id
  cidr_block             = element(var.public_cidr_blocks, count.index)
  availability_zone      = element(var.availability_zones, count.index)
  map_public_ip_on_launch = true

  tags = {
    Name                             = "public_${element(var.availability_zones, count.index)}"
    "kubernetes.io/role/elb"        = "1"
    "kubernetes.io/cluster/eks_cluster" = "owned"
  }
}
