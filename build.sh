#!/bin/bash

PYTHON_BIN=".venv/bin/python"

if [ ! -d ".venv" ]; then
  python3 -m venv .venv
fi

echo "Upgrading pip..."
"$PYTHON_BIN" -m pip install --upgrade pip setuptools

echo "Building the project..."
"$PYTHON_BIN" -m pip install -r requirements.txt

echo "Make Migration..."
"$PYTHON_BIN" manage.py makemigrations --noinput
"$PYTHON_BIN" manage.py migrate --noinput

echo "Collect Static files.."
"$PYTHON_BIN" manage.py collectstatic --noinput --clear
