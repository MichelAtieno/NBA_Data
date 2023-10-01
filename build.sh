#!/usr/bin/env bash
# exit on error
set -o errexit


python3.10 manage.py collectstatic --no-input