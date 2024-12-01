#!/bin/bash

# Script to set up the environment for the project
ENV_NAME="grapher"

# Check if the environment folder exists
if [ ! -d "$ENV_NAME" ]; then
    echo "Creating virtual environment: $ENV_NAME"
    python3 -m venv $ENV_NAME
else
    echo "Virtual environment $ENV_NAME already exists."
fi

# Activate the environment
echo "Activating virtual environment..."
source $ENV_NAME/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Setup complete. To activate the environment, run:"
echo "source $ENV_NAME/bin/activate"
