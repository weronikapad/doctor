# DOCTOR

A terminal app written in Python, made to help users diagnose and fix lagging Windows computers by analyzing system logs and safely matching issues to a command database. Built for the Hack Club Horizons program.

## Supporting OS
- Built for Windows 10/11 (64-bit)
- Standalone compiled folder executable (built using auto-py-to-exe)

## Features
- **System diagnosis**: An AI report based on the `Get-WinEvent -LogName System -MaxEvents 150` command.
- **Safe command execution**: After the report is generated and analyzed, the commands to run are derived based on a curated command database to ensure that the AI does not propose any invasive commands.
- **Conditional feedback loop**: In the command database, each command is assigned some variables. Because of this, after running certain commands, another report will generate or the user will have to make some additional decisions in the terminal

## Setting it up your own machine
1. Dowload the output.zip file from this repo's releases

2. Unzip it

4. Double-click on the main.exe to start the program
<img src="images/Screenshot 2026-07-22 001340.png" alt="Screenshot 2026-07-22 001340.png" width="800"/>

6. Because the binary is unsigned, Windows SmartScreen may pop up. Click "More info" and then "Run anyway"

7. Some commands require Admin right to be run and the program will ask the user for them but, the user has full control over whether or not they choose to authorise admin rights or not
   
8. There is a recording in releases that you can use as a guide while navigating the app


