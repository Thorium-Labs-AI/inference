resource "aws_dynamodb_table" "document_chunks_table" {
  name           = "document_chunks"
  billing_mode   = "PROVISIONED"
  read_capacity  = "30"
  write_capacity = "30"
  attribute {
    name = "document_id" # a unique hash of customer id + document id
    type = "S"
  }
  attribute {
    name = "sequence_number" # ID of chunk inside a document
    type = "N"
  }
  hash_key  = "document_id"
  range_key = "sequence_number"
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

resource "aws_dynamodb_table" "customer_chatbots_table" {
  name           = "customer_chatbots"
  billing_mode   = "PROVISIONED"
  read_capacity  = "30"
  write_capacity = "30"

  attribute {
    name = "customer_id"
    type = "S"
  }
  attribute {
    name = "chatbot_id"
    type = "S"
  }
  attribute {
    name = "display_name"
    type = "S"
  }
  hash_key  = "customer_id"
  range_key = "chatbot_id"
}