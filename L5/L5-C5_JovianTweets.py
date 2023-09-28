# ""Jovian Tweets""
# The Tweet Bot API can be found at http://127.0.0.1:8082
#
# GET method sent to that URL:
# ...returns basic info about API
#
# POST method sent to that URL, with:
# - x-api-key:{KEY} in header
# - user={USER} in querystring
# - status-update={TEXT} in querystring
# ...creates a new social media post
import urllib.request, urllib.parse

api = 'http://127.0.0.1:8082'
header = {'x-api-key': 'tweetbotkeyv1'}

# querystring data containing user=tweetbotuser and status-update=alientest
params = {'user': 'tweetbotuser', 'status-update': 'alientest'}
querystring = urllib.parse.urlencode(params)

req = urllib.request.Request(api, data=bytes(querystring, 'utf-8'), method='POST', headers=header)
res = urllib.request.urlopen(req)
print(res.read())
