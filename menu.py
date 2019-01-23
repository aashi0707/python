#!/usr/bin/python2
import platform
import webbrowser
import getpass
import os

options='''
Press 1 to check your OS version :
Press 2 to open default web browser :
Press 3 to check current logined user :
Press 4 to ask user input and search in google :
Press 5 to check number of tabs in your web browser :
Press 6 to logout your system graphically :
Press 7 to login facebook account :
Press 8 to send email to someone :
Press 9 to to list all connected ip and mac in your current network :
Press 10 to
Press 11 to 
Press 12 to
Press 13 to
Press 14 to
Press 15 to
'''

print options

choice=raw_input("")

if choice=='1':
	p=platform.platform()
	print(p)

if choice=='2':
	wb=webbrowser.open('https://www.google.com')
	print(wb)

if choice=='3':
	user=getpass.getuser()
	print(user)

if choice=='4':
	s=raw_input("type something to search on google")
	webbrowser.open("http://www.google.com/search?q="+s)

if choice=='6':
	l=os.system("shutdown -l")
	print(l)
