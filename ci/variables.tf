variable "AWS_SECRET_ACCESS_KEY" {

}

variable "project_name" {
  default = "chat-server"
}

variable "region" {
  default = "us-east-1"
}

variable "ecr_image" {
  default = "invalid_image"
}

variable "desired_count" {
  default = 1
}
