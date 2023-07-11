#!/usr/bin/env bash

set -euo pipefail

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt


# uvicorn main:app --port 5000 --reload --root-path /api/v1 &
uvicorn main:app --port 5000 --reload  &

nginx -c "$(pwd)/nginx.conf" 
