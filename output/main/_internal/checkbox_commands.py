import subprocess
from command_database import commands
from groq import Groq
import ctypes, sys



print("PC still not working? \nTry those commands:\n")

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() 
    except:
        return False

if __name__ == '__main__':
    if is_admin():
        print("Running as admin, all of the commands are enabled to run")
    else:
        choice = input("\nThe app needs the admin rights to run the commands that require an admin, feel free to chose what ever option works for you\nJust know that some commands will not run without admin rights. Type wther or not you authorise admin rights (y/n)\n")
        if choice == "y":
            print("Running as admin, all of the commands are enabled to run")
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
            sys.exit() 
            print("Running as admin, all of the commands are enabled to run")
        elif choice == "n":
            print("Not running as admin")
        else:
            print("Error: unrecognised input")
        
else:
    print("\nThe user can not authorize admin rights and only certain commands will successfuly run\n") 


AI = open("API.txt").read().strip()
api = Groq(api_key =AI)

sorted_commands = sorted(commands, key=lambda k: int(commands[k]["number"]))
for command in sorted_commands:
    print(f"{commands[command]["number"]}. {commands[command]["name"]}\nDESCRIPTION: {commands[command]["description"]}\nWARNING: {commands[command]["warning_note"]}")

numbers = input("Type the numbers of the commands that you want to run here (plsc write it in this type of format: 1, 2, 3): ")

numbers = numbers.replace(",", " ").split()
number_list = []

x = 1
while x < 19:
    if str(x) in numbers:
        number_list.append(x)
    x += 1



def analysis(terminal_output):
    if not terminal_output:
        return "No output for AI to analyse\n"
    ai_analyser = api.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": """Analyse the contect of the window teminal, and create a short and simple report"""
            },
            {
                "role": "user",
                "content": terminal_output
            }
        ] 
    ) 
    ai_analysis = ai_analyser.choices[0].message.content #in the paretees there needs to be a catch output or smth
    return ai_analysis


for number in number_list:
    for command in commands:
        if commands[command]["number"] == number:
            if commands[command]["further_analysis"] == True:
                print(f"Running {command}")
                value = subprocess.run(command.split(), capture_output = True)
                value = value.stdout.decode("cp1250", errors="replace")
                print(f"successfully run {command}")
                print("\nRunnig AI analysis of the report: \n")
                print(analysis(value))
            elif commands[command]["further_decisions_inteminal"] == True:
                print(f"Running {command}")
                subprocess.run(command.split())
                print(f"successfully run {command}")
            elif commands[command]["print_value"] == True:
                print(f"Running {command}")
                value = subprocess.run(command.split(), capture_output = True)
                value = value.stdout.decode("cp1250", errors="replace")
                print(value)
                print(f"successfully run {command}")
            else:
                print(f"Running {command}")
                subprocess.run(command.split())
                print(f"successfully run {command}")

    