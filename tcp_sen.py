#!/usr/bin/python2
import socket
#calling tcp socket
s=socket.socket()

#if receiver started listening then we can connect
s.connect(("192.168.1.35",9990))

while True:
	msg=raw_input("please enter message -->> ")
	s.send(msg)
	print s.recv(100)
s.close()
