#!/bin/bash

# Define the Python script file
SCRIPT="main.py"

# Define the virtual environment directory
VENV_DIR="venv"

# Ensure the script is executable
chmod +x $SCRIPT

# Create a virtual environment if it doesn't exist
if [ ! -d "$VENV_DIR" ]; then
    python3 -m venv $VENV_DIR
    echo "Virtual environment created."
fi

# Activate the virtual environment
source $VENV_DIR/bin/activate

# Run the Python script
python3 $SCRIPT

# Deactivate the virtual environment
deactivate