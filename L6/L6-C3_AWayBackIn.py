# ""A Way Back In""
# Write a script that connects to 'localhost' port 10000
# You then need to send a command to list the files in the /tmp directory
#
import socket as s

directory = '/tmp'
client = s.socket(s.AF_INET, s.SOCK_STREAM)
client.connect(('localhost', 10000))
client.send(b'ls /tmp')
data = client.recv(1024)			
print(data)
