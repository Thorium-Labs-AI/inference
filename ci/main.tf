provider aws {
  region  = var.region
  profile = var.profile
}

terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
    }
  }

  cloud {
    organization = "AsteriskChat"

    workspaces {
      name = "chat-server"
    }
  }
  required_version = ">= 1.1.0"
}