#!/usr/bin/env python3
# GLOBALS
global repoUtd
import subprocess
import os
import sys
import pyautogui
import time
import funcs
import datetime
import termcolor
scriptLocation = os.getcwd()
def main() -> None: # type: ignore
    funcs.setup()

    sys.stdout.write("\x1b]2;YTShell\x07")

    readCmdFile = open(f"{os.path.expanduser('~')}/.config/ytshell/commands.txt", "r")
    commands = readCmdFile.read().split(",\n")
    commands[-1] = commands[-1].strip("\n")
    readCmdFile.close()
    all_commands = funcs.get_all_commands()    
    reminders = funcs.load_reminders()

    while True:
        try:
            funcs.check_reminders()
            sys.stdout.write(f"\x1b]2;YTShell - {os.getcwd()}\x07")
            if funcs.is_interactive():
                cmd = input(funcs.get_prompt())
                exitCodeFile = open(f"{os.path.expanduser('~')}/.config/ytshell/exitCodeFile.txt", "w")
                if cmd:
                    historyFile = open(f"{os.path.expanduser('~')}/.config/ytshell/history.txt", "a")
                    historyFile.write(f"{cmd}\n")
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
                        exitCodeFile.write(str(subprocess.run(f"ls --color=auto {args}", shell=True).returncode))
                        exitCodeFile.close()
                    elif cmd == "-":
                        with open(f"{os.path.expanduser('~')}/.config/ytshell/history.txt", "r") as historyFile:
                            exitCodeFile.write(str(subprocess.run(historyFile.read().split("\n")[-1], shell=True).returncode))
                            exitCodeFile.close()
                    else:
                        exitCodeFile.write(str(subprocess.run(f"{cmdSplit} {args}", shell=True).returncode))
                        exitCodeFile.close()
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
                            exitCodeFile.write(str(subprocess.run("xdg-open http://youssef-mostafa1534.github.io/NewModernPortfolio", shell=True).returncode))
                            exitCodeFile.close()
                        case "-yt":
                            exitCodeFile.write(str(subprocess.run("xdg-open https://www.youtube.com/channel/UC00bH694nxRfyRQAWhhu5Mw", shell=True).returncode))
                            exitCodeFile.close()
                        case "-discord":
                            print("Discord username: @yousseftech")
                            print("Discord server: https://discord.gg/qWdASj5Nzh")
                            exitCodeFile.write('0')
                            exitCodeFile.close()
                        case "-github":
                            exitCodeFile.write(str(subprocess.run("xdg-open http://github.com/youssef-mostafa1534", shell=True).returncode))
                            exitCodeFile.close()
                        case _:
                            exitCodeFile.write('20')
                            exitCodeFile.close()
                            print(f"Error: Invalid arguments")
                            funcs.usage_message("dev")
                case "cd":
                    if not args:
                        os.chdir(os.path.expanduser("~"))
                        exitCodeFile.write('0')
                    else:
                        try:
                            os.chdir(args)
                            # Handling history file
                            history_file_path = f"{os.path.expanduser('~')}/.config/ytshell/dirHistory.txt"
                            with open(history_file_path, "a+") as dirHistoryFile:
                                dirHistoryFile.seek(0)  # Move to the beginning of the file
                                paths = dirHistoryFile.read().split(",\n")
                                if args not in paths:
                                    if os.path.getsize(history_file_path) == 0:
                                        dirHistoryFile.write(f"{os.getcwd()}")
                                    else:
                                        dirHistoryFile.write(f",\n{os.getcwd()}")
                            exitCodeFile.write('0')
                        except FileNotFoundError:
                            auto_dir = funcs.dirAutoComplete(args)
                            if auto_dir:
                                os.chdir(auto_dir)
                                exitCodeFile.write('0')
                            else:
                                print(funcs.dirAutoComplete(args))
                                exitCodeFile.write('127')
                                print(f"Error: No such file or directory: {args}")
                        except NotADirectoryError:
                            exitCodeFile.write('127')
                            print(f"Error: Not a directory: {args}")
                        except PermissionError:
                            exitCodeFile.write('126')
                            print(f"Error: Permission denied: {args}")
                    exitCodeFile.close()
                case "mkcd":
                    if not args:
                        exitCodeFile.write('20')
                        exitCodeFile.close()
                        print(f"Error: Invalid arguments")
                        funcs.usage_message("mkcd")
                    else:
                        try:
                            os.makedirs(args, exist_ok=True)
                            os.chdir(args)
                            exitCodeFile.write('0')
                            exitCodeFile.close()
                        except:
                            exitCodeFile.write('1')
                            exitCodeFile.close()
                            print(f"Error: Unknown")
                case "uprepo":
                    exitCodeFile.write(str(subprocess.run("git pull", shell=True).returncode))
                    exitCodeFile.close()
                case "sp":
                    match args:
                        case "-web":
                            os.makedirs("html", exist_ok=True)
                            os.makedirs("css", exist_ok=True)
                            os.makedirs("js", exist_ok=True)
                            os.makedirs("libs", exist_ok=True)
                            exitCodeFile.write(str(subprocess.run("touch index.html", shell=True).returncode))
                            exitCodeFile.write(str(subprocess.run("touch html/main.html", shell=True).returncode))
                            exitCodeFile.write(str(subprocess.run("touch css/style.css", shell=True).returncode))
                            exitCodeFile.write(str(subprocess.run("touch js/script.js", shell=True).returncode))
                            exitCodeFile.write(str(subprocess.run("echo '<!DOCTYPE html>\n<html lang=\"en\">\n    <head>\n        <meta charset=\"UTF-8\">\n        <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n        <title>Document</title>\n        <link rel=\"stylesheet\" href=\"style.css\">\n        <script src=\"script.js\"></script>\n    </head>\n    <body>\n        \n    </body>\n</html>' > index.html", shell=True).returncode))
                            exitCodeFile.close()
                        case "-py":
                            os.makedirs("tests", exist_ok=True)
                            os.makedirs("libs", exist_ok=True)
                            os.makedirs("venv", exist_ok=True)
                            exitCodeFile.write(str(subprocess.run("touch main.py", shell=True).returncode))
                            exitCodeFile.write(str(subprocess.run("echo 'def main() -> None:\\n    print(\"Hello World!\")\\n\\nif __name__ == \"__main__\":\\n    main()' > main.py", shell=True).returncode))
                            exitCodeFile.close()
                        case "-cpp":
                            os.makedirs("output", exist_ok=True)
                            os.makedirs("bin", exist_ok=True)
                            exitCodeFile.write(str(subprocess.run("touch main.cpp", shell=True).returncode))
                            exitCodeFile.write(str(subprocess.run("echo '#include <iostream>\n\nusing namespace std;\n\nint main() {\n\tcout << \"Hello World!\" << endl;\n\treturn 0;\n}' > main.cpp", shell=True).returncode))
                            exitCodeFile.close()
                        case _:
                            exitCodeFile.write('20')
                            exitCodeFile.close()
                            print(f"Error: Invalid arguments")
                            funcs.usage_message("sp")
                case "cleanup":
                    if not args:
                        exitCodeFile.write(str(subprocess.run("sudo apt-get clean && sudo apt-get autoremove -y", shell=True).returncode))
                        exitCodeFile.close()
                    else:
                        funcs.usage_message("cleanup")
                        exitCodeFile.write("0")
                        exitCodeFile.close()
                case "url":
                    exitCodeFile.write(str(subprocess.run(f"xdg-open {args}", shell=True).returncode))
                    exitCodeFile.close()
                case "lsc":
                    sort = sorted(commands)
                    for i in range(len(commands)):
                        print(f"{i+1}. {sort[i]}")
                    exitCodeFile.write('0')
                    exitCodeFile.close()
                case "brc":
                    exitCodeFile.write(str(subprocess.run("vim ~/.bashrc", shell=True).returncode))
                    exitCodeFile.close()
                case "zrc":
                    exitCodeFile.write(str(subprocess.run("vim ~/.zshrc", shell=True).returncode))
                    exitCodeFile.close()
                case "rm":
                    if not args:
                        exitCodeFile.write('20')
                        exitCodeFile.close()
                        print(f"Error: Invalid arguments")
                        funcs.usage_message("rm")
                    else:
                        exitCodeFile.write(str(subprocess.run(f"rm -rf {args}", shell=True).returncode))
                        exitCodeFile.close()
                case "gc":
                    if not args:
                        exitCodeFile.write('20')
                        exitCodeFile.close()
                        print(f"Error: Invalid arguments")
                        funcs.usage_message("gc")
                    else:
                        exitCodeFile.write(str(subprocess.run(f"git clone {args}", shell=True).returncode))
                        exitCodeFile.close()
                case "ai":
                    if not args:
                        exitCodeFile.write(str(subprocess.run("xdg-open http://chatgpt.com", shell=True).returncode))
                        exitCodeFile.close()
                    elif "-gpt" in args:
                        exitCodeFile.write(str(subprocess.run("xdg-open http://chatgpt.com", shell=True).returncode))
                        exitCodeFile.close()
                    elif "-cop" in args:
                        exitCodeFile.write(str(subprocess.run("xdg-open https://copilot.microsoft.com/", shell=True).returncode))
                        exitCodeFile.close()
                    elif "-gem" in args:
                        exitCodeFile.write(str(subprocess.run("xdg-open https://gemini.google.com/", shell=True).returncode))
                        exitCodeFile.close()
                    elif "-perp" in args:
                        exitCodeFile.write(str(subprocess.run("xdg-open https://perplexity.ai", shell=True).returncode))
                        exitCodeFile.close()
                    elif "-leo" in args:
                        exitCodeFile.write(str(subprocess.run("xdg-open https://leonardo.ai/", shell=True).returncode))
                        exitCodeFile.close() 
                    else:
                        exitCodeFile.write('20')
                        exitCodeFile.close()
                        print(f"Error: Invalid arguments")
                        funcs.usage_message("ai")     
                case "ask":
                    if not args:
                        exitCodeFile.write('20')
                        exitCodeFile.close()
                        print(f"Error: Invalid arguments")
                        funcs.usage_message("ask")
                    elif "-ai" in args:
                        exitCodeFile.write(str(subprocess.run("xdg-open http://chatgpt.com", shell=True).returncode))
                        time.sleep(4)
                        pyautogui.moveTo(861, 1022)
                        pyautogui.typewrite(args.split("-ai")[1], 0.03)
                        pyautogui.press("enter")
                        exitCodeFile.write('0')
                        exitCodeFile.close()
                    elif "-ggl" in args:
                        exitCodeFile.write(str(subprocess.run("xdg-open http://www.google.com/search?q="+(args.split("-ggl")[1]).replace(" ", "+"), shell=True).returncode))
                        exitCodeFile.close()
                    elif "-rdt" in args:
                        try:
                            args = args.split("-rdt")[1].strip()
                            title, body, subreddit = args.split('---')
                            exitCodeFile.write(str(subprocess.run("xdg-open https://www.reddit.com/submit?type=TEXT", shell=True).returncode))
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
                            exitCodeFile.write('0')
                            exitCodeFile.close()
                        except:
                            exitCodeFile.write('139')
                            exitCodeFile.close()
                            print(f"Error: Segmentation fault")
                            funcs.usage_message("ask")
                    else:
                        exitCodeFile.write('20')
                        exitCodeFile.close()
                        print(f"Error: Invalid arguments")
                        funcs.usage_message("ask")
                case "mc":
                    try:
                        rfile = open(f"{os.path.expanduser('~')}/.config/ytshell/pathToJar.txt", "r")
                        path = rfile.read()
                        if not args:
                            if not path:
                                exitCodeFile.write('20')
                                exitCodeFile.close()
                                print(f"Error: Invalid arguments")
                                print("Use the option '-config' to set the path to your games jar file.")
                            else:
                                exitCodeFile.write(str(subprocess.run("java -jar " + path, shell=True).returncode))
                                exitCodeFile.close()
                        
                        elif "-config" in args:
                            wfile = open(f"{os.path.expanduser('~')}/.config/ytshell/pathToJar.txt", "w")
                            print(args.strip("-config "))
                            wfile.write(args.strip("-config "))
                            wfile.close()
                        rfile.close()
                        exitCodeFile.write('0')
                        exitCodeFile.close()

                    except:
                        exitCodeFile.write('1')
                        exitCodeFile.close()
                        print(f"Error: Unkown")
                case "setrepo":
                    if not args:
                        exitCodeFile.write('20')
                        exitCodeFile.close()
                        print(f"Error: Invalid arguments")
                        funcs.usage_message("setrepo")
                    else:
                        os.makedirs(args, exist_ok=True)
                        os.chdir(args)
                        exitCodeFile.write(str(subprocess.run("git init", shell=True).returncode))
                        exitCodeFile.write(str(subprocess.run("touch .gitignore", shell=True).returncode))
                        exitCodeFile.write(str(subprocess.run("touch README.md", shell=True).returncode))
                        exitCodeFile.write(str(subprocess.run(f"echo '# {args}' > README.md", shell=True).returncode))
                        exitCodeFile.write(str(subprocess.run("echo '*test\ntest*\nTest*\n*Test\n*.log' > .gitignore", shell=True).returncode))
                        exitCodeFile.close()
                case "neofun":
                    funcs.print_neofun()
                    exitCodeFile.write('0')
                    exitCodeFile.close()
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
                    exitCodeFile.write('0')
                    exitCodeFile.close()
                case "vsc":
                    if not args:
                        exitCodeFile.write(str(subprocess.run("code", shell=True).returncode))
                        exitCodeFile.close()
                    else:
                        exitCodeFile.write(str(subprocess.run(f"code {args}", shell=True).returncode))
                        exitCodeFile.close()
                case "vsci":
                    if not args:
                        exitCodeFile.write(str(subprocess.run("code-insiders", shell=True).returncode))
                        exitCodeFile.close()
                    else:
                        exitCodeFile.write(str(subprocess.run(f"code-insiders {args}", shell=True).returncode))
                        exitCodeFile.close()
                case "history":
                    if not args:
                        historyFile = open(f"{os.path.expanduser('~')}/.config/ytshell/history.txt", "r")
                        print(historyFile.read())
                        historyFile.close()
                        exitCodeFile.write('0')
                        exitCodeFile.close()
                    elif "-clear" in args:
                        historyFile = open(f"{os.path.expanduser('~')}/.config/ytshell/history.txt", "w")
                        historyFile.write("")
                        historyFile.close()
                        print("Cleared history")
                        exitCodeFile.write('0')
                        exitCodeFile.close()
                    else:
                        exitCodeFile.write('20')
                        exitCodeFile.close()
                        print(f"Error: Invalid arguments")
                        funcs.usage_message("history")
                case "ytpm":
                    if not args:
                        exitCodeFile.write('20')
                        exitCodeFile.close()
                        print(f"Error: Invalid arguments")
                        funcs.usage_message("ytpm")
                    elif "-install" in args:
                        exitCodeFile.write(str(subprocess.run(f"sudo apt install {args.split('-install ')[1]}", shell=True).returncode))
                        exitCodeFile.close()
                    elif "-rm" in args:
                        exitCodeFile.write(str(subprocess.run(f"sudo apt remove {args.split('-rm ')[1]}", shell=True).returncode))
                        exitCodeFile.close()
                    elif "-ls" in args:
                        exitCodeFile.write(str(subprocess.run("sudo apt list", shell=True).returncode))
                        exitCodeFile.close()
                    elif "-search" in args:
                        exitCodeFile.write(str(subprocess.run(f"sudo apt search {args.split('-search ')[1]}", shell=True).returncode))
                        exitCodeFile.close()
                    elif "-show" in args:
                        exitCodeFile.write(str(subprocess.run(f"sudo apt show {args.split('-show ')[1]}", shell=True).returncode))
                        exitCodeFile.close()
                    elif "-autorm" in args:
                        exitCodeFile.write(str(subprocess.run(f"sudo apt autoremove {args.split('-autorm ')[1]}", shell=True).returncode))
                        exitCodeFile.close()
                    elif "-reinstall" in args:
                        exitCodeFile.write(str(subprocess.run(f"sudo apt reinstall {args.split('-reinstall ')[1]}", shell=True).returncode))
                        exitCodeFile.close()
                    elif "-update":
                        exitCodeFile.write(str(subprocess.run("sudo apt update", shell=True).returncode))
                        exitCodeFile.close()
                    elif "-upgrade":
                        exitCodeFile.write(str(subprocess.run("sudo apt upgrade", shell=True).returncode))
                        exitCodeFile.close()
                    elif "-fupgrade":
                        exitCodeFile.write(str(subprocess.run("sudo apt full-upgrade", shell=True).returncode))
                        exitCodeFile.close()
                    elif "-source-edit":
                        exitCodeFile.write(str(subprocess.run("sudo apt edit-sources", shell=True).returncode))
                        exitCodeFile.close()
                    elif "-satisfy" in args:
                        exitCodeFile.write(str(subprocess.run(f"sudo apt satisfy {args.split('-satisfy ')[1]}", shell=True).returncode))
                        exitCodeFile.close()
                    else:
                        exitCodeFile.write('20')
                        exitCodeFile.close()
                        print(f"Error: Invalid arguments")
                        funcs.usage_message("ytpm")
                case "theme":
                    if not args:
                        themeFile = open(f"{os.path.expanduser('~')}/.config/ytshell/theme.txt", "r")
                        print(themeFile.read())
                        themeFile.close()
                        exitCodeFile.write('0')
                        exitCodeFile.close()
                    elif "-edit" in args:
                        arg = args.split("-edit ")[1].split(" ")
                        themeFile = open(f"{os.path.expanduser('~')}/.config/ytshell/theme.txt", "w")
                        themeFile.write(f"""prompt-bg={arg[0]},
prompt-txt={arg[1]},
time-bg={arg[2]},
time-txt={arg[3]},
stat-bg={arg[4]},
stat-txt={arg[5]},
stat-err-bg={arg[6]},
stat-err-txt={arg[7]}""")
                        themeFile.close()
                        exitCodeFile.write('0')
                        exitCodeFile.close()
                    else:
                        exitCodeFile.write('20')
                        exitCodeFile.close()
                        print(f"Error: Invalid arguments")
                        funcs.usage_message("theme")
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
promptChar={arg[2]}""")
                        configFile.close()
                        exitCodeFile.write('0')
                        exitCodeFile.close()
                    else:
                        exitCodeFile.write('20')
                        exitCodeFile.close()
                        print(f"Error: Invalid arguments")
                        funcs.usage_message("config")
                case "graph":
                    try:
                        print("Click on the graph window to exit")
                        funcs.graph(args.split(",")[0].lower().replace("^", "**"), args.split(",")[1])
                        exitCodeFile.write('0')
                        exitCodeFile.close()
                    except:
                        exitCodeFile.write('20')
                        exitCodeFile.close()
                        print("Error: Invalid arguments")
                        funcs.usage_message("graph")
                case "tuiclock":
                    while True:
                        print(f'''
╭────────────────────────╮
│                        │
│    {funcs.get_ftime()}   │
│                        │
╰────────────────────────╯

Press Ctrl+C to exit''')

                        time.sleep(1)
                        print("\033[2J\033[H", end="", flush=True)
                case "ascii":
                    if not args:
                        exitCodeFile.write('20')
                        exitCodeFile.close()
                        print("Error: Invalid arguments")
                        funcs.usage_message("ascii")
                    elif len(args.split( )) == 1:
                        try:
                            file = args
                            funcs.ascii_art_command([file, "80", "0.43", "False", "True"])
                            exitCodeFile.write('0')
                            exitCodeFile.close()
                        except:
                            exitCodeFile.write('127')
                            exitCodeFile.close()
                            print(f"Error: No such file or directory: {args}")
                    else:
                        try:
                            file = args.split(" ")[0]
                            cols = args.split(" ")[1]
                            scale = args.split(" ")[2]
                            moreLevels = args.split(" ")[3]
                            useBrail = args.split(" ")[4]
                            funcs.ascii_art_command([file, cols, scale, moreLevels, useBrail])
                            exitCodeFile.write('0')
                            exitCodeFile.close()
                        except FileNotFoundError:
                            exitCodeFile.write('127')
                            exitCodeFile.close()
                            print(f"Error: No such file or directory: {args.split(' ')[0]}")
                        except:
                            exitCodeFile.write('20')
                            exitCodeFile.close()
                            print("Error: Invalid arguments")
                            funcs.usage_message("ascii")
                case "remind":
                    args = funcs.parse_remind_args(args)
                    if args.get("clear"):
                        reminders.clear()
                        funcs.save_reminders(reminders)
                        print("All reminders cleared.")
                    elif args.get("list"):
                        # List all reminders
                        all_reminders = funcs.get_all_reminders()
                        if all_reminders:
                            for reminder in all_reminders:
                                print(f"Reminder: {reminder['name']}, Times: {reminder['times']}, Time Interval: {reminder['time']} {reminder['timeType']}")
                        else:
                            print("No active reminders.")
                    else:
                        funcs.remind_command(args)
                    exitCodeFile.write("0")
                    exitCodeFile.close()
                case "addcmd":
                    if not args:
                        exitCodeFile.write('20')
                        exitCodeFile.close()
                        print(f"Error: Invalid arguments")
                        funcs.usage_message("addcmd")
                    else:
                        with open(f"{os.path.expanduser('~')}/.config/ytshell/commands.txt", "a") as commandsFile:
                            commandsFile.write(f",\n{args}")
                        exitCodeFile.write('0')
                        exitCodeFile.close()
                case "rmcmd":
                    if not args:
                        exitCodeFile.write('20')
                        exitCodeFile.close()
                        print(f"Error: Invalid arguments")
                        funcs.usage_message("rmcmd")
                    else:
                        funcs.remove_item_from_file(f"{os.path.expanduser('~')}/.config/ytshell/commands.txt", args)
                        exitCodeFile.write('0')
                        exitCodeFile.close()
                case "root":
                    exitCodeFile.write(str(subprocess.run(f"sudo python3 {scriptLocation}/main.py", shell=True).returncode))
                    exitCodeFile.close()
                case "exit":
                    exitCodeFile.write('0')
                    exitCodeFile.close()
                    exit()
                case _:
                    exitCodeFile.write('126')
                    exitCodeFile.close()
                    print(f"Error: Command invoked cannot be executed")
            print("\n")
        except KeyboardInterrupt:
            subprocess.run("clear", shell=True)
            exitCodeFile = open(f"{os.path.expanduser('~')}/.config/ytshell/exitCodeFile.txt", "w")
            exitCodeFile.write('130')
            exitCodeFile.close()

if __name__ == "__main__":
    main()