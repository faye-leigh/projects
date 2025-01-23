#!/bin/bash

# Install Python if not already installed
if ! command -v python3 &> /dev/null
then
    echo "Python3 could not be found, installing..."
    sudo apt update
    sudo apt install -y python3
fi

# Install pip if not already installed
if ! command -v pip3 &> /dev/null
then
    echo "pip3 could not be found, installing..."
    sudo apt update
    sudo apt install -y python3-pip
fi

# Install necessary Python libraries
REQUIRED_PKG=("pandas" "tkcalendar" "tkinter" "matplotlib")
for PKG in "${REQUIRED_PKG[@]}"; do
    if ! python3 -c "import $PKG" &> /dev/null; then
        echo "$PKG is not installed, installing..."
        pip3 install $PKG
    fi
done

# Ensure the script is run from the correct directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR/src"

# Run the Python script
python3 finances.py