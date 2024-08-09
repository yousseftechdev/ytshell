import subprocess
import os
import sys
import pyautogui
import time

sys.stdout.write("\x1b]2;YTShell\x07")

commands = ["help", "mc", "neofun", "fuckyou", "gc", "dev", "cd", "mkcd", "setrepo", "uprepo", "sp", "url", "cleanup", "lsc", "brc", "zrc", "exit", "touch", "rm", "mv", "cp", "grep", "find", "cat", "echo", "date", "pwd", "ai", "ask"]
try:
    pathFile = open(f"{os.path.expanduser('~')}/.config/ytshell/pathToJar.txt", "x")
    pathFile.close()
except:
    pass

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
    elif command == "cd":
        print("Usage: cd (DIRECTORY)")
        print("Changes the current working directory to the specified argument")
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
        
def is_interactive():
    try:
        return os.isatty(sys.stdin.fileno())
    except Exception:
        return False

def main() -> None:
    all_commands = get_all_commands()

    while True:
        dir = os.getcwd()
        fdir = f"╭─ ~{dir.split('/home')[1]}\n╰─ $ " if "/home" in dir else f"╭─ {dir}\n╰─ $ "

        if is_interactive():
            cmd = input(fdir)
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
                    usage_message("")
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
                    usage_message("")
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
                for i in range(len(commands)):
                    print(f"{i+1}. {commands[i]}")
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
            case "exit":
                exit()
        print("\n")

if __name__ == "__main__":
    main()
