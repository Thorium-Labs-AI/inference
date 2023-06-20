#!/bin/bash

source .env

curl --request POST \
  --url https://asteriskchat.us.auth0.com/oauth/token \
  --header 'content-type: application/json' \
  --data "{\"client_id\":\"${AUTH0_CLIENT_ID}\",\"client_secret\":\"${AUTH0_CLIENT_SECRET}\",\"audience\":\"asterisk-chat-server\",\"grant_type\":\"client_credentials\"}"
