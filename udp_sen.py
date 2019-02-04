#!/usr/bin/env python2
import socket
#calling udp method
#		     ipv4           udp type
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#here s is udp type with ipv4 socket
#defining ip and port for comm
ip_addr="192.168.1.25"
port=8888

while 4>2:
	data=raw_input("enter your data")
	s.sendto("hiii",(ip_addr,port))
#          func    msg

