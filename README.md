# YTShell

YTShell is a modern and customizable shell inspired by [zsh](https://www.zsh.org/). Built entirely in Python, YTShell combines the flexibility of Python scripting with powerful features from tools like [zoxide](https://github.com/ajeetdsouza/zoxide). Whether you're a power user or just looking for a simpler shell experience, YTShell offers an easy-to-customize environment to suit your needs.

![YTShell Logo](https://chatgpt.com/api/content/file-xxkgco2OL4SiPuU4QxKUiNvL)

## Features

- **Inspired by Zsh**: YTShell takes inspiration from the powerful features and customization options of Zsh, offering a familiar experience with the added benefits of Python scripting.
- **Easy Customization**: Easily customize colors and add your own commands by editing simple configuration files.
- **Auto complete cd commands**: YTShell eases directory navigation by remembering the directories you've visited, so you can use the cd command and only type 1 word of the path you want to visit and it will take you there.
- **Python-Based**: YTShell is made entirely in Python, allowing for easy extension and modification.

## Installation

To install YTShell, follow these steps:

1. **Ensure Python is Installed**: Make sure Python 3 is installed on your system. You can check this by running:

    ```bash
    python3 --version
    ```

2. **Clone the repo**:
    ```bash
    git clone https://github.com/youssef-mostafa1534/YTShell
    ```

2. **Run the Install Script**: `cd` into the cloned repo and run the `install.sh` script:

    ```bash
    chmod +x install.sh
    ./install.sh
    ```

3. **Enjoy YTShell**: Once installed, YTShell will be set as your default shell. You can start using it immediately.

## Uninstallation

To remove YTShell from your system, follow these steps:

1. **Remove YTShell from /etc/shells**:

    ```bash
    sudo sed -i '/\/bin\/ytshell/d' /etc/shells
    ```

2. **Change Your Default Shell**: Switch back to your previous shell (e.g., bash or zsh):

    ```bash
    chsh -s /bin/bash
    ```

3. **Delete YTShell Files**: Remove the YTShell files from your system:

    ```bash
    rm -rf ~/.config/ytshell
    sudo rm /bin/ytshell
    ```

## Contributing

Contributions are welcome! If you have ideas for new features or improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
