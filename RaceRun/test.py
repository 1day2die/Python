#Importieren aller Bibliotheken ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import random
import pygame
from tkinter import *
from functions.highscores import *
from PIL import Image, ImageTk
import os
import urllib.request
import urllib
import webbrowser



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

BLACK = ( 0, 0, 0)
GREY = ( 125, 125, 125)
GREEN = (0, 125, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
BLUE = (100, 100, 255)


colorList = (RED, GREEN, PURPLE, YELLOW, CYAN, BLUE)
punkte = 0
username = ""
CurrentGameVersion = "Alpha 2.0"
with urllib.request.urlopen('http://oesterland.de/anderes/gamecoding/noobiracer/version.txt') as response:
	version = response.read().decode('utf-8')
root = Tk() #Erstelle neben unseren Update fenster und Game Fenster ein weiteres 
root.withdraw() #UNSICHTBARES Main Fenster (muss sein -.-")
# CLASS CAR ~~~~☺# CLASS CAR ~~~~☺# CLASS CAR ~~~~☺# CLASS CAR ~~~~☺# CLASS CAR ~~~~☺
class PlayerCar(pygame.sprite.Sprite):
#This class represents a car. It derives from the "Sprite" class in Pygame.

	def __init__(self, color, width, height, speed):
        # Call the parent class (Sprite) constructor
		super().__init__()

		# Pass in the color of the car, and its x and y position, width and height.
		# Set the background color and set it to be transparent
		self.image = pygame.Surface([width, height])
		self.image.fill(WHITE)
		self.image.set_colorkey(WHITE)

		#Initialise attributes of the car.
		self.width=width
		self.height=height
		self.color = color
		self.speed = speed

		# Draw the car (a rectangle!)
		pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])

		# Instead we could load a proper picture of a car...
		self.image = pygame.image.load("sprites/car.png").convert_alpha()
		self.image = pygame.transform.scale(self.image,( 50, 80))
		self.mask = pygame.mask.from_surface(self.image)

		# Fetch the rectangle object that has the dimensions of the image.
		self.rect = self.image.get_rect()

	def moveRight(self, pixels):
		self.rect.x += pixels
	def moveUp(self, pixels):
		self.rect.y -= pixels
	def moveDown(self,pixels):
		self.rect.y += pixels

	def moveLeft(self, pixels):
		self.rect.x -= pixels

	def higherSpeed(self, speed):
		self.rect.y += self.speed * speed / 20

	def reduceSpeed(self, speed):
		self.rect.y -= self.speed * speed / 20

	def changeSpeed(self, speed):
		self.speed = speed

	def repaint(self, color):
		self.color = color
		pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])


class EnemyCar(pygame.sprite.Sprite):
#This class represents a car. It derives from the "Sprite" class in Pygame.

	def __init__(self, color, width, height, speed):
        # Call the parent class (Sprite) constructor
		super().__init__()

		# Pass in the color of the car, and its x and y position, width and height.
		# Set the background color and set it to be transparent
		
		self.image = pygame.Surface([width, height])
		self.image.fill(WHITE)
		self.image.set_colorkey(WHITE)

		#Initialise attributes of the car.
		self.width=width
		self.height=height
		self.color = color
		self.speed = speed

		# Draw the car (a rectangle!)
		pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])

		# Instead we could load a proper picture of a car...
		self.image = pygame.image.load("sprites/enemy.png").convert_alpha()
		self.image = pygame.transform.scale(self.image,( 50, 80))

		# Fetch the rectangle object that has the dimensions of the image.
		self.rect = self.image.get_rect()

	def moveRight(self, pixels):
		self.rect.x += pixels
	def moveUp(self, pixels):
		self.rect.y -= pixels
	def moveDown(self,pixels):
		self.rect.y += pixels

	def moveLeft(self, pixels):
		self.rect.x -= pixels

	def higherSpeed(self, speed):
		self.rect.y += self.speed * speed / 20

	def reduceSpeed(self, speed):
		self.rect.y -= self.speed * speed / 20

	def changeSpeed(self, speed):
		self.speed = speed

	def repaint(self, color):
		self.color = color
		pygame.draw.rect(pygame.image.load("sprites/enemy.png").convert_alpha(), self.color, [0, 0, self.width, self.height])
# CLASS CAR ~~~~☺# CLASS CAR ~~~~☺# CLASS CAR ~~~~☺# CLASS CAR ~~~~☺# CLASS CAR ~~~~☺# CLASS CAR ~~~~☺# CLASS CAR ~~~~☺

def updateGame():
	webbrowser.open('http://oesterland.de/anderes/noobiclicker/noobiclicker.rar')


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
	bclose = Button(win, text="Mit Version "+CurrentGameVersion+" weiter Spielen", command=lambda:[mainmenu(),close()])
	bclose.pack()
	win.mainloop()



def run():
	global punkte
	speed = 1
	punkte = 0
	pygame.init()
	SCREENWIDTH=600
	SCREENHEIGHT=600
	 
	size = (SCREENWIDTH, SCREENHEIGHT)
	screen = pygame.display.set_mode(size)
	pygame.display.set_caption("Car Racing")
	 
	#This will be a list that will contain all the sprites we intend to use in our game.
	all_sprites_list = pygame.sprite.Group()
	 
	 
	playerCar = PlayerCar(RED, 60, 80, 70)
	playerCar.rect.x = 160
	playerCar.rect.y = SCREENHEIGHT - 100
	 
	car1 = EnemyCar(PURPLE, 60, 80, random.randint(50,100))
	car1.rect.x = 125
	car1.rect.y = -100
	 
	car2 = EnemyCar(YELLOW, 60, 80, random.randint(50,100))
	car2.rect.x = 225
	car2.rect.y = -600
	 
	car3 = EnemyCar(CYAN, 60, 80, random.randint(50,100))
	car3.rect.x = 325
	car3.rect.y = -300
	 
	car4 = EnemyCar(BLUE, 60, 80, random.randint(50,100))
	car4.rect.x = 425
	car4.rect.y = -900
	 
	 
	# Add the car to the list of objects
	all_sprites_list.add(playerCar)
	all_sprites_list.add(car1)
	all_sprites_list.add(car2)
	all_sprites_list.add(car3)
	all_sprites_list.add(car4)
	 
	all_coming_cars = pygame.sprite.Group()
	all_coming_cars.add(car1)
	all_coming_cars.add(car2)
	all_coming_cars.add(car3)
	all_coming_cars.add(car4)
 


	#Allowing the user to close the window...
	carryOn = True
	clock=pygame.time.Clock()
	 
	while carryOn:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				carryOn=False
			elif event.type==pygame.KEYDOWN:
				if event.key==pygame.K_x:
					playerCar.moveRight(10)

		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT]:
			playerCar.moveLeft(8)
		if keys[pygame.K_RIGHT]:
			playerCar.moveRight(8)
		if keys[pygame.K_UP]:
			playerCar.moveUp(5)
		if keys[pygame.K_DOWN]:
			playerCar.moveDown(5)


		if keys[pygame.K_KP_PLUS]:
			speed += 0.05
		if keys[pygame.K_KP_MINUS]:
			speed -= 0.05


		#Game Logic

	#Check if there is a car collision
		if playerCar.rect.x > SCREENWIDTH - 100:
			carryOn=False
		if playerCar.rect.x < SCREENWIDTH - 550:
			carryOn=False
		if playerCar.rect.y > SCREENHEIGHT:
			carryOn=False
		if playerCar.rect.y < SCREENHEIGHT - 625:
			carryOn=False


		car_collision_list = pygame.sprite.spritecollide(playerCar,all_coming_cars,False,pygame.sprite.collide_mask)
		for car in car_collision_list:
			print("Car crash!")
			#End Of Game
			carryOn=False
		for car in all_coming_cars:
			car.higherSpeed(speed)
			if car.rect.y > SCREENHEIGHT:
				car.changeSpeed(random.randint(50,100))
				car.repaint(random.choice(colorList))
				car.rect.y = -200
				punkte += 1
				speed += 0.01

		all_sprites_list.update()
		# --- Drawing code should go here
		# First, clear the screen to white. 

		screen.fill(GREEN)
	#The you can draw different shapes and lines or add text to your background stage.
										#X   Y   Größe X Größe Y
		pygame.draw.rect(screen, GREY, [100, 0, 400, 600],0)
		pygame.draw.line(screen, WHITE, [100, 0], [100, 600], 3)
		pygame.draw.line(screen, WHITE, [200, 0], [200, 600], 3)
		pygame.draw.line(screen, WHITE, [300, 0], [300, 600], 3)
		pygame.draw.line(screen, WHITE, [400, 0], [400, 600], 3)
		pygame.draw.line(screen, WHITE, [500, 0], [500, 600], 3)

		font = pygame.font.Font(None, 20)
		text = font.render("Punkte: " + str(punkte) , 1, (10, 10, 10))
		screen.blit(text, (0,0))
	#Now let's draw all the sprites in one go. (For now we only have 1 sprite!)
		all_sprites_list.draw(screen)
	# --- Go ahead and update the screen with what we've drawn.
		pygame.display.flip()

	# --- Limit to 60 frames per second
		clock.tick(60)
 
#Once we have exited the main program loop we can stop the game engine:
	pygame.quit()


#MAIN MENU#
def mainmenu():
	global punkte
	global highscorename
	global erreichtepunkte
	global dbconnection
	global main
	main = Toplevel()
	main.title("TestPythonMainMenu")
	main.geometry("500x300") #You want the size of the app to be 500x500
	main.resizable(0, 0) #Don't allow resizing in the x or y direction
	main.configure(bg='black')
	canvas = Canvas(main, width=100,height=100)
	canvas.pack()
	canvas.config(bg="white")

	menu = Menu(main)
	main.config(menu=menu)
	filemenu = Menu(menu)
	menu.add_cascade(label="Funktionen", menu=filemenu)
	filemenu.add_command(label="Show Highscores")
	filemenu.add_command(label="Open...")
	filemenu.add_separator()
	filemenu.add_command(label="Exit", command=main.quit)

	helpmenu = Menu(menu)
	menu.add_cascade(label="Help")
	helpmenu.add_command(label="About...")

	startbutton = Button (canvas,text="Start Game",command=run,bg="lightgreen")
	startbutton.pack(pady= 10)


	highscoresbutton = Button (canvas,text="Show highscores")
	highscoresbutton.pack(pady= 10)
	if dbconnection:
		highscorename = Entry(canvas)
		highscorename.insert(10,"Enter Username")
		highscorename.pack()
		sendhighscores = Button (canvas,text="Send Highscores",command= lambda: sendtosql("test",highscorename.get(),punkte))
		sendhighscores.pack()
	else:
			erreichtepunkte = Label(canvas, text="Couldn't reach the DB. You won't be able to save your Highscore")
			erreichtepunkte.pack(pady= 10)

	erreichtepunkte = Label(canvas, text=punkte)
	erreichtepunkte.pack()

	quitbutton = Button (canvas, text="Quit", command=main.destroy,bg="red")
	quitbutton.pack(side = BOTTOM, pady= 10)
	Refresher()



def versioncheck():
	global version
	if version != CurrentGameVersion:
		updateinterface()
	elif version == CurrentGameVersion:
		mainmenu()
		Refresher()
		main.mainloop()


def Refresher():
    global erreichtepunkte
    global main
    global punkte
    global highscorename
    erreichtepunkte.configure(text=punkte)
    main.after(1000, Refresher) # every second...







versioncheck()
