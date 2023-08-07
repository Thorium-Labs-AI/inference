#!/bin/bash

set -e

# Convert the environment variables in .env to --build-arg options
BUILD_ARGS=$(awk -F= '{print "--build-arg " $1 "=" $2}' .env)

docker build $BUILD_ARGS -t chat_server .

docker stop chat_server_container || true
docker rm chat_server_container || true
docker run -d --name chat_server_container -p 8000:80 --network asterisk-backend chat_server