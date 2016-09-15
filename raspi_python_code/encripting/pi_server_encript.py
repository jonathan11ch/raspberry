import RPi.GPIO as GPIO
import socket
import sys
from thread import *
import json
import encoder

HOST = ''   # Symbolic name, meaning all available interfaces
PORT = 8888 # Arbitrary non-privileged port
IN_PORT = 4
OUT_PORT = 27
COMMAND = 0
key="a"

def setOutputPort(_OUT_PORT):
	GPIO.setup(_OUT_PORT, GPIO.OUT)  # set up pin 17
	return

def setInputPort(_IN_PORT):
	GPIO.setup(_IN_PORT, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	return

def writePort(_COMMAND):
	GPIO.output(OUT_PORT, _COMMAND)  # turn on pin 17
	return

def readPort(_IN_PORT):
	return GPIO.input(_IN_PORT)	

print("setting gpio ports...")
GPIO.setmode(GPIO.BCM)  # set board mode to Broadcom
setInputPort(IN_PORT)
setOutputPort(OUT_PORT)
print("gpio ports set...")
################################SERVER###############################
def client_request_handler(conn):
	
	conn.send("welcome to the raspi server")
	while True:
		data = conn.recv(1024)
		#j = json.loads('{"command":"in","value":"0"}')
		print(data)
		decripted = encoder.xor_strings(data, key)
		try:
			obj = json.loads(decripted)
		except ValueError:
			print("json could not be decoded... :(")
			conn.send("json could not be decoded... :(")
			break	
		print(obj)


		if obj['command'] == "write":
			if obj['value'] == "0" or obj['value'] == "1":
				writePort(int(obj['value']))
				conn.send("command executed...")
				break
			else:
				conn.send("wrong command sent...")
				break	
		
		elif obj['command'] == "read":
			datatosend=readPort(IN_PORT)
			conn.send("Port state: " + str(datatosend))
			break
		else:
			conn.send("wrong command sent...")
			break
			
	conn.close()			
##################################################################### 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
 
#Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'Socket bind complete'
 
#Start listening on socket
s.listen(10)
print 'Socket now listening'
 
#now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
    start_new_thread(client_request_handler ,(conn,))

     
s.close()


