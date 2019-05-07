import pyautogui, sys
import PIL.ImageGrab
from tkinter import *
import webcolors as webcolors
from pycolorname.pantone.pantonepaint import *


class App:
	def __init__(self, master):
		self.colorwindow = Canvas(root, bg="red")
		self.colorwindow.pack()

		self.textwindow = Canvas(root, bg="white", height=50)
		self.textwindow.pack()

		self.rgbtext = Label(self.textwindow, text="RGB Value: ", font=("Courier", 16))
		self.rgbtext.pack()
		self.hextext = Label(self.textwindow, text="HEX Value: ", font=("Courier", 16))
		self.hextext.pack()
		#self.colornametext = Label(self.textwindow, text="Color Name: ", font=("Courier", 16))
		#self.colornametext.pack()
		self.closestcolortext = Label(self.textwindow, text="Color Name: ", font=("Courier", 16))
		self.closestcolortext.pack()

		self.pantonenametext = Label(self.textwindow, text="Pantone Code: ", font=("Courier", 16))
		self.pantonenametext.pack()


	def closest_colour(self, requested_colour):
		min_colours = {}
		for key, name in webcolors.css3_hex_to_names.items():
			r_c, g_c, b_c = webcolors.hex_to_rgb(key)
			rd = (r_c - requested_colour[0]) ** 2
			gd = (g_c - requested_colour[1]) ** 2
			bd = (b_c - requested_colour[2]) ** 2
			min_colours[(rd + gd + bd)] = name
		return min_colours[min(min_colours.keys())]

	def get_colour_name(self, requested_colour):
		try:
			closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
		except ValueError:
			closest_name = self.closest_colour(requested_colour)
			actual_name = None
		return actual_name, closest_name


	def change(self):
		try:
			x, y = pyautogui.position()
			positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
			print(positionStr, end='')
			print('\b' * len(positionStr), end='', flush=True)

			PIL.ImageGrab.grab().size
			rgb = PIL.ImageGrab.grab().load()[x,y]
			mycolor = '#%02x%02x%02x' % (rgb) 

			requested_colour = (rgb)
			actual_name, closest_name = self.get_colour_name(requested_colour)

			pantone_colors = PantonePaint()
			pantonecolor = pantone_colors.find_closest((rgb))

			self.colorwindow.configure(bg=mycolor)
			self.colorwindow.after(1000, self.change)

			self.rgbtext.config(text="RGB Value: "+ str(rgb))
			self.hextext.config(text="HEX Value: "+ str(mycolor).upper())
			#self.colornametext.config(text="Actual colour name: " + str(actual_name))
			self.closestcolortext.config(text="Closest colour name: " + str(closest_name))
			self.pantonenametext.config(text="Pantone code:" + str(pantonecolor)[6:17])
		except IndexError:
			self.rgbtext.config(text="BEWEGE DEN CURSER ZURÜCK")
			self.hextext.config(text="Nur auf dem 1. Bildschirm arbeiten!")
			#self.colornametext.config(text="Starte das Programm neu")
			self.closestcolortext.config(text="Starte das Programm neu!")





root = Tk()
root.title("WBLK Color Picker ~ DL")
root.geometry("450x400")
app = App(root)
app.change()
root.mainloop()