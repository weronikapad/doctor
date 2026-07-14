#import treatment
#import diagnose
#import checkbox_commands
import customtkinter
import sys, subprocess

while True:
    print("running doctor")
    print("\n1. Diagnose system\n2. Treat issues\n3. Experiment with commands\n4. Exit program")

    choice = input("Which one would you like to run (type the number asigner to the program): ")
    choice = int(choice)
    if choice == 1:
        subprocess.run([sys.executable, "diagnose.py"])
    elif choice == 2:
        subprocess.run([sys.executable, "treatment.py"])
    elif choice == 3:
        subprocess.run([sys.executable, "checkbox_commands.py"])
    elif choice == 4:
        sys.exit()
    else:
        print("Sorry your input was unclear could you type it again?")

