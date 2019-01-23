#!/usr/bin/python2
import webbrowser
import platform


options='''
Press 1 to check your OS version :
Press 2 to login your facebook account:
'''
print options
choice=raw_input("")
if choice=='1':
	p=platform.platform()
	print(p)
