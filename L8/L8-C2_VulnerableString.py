# ""Vulnerable String""
# Write a script which can connect to the following server
# 'localhost', 10000 over TCP send 'GET_KEY' to download a string.
# The string is compressed with a common algorithm found in many
# websites. Decompress the string and print it to get the flag.
#
import socket as s
from io import BytesIO
import gzip

client = s.socket(s.AF_INET, s.SOCK_STREAM)
client.connect(('localhost', 10000))
client.send(b'GET_KEY')
data = client.recv(4096)
file = gzip.GzipFile(fileobj=BytesIO(data))
print(file.read())

client.close()
