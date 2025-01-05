terraform {
  providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.73.0"
    }

    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "~> 2.33.0"
    }
  }
  
  backend "s3" {
    bucket         = "tasty-kfc-bucket"
    key            = "state/terraform.tfstate"
    region         = "eu-central-1"
    encrypt        = true
    dynamodb_table = "eks_tf_api"
  }
  required_version = ">= 1.3.0"
}

provider "aws" {
  region = var.aws_region
}

provider "kubernetes" {
  host                   = module.eks_cluster.cluster_endpoint
  cluster_ca_certificate = base64decode(module.eks.cluster_certificate_authority_data)
  exec {
    api_version = "client.authentication.k8s.io/v1beta1"
    command     = "aws"
    args        = ["eks", "get-token", "--cluster-name", local.cluster_name]
  }
}

module "vpc" {
  source      = "./vpc"
  cidr_block  = var.vpc_cidr
}

module "subnets" {
  source        = "./subnets"
  vpc_id       = module.vpc.id
  private_cidrs = var.private_subnet_cidrs
  public_cidrs  = var.public_subnet_cidrs
}

module "internet_gateway" {
  source  = "./internet_gateway"
  vpc_id  = module.vpc.id
}

module "nat_gateway" {
  source       = "./nat_gateway"
  vpc_id      = module.vpc.id
  public_subnet_ids = module.subnets.public_subnet_ids
}

module "routing_tables" {
  source           = "./routing_tables"
  vpc_id           = module.vpc.id
  public_subnet_ids = module.subnets.public_subnet_ids
  private_subnet_ids = module.subnets.private_subnet_ids
}

module "load_balancer" {
  source = "./load_balancers"
  vpc_id = module.vpc.id
}

module "eks_cluster" {
  source = "./eks_cluster"
  
  cluster_name    = var.cluster_name
  subnet_ids      = module.subnets.private_subnet_ids
  desired_capacity = var.desired_capacity
  max_capacity     = var.max_capacity
  min_capacity     = var.min_capacity
}

module "s3" {
  source      = "./modules/s3"
  bucket_name = var.s3_bucket_name
}

module "dynamodb" {
  source      = "./modules/dynamoDB"
  table_name  = var.dynamodb_table_name
}
