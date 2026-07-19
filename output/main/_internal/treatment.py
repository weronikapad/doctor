import subprocess
from groq import Groq
from diagnose import report
from command_database import commands
import ctypes, sys
#if there's time when the function requred admin create a new file and in that file import ai_commands and run the yk the ones that haven't been run 


print("\n\nRUNNING SYSTEM TREATMENT\n")

AI = open("API.txt").read().strip()
api = Groq(api_key =AI)


#groq currating all the commands that it thinks that will work
def ai_command_report(report_text):
    
    print("no problem with the ai")
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
commands_run = []


#if the command has a warning then we will later use it in the countless sriting of if elif else
def warnings(command):
    global ai_commands, commands_run
    if command == "nslookup":

        
        y_or_n = input("\nWould you like to run: " + command + " (y/n)" + "\nDESCRIPTION: " + commands[command]["description"] + "\n")
        if y_or_n == "y":
            nslookup_output = subprocess.run(command.split(), capture_output = True)
            nslookup_output = nslookup_output.stdout.decode("cp1250", errors="replace")
            print(nslookup_output)
            return nslookup_output
        else:
            print("Skiping over " + command)
            return None
    

    
    if commands[command]["warning"] == True:
            
            y_or_n = input("\nWould you like to run: " + command + " (y/n)" + "\nDESCRIPTION: " + commands[command]["description"] + "\nWARNING: " + commands[command]["warning_note"] + "\n")
            if y_or_n == "y":
                if commands[command]["admin_required"] == True:
                    if __name__ == '__main__':
                        if is_admin():
                            print("Running as admin\n")
                            if commands[command]["further_decisions_inteminal"] == True:
                                val = subprocess.run(command.split())
                                print(val)
                                print("\nsuccessfully run\n")
                                return "User ran this command interactively. No text output was captured."
                            else: 
                                raw_value = subprocess.run(command.split(), capture_output = True)
                                val = raw_value.stdout.decode("cp1250", errors="replace")
                                print("\nsuccessfully run\n")
                                return val
                        else:
                            choice = input(f"\n{command} requires admin to be executed, do you authorise the admin rights? (y/n): \n")
                            if choice == "y":
                                ai_commands = [x for x in ai_commands if x not in commands_run]
                                ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
                                sys.exit()
                                print("Running as admin\n")
                                if commands[command]["further_decisions_inteminal"] == True:
                                    val = subprocess.run(command.split())
                                    print(val)
                                    print("\nsuccessfully run\n")
                                    return "User ran this command interactively. No text output was captured."
                                else: 
                                    raw_value = subprocess.run(command.split(), capture_output = True)
                                    val = raw_value.stdout.decode("cp1250", errors="replace")
                                    print("\nsuccessfully run\n")
                                    return val
                            elif choice == "n":
                                print("\nSkipping over " + command)
                            else:
                                print("Error: unrecognised user input")
                    else:
                        print("\nLoged in user does not have the administrator rights, and the proram will be unable to exectute this command\n")
                #command has a warning, if the anwser to y_or_n is still y but admin is not requried
                else:
                #i think it will hold the the varible value so i can later use it for further analysis and printing out value
                    print(f"\nRunning command {command}")
                    if commands[command]["further_decisions_inteminal"] == True:
                        val = subprocess.run(command.split())
                        print(val)
                        print("\nsuccessfully run\n")
                        return "User ran this command interactively. No text output was captured."
                    else: 
                        raw_value = subprocess.run(command.split(), capture_output = True)
                        val = raw_value.stdout.decode("cp1250", errors="replace")
                        print("\nsuccessfully run\n")
                        return val
            elif y_or_n == "n":
                return None
            else:
                print("\nError: urecognised input\n")
                return None
    #not admin_required
    else:
        y_or_n = input("\nWould you like to run: " + command + " (y/n)" + "\nDESCRIPTION: " + commands[command]["description"]+"\n" )
        if y_or_n == "y":
            if commands[command]["admin_required"] == True:
                if __name__ == '__main__':
                    if is_admin():
                        print("Running as admin\n")
                        if commands[command]["further_decisions_inteminal"] == True:
                            val = subprocess.run(command.split())
                            print(val)
                            print("\nsuccessfully run\n")
                            return "User ran this command interactively. No text output was captured."
                        else: 
                            raw_value = subprocess.run(command.split(), capture_output = True)
                            val = raw_value.stdout.decode("cp1250", errors="replace")
                            print("\nsuccessfully run\n")
                            return val
                    else:
                        choice = input(f"\n{command} requires admin to be executed, do you authorise the admin rights? (y/n): \n")
                        if choice == "y":
                            ai_commands = [x for x in ai_commands if x not in commands_run]
                            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
                            sys.exit() #stops running the program in the termial but it doesn't close the terminal\ does this have anything to do wth restartment?
                            print("Running as admin\n")
                            if commands[command]["further_decisions_inteminal"] == True:
                                val = subprocess.run(command.split())
                                print(val)
                                print("\nsuccessfully run\n")
                                return "User ran this command interactively. No text output was captured."
                            else: 
                                raw_value = subprocess.run(command.split(), capture_output = True)
                                val = raw_value.stdout.decode("cp1250", errors="replace")
                                print("\nsuccessfully run\n")
                                return val
                        elif choice == "n":
                            print("\nSkipping over " + command)
                        else:
                            print("Error: unrecognised user input")
                else:
                    print("\nLoged in user does not have the administrator rights, and the proram will be unable to exectute this command\n")
        #commnd isn't in warning, y_or_n == "y", admin_requred == False
            else: 
                if commands[command]["further_decisions_inteminal"] == True:
                    val = subprocess.run(command.split())
                    print(val)
                    print("\nsuccessfully run\n")
                    return "User ran this command interactively. No text output was captured."
                else: 
                    raw_value = subprocess.run(command.split(), capture_output = True)
                    val = raw_value.stdout.decode("cp1250", errors="replace")
                    print("\nsuccessfully run\n")
                    return val
        elif y_or_n == "n":
            return None
        else:
            print("error: urcognised input")
            return None
        


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
    
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
    if command in commands: 
        value = warnings(command)
        if commands[command]["further_analysis"] == True:
            if value is not None: 
                print("\nRunnig AI analysis of the report: \n")
                commands_run.append(command)
                print(analysis(value))

        elif commands[command]["print_value"] == True:
            if value is not None: 
                print("\nCommand output: \n")
                commands_run.append(command)
                print(value)

        elif commands[command]["further_decisions_inteminal"] == True:
            if value is not None:
                commands_run.append(command) 
        else:
            print(value)
    else:
       print("\nThe command " + command + " was not found in the database")
        


