import socket
import sys
import json
TCP_IP = '192.168.1.2'
TCP_PORT = 8888
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
#obj= json.loads('{"command":"in","value":"0"}')
print(s.recv(BUFFER_SIZE))
s.send('{"command":"write","value":"1"}')
data = s.recv(BUFFER_SIZE)
s.close()

print ("received data:"+ data)
