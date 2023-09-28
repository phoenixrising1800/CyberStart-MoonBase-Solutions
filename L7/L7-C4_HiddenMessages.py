# ""Hidden Messages""
# One of the agents has intercepted a file from the aliens
# The flag is hidden in large amount of non alphanumeric characters.
# The file lives at /tmp/destroymoonbase.gif
#

file = '/tmp/destroymoonbase.gif'

with open(file, 'rb') as f:
	data = str(f.read(), 'utf-8')
	data = data.replace('#', "").replace('$', "")
	print(data)
