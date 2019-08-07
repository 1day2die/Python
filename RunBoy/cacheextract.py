import os
import urllib.request
import urllib


with urllib.request.urlopen('http://oesterland.de/anderes/gamecoding/RunBoy/cache_version.txt') as response:
	cache_version = response.read().decode('utf-8')


def DirChecker():
	print ("Checking Cache DIR")
	if not os.path.isdir(os.path.expanduser("~\\RunBoyDL")):
		os.makedirs(os.path.expanduser("~\\RunBoyDL\\sprites\\char"))
		os.makedirs(os.path.expanduser("~\\RunBoyDL\\sprites\\weapons"))
		os.makedirs(os.path.expanduser("~\\RunBoyDL\\sounds"))
		DownloadSprites()
	else:
		print ("CACHE FOUND")
		CacheUpdate()

def CacheUpdate():
	if os.path.isfile(os.path.expanduser("~\\RunBoyDL\\cache_version.txt")):
		with open(os.path.expanduser("~\\RunBoyDL\\cache_version.txt")) as f:
			first_line = f.readline()
		if first_line == cache_version:
			print ("CACHE UP-TO-DATE")
		else:
			print ("CACHE NOT UP-TO-DATE ... DOWNLOAD STARTING")
			DownloadSprites()

def DownloadSprites():
	print ("DOWNLOADING CACHE.... this might take a few seconds!")

	if not os.path.isdir(os.path.expanduser("~\\RunBoyDL\\sprites\\")):
		os.makedirs(os.path.expanduser("~\\RunBoyDL\\sprites\\"))
	if not os.path.isdir(os.path.expanduser("~\\RunBoyDL\\sprites\\char\\")):
		os.makedirs(os.path.expanduser("~\\RunBoyDL\\sprites\\char"))
	if not os.path.isdir(os.path.expanduser("~\\RunBoyDL\\sprites\\weapons")):
		os.makedirs(os.path.expanduser("~\\RunBoyDL\\sprites\\weapons"))
	if not os.path.isdir(os.path.expanduser("~\\RunBoyDL\\sounds\\")):
		os.makedirs(os.path.expanduser("~\\RunBoyDL\\sounds"))

	backgroundmusicDL = os.path.join(os.path.expanduser("~\\RunBoyDL\\sounds"), 'backgroundmusic.wav')
	urllib.request.urlretrieve("http://www.oesterland.de/anderes/gamecoding/RunBoy/sounds/backgroundmusic.wav", backgroundmusicDL)

	backgroundDL = os.path.join(os.path.expanduser("~\\RunBoyDL\\sprites"), 'background.png')
	urllib.request.urlretrieve("http://www.oesterland.de/anderes/gamecoding/RunBoy/sprites/background.png", backgroundDL)

	char_standDL = os.path.join(os.path.expanduser("~\\RunBoyDL\\sprites\\char"), 'char_stand.png')
	urllib.request.urlretrieve("http://www.oesterland.de/anderes/gamecoding/RunBoy/sprites/char/char_stand.png", char_standDL)

	char_walk_leftDL = os.path.join(os.path.expanduser("~\\RunBoyDL\\sprites\\char"), 'char_walk_left.png')
	urllib.request.urlretrieve("http://www.oesterland.de/anderes/gamecoding/RunBoy/sprites/char/char_walk_left.png", char_walk_leftDL)

	char_walk_rightDL = os.path.join(os.path.expanduser("~\\RunBoyDL\\sprites\\char"), 'char_walk_right.png')
	urllib.request.urlretrieve("http://www.oesterland.de/anderes/gamecoding/RunBoy/sprites/char/char_walk_right.png", char_walk_rightDL)

	wep_bullet_rightDL = os.path.join(os.path.expanduser("~\\RunBoyDL\\sprites\\weapons"), 'bullet_right.png')
	urllib.request.urlretrieve("http://www.oesterland.de/anderes/gamecoding/RunBoy/sprites/weapons/bullet_right.png", wep_bullet_rightDL)
	
	wep_bullet_leftDL = os.path.join(os.path.expanduser("~\\RunBoyDL\\sprites\\weapons"), 'bullet_left.png')
	urllib.request.urlretrieve("http://www.oesterland.de/anderes/gamecoding/RunBoy/sprites/weapons/bullet_left.png", wep_bullet_leftDL)
	
	cacheversionDL = os.path.join(os.path.expanduser("~\\RunBoyDL\\"), 'cache_version.txt')
	urllib.request.urlretrieve("http://www.oesterland.de/anderes/gamecoding/RunBoy/cache_version.txt", cacheversionDL)

	print ("DOWNLOAD COMPLETE")