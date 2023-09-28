# ""Watched by the Eye"
# Hide text in the image /tmp/image.gif
# Append the word alieneye to end of the file.
#
file = '/tmp/image.gif'
appendStr = 'alieneye'

with open(file, 'a') as f:
	f.write(appendStr)
