#!/bin/bash

# Check if Python is installed
if ! command -v python3 &>/dev/null; then
    echo "Python is not installed. Please install Python and try again."
    exit 1
fi

# Install required Python modules
pip3 install pyautogui termcolor numpy

# Create the ytshell config directory
mkdir -p ~/.config/ytshell

# Copy the Python files to the ytshell directory
cp main.py funcs.py ~/.config/ytshell/

# Copy the ytshell script to the /bin directory
sudo cp ytshell /bin/

# Make the ytshell script executable
sudo chmod +x /bin/ytshell

# Add ytshell to /etc/shells
if ! grep -Fxq "/bin/ytshell" /etc/shells; then
    echo "/bin/ytshell" | sudo tee -a /etc/shells
fi

# Change the default shell to ytshell
chsh -s /bin/ytshell

echo "YTShell has been installed and set as the default shell."
