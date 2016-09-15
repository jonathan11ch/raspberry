import socket
import sys
from thread import *
import json
import encoder # encripting function

HOST = ''   # Symbolic name, meaning all available interfaces
PORT = 8888 # Arbitrary non-privileged port
key="a"

def client_request_handler(conn):
	data="hallo wie gehts"
	print("datat to send: " + data)
	xored = encoder.xor_strings(data, key)
	print("Encripted data "+ xored)
	conn.send(xored)
	conn.close()

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

