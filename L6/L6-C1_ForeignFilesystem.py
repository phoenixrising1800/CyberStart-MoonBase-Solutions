# ""Foreign Filesystem""
# Find the file in the alien directories in /tmp/aliendir to get the flag
#
import os

directory = '/tmp/aliendir'
for root, dirs, files in os.walk(directory):
	for file in files:
		print(file)
