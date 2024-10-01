terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.65.0"
    }
  }
  
  backend "s3" {
    bucket         = "tf-state-goofy"
    key            = "state/terrastate.tfstate"
    region         = "eu-central-1"
    dynamodb_table = "tf-state-lock"
    encrypt        = true
  }

  required_version = ">= 1.9.5"
}

provider "aws" {
  region = "eu-central-1"
}

data "http" "my_ip" {
  url = "http://checkip.amazonaws.com/"
}

module "goofy" {
  source = "./module"
}

resource "aws_instance" "labmate" {
  ami                    = "ami-0e04bcbe83a83792e"
  instance_type          = "t2.micro"
  key_name               = "k8s"
  vpc_security_group_ids = [module.goofy.sg_id]

  tags = {
    Name = var.instance_name
  }
}
