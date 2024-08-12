# GLOBALS
global completedProcess
global repoUtd
import subprocess
import os
import sys
import pyautogui
import time
from funcs import *
import datetime
import termcolor

setup()

sys.stdout.write("\x1b]2;YTShell\x07")

readCmdFile = open(f"{os.path.expanduser('~')}/.config/ytshell/commands.txt", "r")
commands = readCmdFile.read().split(",\n")
commands[-1] = commands[-1].strip("\n")


def main() -> None:
    all_commands = get_all_commands()

    while True:
        try:
            sys.stdout.write(f"\x1b]2;YTShell - {dir}\x07")
            if is_interactive():
                cmd = input(get_prompt())
                historyFile = open(f"{os.path.expanduser('~')}/.config/ytshell/history.txt", "a")
                historyFile.write(f"{cmd}         {get_ftime()}\n\n")
                historyFile.close()
            else:
                print("Running in a non-interactive mode. Exiting.")
                break

            try:
                if " " in cmd:
                    cmdSplit, args = cmd.split(maxsplit=1)
                else:
                    cmdSplit = cmd
                    args = ""
            except ValueError:
                cmdSplit = cmd
                args = ""

            match cmdSplit:
                case cmd if cmd not in commands:
                    if cmd == "ls":
                        completedProcess = subprocess.run(f"ls --color=auto {args}", shell=True).returncode
                    else:
                        completedProcess = subprocess.run(cmd, shell=True).returncode
                case "help":
                    print(
                        "Hi, welcome to YTShell, a simple hobby project. It's really bad and unsafe to use, but I was bored and wanted to make something."
                    )
                    print("Here's a list of available commands:")
                    for i in range(len(all_commands)):
                        print(f"{i+1}. {all_commands[i]}")
                case "dev":
                    match args:
                        case "-info":
                            completedProcess = subprocess.run("xdg-open http://youssef-mostafa1534.github.io/NewModernPortfolio", shell=True).returncode
                        case "-yt":
                            completedProcess = subprocess.run("xdg-open https://www.youtube.com/channel/UC00bH694nxRfyRQAWhhu5Mw", shell=True).returncode
                        case "-discord":
                            print("Discord username: @yousseftech")
                            print("Discord server: https://discord.gg/qWdASj5Nzh")
                            completedProcess = 0
                        case "-github":
                            completedProcess = subprocess.run("xdg-open http://github.com/youssef-mostafa1534", shell=True).returncode
                        case _:
                            completedProcess = 20
                            print(f"Error: Invalid arguments")
                            usage_message("dev")
                case "cd":
                    if not args:
                        os.chdir(os.path.expanduser("~"))
                        completedProcess = 0
                    else:
                        try:
                            os.chdir(args)
                            completedProcess = 0
                        except FileNotFoundError:
                            completedProcess = 127
                            print(f"Error:- No such file or directory: {args}")
                        except NotADirectoryError:
                            completedProcess = 127
                            print(f"Error:- Not a directory: {args}")
                        except PermissionError:
                            completedProcess = 126
                            print(f"Error:- Permission denied: {args}")
                case "mkcd":
                    if not args:
                        completedProcess = 20
                        print(f"Error: Invalid arguments")
                        usage_message("mkcd")
                    else:
                        try:
                            os.makedirs(args, exist_ok=True)
                            os.chdir(args)
                            completedProcess = 0
                        except:
                            completedProcess = 1
                            print(f"Error: Unknown")
                case "uprepo":
                    completedProcess = subprocess.run("git pull", shell=True).returncode
                case "sp":
                    match args:
                        case "-web":
                            os.makedirs("html", exist_ok=True)
                            os.makedirs("css", exist_ok=True)
                            os.makedirs("js", exist_ok=True)
                            os.makedirs("libs", exist_ok=True)
                            completedProcess = subprocess.run("touch index.html", shell=True).returncode
                            completedProcess = subprocess.run("touch html/main.html", shell=True).returncode
                            completedProcess = subprocess.run("touch css/style.css", shell=True).returncode
                            completedProcess = subprocess.run("touch js/script.js", shell=True).returncode
                            completedProcess = subprocess.run("echo '<!DOCTYPE html>\n<html lang=\"en\">\n    <head>\n        <meta charset=\"UTF-8\">\n        <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n        <title>Document</title>\n        <link rel=\"stylesheet\" href=\"style.css\">\n        <script src=\"script.js\"></script>\n    </head>\n    <body>\n        \n    </body>\n</html>' > index.html", shell=True).returncode
                        case "-py":
                            os.makedirs("tests", exist_ok=True)
                            os.makedirs("libs", exist_ok=True)
                            os.makedirs("venv", exist_ok=True)
                            completedProcess = subprocess.run("touch main.py", shell=True).returncode
                            completedProcess = subprocess.run("echo 'def main() -> None:\\n    print(\"Hello World!\")\\n\\nif __name__ == \"__main__\":\\n    main()' > main.py", shell=True).returncode
                        case "-cpp":
                            os.makedirs("output", exist_ok=True)
                            os.makedirs("bin", exist_ok=True)
                            completedProcess = subprocess.run("touch main.cpp", shell=True).returncode
                            completedProcess = subprocess.run("echo '#include <iostream>\n\nusing namespace std;\n\nint main() {\n\tcout << \"Hello World!\" << endl;\n\treturn 0;\n}' > main.cpp", shell=True).returncode
                        case _:
                            completedProcess = 20
                            print(f"Error: Invalid arguments")
                            usage_message("sp")
                case "cleanup":
                    completedProcess = subprocess.run("sudo apt-get clean && sudo apt-get autoremove -y", shell=True).returncode
                case "url":
                    completedProcess = subprocess.run(f"xdg-open {args}", shell=True).returncode
                case "lsc":
                    sort = sorted(commands)
                    for i in range(len(commands)):
                        print(f"{i+1}. {sort[i]}")
                    completedProcess = 0
                case "brc":
                    completedProcess = subprocess.run("vim ~/.bashrc", shell=True).returncode
                case "zrc":
                    completedProcess = subprocess.run("vim ~/.zshrc", shell=True).returncode
                case "touch":
                    if not args:
                        completedProcess = 20
                        print(f"Error: Invalid arguments")
                        usage_message("touch")
                    else:
                        completedProcess = subprocess.run(f"touch {args}", shell=True).returncode
                case "rm":
                    if not args:
                        completedProcess = 20
                        print(f"Error: Invalid arguments")
                        usage_message("rm")
                    else:
                        completedProcess = subprocess.run(f"rm -rf {args}", shell=True).returncode
                case "mv":
                    if not args:
                        completedProcess = 20
                        print(f"Error: Invalid arguments")
                        usage_message("mv")
                    else:
                        completedProcess = subprocess.run(f"mv {args}", shell=True).returncode
                case "cp":
                    if not args:
                        completedProcess = 20
                        print(f"Error: Invalid arguments")
                        usage_message("cp")
                    else:
                        completedProcess = subprocess.run(f"cp -r {args}", shell=True).returncode
                case "grep":
                    if not args:
                        completedProcess = 20
                        print(f"Error: Invalid arguments")
                        usage_message("grep")
                    else:
                        completedProcess = subprocess.run(f"grep {args}", shell=True).returncode
                case "find":
                    if not args:
                        completedProcess = 20
                        print(f"Error: Invalid arguments")
                        usage_message("find")
                    else:
                        completedProcess = subprocess.run(f"find {args}", shell=True).returncode
                case "cat":
                    if not args:
                        completedProcess = 20
                        print(f"Error: Invalid arguments")
                        usage_message("cat")
                    else:
                        completedProcess = subprocess.run(f"cat {args}", shell=True).returncode
                case "echo":
                    if not args:
                        completedProcess = 20
                        print(f"Error: Invalid arguments")
                        usage_message("echo")
                    else:
                        completedProcess = subprocess.run(f"echo {args}", shell=True).returncode
                case "date":
                    completedProcess = subprocess.run("date", shell=True).returncode
                case "tree":
                    completedProcess = subprocess.run(f"tree {args}", shell=True).returncode
                case "pwd":
                    completedProcess = subprocess.run("pwd", shell=True).returncode
                case "gc":
                    if not args:
                        completedProcess = 20
                        print(f"Error: Invalid arguments")
                        usage_message("gc")
                    else:
                        completedProcess = subprocess.run(f"git clone {args}", shell=True).returncode
                case "ai":
                    if not args:
                        completedProcess = subprocess.run("xdg-open http://chatgpt.com", shell=True).returncode
                    elif "-gpt" in args:
                        completedProcess = subprocess.run("xdg-open http://chatgpt.com", shell=True).returncode
                    elif "-cop" in args:
                        completedProcess = subprocess.run("xdg-open https://copilot.microsoft.com/", shell=True).returncode
                    elif "-gem" in args:
                        completedProcess = subprocess.run("xdg-open https://gemini.google.com/", shell=True).returncode
                    elif "-perp" in args:
                        completedProcess = subprocess.run("xdg-open https://perplexity.ai", shell=True).returncode
                    elif "-leo" in args:
                        completedProcess = subprocess.run("xdg-open https://leonardo.ai/", shell=True).returncode 
                    else:
                        completedProcess = 20
                        print(f"Error: Invalid arguments")
                        usage_message("ai")     
                case "ask":
                    if not args:
                        completedProcess = 20
                        print(f"Error: Invalid arguments")
                        usage_message("ask")
                    elif "-ai" in args:
                        completedProcess = subprocess.run("xdg-open http://chatgpt.com", shell=True).returncode
                        time.sleep(4)
                        pyautogui.moveTo(861, 1022)
                        pyautogui.typewrite(args.split("-ai")[1], 0.03)
                        pyautogui.press("enter")
                        completedProcess = 0
                    elif "-ggl" in args:
                        completedProcess = subprocess.run("xdg-open http://www.google.com/search?q="+(args.split("-ggl")[1]).replace(" ", "+"), shell=True).returncode
                    elif "-rdt" in args:
                        try:
                            args = args.split("-rdt")[1].strip()
                            title, body, subreddit = args.split('---')
                            completedProcess = subprocess.run("xdg-open https://www.reddit.com/submit?type=TEXT", shell=True).returncode
                            time.sleep(4)

                            pyautogui.click(658, 429)
                            pyautogui.typewrite(title, 0.03)
                            
                            pyautogui.click(623, 606)
                            pyautogui.typewrite(body, 0.03)
                    
                            pyautogui.click(640, 300)
                            pyautogui.typewrite(subreddit, 0.03)
                            pyautogui.press("down")
                            pyautogui.press("enter")

                            pyautogui.click(1142, 726)
                            completedProcess = 0
                        except:
                            completedProcess = 139
                            print(f"Error: Segmentation fault")
                            usage_message("ask")
                    else:
                        completedProcess = 20
                        print(f"Error: Invalid arguments")
                        usage_message("ask")
                case "mc":
                    try:
                        rfile = open(f"{os.path.expanduser('~')}/.config/ytshell/pathToJar.txt", "r")
                        path = rfile.read()
                        if not args:
                            if not path:
                                completedProcess = 20
                                print(f"Error: Invalid arguments")
                                print("Use the option '-config' to set the path to your games jar file.")
                            else:
                                completedProcess = subprocess.run("java -jar " + path, shell=True).returncode
                        
                        elif "-config" in args:
                            wfile = open(f"{os.path.expanduser('~')}/.config/ytshell/pathToJar.txt", "w")
                            print(args.strip("-config "))
                            wfile.write(args.strip("-config "))
                            wfile.close()
                        rfile.close()
                        completedProcess = 0

                    except:
                        completedProcess = 1
                        print(f"Error: Unkown")
                case "setrepo":
                    if not args:
                        completedProcess = 20
                        print(f"Error: Invalid arguments")
                        usage_message("setrepo")
                    else:
                        os.makedirs(args, exist_ok=True)
                        os.chdir(args)
                        completedProcess = subprocess.run("git init", shell=True).returncode
                        completedProcess = subprocess.run("touch .gitignore", shell=True).returncode
                        completedProcess = subprocess.run("touch README.md", shell=True).returncode
                        completedProcess = subprocess.run(f"echo '# {args}' > README.md", shell=True).returncode
                        completedProcess = subprocess.run("echo '*test\ntest*\nTest*\n*Test\n*.log' > .gitignore", shell=True).returncode
                case "neofun":
                    print(termcolor.colored("""
    ⡆⣐⢕⢕⢕⢕⢕⢕⢕⢕⠅⢗⢕⢕⢕⢕⢕⢕⢕⠕⠕⢕⢕⢕⢕⢕⢕⢕⢕⢕
    ⢐⢕⢕⢕⢕⢕⣕⢕⢕⠕⠁⢕⢕⢕⢕⢕⢕⢕⢕⠅⡄⢕⢕⢕⢕⢕⢕⢕⢕⢕
    ⢕⢕⢕⢕⢕⠅⢗⢕⠕⣠⠄⣗⢕⢕⠕⢕⢕⢕⠕⢠⣿⠐⢕⢕⢕⠑⢕⢕⠵⢕
    ⢕⢕⢕⢕⠁⢜⠕⢁⣴⣿⡇⢓⢕⢵⢐⢕⢕⠕⢁⣾⢿⣧⠑⢕⢕⠄⢑⢕⠅⢕
    ⢕⢕⠵⢁⠔⢁⣤⣤⣶⣶⣶⡐⣕⢽⠐⢕⠕⣡⣾⣶⣶⣶⣤⡁⢓⢕⠄⢑⢅⢑
    ⠍⣧⠄⣶⣾⣿⣿⣿⣿⣿⣿⣷⣔⢕⢄⢡⣾⣿⣿⣿⣿⣿⣿⣿⣦⡑⢕⢤⠱⢐
    ⢠⢕⠅⣾⣿⠋⢿⣿⣿⣿⠉⣿⣿⣷⣦⣶⣽⣿⣿⠈⣿⣿⣿⣿⠏⢹⣷⣷⡅⢐
    ⣔⢕⢥⢻⣿⡀⠈⠛⠛⠁⢠⣿⣿⣿⣿⣿⣿⣿⣿⡀⠈⠛⠛⠁⠄⣼⣿⣿⡇⢔
    ⢕⢕⢽⢸⢟⢟⢖⢖⢤⣶⡟⢻⣿⡿⠻⣿⣿⡟⢀⣿⣦⢤⢤⢔⢞⢿⢿⣿⠁⢕
    ⢕⢕⠅⣐⢕⢕⢕⢕⢕⣿⣿⡄⠛⢀⣦⠈⠛⢁⣼⣿⢗⢕⢕⢕⢕⢕⢕⡏⣘⢕
    ⢕⢕⠅⢓⣕⣕⣕⣕⣵⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣷⣕⢕⢕⢕⢕⡵⢀⢕⢕
    ⢑⢕⠃⡈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢃⢕⢕⢕
    ⣆⢕⠄⢱⣄⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢁⢕⢕⠕⢁
    ⣿⣦⡀⣿⣿⣷⣶⣬⣍⣛⣛⣛⡛⠿⠿⠿⠛⠛⢛⣛⣉⣭⣤⣂⢜⠕⢑⣡⣴⣿
    """, attrs=["bold"]))
                    completedProcess = 0
                case "fuckyou":
                    print(termcolor.colored("""
    ⠐⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠂
    ⠄⠄⣰⣾⣿⣿⣿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣆⠄⠄
    ⠄⠄⣿⣿⣿⡿⠋⠄⡀⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠋⣉⣉⣉⡉⠙⠻⣿⣿⠄⠄
    ⠄⠄⣿⣿⣿⣇⠔⠈⣿⣿⣿⣿⣿⡿⠛⢉⣤⣶⣾⣿⣿⣿⣿⣿⣿⣦⡀⠹⠄⠄
    ⠄⠄⣿⣿⠃⠄⢠⣾⣿⣿⣿⠟⢁⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠄⠄
    ⠄⠄⣿⣿⣿⣿⣿⣿⣿⠟⢁⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠄⠄
    ⠄⠄⣿⣿⣿⣿⣿⡟⠁⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄⠄
    ⠄⠄⣿⣿⣿⣿⠋⢠⣾⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⠄⠄
    ⠄⠄⣿⣿⡿⠁⣰⣿⣿⣿⣿⣿⣿⣿⣿⠗⠄⠄⠄⠄⣿⣿⣿⣿⣿⣿⣿⡟⠄⠄
    ⠄⠄⣿⡿⠁⣼⣿⣿⣿⣿⣿⣿⡿⠋⠄⠄⠄⣠⣄⢰⣿⣿⣿⣿⣿⣿⣿⠃⠄⠄
    ⠄⠄⡿⠁⣼⣿⣿⣿⣿⣿⣿⣿⡇⠄⢀⡴⠚⢿⣿⣿⣿⣿⣿⣿⣿⣿⡏⢠⠄⠄
    ⠄⠄⠃⢰⣿⣿⣿⣿⣿⣿⡿⣿⣿⠴⠋⠄⠄⢸⣿⣿⣿⣿⣿⣿⣿⡟⢀⣾⠄⠄
    ⠄⠄⢀⣿⣿⣿⣿⣿⣿⣿⠃⠈⠁⠄⠄⢀⣴⣿⣿⣿⣿⣿⣿⣿⡟⢀⣾⣿⠄⠄
    ⠄⠄⢸⣿⣿⣿⣿⣿⣿⣿⠄⠄⠄⠄⢶⣿⣿⣿⣿⣿⣿⣿⣿⠏⢀⣾⣿⣿⠄⠄
    ⠄⠄⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⠋⣠⣿⣿⣿⣿⠄⠄
    ⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢁⣼⣿⣿⣿⣿⣿⠄⠄
    ⠄⠄⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢁⣴⣿⣿⣿⣿⣿⣿⣿⠄⠄
    ⠄⠄⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⢁⣴⣿⣿⣿⣿⠗⠄⠄⣿⣿⠄⠄
    ⠄⠄⣆⠈⠻⢿⣿⣿⣿⣿⣿⣿⠿⠛⣉⣤⣾⣿⣿⣿⣿⣿⣇⠠⠺⣷⣿⣿⠄⠄
    ⠄⠄⣿⣿⣦⣄⣈⣉⣉⣉⣡⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⠉⠁⣀⣼⣿⣿⣿⠄⠄
    ⠄⠄⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣾⣿⣿⡿⠟⠄⠄
    ⠠⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
    """, "red"))
                    completedProcess = 0
                case "vsc":
                    completedProcess = subprocess.run("code", shell=True).returncode
                case "vsci":
                    completedProcess = subprocess.run("code-insiders", shell=True).returncode
                case "history":
                    if not args:
                        historyFile = open(f"{os.path.expanduser('~')}/.config/ytshell/history.txt", "r")
                        print(historyFile.read())
                        historyFile.close()
                        completedProcess = 0
                    elif "-clear" in args:
                        historyFile = open(f"{os.path.expanduser('~')}/.config/ytshell/history.txt", "w")
                        historyFile.write("")
                        historyFile.close()
                        print("Cleared history")
                        completedProcess = 0
                    else:
                        completedProcess = 20
                        print(f"Error: Invalid arguments")
                        usage_message("history")
                case "ytpm":
                    if not args:
                        completedProcess = 20
                        print(f"Error: Invalid arguments")
                        usage_message("ytpm")
                    elif "-install" in args:
                        completedProcess = subprocess.run(f"sudo apt install {args.split('-install ')[1]}", shell=True).returncode
                    elif "-rm" in args:
                        completedProcess = subprocess.run(f"sudo apt remove {args.split('-rm ')[1]}", shell=True).returncode
                    elif "-ls" in args:
                        completedProcess = subprocess.run("sudo apt list", shell=True).returncode
                    elif "-search" in args:
                        completedProcess = subprocess.run(f"sudo apt search {args.split('-search ')[1]}", shell=True).returncode
                    elif "-show" in args:
                        completedProcess = subprocess.run(f"sudo apt show {args.split('-show ')[1]}", shell=True).returncode
                    elif "-autorm" in args:
                        completedProcess = subprocess.run(f"sudo apt autoremove {args.split('-autorm ')[1]}", shell=True).returncode
                    elif "-reinstall" in args:
                        completedProcess = subprocess.run(f"sudo apt reinstall {args.split('-reinstall ')[1]}", shell=True).returncode
                    elif "-update":
                        completedProcess = subprocess.run("sudo apt update", shell=True).returncode
                    elif "-upgrade":
                        completedProcess = subprocess.run("sudo apt upgrade", shell=True).returncode
                    elif "-fupgrade":
                        completedProcess = subprocess.run("sudo apt full-upgrade", shell=True).returncode
                    elif "-source-edit":
                        completedProcess = subprocess.run("sudo apt edit-sources", shell=True).returncode
                    elif "-satisfy" in args:
                        completedProcess = subprocess.run(f"sudo apt satisfy {args.split('-satisfy ')[1]}", shell=True).returncode
                    else:
                        completedProcess = 20
                        print(f"Error: Invalid arguments")
                        usage_message("ytpm")
                case "theme":
                    if not args:
                        themeFile = open(f"{os.path.expanduser('~')}/.config/ytshell/theme.txt", "r")
                        print(themeFile.read())
                        themeFile.close()
                        completedProcess = 0
                    elif "-edit" in args:
                        arg = args.split("-edit ")[1].split(" ")
                        themeFile = open(f"{os.path.expanduser('~')}/.config/ytshell/theme.txt", "w")
                        themeFile.write(f"""get_prompt()-bg={arg[0]},
get_prompt()-txt={arg[1]},
time-bg={arg[2]},
time-txt={arg[3]},
stat-bg={arg[4]},
stat-txt={arg[5]},
stat-err-bg={arg[6]},
stat-err-txt={arg[7]}""")
                        themeFile.close()
                        completedProcess = 0
                    else:
                        completedProcess = 20
                        print(f"Error: Invalid arguments")
                        usage_message("theme")
                case "config":
                    if not args:
                        configFile = open(f"{os.path.expanduser('~')}/.config/ytshell/config.txt", "r")
                        print(configFile.read())
                        configFile.close()
                    elif "-edit" in args:
                        arg = args.split("-edit ")[1].split(" ")
                        configFile = open(f"{os.path.expanduser('~')}/.config/ytshell/config.txt", "w")
                        configFile.write(f"""time={arg[0]},
timeFormat={arg[1]},
get_prompt()Char={arg[2]}""")
                        configFile.close()
                        completedProcess = 0
                    else:
                        completedProcess = 20
                        print(f"Error: Invalid arguments")
                        usage_message("config")
                case "graph":
                    try:
                        print("Click on the graph window to exit")
                        graph(args.split(",")[0].lower().replace("^", "**"), args.split(",")[1])
                        completedProcess = 0
                    except:
                        completedProcess = 20
                        print("Error: Invalid arguments")
                        usage_message("graph")
                case "sudo":
                    completedProcess = subprocess.run(f"sudo {args}", shell=True).returncode
                case "root":
                    completedProcess = subprocess.run(f"sudo python3 ~/.config/ytshell/main.py", shell=True).returncode
                case "exit":
                    completedProcess = 0
                    exit()
                case _:
                    completedProcess = 126
                    print(f"Error: Command invoked cannot be executed")
            print("\n")
        except KeyboardInterrupt:
            subprocess.run("clear", shell=True)
            completedProcess = 130
            pass

if __name__ == "__main__":
    main()