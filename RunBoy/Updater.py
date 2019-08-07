print ("LOADING RUNBOY")
print ("...")
print ("...")

from tkinter import *
import os
import urllib.request
import urllib
import webbrowser
from tkinter.messagebox import showinfo
from Run import *
from cacheextract import *
from interfaces import *


with urllib.request.urlopen('http://oesterland.de/anderes/gamecoding/RunBoy/game_version.txt') as response:
	version = response.read().decode('utf-8')

root = Tk() #Erstelle neben unseren Update fenster und Game Fenster ein weiteres 
root.withdraw() #UNSICHTBARES Main Fenster (muss sein -.-")

def versioncheck():
	global version
	if version != CurrentGameVersion:
		updateinterface()
	elif version == CurrentGameVersion:
		MainMenu()

def updateGame():
	DownloadSprites()
	webbrowser.open('http://oesterland.de/anderes/gamecoding/RunBoy/RunBoy.rar')

def updateinterface():
	def quit():
		win.destroy()
	win = Toplevel()
	win.wm_title("Game Update benötigt!")
	win.geometry("500x200")
	l = Label(win, text="Deine Version des Spiels ist Outdated")
	l.pack()
	bupdate = Button(win, text="Jetzt Updaten auf Version "+ version, command=updateGame)
	bupdate.pack()
	#bclose = Button(win, command=quit)
	bclose = Button(win, text="Mit Version "+CurrentGameVersion+" weiter Spielen", command=lambda:[MainMenu(),quit()])
	bclose.pack()
	win.mainloop()

versioncheck()
