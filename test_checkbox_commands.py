import subprocess
from command_database import commands
import customtkinter
import ctypes, sys
print("\nno problem with importing\n")#testing

command_list = ["sfc /scannow", "ipconfig /all", "winget upgrade --all", "cleanmgr /lowdisk", "powercfg /batteryreport", "netsh", "dxdiag", "nslookup", "w32tm /resync", "get-printer", "dism /online /cleanup-image /restorehealth", "gpresult /h FileNameHere.html", "gpupdate /force", "ipconfig /flushdns", "ipconfig /all", "net share", "net user", "chkdsk C: /f", "ipconfig /`flushdns", "sfc /scannow"]

print("PC still not working? \nCheck of the commands that you want to run")

def is_admin():
    print("screen?1")#testing
    try:
        print("screen?2")#testing
        return ctypes.windll.shell32.IsUserAnAdmin() 
    except:
        print("screen?3")#testing
        return False

if __name__ == '__main__':
    print("screen?7")#testing
    if is_admin():
        print("running as admin, all of the commands are enabled to run")
    else:
        print("\nThe app needs the admin rights to run the commands that require an admin, feel free to chose what ever option works for you\nJust know that some commands will not run without admin rights")#testing
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        
else:
    print("\nThe user can not authorize admin rights and only certain commands will successfuly run\n") 


app = customtkinter.CTk()
app.geometry("400x500")
app.title("Command CheckBox")
app.configure(fg_color = "#fffbdc")

print("\nno porblem with app configuration\n")#testing

scrollable_frame = customtkinter.CTkScrollableFrame(master = app, width = 400, height = 500, corner_radius= 5, border_width = 2, bg_color = "pink", fg_color = "light gray")
scrollable_frame.pack(padx = 20, pady = 20)
print("\nno porblem with scrollable frame\n")#testing

commands_to_run = []

for command in commands:
    tracker = customtkinter.StringVar(value = "off")
    print("screen?14")#testing
    checkbox = customtkinter.CTkCheckBox(master = scrollable_frame, text = f"{commands[command]["name"]}\nDESCRIPTION: {commands[command]["description"]}\nWARNING: {commands[command]["warning_note"]}", onvalue = "on", offvalue = "off", text_color = "black", fg_color = "#000C65", variable = tracker)# command = checkbox_event)
    print("screen?15")#testing
    checkbox.pack(pady=10)
    
    actual_command = commands[command]["name"]
    print("screen?15")#testing
    is_admin_requried = commands[command]["admin_required"]
    print("screen?16")#testing
    commands_to_run.append([actual_command, tracker, is_admin_requried])
    print("screen?17")#testing

print(f"\nno porblem with list {commands_to_run}\n")#testing

    
#commands run need to be defined as a list storing all of the commads that were checked on
def button_clicked():
    print("screen?4")#testing
    for item in commands_to_run:
        command = item[0]
        tracker = item[1]
        is_admin_requried = item[2]

        
        if tracker.get() == "on":
            print("screen?5")#testing
            print("after the if tracker.get() == on; this is what command the program will be running: "+ command)#testing
            if is_admin_requried == True:
                print("screen?6")#testing
                if __name__ == '__main__':
                    print("screen?7")#testing
                    if is_admin():
                        print("screen?8")#testing
                        print("\nuser is running as admin and there was no problems with the is_admin function\n")#testing
                        #type_admin = customtkinter.CTkLabel(master = app, text = "running as admin")
                        #type_admin.pack(pady = 10)
                        print(f"The program will NOW run the command: {command}")#testing
                        subprocess.run(command)#this used to be command.split()
                        print("screen?9")#testing
                        tracker.set("off")
                    else:
                        print("\nuser is not admin and there's no problem with the is_admin function\n")#testing
                        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
                        print("screen?10")#testing
                        #type_admin = customtkinter.CTkLabel(master = app, text = "running as admin") #deleted: varible = is_admin
                        #type_admin.pack(pady = 10) 
                        print(f"The program will NOW run the command: {command}")#testing
                        subprocess.run(command)#this used to be command.split()
                        print("screen?11")#testing
                        tracker.set("off")
                else:
                    print("\nno problem if user does not have the admin right\n")#testing /this needs to be visible to the user
                    #type_not_admin = customtkinter.CTkLabel(master = app, text = "loged in user does not have the administrator rights")
                    #type_not_admin.pack(pady = 10)
            else:
                print(f"Running {command}")#testing
                subprocess.run(command.split())
                print("screen?12")#testing
                tracker.set("off")

                

run_button = customtkinter.CTkButton(master = scrollable_frame, text = "Run!", command = button_clicked)
print("screen?13")#testing
run_button.pack(side = "bottom", pady = 10,)


app.mainloop()

