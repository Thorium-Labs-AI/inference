variable "AWS_SECRET_ACCESS_KEY" {
  description = "The secret access key for AWS."
}

variable "project_name" {
  default = "chat-server"
}

variable "region" {
  default = "us-east-1"
}

variable "ecr_repository" {
  default = "883869506849.dkr.ecr.us-east-1.amazonaws.com/chat-server"
}

variable "ecr_image" {
  description = "The tag for the ECR image. Defaults to 'latest'."
  default     = "latest"
}

variable "desired_count" {
  default = 1
}
