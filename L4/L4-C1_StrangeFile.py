# ""Strange File""
# Ok, quick task for you agent - we've received a strange file from
# the first alien communication.
# It's at /tmp/alien-signal.txt, we need you to open and read the file.
#
#
file = '/tmp/alien-signal.txt'

with open(file, 'r') as f:
	for line in f:
		print(line)
