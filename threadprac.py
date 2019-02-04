#!/usr/bin/env/python2
import thread

#creating a function1
def one():
	while True:
		print "hello"

#creating a function2
def two():
	while True:
		print "world"

thread.start_new_thread(one,())
thread.start_new_thread(two,())

while True:
	pass
