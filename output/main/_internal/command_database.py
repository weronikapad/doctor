commands = {
    "sfc /scannow": { #semi-ok (otwiera sie nowe okno zeby run)
        "name": "sfc /scannow",
        "description": "Scans and repairs corrupted system files.",
        "admin_required": True,
        "further_analysis": False,
        "further_decisions_inteminal": False,
        "print_value":True,
        "warning": False,
        "warning_note": "none",
        "number": 1
    },
    "ipconfig /flushdns": { #ok
        "name": "ipconfig /`flushdns",
        "description": "Clears internet DNS cache to fix connectivity glitches",
        "admin_required": False,
        "further_analysis": True,
        "further_decisions_inteminal": False,
        "print_value":False,
        "warning": False,
        "warning_note": "none",
        "number": 2
        
    },
    "chkdsk C: /f":{ #ok
        "name": "chkdsk C: /f",
        "description": "Checks main hard drive for filesystem errors (it will requrie a restart either right now or scheduled for next restart)",
        "admin_required": True,
        "further_analysis": False,
        "further_decisions_inteminal": True,
        "print_value":False,
        "warning": False,
        "warning_note": "none",
        "number": 3
    },
    "net user": { #ok
        "name": "net user",
        "description": "Displays user accounts on the system.",
        "admin_required": False,
        "further_analysis": False,
        "further_decisions_inteminal": False,
        "print_value":True,
        "warning": False,
        "warning_note": "none",
        "number": 4
    },
    "net share": { #ok
        "name": "net share",
        "description": "Displays shared resources on the system.",
        "admin_required": False,
        "further_analysis": True,
        "further_decisions_inteminal": False,
        "print_value":False,
        "warning": False,
        "warning_note": "none",
        "number": 5
        
    },
    "ipconfig /all": { #ok
        "name": "ipconfig /all",
        "description": "Displays detailed network configuration information.",
        "admin_required": False,
        "further_analysis": True,
        "further_decisions_inteminal": False,
        "print_value":False,
        "warning": False,
        "warning_note": "none",
        "number": 6
    },
    "ipconfig /flushdns": {#ok
        "name": "ipconfig /flushdns",
        "description": "Clearing the DNS resolver cache erases your computer's temporary memory of website locations, forcing it to look up fresh, accurate addresses to fix internet connection glitches.",
        "admin_required": False,
        "further_analysis": False,
        "further_decisions_inteminal": False,
        "print_value":True,
        "warning": False,
        "warning_note": "none",
        "number": 7
    },
    "gpupdate /force": { #ok
        "name": "gpupdate /force",
        "description": "Forcefully applies all corporate or system Group Policy updates to the computer immediately, bypassing the normal background waiting period. This command may take a moment to run",
        "admin_required": True,
        "further_analysis": False,
        "further_decisions_inteminal": False,
        "print_value":False,
        "warning": True,
        "warning_note": "it may requrie a restart, but olny after user aproval",
        "number": 8
    },
    "gpresult /h FileNameHere.html": { #ok
        "name": "gpresult /h FileNameHere.html",
        "description": "Generates an HTML web report showing all active system restrictions and security policies currently applied to your account and PC.",
        "admin_required": False,
        "further_analysis": False,
        "further_decisions_inteminal": False,
        "print_value":True,
        "warning": False,
        "warning_note": "none",
        "number": 9
    },
    "dism /online /cleanup-image /restorehealth": { #ok
        "name": "dism /online /cleanup-image /restorehealth",
        "description": "Reaches out to Windows Update servers to download and repair deeply broken Windows operating system image files that regular scanners can't fix.",
        "admin_required": True,
        "further_analysis": False,
        "further_decisions_inteminal": False,
        "print_value":False,
        "warning": True,
        "warning_note": "This command can take a long time to complete and may require a restart.",
        "number": 10
    },
    "powershell -Command get-printer": {#ok
        "name": "powershell -Command get-printer",
        "description": "Pulls a detailed diagnostic list of every local and network printer currently configured on your machine.",
        "admin_required": False,
        "further_analysis": True,
        "further_decisions_inteminal": False,
        "print_value":True,
        "warning": False,
        "warning_note": "none",
        "number": 11
    },
    "w32tm /resync": { #ok
        "name": "w32tm /resync",
        "description": "Forces your computer's internal clock to instantly update and correct itself against internet time servers to fix time-sync glitches.",
        "admin_required": False,
        "further_analysis": True, #make sure the analysys also prints out the teminal response
        "further_decisions_inteminal": False,
        "print_value":True,
        "warning": False,
        "warning_note": "none",
        "number": 12
    },
    "dxdiag": { #ok
        "name": "dxdiag",
        "description": "Opens the DirectX Diagnostic tool to view your exact graphics card specs, audio hardware, and driver versions for troubleshooting games.",
        "admin_required": False,
        "further_analysis": True, #make sure it also prints terminal value
        "further_decisions_inteminal": False,
        "print_value":False,
        "warning": False,
        "warning_note": "none",
        "number": 13
    },
    "netsh mbn show connection": {  #ok
        "name": "netsh mbn show connection",
        "description": "Launches a powerful network configuration console that allows you to directly edit, reset, or view your system's firewalls and network card settings.",
        "admin_required": False,
        "further_analysis": True, #print value in the analysys
        "further_decisions_inteminal": False,
        "print_value":False,
        "warning": False,
        "warning_note": "none",
        "number": 14
    },
    "powercfg /batteryreport": { #ok
        "name": "powercfg /batteryreport",
        "description": "Generates a detailed document showing your laptop battery’s health history, factory capacity, and actual remaining lifespan.",
        "admin_required": False,
        "further_analysis": True, #print value in the analysys
        "further_decisions_inteminal": False,
        "print_value":False,
        "warning": False,
        "warning_note": "none",
        "number": 15
    },
    "cleanmgr /lowdisk": { #ok
        "name": "cleanmgr /lowdisk",
        "description": "Instantly triggers Windows Disk Cleanup in an automated mode to aggressively wipe temporary junk files and clear up drive space.",
        "admin_required": False,
        "further_analysis": True, #print value in the analysys
        "further_decisions_inteminal": False,
        "print_value":False,
        "warning": False,
        "warning_note": "none",
        "number": 16
    },
    "winget upgrade --all": { #ok
        "name": "winget upgrade --all",
        "description": "Scans all installed software on your computer and updates every single app to its latest version simultaneously.",
        "admin_required": False,
        "further_analysis": False, #print value in the analysys
        "further_decisions_inteminal": True,
        "print_value":False,
        "warning": True,
        "warning_note": "Updates all the apps and may close them while doing so",
        "number": 17
    },
    "ipconfig /all": {
        "name": "ipconfig /all",
        "description": "Displays a master sheet of your internet setups, including every hardware MAC address, IP address, and network adapter configuration.",
        "admin_required": False,
        "further_analysis": True, #print value in the analysys
        "further_decisions_inteminal": False,
        "print_value":False,
        "warning": False,
        "warning_note": "none",
        "number": 18
    },
 
}   