import os
import sys

readCmdFile = open(f"{os.path.expanduser('~')}/.config/ytshell/commands.txt", "r")

commands = readCmdFile.read().split(", ")

def setup():
    pathFile = open(f"{os.path.expanduser('~')}/.config/ytshell/pathToJar.txt", "a")
    pathFile.close()
    commandsFile = open(f"{os.path.expanduser('~')}/.config/ytshell/commands.txt", "a")
    commandsFile.close()
    historyFile = open(f"{os.path.expanduser('~')}/.config/ytshell/history.txt", "a")
    historyFile.close()
    themeFile = open(f"{os.path.expanduser('~')}/.config/ytshell/theme.txt", "a")
    themeFileRead = open(f"{os.path.expanduser('~')}/.config/ytshell/theme.txt", "r")
    if os.path.getsize(f"{os.path.expanduser('~')}/.config/ytshell/theme.txt") == 0:
        themeFile.write("""prompt-bg = blue,
prompt-txt = white,
time-bg = light_grey,
time-txt = black""")
    themeFileRead.close
    themeFile.close()

def get_all_commands():
    try:
        paths = os.getenv("PATH", "").split(os.pathsep)
        system_commands = set()
        for path in paths:
            if os.path.isdir(path):
                for item in os.listdir(path):
                    if os.access(os.path.join(path, item), os.X_OK):
                        system_commands.add(item)
    except Exception as e:
        system_commands = set()
        print(f"Error retrieving system commands: {e}")

    all_commands = system_commands.union(commands)
    return sorted(all_commands)

def usage_message(command):
    if command == "dev":
        print("Usage: dev (OPTION)")
        print(
            "Options:\n-info : Pulls up the developer's portfolio in a browser.\n-yt : Pulls up the developer's YouTube channel.\n-discord : Outputs the developer's discord username and his server.\n-github : Pulls up the developer's github profile in a browser."
        )
    elif command == "mkcd":
        print("Usage: mkcd (DIRECTORY)")
        print("Creates a directory with the name of the argument and changes the current working directory to that directory")
    elif command == "sp":
        print("Usage: sp (OPTION)")
        print(
            "Options:\n-web : Creates a project structure for a web project.\n-py : Creates a project structure for a Python project.\n-cpp : Creates a project structure for a C++ project."
        )
    elif command == "cleanup":
        print("Usage: cleanup")
        print("Cleans up your system from unused packages")
    elif command == "lsc":
        print("Usage: lsc")
        print("Lists all custom commands added by the shell")
    elif command == "touch":
        print("Usage: touch (FILE)")
        print("Creates a new empty file with the specified name")
    elif command == "rm":
        print("Usage: rm (FILE/DIRECTORY)")
        print("Removes the specified file or directory")
    elif command == "mv":
        print("Usage: mv (SOURCE) (DESTINATION)")
        print("Moves or renames files and directories")
    elif command == "cp":
        print("Usage: cp (SOURCE) (DESTINATION)")
        print("Copies files and directories")
    elif command == "grep":
        print("Usage: grep (PATTERN) (FILE)")
        print("Searches for the specified pattern in the file")
    elif command == "find":
        print("Usage: find (PATH) (EXPRESSION)")
        print("Searches for files and directories within the file system")
    elif command == "cat":
        print("Usage: cat (FILE)")
        print("Displays the content of the specified file")
    elif command == "echo":
        print("Usage: echo (TEXT) (OPTIONAL: FILE)")
        print("Outputs text to terminal or file")
    elif command == "gc":
        print("Usage: gc (REPO URL)")
        print("Clones the repository from the provided url")
    elif command == "ask":
        print("Usage: ai (OPTION) (QUESTION)")
        print("Options:\n-ai : Asks chatgpt\n-ggl : Asks google\n-rdt : Makes a post draft on reddit, title, body, and sub should be seperated by a '---'")
    elif command == "setrepo":
        print("Usage: setrepo (REPO NAME)")
        print("creates a folder with the name provided and initializes it as a git repository")
    elif command == "history":
        print("Usage: history (OPTIONAL)")
        print("Shows command history")
        print("Options:\n-clear : Clears command history")
        
def is_interactive():
    try:
        return os.isatty(sys.stdin.fileno())
    except Exception:
        return False