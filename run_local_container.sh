#!/bin/bash

# Convert the environment variables in .env to --build-arg options
BUILD_ARGS=$(awk -F= '{print "--build-arg " $1 "=" $2}' .env)

docker build $BUILD_ARGS -t chat_server .

docker stop chat_server_container
docker rm chat_server_container
docker run -d --name chat_server_container -p 8000:80 chat_server


