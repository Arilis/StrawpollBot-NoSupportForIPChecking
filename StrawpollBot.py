import requests
import string
import time
import sys
import colorful
import os

clear = lambda: os.system('cls')
strawid = input("What is the poll ID located in the poll URL?: ")
opid = input("What is the option ID located in the F12 menu?: ")

print("Strawpoll ID Set to: " + colorful.green(strawid))
time.sleep(2)
print("Strawpoll Option ID Set to: " + colorful.green(opid))
time.sleep(2)

url = 'https://www.strawpoll.me/' + strawid
print(colorful.red("Starting bot in 5 seconds!"))
time.sleep(1)
print(colorful.red("Starting bot in 4 seconds!"))
time.sleep(1)
print(colorful.orange("Starting bot in 3 seconds!"))
time.sleep(1)
print(colorful.yellow("Starting bot in 2 seconds!"))
time.sleep(1)
print(colorful.green("Starting bot in 1 seconds!"))
time.sleep(1)
clear()

while True:
	requests.post(url, allow_redirects=False, data={
	'options': opid
	})

	print(colorful.green("Sent multiple request to %s " % (url)))
