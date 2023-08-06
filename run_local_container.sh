#!/bin/bash

set -e

# Convert the environment variables in .env to --build-arg options
BUILD_ARGS=$(awk -F= '{print "--build-arg " $1 "=" $2}' .env)

docker build $BUILD_ARGS -t chat_server .


docker stop redis || true
docker rm redis || true
docker run --name redis --network asterisk-backend -d redis

docker stop chat_server_container || true
docker rm chat_server_container || true
docker run -d --name chat_server_container -p 8000:80 --network asterisk-backend chat_server

docker stop dynamodb || true
docker rm dynamodb || true
docker run --name dynamodb --network asterisk-backend -p 8888:8000 -d amazon/dynamodb-local

docker stop localstack || true
docker rm localstack || true
docker run --name localstack -p 4566:4566 \
  -e SERVICES=s3,lambda,dynamodb,sqs \
  -e DEFAULT_REGION=us-east-1 -e \
  EDGE_PORT=4566 \
  -d localstack/localstack


# Create the document_chunks_table
aws dynamodb create-table \
    --endpoint-url http://localhost:4566 \
    --table-name document_chunks \
    --attribute-definitions \
        AttributeName=documentID,AttributeType=S \
        AttributeName=chunkID,AttributeType=S \
    --key-schema AttributeName=documentID,KeyType=HASH AttributeName=chunkID,KeyType=RANGE \
    --provisioned-throughput ReadCapacityUnits=30,WriteCapacityUnits=30 \
    --billing-mode PROVISIONED > /dev/null


# Create the customer_documents_table
aws dynamodb create-table \
    --endpoint-url http://localhost:4566 \
    --table-name customer_documents \
    --attribute-definitions \
        AttributeName=customerID,AttributeType=S \
        AttributeName=documentID,AttributeType=S \
    --key-schema AttributeName=customerID,KeyType=HASH AttributeName=documentID,KeyType=RANGE \
    --provisioned-throughput ReadCapacityUnits=30,WriteCapacityUnits=30 \
    --billing-mode PROVISIONED > /dev/null

# Create the configuration table
aws dynamodb create-table \
    --endpoint-url http://localhost:4566 \
    --table-name configuration \
    --attribute-definitions \
        AttributeName=customerID,AttributeType=S \
        AttributeName=chatbotID,AttributeType=S \
    --key-schema AttributeName=customerID,KeyType=HASH AttributeName=chatbotID,KeyType=RANGE \
    --provisioned-throughput ReadCapacityUnits=30,WriteCapacityUnits=30 \
    --billing-mode PROVISIONED > /dev/null