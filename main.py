import subprocess
import os
import sys
import pyautogui
import time
from funcs import *
import datetime
import termcolor

sys.stdout.write("\x1b]2;YTShell\x07")

readCmdFile = open(f"{os.path.expanduser('~')}/.config/ytshell/commands.txt", "r")

commands = readCmdFile.read().split(", ")
commands[-1] = commands[-1].strip("\n")

def main() -> None:
    all_commands = get_all_commands()
    while True:
        dir = os.getcwd()
        currentFolder = os.getcwd().split("/")[-1]
        if currentFolder == os.path.expanduser("~").split("/home/")[1]:
            currentFolder = ""

        fdir = ' '+dir.replace(os.path.expanduser('~'), '~').strip(currentFolder)
        sys.stdout.write(f"\x1b]2;YTShell - {dir}\x07")
        dt = datetime.datetime.now()
        ftime = dt.strftime('%H:%M:%S  %d/%m/%y')
        themeFile = open(f"{os.path.expanduser('~')}/.config/ytshell/theme.txt", "r")
        colors = themeFile.read().split(",")
        promptBg = colors[0].split("prompt-bg = ")[1]
        promptTxt = colors[1].split("prompt-txt = ")[1]
        timeBg = colors[2].split("time-bg = ")[1]
        timeTxt = colors[3].split("time-txt = ")[1]
        prompt = f"╭─{termcolor.colored('', promptBg)+termcolor.colored(fdir, promptTxt, f'on_{promptBg}')+termcolor.colored(currentFolder+' ', promptTxt, f'on_{promptBg}', attrs=['bold'])+termcolor.colored('', promptBg)}·······························{termcolor.colored('', timeBg)+termcolor.colored(' '+ftime+' ', timeTxt, f'on_{timeBg}')+termcolor.colored('', timeBg)}\n│\n╰─ $ " # type: ignore
        if is_interactive():
            cmd = input(prompt)
            historyFile = open(f"{os.path.expanduser('~')}/.config/ytshell/history.txt", "a")
            historyFile.write(f"{cmd}         {ftime}\n\n")
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
                    subprocess.run(f"ls --color=auto {args}", shell=True)
                else:
                    print("Not implemented, running with bash.")
                    subprocess.run(cmd, shell=True)
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
                        subprocess.run("xdg-open http://youssef-mostafa1534.github.io/NewModernPortfolio", shell=True)
                    case "-yt":
                        subprocess.run("xdg-open https://www.youtube.com/channel/UC00bH694nxRfyRQAWhhu5Mw", shell=True)
                    case "-discord":
                        print("Discord username: @yousseftech")
                        print("Discord server: https://discord.gg/qWdASj5Nzh")
                    case "-github":
                        subprocess.run("xdg-open http://github.com/youssef-mostafa1534", shell=True)
                    case _:
                        usage_message("dev")
            case "cd":
                if not args:
                    os.chdir(os.path.expanduser("~"))
                else:
                    try:
                        os.chdir(args)
                    except FileNotFoundError:
                        print(f"No such directory: {args}")
                    except NotADirectoryError:
                        print(f"Not a directory: {args}")
                    except PermissionError:
                        print(f"Permission denied: {args}")
            case "mkcd":
                if not args:
                    usage_message("mkcd")
                else:
                    os.makedirs(args, exist_ok=True)
                    os.chdir(args)
            case "uprepo":
                subprocess.run("git pull", shell=True)
            case "sp":
                match args:
                    case "-web":
                        os.makedirs("html", exist_ok=True)
                        os.makedirs("css", exist_ok=True)
                        os.makedirs("js", exist_ok=True)
                        os.makedirs("libs", exist_ok=True)
                        subprocess.run("touch index.html", shell=True)
                        subprocess.run("touch html/main.html", shell=True)
                        subprocess.run("touch css/style.css", shell=True)
                        subprocess.run("touch js/script.js", shell=True)
                        subprocess.run("echo '<!DOCTYPE html>\n<html lang=\"en\">\n    <head>\n        <meta charset=\"UTF-8\">\n        <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n        <title>Document</title>\n        <link rel=\"stylesheet\" href=\"style.css\">\n        <script src=\"script.js\"></script>\n    </head>\n    <body>\n        \n    </body>\n</html>' > index.html", shell=True)
                    case "-py":
                        os.makedirs("tests", exist_ok=True)
                        os.makedirs("libs", exist_ok=True)
                        os.makedirs("venv", exist_ok=True)
                        subprocess.run("touch main.py", shell=True)
                        subprocess.run("echo 'def main() -> None:\\n    print(\"Hello World!\")\\n\\nif __name__ == \"__main__\":\\n    main()' > main.py", shell=True)
                    case "-cpp":
                        os.makedirs("output", exist_ok=True)
                        os.makedirs("bin", exist_ok=True)
                        subprocess.run("touch main.cpp", shell=True)
                        subprocess.run("echo '#include <iostream>\n\nusing namespace std;\n\nint main() {\n\tcout << \"Hello World!\" << endl;\n\treturn 0;\n}' > main.cpp", shell=True)
                    case _:
                        usage_message("sp")
            case "cleanup":
                subprocess.run("sudo apt-get clean && sudo apt-get autoremove -y", shell=True)
            case "url":
                subprocess.run(f"xdg-open {args}", shell=True)
            case "lsc":
                sort = sorted(commands)
                for i in range(len(commands)):
                    print(f"{i+1}. {sort[i]}")
            case "brc":
                subprocess.run("vim ~/.bashrc", shell=True)
            case "zrc":
                subprocess.run("vim ~/.zshrc", shell=True)
            case "touch":
                if not args:
                    usage_message("touch")
                else:
                    subprocess.run(f"touch {args}", shell=True)
            case "rm":
                if not args:
                    usage_message("rm")
                else:
                    subprocess.run(f"rm -rf {args}", shell=True)
            case "mv":
                if not args:
                    usage_message("mv")
                else:
                    subprocess.run(f"mv {args}", shell=True)
            case "cp":
                if not args:
                    usage_message("cp")
                else:
                    subprocess.run(f"cp -r {args}", shell=True)
            case "grep":
                if not args:
                    usage_message("grep")
                else:
                    subprocess.run(f"grep {args}", shell=True)
            case "find":
                if not args:
                    usage_message("find")
                else:
                    subprocess.run(f"find {args}", shell=True)
            case "cat":
                if not args:
                    usage_message("cat")
                else:
                    subprocess.run(f"cat {args}", shell=True)
            case "echo":
                if not args:
                    usage_message("echo")
                else:
                    subprocess.run(f"echo {args}", shell=True)
            case "date":
                subprocess.run("date", shell=True)
            case "pwd":
                subprocess.run("pwd", shell=True)
            case "gc":
                if not args:
                    usage_message("gc")
                else:
                    subprocess.run(f"git clone {args}", shell=True)
            case "ai":
                if not args:
                    subprocess.run("xdg-open http://chatgpt.com", shell=True)
                elif "-gpt" in args:
                    subprocess.run("xdg-open http://chatgpt.com", shell=True)
                elif "-cop" in args:
                    subprocess.run("xdg-open https://copilot.microsoft.com/", shell=True)
                elif "-gem" in args:
                    subprocess.run("xdg-open https://gemini.google.com/", shell=True)
                elif "-perp" in args:
                    subprocess.run("xdg-open https://perplexity.ai", shell=True)
                elif "-leo" in args:
                    subprocess.run("xdg-open https://leonardo.ai/", shell=True)      
            case "ask":
                if not args:
                    usage_message("ask")
                elif "-ai" in args:
                    subprocess.run("xdg-open http://chatgpt.com", shell=True)
                    time.sleep(4)
                    pyautogui.moveTo(861, 1022)
                    pyautogui.typewrite(args.split("-ai")[1], 0.03)
                    pyautogui.press("enter")
                elif "-ggl" in args:
                    subprocess.run("xdg-open http://www.google.com/search?q="+(args.split("-ggl")[1]).replace(" ", "+"), shell=True)
                elif "-rdt" in args:
                    try:
                        args = args.split("-rdt")[1].strip()
                        title, body, subreddit = args.split('---')
                        subprocess.run("xdg-open https://www.reddit.com/submit?type=TEXT", shell=True)
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
                    except:
                        usage_message("ask")
            case "mc":
                rfile = open(f"{os.path.expanduser('~')}/.config/ytshell/pathToJar.txt", "r")
                path = rfile.read()
                if not args:
                    if not path:
                        print("Use the option '-config' to set the path to your games jar file.")
                    else:
                        subprocess.run("java -jar " + path, shell=True)
                
                elif "-config" in args:
                    wfile = open(f"{os.path.expanduser('~')}/.config/ytshell/pathToJar.txt", "w")
                    print(args.strip("-config "))
                    wfile.write(args.strip("-config "))
                    wfile.close()
                rfile.close()
            case "setrepo":
                if not args:
                    usage_message("setrepo")
                else:
                    os.makedirs(args, exist_ok=True)
                    os.chdir(args)
                    subprocess.run("git init", shell=True)
                    subprocess.run("touch .gitignore", shell=True)
                    subprocess.run("touch README.md", shell=True)
                    subprocess.run(f"echo '# {args}' > README.md", shell=True)
                    subprocess.run("echo '*test\ntest*\nTest*\n*Test\n*.log' > .gitignore", shell=True)
            case "neofun":
                print("""
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
""")
            case "fuckyou":
                print("""
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
""")
            case "vsc":
                subprocess.run("code", shell=True)
            case "vsci":
                subprocess.run("code-insiders", shell=True)
            case "history":
                if not args:
                    historyFile = open(f"{os.path.expanduser('~')}/.config/ytshell/history.txt", "r")
                    print(historyFile.read())
                    historyFile.close()
                elif "-clear" in args:
                    historyFile = open(f"{os.path.expanduser('~')}/.config/ytshell/history.txt", "w")
                    historyFile.write("")
                    historyFile.close()
                else:
                    usage_message("history")
            case "exit":
                exit()
        print("\n")

if __name__ == "__main__":
    setup()
    main()
