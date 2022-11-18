from tkinter import *
import time
import threading
from PIL import Image, ImageTk
import os
import urllib.request
import urllib
import webbrowser
from tkinter.messagebox import showinfo

#ALLE VARIABLEN-------------------------------------------------------------------------------------------------------------------------------------------------
Autoklicker = 0
NoobisProKlick = 1
AutoKlickerKosten = 50
KlickUpgradeKosten = 150
CurrentGameVersion = "Alpha 1.5"
SkinPack = 0
pic_dir = os.path.dirname(__file__)+"/assets" # / ENTFERNEN BEVOR EXE COVNERTIERUNG
version = ''
level1 = ''  
level2 = ''	
level3 = ''	
level4 = ''	
level5 = ''	
level6 = ''
level7 = ''	

print ("Lade NoobiKlicker!")

root = Tk() #Erstelle neben unseren Update fenster und Game Fenster ein weiteres 
root.withdraw() #UNSICHTBARES Main Fenster (muss sein -.-")


#ERSTER RUN: CHECK DIE VERSIONEN-------------------------------------------------------------------------------------------------------------------------------------------------
def versioncheck():
	global version
	if version != CurrentGameVersion:
		updateinterface()
	elif version == CurrentGameVersion:
		startgame()

#ÖFFNE DIE WEBSITE UM DAS SPIEL ZU UPDATEN-------------------------------------------------------------------------------------------------------------------------------------------------	
def updateGame():
	webbrowser.open('http://oesterland.de/anderes/noobiclicker/noobiclicker.rar')

#STARTE UND BAUE DAS SPIEL-------------------------------------------------------------------------------------------------------------------------------------------------
def startgame():
	global Klickkonto
	global Autoklicker
	global AutoKlickerKosten
#ERSTELLE UNSERE SAVEDATEI ------------------------------------------------------------------------------------------------
	if os.path.isfile('./savestate.dennis'):
		with open("savestate.dennis", "r") as savefile:
		    lines = savefile.readlines()
		Klickkonto = float(lines[0])
		NoobisProKlick = float(lines[1])
		Autoklicker = float(lines[2])
		savefile.close()
	else:
		Klickkonto = 0
		saveload = open("savestate.dennis", "w")
		saveload.write(str(Klickkonto)+"\n"+str(NoobisProKlick)+"\n"+str(Autoklicker))
		saveload.close()
	def savegame():
		writesave = open("savestate.dennis", "w")
		writesave.write(str(Klickkonto)+"\n"+str(NoobisProKlick)+"\n"+str(Autoklicker))
		writesave.close()
		canvas.after(15000, savegame)
		print("Game Saved")
#FUNTKION WENN MAN DEN BUTTON KLICKT-------------------------------------------------------------------------------------------------------------------------------------------------
	
	def DoKlick():
		global Klickkonto
		Klickkonto += round(NoobisProKlick,1)
		KlickCounterText.config(text="Dein Klickkonto: " + str(Klickkonto)[:5])
#FUNKTION FÜR DEN KAUF EINES AUTOKLICKERS-------------------------------------------------------------------------------------------------------------------------------------------------
	def BuyAutoKlicker():
		global Klickkonto
		global AutoKlickerKosten
		if Klickkonto >= AutoKlickerKosten:
			global Autoklicker
			Autoklicker += 1
			Klickkonto -= AutoKlickerKosten
			AutoKlickerKosten = round(int(AutoKlickerKosten) * 1.05,0)
			KlickCounterText.config(text="Dein Klickkonto: " + str(Klickkonto)[:5])
			AutoklickerText.config (text= "Deine Autoklicker: " + str(Autoklicker))
			KaufKlickerButton.config (text= "Kaufe einen Autoklicker (" + str(AutoKlickerKosten) + ")")
#FUNKTION UM DIE AUTOKLICKER AUSZUFÜHREN-------------------------------------------------------------------------------------------------------------------------------------------------
	def DoAutoKlick():
		global Autoklicker
		global Klickkonto
		KlickAmount = int(Autoklicker) * 1
		Klickkonto += KlickAmount
		KlickCounterText.config(text="Dein Klickkonto: " + str(Klickkonto)[:5])
		canvas.after(1000, DoAutoKlick)

		#FUNKTION FÜR DEN KAUF EINES AUTOKLICKERS-------------------------------------------------------------------------------------------------------------------------------------------------
	def BuyKlickerUpgrade():
		global Klickkonto
		global KlickUpgradeKosten
		if Klickkonto >= KlickUpgradeKosten:
			global NoobisProKlick
			NoobisProKlick += 0.1
			Klickkonto -= KlickUpgradeKosten
			KlickUpgradeKosten = round(int(KlickUpgradeKosten) * 1.07,0)
			KlickCounterText.config(text="Dein Klickkonto: " + str(Klickkonto)[:5])
			KlickUpgradeText.config (text= "Noobis pro Klick: " + str(NoobisProKlick)[:3])
			KaufKlickUpgradeButton.config (text= "Kaufe Klick Upgrade (" + str(KlickUpgradeKosten) + ")")


#FUNKTION FÜR DAS ÄNDERN DES BILDES------------------------------------------------------------------------------------------------------------------------------------------------
	def UpdateNoobi():
		global Klickkonto
		if Klickkonto >= 50 and Klickkonto < 100:
			KlickButton.configure(image= level2)
		elif Klickkonto >= 100 and Klickkonto < 200:
			KlickButton.configure(image= level3)
		elif Klickkonto >= 200 and Klickkonto < 500:
			KlickButton.configure(image= level4)
		elif Klickkonto >= 500 and Klickkonto < 1000:
			KlickButton.configure(image= level5)
		elif Klickkonto >= 1000 and Klickkonto < 2000:
			KlickButton.configure(image= level6)
		elif Klickkonto >= 2000:
			KlickButton.configure(image= level7)
		else:
			KlickButton.configure(image= level1)
		canvas.after(1000, UpdateNoobi)

	def SelectSkin():
		global level1, level2, level3, level4, level5, level6, level7, SkinPack
		if SkinPack == 0:
		#LADE DIE BILDER INS PORGRAMM ---------------------------------
			level1 = ImageTk.PhotoImage(Image.open(pic_dir+"/noobis/rs/bronze.png"))   #FÜHREDE BACKSLASHES ENTFERNEN BEVOR MAN ZU EXE KONVERTIERT
			level2 = ImageTk.PhotoImage(Image.open(pic_dir+"/noobis/rs/steel.png"))	#FÜHREDE BACKSLASHES ENTFERNEN BEVOR MAN ZU EXE KONVERTIERT
			level3 = ImageTk.PhotoImage(Image.open(pic_dir+"/noobis/rs/mith.png"))	#FÜHREDE BACKSLASHES ENTFERNEN BEVOR MAN ZU EXE KONVERTIERT
			level4 = ImageTk.PhotoImage(Image.open(pic_dir+"/noobis/rs/rune.png"))	#FÜHREDE BACKSLASHES ENTFERNEN BEVOR MAN ZU EXE KONVERTIERT
			level5 = ImageTk.PhotoImage(Image.open(pic_dir+"/noobis/rs/dragon.png"))	#FÜHREDE BACKSLASHES ENTFERNEN BEVOR MAN ZU EXE KONVERTIERT
			level6 = ImageTk.PhotoImage(Image.open(pic_dir+"/noobis/rs/barrows.png"))	#FÜHREDE BACKSLASHES ENTFERNEN BEVOR MAN ZU EXE KONVERTIERT
			level7 = ImageTk.PhotoImage(Image.open(pic_dir+"/noobis/rs/tamelee.png"))	#FÜHREDE BACKSLASHES ENTFERNEN BEVOR MAN ZU EXE KONVERTIERT
		elif SkinPack ==1:
			level1 = ImageTk.PhotoImage(Image.open(pic_dir+"/noobis/shisha/shisha.png"))   #FÜHREDE BACKSLASHES ENTFERNEN BEVOR MAN ZU EXE KONVERTIERT
			level2 = ImageTk.PhotoImage(Image.open(pic_dir+"/noobis/shisha/michi.png"))	#FÜHREDE BACKSLASHES ENTFERNEN BEVOR MAN ZU EXE KONVERTIERT
			level3 = ImageTk.PhotoImage(Image.open(pic_dir+"/noobis/shisha/rex.png"))	#FÜHREDE BACKSLASHES ENTFERNEN BEVOR MAN ZU EXE KONVERTIERT
			level4 = ImageTk.PhotoImage(Image.open(pic_dir+"/noobis/shisha/jannis.png"))	#FÜHREDE BACKSLASHES ENTFERNEN BEVOR MAN ZU EXE KONVERTIERT
			level5 = ImageTk.PhotoImage(Image.open(pic_dir+"/noobis/shisha/lars.png"))	#FÜHREDE BACKSLASHES ENTFERNEN BEVOR MAN ZU EXE KONVERTIERT
			level6 = ImageTk.PhotoImage(Image.open(pic_dir+"/noobis/shisha/matze.png"))	#FÜHREDE BACKSLASHES ENTFERNEN BEVOR MAN ZU EXE KONVERTIERT
			level7 = ImageTk.PhotoImage(Image.open(pic_dir+"/noobis/shisha/dennis.png"))	#FÜHREDE BACKSLASHES ENTFERNEN BEVOR MAN ZU EXE KONVERTIERT
	def changeskin():
		global SkinPack
		if SkinPack == 1:
			SkinPack = 0
			SelectSkin()
			print ("Skinpack : Runescape")
		elif SkinPack == 0:
			SkinPack = 1
			SelectSkin()
			print ("Skinpack : Shishasheesh")

#BAUE UNSER GUI-------------------------------------------------------------------------------------------------------------------------------------------------
	canvas = Toplevel()
	canvas.title('NoobiClicker')
	canvas.columnconfigure(0, weight=1)
	canvas.rowconfigure(0, weight=1)
	canvas.resizable(False, False)

	menubar = Menu(canvas)
	# create a pulldown menu, and add it to the menu bar
	optionmenu = Menu(menubar, tearoff=0)
	optionmenu.add_command(label="Ändere Skin", command=changeskin)
	optionmenu.add_command(label="Sei Cool")
	optionmenu.add_separator()
	optionmenu.add_command(label="Exit")
	menubar.add_cascade(label="Optionen", menu=optionmenu)

	# create more pulldown menus
	mehrmenu = Menu(menubar, tearoff=0)
	mehrmenu.add_command(label="Platzhalter")
	mehrmenu.add_command(label="Platzhalter")
	mehrmenu.add_command(label="Platzhalter")
	menubar.add_cascade(label="Mehr", menu=mehrmenu)

	helpmenu = Menu(menubar, tearoff=0)
	helpmenu.add_command(label="About")
	canvas.config(menu=menubar)

	MainFrame = Frame(canvas, bg='red')
	MainFrame.grid(row=0, column=0, sticky='news')
	MainFrame.columnconfigure(0 , weight=1)
	MainFrame.rowconfigure(1, weight=1)

	GameFrame = Frame(MainFrame, bg='green')
	GameFrame.grid(row=1, column=0,columnspan=3,padx=20, sticky='nsew')

	SpacerFrame = Frame(MainFrame, bg='blue')
	SpacerFrame.grid(row=2,column=0,columnspan=3, sticky='ew')

	WaterMark = Frame(MainFrame)
	WaterMark.grid(row=3,column=0,columnspan=3)
	Label(WaterMark,text="Erstellt von Dennis Leipe // Version "+CurrentGameVersion+" (Neuste " +version+ ")", fg='blue',font=('Helvetica',8,'underline')).pack(side=LEFT)
	SelectSkin()
	#canvas.geometry("500x200") 
	#Klick Button und Text -----------------------------------------
	KlickButton = Button(GameFrame, text="Click Mich!",image=level1, command= DoKlick, bg='green', activebackground="red")
	KlickButton.grid(row=1, column=3, padx=3, pady=3)
	KlickCounterText = Label(GameFrame, text="Dein Klickkonto: " + str(Klickkonto))
	KlickCounterText.grid(row=2, column=1, padx=3, pady=3)

	#BUTTON UND TEXT FÜR AUTOKLICKER INFOS---------------------------
	KaufKlickerButton = Button(GameFrame, text="Kaufe einen Autoklicker (" + str(AutoKlickerKosten) + ")", command= BuyAutoKlicker)
	KaufKlickerButton.grid(row=6, column=4, padx=3, pady=3)
	AutoklickerText = Label (GameFrame, text= "Deine Autoklicker: " + str(Autoklicker))
	AutoklickerText.grid(row=4, column=1, padx=3, pady=3)

	KaufKlickUpgradeButton = Button(GameFrame, text="Kaufe Klick Upgrade (" + str(KlickUpgradeKosten) + ")", command= BuyKlickerUpgrade)
	KaufKlickUpgradeButton.grid(row=5, column=4, padx=3, pady=3)
	KlickUpgradeText = Label (GameFrame, text= "Noobis pro Klick: " + str(NoobisProKlick)[:3])
	KlickUpgradeText.grid(row=3, column=1, padx=3, pady=3)
	#STARTE DEN LOOP FÜR DIE AUTOKLICKER UND DAS IMAGE UPDATE------------------------------------------------------------------------------------------------------------------
	DoAutoKlick()
	UpdateNoobi()
	savegame()
	canvas.mainloop()


#BAUE UNSER UPDATE INTERFACE-------------------------------------------------------------------------------------------------------------------------------------------------

def updateinterface():
	def close():
		win.destroy()
	win = Toplevel()
	win.wm_title("Game Update benötigt!")
	win.geometry("500x200")
	l = Label(win, text="Deine Version des Spiels ist Outdated")
	l.pack()
	bupdate = Button(win, text="Jetzt Updaten auf Version "+ version, command=updateGame)
	bupdate.pack()
	bclose = Button(win, command=close)
	bclose = Button(win, text="Mit Version "+CurrentGameVersion+" weiter Spielen", command=lambda:[startgame(),close()])
	bclose.pack()
	win.mainloop()


#RUN!
try:
	with urllib.request.urlopen('http://oesterland.de/anderes/noobiclicker/version.txt') as response:
		version = response.read().decode('utf-8')
		versioncheck()
except urllib.error.HTTPError:
	print ("Kann neue Version nicht Laden")
	startgame()

