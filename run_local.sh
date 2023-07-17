#! /bin/bash

set -e

uvicorn src.server.app:app --host 0.0.0.0 --port 8000 --reload