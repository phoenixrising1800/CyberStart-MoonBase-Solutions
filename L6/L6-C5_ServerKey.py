# ""Server Key""
# Send server ('localhost', 10000) GET_KEY to retrieve key,
# user needs to reverse and send back to server to get flag.
# It will change each execution so the
# user can not manually achieve this.
#
import socket as s

client = s.socket(s.AF_INET, s.SOCK_STREAM)
client.connect(('localhost', 10000))
client.send(b'GET_KEY')
key = client.recv(1024)			
revKey = key[::-1]
client.send(revKey)
print(client.recv(1024).decode())
