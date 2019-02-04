#!/usr/bin/env python2
import socket
#defining ip and port for comm
#calling udp method
#		  ipv4           udp type
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# here s i udp type with ipv4 socket

#defining ip and port for comm
ip_addr="192.168.1.25"
port=8888

#binding ip and port

	# s.bind(ip_addr,port)

	#	or

conn=(ip_addr,port)
s.bind(conn)
while true:
	print s.recvfrom(100)
#here 100 is data buffer size received from per client/server
