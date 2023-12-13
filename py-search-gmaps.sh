#!/bin/bash

VENV_FOLDER="venv"
MAIN_SCRIPT="main.py"
REQUIREMENTS_FILE="requirements.txt"

# Check if venv folder exists
if [ ! -d "$VENV_FOLDER" ]; then
    # If not, create a virtual environment
    python3 -m venv $VENV_FOLDER
fi

# Activate virtual environment
source $VENV_FOLDER/bin/activate

# Install dependencies if needed
if [ -f "$REQUIREMENTS_FILE" ]; then
    # If requirements.txt exists, install dependencies
    pip install -r $REQUIREMENTS_FILE
fi

# Run main.py
python $MAIN_SCRIPT

# Deactivate virtual environment after running main.py
deactivate
