# YTShell

YTShell is a modern and customizable shell inspired by [zsh](https://www.zsh.org/). Built entirely in Python, YTShell combines the flexibility of Python scripting with powerful features from tools like [zoxide](https://github.com/ajeetdsouza/zoxide). Whether you're a power user or just looking for a simpler shell experience, YTShell offers an easy-to-customize environment to suit your needs.

## Features

- **Inspired by Zsh**: YTShell takes inspiration from the powerful features and customization options of Zsh, offering a familiar experience with the added benefits of Python scripting.
- **Easy Customization**: Easily customize colors and add your own commands by editing simple configuration files.
- **Auto complete cd commands**: YTShell eases directory navigation by remembering the directories you've visited, so you can use the cd command and only type 1 word of the path you want to visit and it will take you there.
- **Python-Based**: YTShell is made entirely in Python, allowing for easy extension and modification.

### **Planned features**:
- Returning to previous commands using the up arrow key
- Going back while typing prompt using the left arror key
- Adding a "clear" shortcut (Ctrl+L)
- Adding more commands, by listening to your suggestions 🤗

## Customizing YTShell

YTShell is designed to be highly customizable, allowing you to personalize the look and feel of your shell environment. This can be done through the `theme` and `config` commands.

### `theme` Command

The `theme` command allows you to customize the appearance of YTShell, including colors for different elements like the prompt, time, and status messages.

#### Usage:

- **View Current Theme**: 
  To display the current theme settings, simply run:
  
  ```bash
  theme
  ```

- **Edit Theme**: 
  To customize the theme, use the `-edit` flag followed by the colors you want to set for various elements. The color values should be provided in the following order:
  
  1. `prompt-bg`: Background color of the prompt
  2. `prompt-txt`: Text color of the prompt
  3. `time-bg`: Background color of the time display
  4. `time-txt`: Text color of the time display
  5. `stat-bg`: Background color of the status message
  6. `stat-txt`: Text color of the status message
  7. `stat-err-bg`: Background color of error messages
  8. `stat-err-txt`: Text color of error messages
  
  Example:
  
  ```bash
  theme -edit black white green yellow blue red cyan magenta
  ```
  **Available colors:**
  black, red, green, yellow, blue, magenta, cyan, white,
  light_grey, dark_grey, light_red, light_green, light_yellow, light_blue,
  light_magenta, light_cyan.

  
  This command sets the colors for the prompt, time, and status messages according to the provided values.

### `config` Command

The `config` command allows you to configure various operational settings for YTShell, such as time display and prompt character.

#### Usage:

- **View Current Configuration**:
  To display the current configuration settings, simply run:
  
  ```bash
  config
  ```

- **Edit Configuration**:
  To customize the configuration, use the `-edit` flag followed by the settings you want to modify. The settings should be provided in the following order:
  
  1. `time`: Display time in the prompt (`true` or `false`)
  2. `timeFormat`: Format of the time display (e.g. `%H:%M:%S-%d/%m/%y`)
  3. `promptChar`: The character used as the prompt symbol
  
  Example:
  
  ```bash
  config -edit true 24h $
  ```
  
  This command enables the time display in 24-hour format and sets the prompt symbol to `$`.

### Notes

- Ensure that you provide valid values when using the `-edit` flag with either command.
- If you encounter errors, double-check the arguments you’ve provided.

### Explanation:

1. **Introduction to Commands**: Describes the purpose of the `theme` and `config` commands.
2. **Usage Instructions**: Provides clear instructions on how to view and edit both the theme and configuration settings.
3. **Examples**: Includes examples to demonstrate how to use each command with the appropriate flags and values.
4. **Notes**: Adds additional tips and reminders to ensure users follow the correct syntax and understand how to use the commands effectively. 

This Markdown can be added to your `README.md` file to guide users on customizing YTShell with the `theme` and `config` commands.

## Installation

To install YTShell, follow these steps:

1. **Ensure Python is Installed**: Make sure Python 3 is installed on your system. You can check this by running:

    ```bash
    python3 --version
    ```

2. **Clone the repo**:
    ```bash
    git clone https://github.com/yousseftechdev/YTShell
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
