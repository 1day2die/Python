from tkinter import *
import os
from tkinter.messagebox import showinfo
from Run import *
import urllib.request
import urllib
from PIL import ImageTk,Image
import winsound
import webbrowser


root = Tk() #Erstelle neben unseren Update fenster und Game Fenster ein weiteres 
root.withdraw() #UNSICHTBARES Main Fenster (muss sein -.-")

with urllib.request.urlopen('http://oesterland.de/anderes/gamecoding/RunBoy/game_version.txt') as response:
	version = response.read().decode('utf-8')

#MAIN MENU#
def opendonatelink():
	webbrowser.open("www.paypal.me/leipe")
def mute():
	winsound.PlaySound(None, winsound.SND_PURGE)

def MainMenu():
	DirChecker()
	main = Toplevel()
	main.title("TestPythonMainMenu")
	main.geometry("500x300") #You want the size of the app to be 500x500
	main.resizable(0, 0) #Don't allow resizing in the x or y direction
	main.configure(bg='black')
	bgm = winsound.PlaySound(os.path.expanduser("~\\RunBoyDL\\sounds\\backgroundmusic.wav"), winsound.SND_ASYNC | winsound.SND_FILENAME)
	background_image=ImageTk.PhotoImage(Image.open(cachedir + ("sprites\\background.png")))
	background = Label(main, image=background_image)
	background.place(x=0, y=0, relwidth=1, relheight=1)

	#canvas = Canvas(main, width=100,height=100)
	#canvas.pack(side = RIGHT)
	#canvas.config(bg="white")


	menu = Menu(main)
	main.config(menu=menu)
	filemenu = Menu(menu)
	menu.add_cascade(label="Funktionen", menu=filemenu)
	filemenu.add_command(label="Show Highscores")
	filemenu.add_command(label="Controls", command=ControlsMenu)
	filemenu.add_separator()
	filemenu.add_command(label="DONATE", command=opendonatelink)
	filemenu.add_separator()
	filemenu.add_command(label="Exit", command=main.quit)


	startbutton = Button (main,text="Start Game",command=StartGame,bg="lightgreen", width = 30)
	startbutton.pack(pady= (60,10), padx = (0,20), side = TOP, anchor="e")


	controlsbutton = Button (main,text="Controls", command=ControlsMenu, width = 30)
	controlsbutton.pack(pady= 10, padx = (0,20), side = TOP, anchor="e")

	quitbutton = Button (main, text="Quit", command=main.destroy,bg="red", width = 30)
	quitbutton.pack(pady= 10, padx = (0,20), side = TOP, anchor="e")



	WaterMark = Frame(main)
	WaterMark.pack(side = BOTTOM)
	mutebutton = Button (WaterMark, text="Mute", command=mute,bg="blue",fg="white")
	mutebutton.pack(pady= 0, padx = (0,50), side = LEFT, anchor="w")

	Label(WaterMark, pady=0, text="Erstellt von Dennis Leipe // Version "+CurrentGameVersion+" (Neuste " +version+ ")", bg="white", fg='blue',font=('Helvetica',8,'underline')).pack(side=LEFT)

	donatebutton = Button (WaterMark, text="Donate", command=opendonatelink,bg="blue",fg="white")
	donatebutton.pack(pady= 0, padx = (50,0), side = LEFT, anchor="e")



	main.mainloop()

def ControlsMenu():
	main = Toplevel()
	main.title("Controls")
	main.geometry("300x300") #You want the size of the app to be 500x500
	main.resizable(0, 0) #Don't allow resizing in the x or y direction

	T = Text(main, height=2, width=30)
	T.pack()
	T.insert(END, "W A S D: MOVE\nShift: SPRINT\n")
	main.mainloop()