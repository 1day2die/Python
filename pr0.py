names = ["skylar", "HigPingh", "halftimenerd1", "rothe"]

import sys, json, urllib, re
import urllib.request
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


for name in names:
	url = f"https://pr0gramm.com/api/profile/info?name={name}"
	print(url)
	data = json.load(urllib.request.urlopen(url))
	benis = re.sub(r"(?<=.)(?=(?:...)+$)", ".", str(data["user"]["score"]))
	print (Fore.RED + Style.BRIGHT + ">_ ",Fore.RED + Style.BRIGHT + name, Fore.RED + Style.BRIGHT +  benis)
	print ("---")
	print ("+Benis: " +Fore.GREEN+ str(data["user"]["up"] ))
	print ("-Benis: " + Fore.RED + str(data["user"]["down"]))
	print ("Uploads: " + str(data["uploadCount"]))
	print ("Tags: " + str(data["tagCount"]))
	print ("Badges: " + str(len(data["badges"])))
	print()
	print("+++")
	print("+++")
	print()

input("lol")