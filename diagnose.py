import subprocess
from groq import Groq
#checking if it's even working
print("\nRUNING SYSTEM DIGNOSIS\n\n")

def fetch_windows_logs(): 
    data = subprocess.run(["powershell", "-Command", "Get-WinEvent -LogName System -MaxEvents 150"], capture_output=True)
  
    rawdata = data.stdout
    rawtext = rawdata.decode("cp1250", errors="replace")

    return rawtext
# test the function: print(fetch_windows_logs())

AI = open("API.txt").read().strip()

api = Groq(api_key =AI)

print("This is an ai analyse report,")
print("plsc do not take everything for granted, some informaion may be wrong\n")

def ai_report(rawtext):
    ai_analyser = api.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": """Analyze this windows log in context of any thing that might me causing any problems with the pc, and give a report of what you find in this format
                problem | exact log which indicated that problem | posible solution, do state that is is posible and that it might not work |
                , if you find nothing, say so."""
            },
            {
                "role": "user",
                "content": rawtext
            }
        ] 
    ) 

    ai_output = ai_analyser.choices[0].message.content
    return ai_output

scanned_logs = fetch_windows_logs()
report = ai_report(scanned_logs)
print(report)



