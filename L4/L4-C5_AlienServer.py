# ""Alien Server""
# Connect to alien server ('localhost', 10000)
#
# Then send each of these values...
# USER
# aliensignal
# PASS
# unlockserver
# SEND
# moonbase
# END
# ...and receive the response from each.
#
# Note: You must receive data back from the server after you send each value
#
import socket as s

client = s.socket(s.AF_INET, s.SOCK_STREAM)
client.connect(('localhost', 10000))

client.send(b'USER')
print(client.recv(1024).decode())
client.send(b'aliensignal')
print(client.recv(1024).decode())
client.send(b'PASS')
print(client.recv(1024).decode())
client.send(b'unlockserver')
print(client.recv(1024).decode())
client.send(b'SEND')
print(client.recv(1024).decode())
client.send(b'moonbase')
print(client.recv(1024).decode())
client.send(b'END')
flag = client.recv(1024)			
print(flag)
