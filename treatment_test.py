import subprocess
from groq import Groq
from diagnose import report
from command_database import commands
import ctypes, sys



print("\n\nRUNNING SYSTEM TREATMENT\n")

AI = open("API.txt").read().strip()
api = Groq(api_key =AI)

#groq currating all the commands that it thinks that will work
def ai_command_report(report_text):
    ai_analyser = api.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": f"""Analyse this report and sugest what type of commands may be aplicable from this database: {commands} to those issues, and print them in this EXACT format, no extra text just that EXACT format:
                [command, command, command]"""
            },
            {
                "role": "user",
                "content": report_text
            }
        ] 
    ) 
    
    return ai_analyser.choices[0].message.content

#ai commands but made into idividual
ai_commands = ai_command_report(report)
ai_commands = ai_commands.replace("[", "").replace("]", "").split(", ")

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
    

def admin_commands(command):
    if commands[command]["admin_required"] == True:
            if value is not None:
                choice = input(f"\n{command} reguires admin to be executed, do you authorise the admin rights? (y/n): \n")
                if choice == "y":
                    if __name__ == '__main__':
                        if is_admin():
                            print("Running as admin\n")
                        else:
                            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
                            print("Running as admin\n")
                    else:
                        print("\nLoged in user does not have the administrator rights, and the proram will be unable to exectute this command\n")
                elif choice == "n":
                    print("\nSkipping over " + command)
                else:
                    print("Error: unrecognised user input")
            else:
                print("\nSkipping over " + command)

#if the command has a warning then we will later use it in the countless sriting of if elif else
def warnings(command0):
    if commands[command0]["warning"] == True:
            
            y_or_n = input("Would you like to run: " + command0 + " (y/n)" + "\nDESCRIPTION: " + commands[command0]["description"] + "\nWARNING: " + commands[command0]["warning_note"] + "\n")
            
            if y_or_n == "y":
                if commands[command0]["admin_required"] == True:
                    admin_commands(command0)
                    print(f"\nRunning command {command0}")
                    raw_value = subprocess.run(command0.split(), capture_output = True)
                    val = raw_value.stdout.decode("cp1250", errors="replace")
                    print("\nsuccessfully run\n")
                    return val
                else:
                    admin_commands(command0)
                    print(f"\nRunning command {command0}")
                    raw_value = subprocess.run(command0.split(), capture_output = True)
                    val = raw_value.stdout.decode("cp1250", errors="replace")
                    print("\nsuccessfully run\n")
                    return val
            elif y_or_n == "n":
                 return None
            else:
                 print("\nError: urecognised input\n")
                 return None
    else:
        y_or_n = input("\nWould you like to run: " + command0 + " (y/n)" + "\nDESCRIPTION: " + commands[command0]["description"]+"\n" )
    
        if y_or_n == "y":
            if commands[command0]["admin_required"] == True:
                admin_commands(command0)
                raw_value = subprocess.run(command0.split(), capture_output = True)
                val = raw_value.stdout.decode("cp1250", errors="replace")
                return val
            else:
                admin_commands(command0)
                raw_value = subprocess.run(command0.split(), capture_output = True)
                val = raw_value.stdout.decode("cp1250", errors="replace")
                return val
        elif y_or_n == "n":
            return None
        else:
            print("error: urcognised input")
            return None
        

#ai analysis of the terminal out put
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


#run as admin code from: https://www.reddit.com/r/learnpython/comments/pf1h2z/making_script_run_as_administrator/
print(f"\nAproved commands proposed by ai: {ai_commands}\n")
for command in ai_commands:
    value = warnings(command)
    if command in commands:

        if commands[command]["further_analysis"] == True:
            if value is not None: 
                print("\nRunnig AI analysis of the report: \n")
                print(analysis(value))

        elif commands[command]["print_value"] == True:
            if value is not None: 
                print("\nCommand output: \n")
                print(value)

        elif commands[command]["further_decisions_inteminal"] == True:
            if value is not None:
                print("\nThe command requires further decisions in the terminal: \n")
                print(value)
                user_decision = input("\ntype here: ")
                subprocess.run(user_decision)
        else:
            warnings(command)
    else:
        print("\nThe command " + command + " was not found in the database")
        


