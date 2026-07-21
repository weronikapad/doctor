import sys, runpy, os
from groq import Groq

def get_script_path(filename):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, filename)
    return os.path.abspath(filename)

def run_script(filename):
    script_path = get_script_path(filename)
    with open(script_path, "r", encoding="utf-8") as f:
        exec(f.read(), globals())

while True:
    print("running doctor")
    print("\n1. Diagnose system\n2. Diagnose and Treat issues\n3. Experiment with commands\n4. Exit program")

    choice = input("Which one would you like to run (type the number asigner to the program): ")
    choice = int(choice)
    if choice == 1:
        run_script("diagnose.py")
    elif choice == 2:
        run_script("treatment.py")
    elif choice == 3:
        run_script("checkbox_commands.py")
    elif choice == 4:
        sys.exit()
    else:
        print("Sorry your input was unclear could you type it again?")

