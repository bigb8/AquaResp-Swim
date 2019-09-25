Dim WSHShell 
Dim MyShortcut 
Dim DesktopPath

Set WSHShell = CreateObject("WScript.Shell") 
DesktopPath = WSHShell.SpecialFolders("Desktop")


scriptdir = CreateObject("Scripting.FileSystemObject").GetParentFolderName(WScript.ScriptFullName)


Set MyShortcut = WSHShell.CreateShortCut(DesktopPath & "\AquaResp Swim" & ".lnk") 
MyShortcut.TargetPath = scriptdir & "\lib\main.py"
MyShortcut.WindowStyle = 1 
MyShortcut.Arguments = "" 
MyShortcut.IconLocation = scriptdir & "\favicon.ico"

MyShortcut.Save 


Set MyShortcut = WSHShell.CreateShortCut(DesktopPath & "\AquaResp Swim Plots" & ".lnk") 
MyShortcut.TargetPath = scriptdir & "\plots.html"
MyShortcut.WindowStyle = 1 
MyShortcut.Arguments = ""
MyShortcut.IconLocation = scriptdir & "\ploticon.ico" 
MyShortcut.Save 
