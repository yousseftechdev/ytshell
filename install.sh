#!/bin/bash

configDir="$HOME/.config/ytshell/"
modules="pyautogui termcolor"
shellScript="ytshell"
pyScripts="main.py funcs.py"

# Check if Python is installed
if ! command -v python3 &>/dev/null; then
    echo "Python is not installed. Please install Python and try again."
    exit 1
fi

# Install required Python modules
pip3 install $modules

# Create the ytshell config directory
mkdir -p "$configDir"

# Copy the Python files to the ytshell directory
cp $pyScripts "$configDir"

# Copy the ytshell script to the /bin directory
sudo cp $shellScript /bin/

# Make the ytshell script executable
sudo chmod +x /bin/$shellScript

# Add ytshell to /etc/shells
if ! grep -Fxq "/bin/$shellScript" /etc/shells; then
    echo "/bin/$shellScript" | sudo tee -a /etc/shells
fi

# Change the default shell to ytshell
chsh -s /bin/$shellScript

echo "YTShell has been installed and set as the default shell."