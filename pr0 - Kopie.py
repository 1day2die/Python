names = ["skylar", "HigPingh", "halftimenerd1", "rothe"]

import sys, json, urllib, re
import urllib.request
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


for name in names:
	url = f"https://pr0gramm.com/api/profile/info?name={name}"
	data = json.load(urllib.request.urlopen(url))

	benis = re.sub(r"(?<=.)(?=(?:...)+$)", ".", str(data["user"]["score"]))
	upvotes = data["user"]["up"]
	downvotes = data["user"]["down"]
	uploads = data["uploadCount"]
	tags = data["tagCount"]
	badges = len(data["badges"])

	print(url)

	print (Fore.RED + Style.BRIGHT + ">_ ",Fore.RED + Style.BRIGHT + name, Fore.RED + Style.BRIGHT +  benis)
	print ("---")
	print ("+Benis: " +Fore.GREEN+ str(upvotes))
	print ("-Benis: " + Fore.RED + str(downvotes))
	print ("Uploads: " + str(uploads))
	print ("Tags: " + str(tags))
	print ("Badges: " + str(badges))
	print()
	print("+++")
	print("+++")
	print()

input("lol")