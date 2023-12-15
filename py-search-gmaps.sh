#!/bin/bash

INTERNET_CHECK_URL="http://www.google.com"
VENV_FOLDER="venv"
MAIN_SCRIPT="main.py"
REQUIREMENTS_FILE="requirements.txt"

# Check for the operating system
if [[ "$OSTYPE" == "linux-gnu" ]]; then
    OS="Linux"
elif [[ "$OSTYPE" == "darwin"* ]]; then
    OS="macOS"
elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    OS="Windows"
else
    OS="Unknown"
fi

echo "Operating System: $OS"

# Check if Python 3 is installed
if command -v python3 &> /dev/null; then
    echo "Python 3 is installed"
else
    echo "Python 3 is not installed. Please install Python 3."
    exit 1
fi

# Check for an internet connection
if curl --output /dev/null --silent --head --fail "$INTERNET_CHECK_URL"; then
    echo "Internet connection detected"
else
    echo "No internet connection. Please connect to the internet."
    exit 1
fi

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
