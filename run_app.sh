#!/bin/bash

# Define venv directory
VENV_DIR="venv"

# Create virtual environment if it doesn't exist
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment..."
    python3 -m venv "$VENV_DIR"
fi

# Activate virtual environment
source "$VENV_DIR/bin/activate"

# Install requirements
echo "Installing dependencies..."
pip install -r requirements.txt

# Run the app
echo "Starting AutoNB..."
python app.py