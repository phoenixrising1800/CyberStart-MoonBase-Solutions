# ""Alien Zip""
# Sample Alien Zip file found at /tmp/alien-zip-2092.zip is password protected
# We have worked out they are using three digit code
# Brute force the Zip file to extract to /tmp
#
# Note: The script can timeout if this occurs try narrowing
# down your search
import os
import zipfile 

file = '/tmp/alien-zip-2092.zip'
code = "000"

def inc(codeStr):
	return str(int(codeStr)+1).zfill(len(codeStr))

with zipfile.ZipFile(file) as archive:
	while int(code) < 1000:
		#print("Possible password: " + code)
		try:
			archive.extract(member='alien-zip-2092.txt', path='/tmp', pwd=bytes(code, 'utf-8'))
			code = inc(code)
			break
		except RuntimeError:
			code = inc(code)
			continue
