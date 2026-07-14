commands = {
    "sfc /scannow": {
        "name": "sfc /scannow",
        "description": "Scans and repairs corrupted system files.",
        "admin_required": True,
        "further_analysis": False,
        "further_decisions_inteminal": False,
        "print_value":False,
        "warning": False,
        "warning_note": "none"
    },
    "ipconfig /flushdns": {
        "name": "ipconfig /`flushdns",
        "description": "Clears internet DNS cache to fix connectivity glitches",
        "admin_required": False,
        "further_analysis": True,
        "further_decisions_inteminal": False,
        "print_value":False,
        "warning": False,
        "warning_note": "none"
    },
    "chkdsk C: /f":{
        "name": "chkdsk C: /f",
        "description": "Checks main hard drive for filesystem errors (it will requrie a restart either right now or scheduled for next restart)",
        "admin_required": True,
        "further_analysis": False,
        "further_decisions_inteminal": True,
        "print_value":False,
        "warning": False,
        "warning_note": "none"
    },
    "net user": {
        "name": "net user",
        "description": "Displays user accounts on the system.",
        "admin_required": False,
        "further_analysis": False,
        "further_decisions_inteminal": False,
        "print_value":True,
        "warning": False,
        "warning_note": "none"
    },
    "net share": {
        "name": "net share",
        "description": "Displays shared resources on the system.",
        "admin_required": False,
        "further_analysis": True,
        "further_decisions_inteminal": False,
        "print_value":False,
        "warning": False,
        "warning_note": "none"
        
    },
    "ipconfig /all": {
        "name": "ipconfig /all",
        "description": "Displays detailed network configuration information.",
        "admin_required": False,
        "further_analysis": True,
        "further_decisions_inteminal": False,
        "print_value":False,
        "warning": False,
        "warning_note": "none"
    },
    "ipconfig /flushdns": {
        "name": "ipconfig /flushdns",
        "description": "Clearing the DNS resolver cache erases your computer's temporary memory of website locations, forcing it to look up fresh, accurate addresses to fix internet connection glitches.",
        "admin_required": False,
        "further_analysis": False,
        "further_decisions_inteminal": False,
        "print_value":True,
        "warning": False,
        "warning_note": "none"
    },
    "gpupdate /force": {
        "name": "gpupdate /force",
        "description": "Forcefully applies all corporate or system Group Policy updates to the computer immediately, bypassing the normal background waiting period.",
        "admin_required": True,
        "further_analysis": False,
        "further_decisions_inteminal": False,
        "print_value":False,
        "warning": True,
        "warning_note": "it may requrie a restart, but olny after user aproval"
    },
    "gpresult /h FileNameHere.html": {
        "name": "gpresult /h FileNameHere.html",
        "description": "Generates an HTML web report showing all active system restrictions and security policies currently applied to your account and PC.",
        "admin_required": False,
        "further_analysis": False,
        "further_decisions_inteminal": False,
        "print_value":True,
        "warning": False,
        "warning_note": "none"
    },
    "dism /online /cleanup-image /restorehealth": {
        "name": "dism /online /cleanup-image /restorehealth",
        "description": "Reaches out to Windows Update servers to download and repair deeply broken Windows operating system image files that regular scanners can't fix.",
        "admin_required": True,
        "further_analysis": False,
        "further_decisions_inteminal": False,
        "print_value":False,
        "warning": True,
        "warning_note": "This command can take a long time to complete and may require a restart."
        #check the booleans
    },
    "get-printer": {
        "name": "get-printer",
        "description": "Pulls a detailed diagnostic list of every local and network printer currently configured on your machine.",
        "admin_required": False,
        "further_analysis": True,
        "further_decisions_inteminal": False,
        "print_value":True,
        "warning": False,
        "warning_note": "none"
    },
    "w32tm /resync": {
        "name": "w32tm /resync",
        "description": "Forces your computer's internal clock to instantly update and correct itself against internet time servers to fix time-sync glitches.",
        "admin_required": False,
        "further_analysis": True, #make sure the analysys also prints out the teminal response
        "further_decisions_inteminal": False,
        "print_value":True,
        "warning": False,
        "warning_note": "none"
    },
    "nslookup": {
        "name": "nslookup",
        "description": "Launches an interactive tool to test network name servers, letting you see exactly what IP address a website name translates to.",
        "admin_required": False,
        "further_analysis": True,
        "further_decisions_inteminal": False,
        "print_value":False,
        "warning": False,
        "warning_note": "none"
    },
    "dxdiag": {
        "name": "dxdiag",
        "description": "Opens the DirectX Diagnostic tool to view your exact graphics card specs, audio hardware, and driver versions for troubleshooting games.",
        "admin_required": False,
        "further_analysis": True, #make sure it also prints terminal value
        "further_decisions_inteminal": False,
        "print_value":False,
        "warning": False,
        "warning_note": "none"
    },
    "netsh mbn show connection": {
        "name": "netsh mbn show connection",
        "description": "Launches a powerful network configuration console that allows you to directly edit, reset, or view your system's firewalls and network card settings.",
        "admin_required": False,
        "further_analysis": True, #print value in the analysys
        "further_decisions_inteminal": False,
        "print_value":False,
        "warning": False,
        "warning_note": "none"
    },
    "powercfg /batteryreport": {
        "name": "powercfg /batteryreport",
        "description": "Generates a detailed document showing your laptop battery’s health history, factory capacity, and actual remaining lifespan.",
        "admin_required": False,
        "further_analysis": True, #print value in the analysys
        "further_decisions_inteminal": False,
        "print_value":False,
        "warning": False,
        "warning_note": "none"
    },
    "cleanmgr /lowdisk": {
        "name": "cleanmgr /lowdisk",
        "description": "Instantly triggers Windows Disk Cleanup in an automated mode to aggressively wipe temporary junk files and clear up drive space.",
        "admin_required": False,
        "further_analysis": True, #print value in the analysys
        "further_decisions_inteminal": False,
        "print_value":False,
        "warning": False,
        "warning_note": "none"
    },
    "winget upgrade --all": {
        "name": "winget upgrade --all",
        "description": "Scans all installed software on your computer and updates every single app to its latest version simultaneously.",
        "admin_required": False,
        "further_analysis": True, #print value in the analysys
        "further_decisions_inteminal": False,
        "print_value":False,
        "warning": True,
        "warning_note": "Updates all the apps and may close them while doing so"
    },
    "ipconfig /all": {
        "name": "ipconfig /all",
        "description": "Displays a master sheet of your internet setups, including every hardware MAC address, IP address, and network adapter configuration.",
        "admin_required": False,
        "further_analysis": True, #print value in the analysys
        "further_decisions_inteminal": False,
        "print_value":False,
        "warning": False,
        "warning_note": "none"
    },
 
}   