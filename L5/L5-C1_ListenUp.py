# ""Listen Up""
# The aliens seem to be trying to make direct contact, so it's time
# for us to properly listen.
# Write a server that listens on ('localhost', 10000).
# The flag will be sent to that address.
# Record signal to /tmp/aliensignallog.txt
#
# If you get an address already in use error then try again in a few
# moments.
#
import socket as s

def debugMsg(msg):
  # Use this function if you need any debug messages
  with open("/tmp/userdebug.log", "a") as myfile:
    myfile.write(msg + "\\n")

file = '/tmp/aliensignallog.txt'

server = s.socket(s.AF_INET, s.SOCK_STREAM)
server.bind(("localhost", 10000))
server.listen(1)
while True:
	conn, addr = server.accept()
	data = conn.recv(1024).decode()
	if len(data) > 0:
		with open(file, 'w+') as f:
			f.write(data)
			conn.close()
		break
server.close()
