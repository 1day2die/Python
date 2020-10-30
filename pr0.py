names = ["skylar", "HigPingh", "halftimenerd1", "rothe"]

pr0 = {}

import sys, json, urllib, re
import urllib.request
import colorama
from colorama import Fore, Back, Style
from datetime import date
colorama.init(autoreset=True)

today = date.today()
d1 = today.strftime("%d.%m.%Y")
pr0['person'] = []

for name in names:
	url = f"https://pr0gramm.com/api/profile/info?name={name}"
	data = json.load(urllib.request.urlopen(url))

	benis = re.sub(r"(?<=.)(?=(?:...)+$)", ".", str(data["user"]["score"]))
	upvotes = data["user"]["up"]
	downvotes = data["user"]["down"]
	uploads = data["uploadCount"]
	tags = data["tagCount"]
	badges = len(data["badges"])

	pr0['person'].append({
		'date':d1,
		'name':name,
		'benis':benis,
		'upvotes':upvotes,
		'downvotes':downvotes,
		'uploads':uploads,
		'tags':tags,
		'badges':badges
		})

	with open(f'pr0/pr0_{d1}.json', 'w') as outfile:
		json.dump(pr0, outfile)

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