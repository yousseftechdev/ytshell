import os
import sys
import turtle
from math import * # type: ignore

readCmdFile = open(f"{os.path.expanduser('~')}/.config/ytshell/commands.txt", "r")

commands = readCmdFile.read().split(",\n")

# Graph setup
ww = 1800
wh = 800

hww = ww/2
hwh = wh/2

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
        themeFile.write("""prompt-bg=blue,
prompt-txt=white,
time-bg=light_grey,
time-txt=black,
stat-bg=white,
stat-txt=green,
stat-err-bg=light_red,
stat-err-txt=white""")
    themeFileRead.close
    themeFile.close()
    configFile = open(f"{os.path.expanduser('~')}/.config/ytshell/config.txt", "a")
    if os.path.getsize(f"{os.path.expanduser('~')}/.config/ytshell/config.txt") == 0:
        configFile.write("""time=True
timeFormat=%H:%M:%S-%d/%m/%y
promptChar=$
""")
    configFile.close()

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
        print("Displays the content of the specified file.")
    elif command == "echo":
        print("Usage: echo (TEXT) (OPTIONAL: FILE)")
        print("Outputs text to terminal or file.")
    elif command == "gc":
        print("Usage: gc (REPO URL)")
        print("Clones the repository from the provided url.")
    elif command == "ask":
        print("Usage: ai (OPTION) (QUESTION)")
        print("Asks a question to ChatGPT, Google, or Reddit.")
        print("Options:\n-ai : Asks chatgpt\n-ggl : Asks google\n-rdt : Makes a post draft on reddit, title, body, and sub should be seperated by a '---'")
    elif command == "setrepo":
        print("Usage: setrepo (REPO NAME)")
        print("creates a folder with the name provided and initializes it as a git repository.")
    elif command == "history":
        print("Usage: history (OPTIONAL)")
        print("Shows command history")
        print("Options:\n-clear : Clears command history.")
    elif command == "ytpm":
        print("Usage: ytpm (OPTION) (PACKAGE)")
        print("APT package manager knockoff.")
        print("Options:\n-install : Installs the specified package\n-rm : Removes the specified package\n-ls : Lists all installed packages\n-search : Searches sources for specified package\n-show : Shows info about specified package\n-autorm : Removes any unnecessary packages and dependencies\n-reinstall : Removes and reinstalls a package\n-update : Update list of available packages\n-upgrade : Upgrade the system by installing/upgrading packages\n-fupgrade : Fully upgrade the system by removing/installing/upgrading packages\n-source-edit : Edit the source information file\n-satisfy : Satisfy dependency strings")
    elif command == "theme":
        print("Usage: theme (OPTIONAL)")
        print("Show current theme colors and allows you to edit them.")
        print("Options:\n-edit : Sets the colors for the shell prompt, used like this: theme -edit (COLOR1) (COLOR2) (COLOR3) (COLOR4) (COLOR5) (COLOR6) (COLOR7) (COLOR8)")
        print("\nIf you want to edit the colors by hand, the theme file is at ~/.config/ytshell/theme.txt")
        print("""\nAvailable colors:
black, red, green, yellow, blue, magenta, cyan, white,
light_grey, dark_grey, light_red, light_green, light_yellow, light_blue,
light_magenta, light_cyan.""")
    elif command == "config":
        print("Usage: config (OPTIONAL)")
        print("Show current prompt settings and allows you to edit them.")
        print("Options:\n-edit : Sets the settings for the shell prompt, used like this: config -edit (SHOW TIME AND DATE: t/f) (TIME FORMAT) (PROMPT CHARACTER: $)")
        print("\nIf you want to edit the colors by hand, the theme file is at ~/.config/ytshell/config.txt")
    elif command == "graph":
        print("Usage: graph (EQUATION),(RESOLUTION)")
        print("Graphs an equation using the turtle library, the exponent operator is '**' not '^'.")
        print("Functions like: sin(), cos(), tan(), log(), and factorial() are available.")
        print("ONLY USE THE X VARIABLE IN YOUR EQUATION")
def is_interactive():
    try:
        return os.isatty(sys.stdin.fileno())
    except Exception:
        return False
def graph(equ, res):
    wn = turtle.Screen()

    wn.setup(ww, wh)
    wn.bgcolor("black")

    pen = turtle.Turtle()
    pen.color("white")
    pen.speed(0)
    pen.width(2)
    pen.goto(0, hwh)
    pen.write("y", font=("monospace", 20, "bold"))
    pen.goto(0,-hwh)
    pen.goto(0, 0)
    pen.goto(hww, 0)
    pen.write("x", font=("monospace", 20, "bold"))
    pen.goto(-hww, 0)
    pen.hideturtle()
    
    func = turtle.Turtle()
    func.hideturtle()
    func.color("cyan")
    func.speed(0)
    func.width(2)
    
    for i in range(int(-hww), int(hww), int(res)):
        if i == -hww:
            func.penup()
            x = i
            y = eval(equ)
            func.goto(x, y)
            func.pendown()
        elif i == 0:
            pass
        else:
            x = i
            y = eval(equ)
            func.goto(x, y)
    wn.exitonclick()