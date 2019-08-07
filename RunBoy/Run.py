# ALLE IMPORTS	#######################################################################################################################
import pygame
from pygame.locals import *
from cacheextract import *
import os,sys
import winsound
from chars import *
#INITIALISIERE PYGAME 	#####################################################################################################################
pygame.init()

CurrentGameVersion = "Alpha 1.2"
#DEKLARIERE EIN PAAR FARBEN 	##########################################################################################################
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)
cyan = (224,255,255)
brown = (222,184,135)
#GLOBALE VARIABLEN 	###################################################################################################################
gravity = 2
cachedir = os.path.expanduser("~\\RunBoyDL\\")

#ERSTE FUNKTION ZUM MALEN VOM SCREEN 	########################################################################################

def DrawScreen():
	MainGameLoop = True
	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	clock = pygame.time.Clock()
	screen = pygame.display.set_mode((640,480))
	pygame.display.set_caption("TopDownShooter")
	char = Player("Admin", 100, 320, 310)
	enemy1 = Enemy("Gunner", 100, 330, 310)
	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	while MainGameLoop:
		screen.fill(cyan)				#X Y With Height
		boden = pygame.draw.rect(screen, brown, [0, 410, 640, 70],0)
		font = pygame.font.SysFont("comicsansms", 12)
		debuginfo = font.render("Char-X: " + str(char.x) + "     Char-Y: " + str(char.y) , 1, (10, 10, 10))
		screen.blit(debuginfo, (0,0))
		HealthAmount = font.render("Health: 100", 1, (255, 10, 10))
		screen.blit(HealthAmount, (400,0))
		GunAmmoAmount = font.render("Gun: M4a1 - 30/4", 1, (10, 10, 200))
		screen.blit(GunAmmoAmount, (500,0))
	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



		for event in pygame.event.get(): # User did something
			if event.type == pygame.QUIT: # If user clicked close
				MainGameLoop = False # Flag that we are done so we exit this loop
	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
			if event.type == KEYDOWN:
				if (event.key == pygame.K_a):
					char.left = True
				elif (event.key == pygame.K_d):
					print("Rechts")
				elif (event.key == pygame.K_w):
					print ("Oben")
					if onGround == True:
						while char.y >= 250:
							char.y -= gravity
				elif (event.key == pygame.K_s):
					print("UNTEN")
	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		keys_pressed = pygame.key.get_pressed()
		char.draw(screen)
		enemy1.draw(screen)
		while enemy1.x >= 600:
			enemy1.x += 1
		


		if keys_pressed[pygame.K_a]:
			char.x -= 1
			char.left = True
			char.draw(screen)
		if keys_pressed[pygame.K_d]:
			char.x += 1
		if keys_pressed[pygame.K_d] and keys_pressed[pygame.K_LSHIFT]:
			char.x += 2.5
		if keys_pressed[pygame.K_a] and keys_pressed[pygame.K_LSHIFT]:
			char.x -= 2.5
		#if keys_pressed[pygame.K_UP]:

		if keys_pressed[pygame.K_DOWN]:
			print ("Eins nach UNTEN")
	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		if char.y <= 310:
			char.y += gravity
			onGround = False
		else:
			onGround = True

		if char.x <= -38:
			char.x = 590
		if char.x >= 615:
			char.x = -27



	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		pygame.display.update()
		clock.tick(60)
	pygame.quit()
##########################################################################################################################################


def StartGame():
	winsound.PlaySound(None, winsound.SND_PURGE)
	DrawScreen()
##########################################################################################################################################