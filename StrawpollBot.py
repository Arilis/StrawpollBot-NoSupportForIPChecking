import requests
import string
strawpollID = "ID HERE"
url = 'https://www.strawpoll.me/' + strawpollID
while True:
	requests.post(url, allow_redirects=False, data={
	'options': OPTION HERE (check in F12)
	})

	print("Sent a reqest to %s " % (url))
