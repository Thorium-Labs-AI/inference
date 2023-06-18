#!/bin/bash

# Convert the environment variables in build_args.env to --build-arg options
BUILD_ARGS=$(awk -F= '{print "--build-arg " $1 "=" $2}' build_args.env)

# Docker build command with build arguments
docker build $BUILD_ARGS -t chat_server .

# Docker run command
docker run -d -p 8000:8000 chat_server

