import numpy as np
from PIL import Image
import os
import sys
import turtle
from math import * # type: ignore
import subprocess
import termcolor
from datetime import datetime, timedelta
import random
import platform
import psutil
import socket
import time
import json

# ASCII grayscale characters
gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. " # type: ignore
gscale2 = '@%#*+=-:. '

# Braille grayscale characters
BRAILLE_SCALE = [
    '⠀', '⠁', '⠃', '⠇', '⠧', '⠷', '⠿', '⡿',
    '⣿', '⡟', '⡏', '⡇', '⡆', '⡄', '⡀', '⠂',
]

def setup():
    os.makedirs(f"{os.path.expanduser('~')}/.config/ytshell", exist_ok=True)
    exitCodeFile = open(f"{os.path.expanduser('~')}/.config/ytshell/exitCodeFile.txt", "w")
    exitCodeFile.write("-200")
    exitCodeFile.close()
    dirHistoryFile = open(f"{os.path.expanduser('~')}/.config/ytshell/dirHistory.txt", "a")
    dirHistoryFile.close()
    pathFile = open(f"{os.path.expanduser('~')}/.config/ytshell/pathToJar.txt", "a")
    pathFile.close()
    commandsFile = open(f"{os.path.expanduser('~')}/.config/ytshell/commands.txt", "a")
    if os.path.getsize(f"{os.path.expanduser('~')}/.config/ytshell/commands.txt") == 0:
        commandsFile.write("""help,
mc,
neofun,
fuckyou,
gc,
dev,
cd,
mkcd,
setrepo,
uprepo,
sp,
url,
cleanup,
lsc,
brc,
zrc,
exit,
rm,
ai,
ask,
vsc,
vsci,
history,
ytpm,
theme,
test,
config,
graph,
root,
addcmd,
rmcmd,
tuiclock,
ascii""")
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
        configFile.write("""time=True,
timeFormat=%H:%M:%S-%d/%m/%y,
promptChar=$""")
    configFile.close()
    phraseFile = open(f"{os.path.expanduser('~')}/.config/ytshell/phrases.txt", "a")
    if os.path.getsize(f"{os.path.expanduser('~')}/.config/ytshell/phrases.txt") == 0:
        phraseFile.write("""
I am watching you, pookie,
I bet you don't remember what you had for lunch,
Nice try CockSucker69, I can recognize your alt accounts anywhere,
Don't worry, I won't tell anyone about your secret project,
Just because you can code, doesn't mean you should,
Did you really think that would work?,
Your secret is safe with me... for now,
Oh look, the master coder has arrived!,
Why do you keep typing that? It's not going to work,
I know what you did last summer,
You do realize this is all going into your permanent record, right?,
Trying to outsmart me? Good luck with that,
Is this really the best use of your time?,
If only you knew how many bugs are lurking in your code,
One day, you'll look back and laugh... or cry,
Are you sure you know what you're doing?,
You didn't forget to save your work, did you?,
I'm starting to think you're just guessing now,
This is why we can't have nice things,
I see you're up to your old tricks again,
Not sure if genius or madness, but let's go with it,
Remember when this was supposed to be a quick task?,
Ah, the sweet smell of desperation in the morning,
So, you really think this will work?,
Warning: Genius at work... or not,
If code could talk, it would cry right now,
Oh, you think you're clever, don't you?,
I saw that typo, but I'll pretend I didn't,
Are you debugging or just adding more bugs?,
Another day, another bug,
Pro tip: Code first, panic later,
You can't keep doing this and expecting different results,
I hope you backed that up...,
Code like nobody's watching... but I am,
Do you even know what you're doing?,
Nice try, but it's still broken,
Keep going, you're almost there... or maybe not,
What could possibly go wrong?,
Just another 'quick fix,' right?,
You're one typo away from greatness... or disaster,
Remember, the code always wins,
Are we having fun yet?,
If in doubt, blame the compiler,
This isn't what you signed up for, is it?,
Looks like someone's in over their head,
You sure about that last change?,
Well, that escalated quickly,
It's not a bug, it's a feature... or so they say,
You're making progress... I think,
If only coding was as easy as you make it look,
Time to break something else,
Just another day in the life of a code wrangler,
Trying to impress me? Nice try,
That moment when you realize... this isn't going to work,
Did you really mean to do that?,
I hope you're ready for the consequences,
Let's pretend that didn't just happen,
You're really pushing your luck today,
Welcome to the club of endless debugging,
Who needs sleep when you have code?,
Remember, Ctrl+Z is your best friend,
Congratulations! You just created a whole new bug,
I see you're living on the edge today,
Coding: the fine art of convincing a computer to do what you want""")
    phraseFile.close()
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
    readCmdFile = open(f"{os.path.expanduser('~')}/.config/ytshell/commands.txt", "r")
    commands = readCmdFile.read().split(",\n")
    readCmdFile.close()
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
        print("Options:\n-ai : Asks chatgpt\n-ggl : Asks google\n-rdt : Makes a post draft on reddit, title, body, and sub should be separated by a '---'")
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
    elif command == "addcmd":
        print("Usage: addcmd (CUSTOM COMMAND)")
        print("This command is used to add custom commands to the shell, it appends the command name to the commands.txt file located at '~/.config/ytshell/commands.txt'.")
        print("You can edit the commands file manually.")
        print("Keep in mind that the added command won't do anything if not programmed correctly in the main.py file located at '~/.config/ytshell/main.py'.")
        print("If the command is not programmed it will return a 126 error.")
    elif command == "rmcmd":
        print("Usage: addcmd (CUSTOM COMMAND)")
        print("This command is used to remove custom commands from the shell, it removes the command name from the commands.txt file located at '~/.config/ytshell/commands.txt'.")
        print("You can edit the commands file manually.")
    elif command == "ascii":
        print("Usage: ascii (FILE) (WIDTH) (SCALE) (HIGH DETAIL) (BRAIL CHARS)")
        print("Turns images into their ascii representation and prints them.")
        print("Example usage: ascii image.png 80 0.43 False True")
        
def is_interactive():
    try:
        return os.isatty(sys.stdin.fileno())
    except Exception:
        return False

def get_git_info():
    try:
        branch = subprocess.check_output(
            ['git', 'rev-parse', '--abbrev-ref', 'HEAD'], stderr=subprocess.DEVNULL
        ).strip().decode('utf-8')

        status = subprocess.check_output(['git', 'status', '--short'], stderr=subprocess.DEVNULL).decode('utf-8')

        modified = f" !{str(len([line for line in status.splitlines() if line.startswith(' M ')]))} "
        created = f" ?{str(len([line for line in status.splitlines() if line.startswith('??')]))} "
        deleted = f" #{str(len([line for line in status.splitlines() if line.startswith(' D ')]))} "
        
        staged_modified = f" ~{str(len([line for line in status.splitlines() if line.startswith('M ')]))} "
        staged_added = f" +{str(len([line for line in status.splitlines() if line.startswith('A ')]))} "
        staged_deleted = f" -{str(len([line for line in status.splitlines() if line.startswith('D ')]))} "

        if created == ' ?0 ':
            created = ''
        if modified == ' !0 ':
            modified = ''
        if deleted == ' #0 ':
            deleted = ''
        if staged_modified == ' ~0 ':
            staged_modified = ''
        if staged_added == ' +0 ':
            staged_added = ''
        if staged_deleted == ' -0 ':
            staged_deleted = ''
        
        if not any([created, deleted, modified, staged_modified, staged_added, staged_deleted]):
            repoUtd = True
            color = 'light_green'
        else:
            repoUtd = False
            color = 'light_red'

        git_info = (
            termcolor.colored(f' {branch}{modified}{created}{deleted}{staged_modified}{staged_added}{staged_deleted} ', 'white', f'on_{color}') # type: ignore
            + termcolor.colored('', color)
        )

        return git_info, repoUtd

    except Exception as e:
        return None, False


def get_prompt():
    with open(f"{os.path.expanduser('~')}/.config/ytshell/phrases.txt", "r") as phraseFile:
        phrase = random.choice(phraseFile.read().split(",\n"))
    exitCodeFile = open(f"{os.path.expanduser('~')}/.config/ytshell/exitCodeFile.txt", "r")
    exitCode = int(exitCodeFile.read())
    dir = os.getcwd()
    currentFolder = os.getcwd().split("/")[-1]
    if os.getuid() != 0:
        if currentFolder == os.path.expanduser("~").split("/home/")[1]:
            currentFolder = ""

    fdir = ' ' + dir.replace(os.path.expanduser('~'), '~').strip(currentFolder)
    configFile = open(f"{os.path.expanduser('~')}/.config/ytshell/config.txt", "r")
    configContent = configFile.read().split(",\n")
    timeInPrompt = configContent[0].split("time=")[1]
    timeFormat = configContent[1].split("timeFormat=")[1]
    promptChar = configContent[2].split("promptChar=")[1]
    dt = datetime.now()
    ftime = dt.strftime(timeFormat)
    themeFile = open(f"{os.path.expanduser('~')}/.config/ytshell/theme.txt", "r")
    colors = themeFile.read().split(",\n")
    promptBg = colors[0].split("prompt-bg=")[1]
    promptTxt = colors[1].split("prompt-txt=")[1]
    timeBg = colors[2].split("time-bg=")[1]
    timeTxt = colors[3].split("time-txt=")[1]
    statBg = colors[4].split("stat-bg=")[1]
    statTxt = colors[5].split("stat-txt=")[1]
    statErrBg = colors[6].split("stat-err-bg=")[1]
    statErrTxt = colors[7].split("stat-err-txt=")[1]

    # Get Git info if in a Git repository
    git_info, repoUtd = get_git_info()
    if git_info:
        git_prompt = f"{git_info}"
    else:
         git_prompt = ""
    if repoUtd:
        git_cross_color = 'light_green'
    else:
        git_cross_color = 'light_red'

    if os.getuid() == 0:
        if timeInPrompt.lower() in ["t", "true"]:
            if exitCode != -200:
                if exitCode == 0:
                    prompt = f"╭─{termcolor.colored('', 'red') + termcolor.colored(' ' + os.getlogin() + f'@{os.uname().nodename} 💀 [' + fdir, 'white', 'on_red') + termcolor.colored(currentFolder.replace('root', ''), 'white', 'on_red', attrs=['bold']) + termcolor.colored(' ] ', 'white', 'on_red') + termcolor.colored('', 'red', f'on_{git_cross_color}')}{git_prompt}···{termcolor.colored('', statBg) + termcolor.colored(' ✔ ', statTxt, f'on_{statBg}') + termcolor.colored('', timeBg, f'on_{statBg}') + termcolor.colored(' ' + ftime + ' ', timeTxt, f'on_{timeBg}') + termcolor.colored('', timeBg)}\n│\n╰─ {promptChar} " if git_prompt else f"╭─{termcolor.colored('', 'red') + termcolor.colored(' ' + os.getlogin() + f'@{os.uname().nodename} 💀 [' + fdir, 'white', 'on_red') + termcolor.colored(currentFolder.replace('root', ''), 'white', 'on_red', attrs=['bold']) + termcolor.colored(' ] ', 'white', 'on_red') + termcolor.colored('', 'red')}···{termcolor.colored('', statBg) + termcolor.colored(' ✔ ', statTxt, f'on_{statBg}') + termcolor.colored('', timeBg, f'on_{statBg}') + termcolor.colored(' ' + ftime + ' ', timeTxt, f'on_{timeBg}') + termcolor.colored('', timeBg)}\n│\n╰─ {promptChar} " # type: ignore
                else:
                    prompt = f"╭─{termcolor.colored('', 'red') + termcolor.colored(' ' + os.getlogin() + f'@{os.uname().nodename} 💀 [' + fdir, 'white', 'on_red') + termcolor.colored(currentFolder.replace('root', ''), 'white', 'on_red', attrs=['bold']) + termcolor.colored(' ] ', 'white', 'on_red') + termcolor.colored('', 'red', f'on_{git_cross_color}')}{git_prompt}···{termcolor.colored('', statErrBg) + termcolor.colored(f' {exitCode} ✘ ', statErrTxt, f'on_{statErrBg}') + termcolor.colored('', timeBg, f'on_{statErrBg}') + termcolor.colored(' ' + ftime + ' ', timeTxt, f'on_{timeBg}') + termcolor.colored('', timeBg)}\n│\n╰─ {promptChar} " if git_prompt else f"╭─{termcolor.colored('', 'red') + termcolor.colored(' ' + os.getlogin() + f'@{os.uname().nodename} 💀 [' + fdir, 'white', 'on_red') + termcolor.colored(currentFolder.replace('root', ''), 'white', 'on_red', attrs=['bold']) + termcolor.colored(' ] ', 'white', 'on_red') + termcolor.colored('', 'red')}···{termcolor.colored('', statErrBg) + termcolor.colored(f' {exitCode} ✘ ', statErrTxt, f'on_{statErrBg}') + termcolor.colored('', timeBg, f'on_{statErrBg}') + termcolor.colored(' ' + ftime + ' ', timeTxt, f'on_{timeBg}') + termcolor.colored('', timeBg)}\n│\n╰─ {promptChar} " # type: ignore
            else:
                prompt = f"╭─{termcolor.colored('', 'red') + termcolor.colored(' ' + os.getlogin() + f'@{os.uname().nodename} 💀 [' + fdir, 'white', 'on_red') + termcolor.colored(currentFolder.replace('root', ''), 'white', 'on_red', attrs=['bold']) + termcolor.colored(' ] ', 'white', 'on_red') + termcolor.colored('', 'red', f'on_{git_cross_color}')}{git_prompt}···{termcolor.colored('', timeBg) + termcolor.colored(' ' + ftime + ' ', timeTxt, f'on_{timeBg}') + termcolor.colored('', timeBg)}\n│\n╰─ {promptChar} " if git_prompt else f"╭─{termcolor.colored('', 'red') + termcolor.colored(' ' + os.getlogin() + f'@{os.uname().nodename} 💀 [' + fdir, 'white', 'on_red') + termcolor.colored(currentFolder.replace('root', ''), 'white', 'on_red', attrs=['bold']) + termcolor.colored(' ] ', 'white', 'on_red') + termcolor.colored('', 'red')}···{termcolor.colored('', timeBg) + termcolor.colored(' ' + ftime + ' ', timeTxt, f'on_{timeBg}') + termcolor.colored('', timeBg)}\n│\n╰─ {promptChar} " # type: ignore
        else:
            if exitCode != -200:
                if exitCode == 0:
                    prompt = f"╭─{termcolor.colored('', 'red') + termcolor.colored(' ' + os.getlogin() + f'@{os.uname().nodename} - [' + fdir, 'white', 'on_red') + termcolor.colored(currentFolder, promptTxt, f'on_{promptBg}', attrs=['bold']) + termcolor.colored(' ] ', promptTxt, f'on_{promptBg}') + termcolor.colored('', promptBg, f'on_{statBg}') + termcolor.colored(' ✔ ', statTxt, f'on_{statBg}', attrs=['bold']) + termcolor.colored('', statBg, f'on_{git_cross_color}')}{git_prompt}\n│\n╰─ {promptChar} " if git_prompt else f"╭─{termcolor.colored('', 'red') + termcolor.colored(' ' + os.getlogin() + f'@{os.uname().nodename} - [' + fdir, 'white', 'on_red') + termcolor.colored(currentFolder, promptTxt, f'on_{promptBg}', attrs=['bold']) + termcolor.colored(' ] ', promptTxt, f'on_{promptBg}') + termcolor.colored('', promptBg, f'on_{statBg}') + termcolor.colored(' ✔ ', statTxt, f'on_{statBg}', attrs=['bold']) + termcolor.colored('', statBg)}\n│\n╰─ {promptChar} " # type: ignore
                else:
                    prompt = f"╭─{termcolor.colored('', 'red') + termcolor.colored(' ' + os.getlogin() + f'@{os.uname().nodename} - [' + fdir, 'white', 'on_red') + termcolor.colored(currentFolder, promptTxt, f'on_{promptBg}', attrs=['bold']) + termcolor.colored(' ] ', promptTxt, f'on_{promptBg}') + termcolor.colored('', promptBg, f'on_{statErrBg}') + termcolor.colored(f' {exitCode} ✘ ', statErrTxt, f'on_{statErrBg}', attrs=['bold']) + termcolor.colored('', statErrBg, f'on_{git_cross_color}')}{git_prompt}\n│\n╰─ {promptChar} " if git_prompt else f"╭─{termcolor.colored('', 'red') + termcolor.colored(' ' + os.getlogin() + f'@{os.uname().nodename} - [' + fdir, 'white', 'on_red') + termcolor.colored(currentFolder, promptTxt, f'on_{promptBg}', attrs=['bold']) + termcolor.colored(' ] ', promptTxt, f'on_{promptBg}') + termcolor.colored('', promptBg, f'on_{statErrBg}') + termcolor.colored(f' {exitCode} ✘ ', statErrTxt, f'on_{statErrBg}', attrs=['bold']) + termcolor.colored('', statErrBg)}\n│\n╰─ {promptChar} " # type: ignore
            else:
                prompt = f"╭─{termcolor.colored('', 'red') + termcolor.colored(' ' + os.getlogin() + f'@{os.uname().nodename} - [' + fdir, 'white', 'on_red') + termcolor.colored(currentFolder, promptTxt, f'on_{promptBg}', attrs=['bold']) + termcolor.colored(' ] ', promptTxt, f'on_{promptBg}') + termcolor.colored('', promptBg, f'on_{git_cross_color}')}{git_prompt}\n│\n╰─ {promptChar} " if git_prompt else f"╭─{termcolor.colored('', 'red') + termcolor.colored(' ' + os.getlogin() + f'@{os.uname().nodename} - [' + fdir, 'white', 'on_red') + termcolor.colored(currentFolder, promptTxt, f'on_{promptBg}', attrs=['bold']) + termcolor.colored(' ] ', promptTxt, f'on_{promptBg}') + termcolor.colored('', promptBg)}\n│\n╰─ {promptChar} " # type: ignore

    else:
        if timeInPrompt.lower() in ["t", "true"]:
            if exitCode != -200:
                if exitCode == 0:
                    prompt = f"╭─{termcolor.colored('', promptBg) + termcolor.colored(' ' + os.getlogin() + f'@{os.uname().nodename} [' + fdir, promptTxt, f'on_{promptBg}') + termcolor.colored(currentFolder, promptTxt, f'on_{promptBg}', attrs=['bold']) + termcolor.colored(' ] ', promptTxt, f'on_{promptBg}') + termcolor.colored('', promptBg, f'on_{git_cross_color}')}{git_prompt}···{termcolor.colored('', statBg) + termcolor.colored(' ✔ ', statTxt, f'on_{statBg}') + termcolor.colored('', timeBg, f'on_{statBg}') + termcolor.colored(' ' + ftime + ' ', timeTxt, f'on_{timeBg}') + termcolor.colored('', timeBg)}\n│\n╰─ {promptChar} " if git_prompt else f"╭─{termcolor.colored('', promptBg) + termcolor.colored(' ' + os.getlogin() + f'@{os.uname().nodename} [' + fdir, promptTxt, f'on_{promptBg}') + termcolor.colored(currentFolder, promptTxt, f'on_{promptBg}', attrs=['bold']) + termcolor.colored(' ] ', promptTxt, f'on_{promptBg}') + termcolor.colored('', promptBg)}···{termcolor.colored('', statBg) + termcolor.colored(' ✔ ', statTxt, f'on_{statBg}') + termcolor.colored('', timeBg, f'on_{statBg}') + termcolor.colored(' ' + ftime + ' ', timeTxt, f'on_{timeBg}') + termcolor.colored('', timeBg)}\n│\n╰─ {promptChar} " # type: ignore
                else:
                    prompt = f"╭─{termcolor.colored('', promptBg) + termcolor.colored(' ' + os.getlogin() + f'@{os.uname().nodename} [' + fdir, promptTxt, f'on_{promptBg}') + termcolor.colored(currentFolder, promptTxt, f'on_{promptBg}', attrs=['bold']) + termcolor.colored(' ] ', promptTxt, f'on_{promptBg}') + termcolor.colored('', promptBg, f'on_{git_cross_color}')}{git_prompt}···{termcolor.colored('', statErrBg) + termcolor.colored(f' {exitCode} ✘ ', statErrTxt, f'on_{statErrBg}') + termcolor.colored('', timeBg, f'on_{statErrBg}') + termcolor.colored(' ' + ftime + ' ', timeTxt, f'on_{timeBg}') + termcolor.colored('', timeBg)}\n│\n╰─ {promptChar} " if git_prompt else f"╭─{termcolor.colored('', promptBg) + termcolor.colored(' ' + os.getlogin() + f'@{os.uname().nodename} [' + fdir, promptTxt, f'on_{promptBg}') + termcolor.colored(currentFolder, promptTxt, f'on_{promptBg}', attrs=['bold']) + termcolor.colored(' ] ', promptTxt, f'on_{promptBg}') + termcolor.colored('', promptBg)}···{termcolor.colored('', statErrBg) + termcolor.colored(f' {exitCode} ✘ ', statErrTxt, f'on_{statErrBg}') + termcolor.colored('', timeBg, f'on_{statErrBg}') + termcolor.colored(' ' + ftime + ' ', timeTxt, f'on_{timeBg}') + termcolor.colored('', timeBg)}\n│\n╰─ {promptChar} " # type: ignore
            else:
                prompt = f"╭─{termcolor.colored('', promptBg) + termcolor.colored(' ' + os.getlogin() + f'@{os.uname().nodename} [' + fdir, promptTxt, f'on_{promptBg}') + termcolor.colored(currentFolder, promptTxt, f'on_{promptBg}', attrs=['bold']) + termcolor.colored(' ] ', promptTxt, f'on_{promptBg}') + termcolor.colored('', promptBg, f'on_{git_cross_color}')}{git_prompt}···{termcolor.colored('', timeBg) + termcolor.colored(' ' + ftime + ' ', timeTxt, f'on_{timeBg}') + termcolor.colored('', timeBg)}\n│\n╰─ {promptChar} " if git_prompt else f"╭─{termcolor.colored('', promptBg) + termcolor.colored(' ' + os.getlogin() + f'@{os.uname().nodename} [' + fdir, promptTxt, f'on_{promptBg}') + termcolor.colored(currentFolder, promptTxt, f'on_{promptBg}', attrs=['bold']) + termcolor.colored(' ] ', promptTxt, f'on_{promptBg}') + termcolor.colored('', promptBg)}···{termcolor.colored('', timeBg) + termcolor.colored(' ' + ftime + ' ', timeTxt, f'on_{timeBg}') + termcolor.colored('', timeBg)}\n│\n╰─ {promptChar} " # type: ignore
        else:
            if exitCode != -200:
                if exitCode == 0:
                    prompt = f"╭─{termcolor.colored('', promptBg) + termcolor.colored(' ' + os.getlogin() + f'@{os.uname().nodename} [' + fdir, promptTxt, f'on_{promptBg}') + termcolor.colored(currentFolder, promptTxt, f'on_{promptBg}', attrs=['bold']) + termcolor.colored(' ] ', promptTxt, f'on_{promptBg}') + termcolor.colored('', promptBg, f'on_{statBg}') + termcolor.colored(' ✔ ', statTxt, f'on_{statBg}', attrs=['bold']) + termcolor.colored('', statBg, f'on_{git_cross_color}')}{git_prompt}\n│\n╰─ {promptChar} " if git_prompt else f"╭─{termcolor.colored('', promptBg) + termcolor.colored(' ' + os.getlogin() + f'@{os.uname().nodename} [' + fdir, promptTxt, f'on_{promptBg}') + termcolor.colored(currentFolder, promptTxt, f'on_{promptBg}', attrs=['bold']) + termcolor.colored(' ] ', promptTxt, f'on_{promptBg}') + termcolor.colored('', promptBg, f'on_{statBg}') + termcolor.colored(' ✔ ', statTxt, f'on_{statBg}', attrs=['bold']) + termcolor.colored('', statBg)}\n│\n╰─ {promptChar} "# type: ignore
                else:
                    prompt = f"╭─{termcolor.colored('', promptBg) + termcolor.colored(' ' + os.getlogin() + f'@{os.uname().nodename} [' + fdir, promptTxt, f'on_{promptBg}') + termcolor.colored(currentFolder, promptTxt, f'on_{promptBg}', attrs=['bold']) + termcolor.colored(' ] ', promptTxt, f'on_{promptBg}') + termcolor.colored('', promptBg, f'on_{statErrBg}') + termcolor.colored(f' {exitCode} ✘ ', statErrTxt, f'on_{statErrBg}', attrs=['bold']) + termcolor.colored('', statErrBg, f'on_{git_cross_color}')}{git_prompt}\n│\n╰─ {promptChar} " if git_prompt else f"╭─{termcolor.colored('', promptBg) + termcolor.colored(' ' + os.getlogin() + f'@{os.uname().nodename} [' + fdir, promptTxt, f'on_{promptBg}') + termcolor.colored(currentFolder, promptTxt, f'on_{promptBg}', attrs=['bold']) + termcolor.colored(' ] ', promptTxt, f'on_{promptBg}') + termcolor.colored('', promptBg, f'on_{statErrBg}') + termcolor.colored(f' {exitCode} ✘ ', statErrTxt, f'on_{statErrBg}', attrs=['bold']) + termcolor.colored('', statErrBg)}\n│\n╰─ {promptChar} " # type: ignore
            else:
                prompt = f"╭─{termcolor.colored('', promptBg) + termcolor.colored(' ' + os.getlogin() + f'@{os.uname().nodename} [' + fdir, promptTxt, f'on_{promptBg}') + termcolor.colored(currentFolder, promptTxt, f'on_{promptBg}', attrs=['bold']) + termcolor.colored(' ] ', promptTxt, f'on_{promptBg}') + termcolor.colored('', promptBg, f'on_{git_cross_color}')}{git_prompt}\n│\n╰─ {promptChar} " if git_prompt else f"╭─{termcolor.colored('', promptBg) + termcolor.colored(' ' + os.getlogin() + f'@{os.uname().nodename} [' + fdir, promptTxt, f'on_{promptBg}') + termcolor.colored(currentFolder, promptTxt, f'on_{promptBg}', attrs=['bold']) + termcolor.colored(' ] ', promptTxt, f'on_{promptBg}') + termcolor.colored('', promptBg)}\n│\n╰─ {promptChar} " if git_prompt else f"╭─{termcolor.colored('', promptBg) + termcolor.colored(' ' + os.getlogin() + f'@{os.uname().nodename} [' + fdir, promptTxt, f'on_{promptBg}') + termcolor.colored(currentFolder, promptTxt, f'on_{promptBg}', attrs=['bold']) + termcolor.colored(' ] ', promptTxt, f'on_{promptBg}') + termcolor.colored('', promptBg)}\n│\n╰─ {promptChar} " if git_prompt else f"╭─{termcolor.colored('', promptBg) + termcolor.colored(' ' + os.getlogin() + f'@{os.uname().nodename} [' + fdir, promptTxt, f'on_{promptBg}') + termcolor.colored(currentFolder, promptTxt, f'on_{promptBg}', attrs=['bold']) + termcolor.colored(' ] ', promptTxt, f'on_{promptBg}') + termcolor.colored('', promptBg)}\n│\n╰─ {promptChar} "# type: ignore
    exitCodeFile.close()
    if random.randint(0, 1000000) > 999000:
        return phrase
    return prompt
def get_ftime():
    configFile = open(f"{os.path.expanduser('~')}/.config/ytshell/config.txt", "r")
    configContent = configFile.read().split(",\n")
    timeFormat = configContent[1].split("timeFormat=")[1]
    dt = datetime.now()
    ftime = dt.strftime(timeFormat)
    return ftime

def dirAutoComplete(dir):
    with open(f"{os.path.expanduser('~')}/.config/ytshell/dirHistory.txt", "r") as dirHistoryFile:
        paths = dirHistoryFile.read().split(",\n")
        for path in paths:
            if dir.lower() in path.lower():
                print(path)
                return path
    return None

def remove_item_from_file(file_path, item_to_remove):
    try:
        # Read the file contents into a list
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        # Strip newline characters and remove the item if it exists
        lines = [line.strip() for line in lines]
        for l in lines:
            if item_to_remove in l:
                lines.remove(l)
        
        # Write the updated list back to the file
        with open(file_path, 'w') as file:
            for line in lines:
                if line is not lines[-1]:
                    file.write(line + '\n')
                else:
                    print(lines[-1])
                    file.write(line.strip(","))
        print(f"Item '{item_to_remove}' removed successfully.")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def getAverageL(image):
    im = np.array(image)
    w, h = im.shape
    return np.average(im.reshape(w*h))

def covertImageToAscii(fileName, cols=80, scale=0.43, moreLevels="false", useBraille="false"):
    image = Image.open(fileName).convert('L')
    W, H = image.size[0], image.size[1]

    w = W / cols
    h = w / scale
    rows = int(H / h)

    if cols > W or rows > H:
        print("Image too small for specified cols!")
        return

    aimg = []
    for j in range(rows):
        y1 = int(j * h)
        y2 = int((j + 1) * h)
        if j == rows - 1:
            y2 = H

        aimg.append("")
        for i in range(cols):
            x1 = int(i * w)
            x2 = int((i + 1) * w)
            if i == cols - 1:
                x2 = W

            img = image.crop((x1, y1, x2, y2))
            avg = int(getAverageL(img))

            if useBraille.lower() == "true":
                gsval = BRAILLE_SCALE[int((avg * (len(BRAILLE_SCALE) - 1)) / 255)]
            else:
                if moreLevels.lower() == "true":
                    gsval = gscale1[int((avg * 69) / 255)]
                else:
                    gsval = gscale2[int((avg * 9) / 255)]

            aimg[j] += gsval
    
    return aimg

def ascii_art_command(args):
    fileName = args[0]  # Assuming first argument is the image file name
    cols = int(args[1])
    scale = float(args[2])
    moreLevels = args[3]
    useBraille = args[4]

    print('Generating ASCII art...')
    aimg = covertImageToAscii(fileName, cols, scale, moreLevels, useBraille)

    if aimg:
        for row in aimg:
            print(row)

def get_system_info():
    uname_info = platform.uname()
    os_name = uname_info.system
    os_version = uname_info.version
    kernel_version = uname_info.release
    architecture = uname_info.machine

    uptime_seconds = int(psutil.boot_time())
    uptime = str(timedelta(seconds=(time.time() - uptime_seconds)))

    cpu_name = platform.processor()
    cpu_cores = psutil.cpu_count(logical=False)
    cpu_threads = psutil.cpu_count(logical=True)
    cpu_usage = psutil.cpu_percent(interval=1)

    mem = psutil.virtual_memory()
    total_memory = mem.total / (1024 ** 3)
    used_memory = mem.used / (1024 ** 3)
    free_memory = mem.available / (1024 ** 3)

    disk = psutil.disk_usage('/')
    total_disk = disk.total / (1024 ** 3)
    used_disk = disk.used / (1024 ** 3)
    free_disk = disk.free / (1024 ** 3)

    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    return {
        'OS': os_name,
        'OS Version': os_version,
        'Kernel Version': kernel_version,
        'Architecture': architecture,
        'Uptime': uptime,
        'CPU': cpu_name,
        'CPU Cores': cpu_cores,
        'CPU Threads': cpu_threads,
        'CPU Usage': f"{cpu_usage}%",
        'Total Memory': f"{total_memory:.2f} GB",
        'Used Memory': f"{used_memory:.2f} GB",
        'Free Memory': f"{free_memory:.2f} GB",
        'Total Disk': f"{total_disk:.2f} GB",
        'Used Disk': f"{used_disk:.2f} GB",
        'Free Disk': f"{free_disk:.2f} GB",
        'Hostname': hostname,
        'IP Address': ip_address,
    }
def get_linux_distro():
    distro_name = "Unknown"
    try:
        with open("/etc/os-release", "r") as f:
            for line in f:
                if line.startswith("PRETTY_NAME"):
                    distro_name = line.split("=")[1].strip().replace('"', '')
                    break
                elif line.startswith("NAME"):
                    distro_name = line.split("=")[1].strip().replace('"', '')
    except FileNotFoundError:
        pass
    
    return distro_name
def print_neofun():
    info = get_system_info()
    ascii_art = """
    ⡆⣐⢕⢕⢕⢕⢕⢕⢕⢕⠅⢗⢕⢕⢕⢕⢕⢕⢕⠕⠕⢕⢕⢕⢕⢕⢕⢕⢕⢕                    {username}@{hostname}
    ⢐⢕⢕⢕⢕⢕⣕⢕⢕⠕⠁⢕⢕⢕⢕⢕⢕⢕⢕⠅⡄⢕⢕⢕⢕⢕⢕⢕⢕⢕                    -----------------------------------------
    ⢕⢕⢕⢕⢕⠅⢗⢕⠕⣠⠄⣗⢕⢕⠕⢕⢕⢕⠕⢠⣿⠐⢕⢕⢕⠑⢕⢕⠵⢕                    OS: {os}
    ⢕⢕⢕⢕⠁⢜⠕⢁⣴⣿⡇⢓⢕⢵⢐⢕⢕⠕⢁⣾⢿⣧⠑⢕⢕⠄⢑⢕⠅⢕                    OS Version: {os_version}
    ⢕⢕⠵⢁⠔⢁⣤⣤⣶⣶⣶⡐⣕⢽⠐⢕⠕⣡⣾⣶⣶⣶⣤⡁⢓⢕⠄⢑⢅⢑                    Host: {hostname}
    ⠍⣧⠄⣶⣾⣿⣿⣿⣿⣿⣿⣷⣔⢕⢄⢡⣾⣿⣿⣿⣿⣿⣿⣿⣦⡑⢕⢤⠱⢐                    Kernel Version: {kernel}
    ⢠⢕⠅⣾⣿⠋⢿⣿⣿⣿⠉⣿⣿⣷⣦⣶⣽⣿⣿⠈⣿⣿⣿⣿⠏⢹⣷⣷⡅⢐                    Architecture: {arch}
    ⣔⢕⢥⢻⣿⡀⠈⠛⠛⠁⢠⣿⣿⣿⣿⣿⣿⣿⣿⡀⠈⠛⠛⠁⠄⣼⣿⣿⡇⢔                    Uptime: {uptime}
    ⢕⢕⢽⢸⢟⢟⢖⢖⢤⣶⡟⢻⣿⡿⠻⣿⣿⡟⢀⣿⣦⢤⢤⢔⢞⢿⢿⣿⠁⢕                    CPU Cores: {cpu_cores}
    ⢕⢕⠅⣐⢕⢕⢕⢕⢕⣿⣿⡄⠛⢀⣦⠈⠛⢁⣼⣿⢗⢕⢕⢕⢕⢕⢕⡏⣘⢕                    CPU Threads: {cpu_threads}
    ⢕⢕⠅⢓⣕⣕⣕⣕⣵⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣷⣕⢕⢕⢕⢕⡵⢀⢕⢕                    CPU Usage: {cpu_usage}
    ⢑⢕⠃⡈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢃⢕⢕⢕                    Total Memory: {total_memory}
    ⣆⢕⠄⢱⣄⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢁⢕⢕⠕⢁                    Memory Usage: {used_memory}
    ⣿⣦⡀⣿⣿⣷⣶⣬⣍⣛⣛⣛⡛⠿⠿⠿⠛⠛⢛⣛⣉⣭⣤⣂⢜⠕⢑⣡⣴⣿                    Shell: ytshell
    """.format(
        username=os.getlogin(),
        hostname=platform.node(),
        os=platform.system(),
        # os_version=platform.version(),
        os_version=get_linux_distro(),
        kernel=platform.release(),
        arch=platform.machine(),
        uptime=get_system_info()['Uptime'],
        cpu=get_system_info()['CPU'],
        cpu_cores=get_system_info()['CPU Cores'],
        cpu_threads=get_system_info()['CPU Threads'],
        cpu_usage=get_system_info()['CPU Usage'],
        total_memory=get_system_info()['Total Memory'],
        used_memory=get_system_info()['Used Memory'],
        free_memory=get_system_info()['Free Memory'],
    )

    print(termcolor.colored(ascii_art))

# File path to store reminders
REMINDERS_FILE = f"{os.path.expanduser('~')}/.config/ytshell/reminders.json"

# Load reminders from file
def load_reminders():
    try:
        with open(REMINDERS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Save reminders to file
def save_reminders(reminders):
    with open(REMINDERS_FILE, "w") as file:
        json.dump(reminders, file, default=str)

# Load reminders on startup
reminders = load_reminders()

def parse_remind_args(command):
    # Split the command into arguments
    args = command.split()
    parsed_args = {}

    # Initialize flags and options
    parsed_args["onStartUp"] = False
    parsed_args["periodic"] = False
    parsed_args["times"] = 1
    parsed_args["time"] = 1
    parsed_args["timeType"] = "seconds"
    parsed_args["name"] = "Reminder"
    parsed_args["clear"] = False  # New flag for clearing reminders
    parsed_args["list"] = False  # New flag for clearing reminders

    # Iterate through the arguments and update parsed_args accordingly
    i = 0
    while i < len(args):
        if args[i] == "--clear":
            parsed_args["clear"] = True  # Set the clear flag
            return parsed_args  # Immediately return if --clear is found
        elif args[i] == "--list":
            parsed_args["list"] = True  # Set the clear flag
            return parsed_args  # Immediately return if --list is found
        elif args[i] == "--onStartUp":
            parsed_args["onStartUp"] = True
        elif args[i] == "--periodic":
            parsed_args["periodic"] = True
        elif args[i] == "--times" and i + 1 < len(args):
            parsed_args["times"] = int(args[i + 1])
            i += 1
        elif args[i] == "--time" and i + 1 < len(args):
            parsed_args["time"] = int(args[i + 1])
            i += 1
        elif args[i] == "--timeType" and i + 1 < len(args):
            parsed_args["timeType"] = args[i + 1].lower()
            i += 1
        elif args[i] == "--name" and i + 1 < len(args):
            parsed_args["name"] = args[i + 1]
            i += 1
        i += 1

    return parsed_args

def calculate_next_time(time_amount, time_type):
    """Calculate the next reminder time based on the time type."""
    time_types = {
        'seconds': timedelta(seconds=time_amount),
        'minutes': timedelta(minutes=time_amount),
        'hours': timedelta(hours=time_amount),
        'days': timedelta(days=time_amount),
        'weeks': timedelta(weeks=time_amount),
        # Months calculation is approximate, set to 30 days
        'months': timedelta(days=30 * time_amount),
    }
    return time_types.get(time_type.lower(), timedelta(seconds=time_amount))

def remind_command(args):
    global reminders

    # Parse arguments
    try:
        reminder_type = args.get("onStartUp") if "onStartUp" in args else args.get("periodic")
        times = int(args.get("times", 1))
        time_amount = int(args.get("time", 1))
        time_type = args.get("timeType", "seconds").lower()
        name = args.get("name", "Reminder")
        
        # Calculate the time interval for the reminder
        time_interval = calculate_next_time(time_amount, time_type)
        next_reminder_time = datetime.now() + time_interval
        
        reminder_data = {
            "name": name,
            "interval": time_interval.total_seconds(),
            "times": times,
            "type": "onStartUp" if reminder_type == "onStartUp" else "periodic",
            "next_reminder": next_reminder_time.isoformat()
        }

        reminders.append(reminder_data)
        save_reminders(reminders)

        print(f"Reminder '{name}' set! Will remind once every {time_amount} {time_type} for {times} times .")
    except Exception as e:
        print(f"Error: {e}")

def check_reminders():
    global reminders
    current_time = datetime.now()

    for reminder in reminders[:]:
        next_reminder_time = datetime.fromisoformat(reminder["next_reminder"])

        if next_reminder_time <= current_time:
            print(f"Reminder: {reminder['name']}")

            if reminder["times"] > 0:
                reminder["times"] -= 1
                if reminder["times"] == 0:
                    reminders.remove(reminder)
                    continue

            # Update the next reminder time
            next_reminder_time += timedelta(seconds=reminder["interval"])
            reminder["next_reminder"] = next_reminder_time.isoformat()
            print(f"Next reminder in {str(next_reminder_time - current_time)}.")

    # Save the updated reminders back to the file
    save_reminders(reminders)

def get_all_reminders():
    """Returns a list of all active reminders."""
    reminders = load_reminders()  # Load the reminders from the file
    return reminders