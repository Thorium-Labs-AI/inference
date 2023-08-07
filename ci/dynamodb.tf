resource "aws_dynamodb_table" "document_chunks_table" {
  name           = "document_chunks"
  billing_mode   = "PROVISIONED"
  read_capacity  = "30"
  write_capacity = "30"
  attribute {
    name = "documentID" # a unique hash of customer id + document id
    type = "S"
  }
  attribute {
    name = "chunkID" # ID of chunk inside a document
    type = "N"
  }
  hash_key  = "documentID"
  range_key = "chunkID"
}

resource "aws_dynamodb_table" "customer_documents_table" {
  name           = "customer_documents"
  billing_mode   = "PROVISIONED"
  read_capacity  = "30"
  write_capacity = "30"

  attribute {
    name = "customerID"
    type = "S"
  }
  attribute {
    name = "documentID"
    type = "S"
  }
  attribute {
    name = "title"
    type = "S"
  }
  attribute {
    name = "description"
    type = "S"
  }
  hash_key  = "customerID"
  range_key = "documentID"
}

resource "aws_dynamodb_table" "configuration_table" {
  name           = "configuration"
  billing_mode   = "PROVISIONED"
  read_capacity  = "30"
  write_capacity = "30"

  attribute {
    name = "customerID"
    type = "S"
  }
  attribute {
    name = "chatbotID"
    type = "S"
  }
  hash_key  = "customerID"
  range_key = "chatbotID"
}