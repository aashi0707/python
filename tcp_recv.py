#!/usr/bin/python2
import socket
#calling tcp socket
#s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#	or
s=socket.socket()

#binding ip and port
s.bind(("192.168.1.35",9990))

# listen number of parallelor consecutive connection
# maximum 50 connection 
s.listen(50)

# receiver must accept connection from client
# data variable--?? client ip + port, client socket

while True:
	cliskt,cliaddr=s.accept()
	print cliskt
	print cliaddr
	print cliskt.recv(100)
	cliskt.send("okay",cliaddr)
s.close()

