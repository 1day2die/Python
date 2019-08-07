import os
import pygame
cachedir = os.path.expanduser("~\\RunBoyDL\\")

class Player():
	def __init__ (self, name, health, x, y):
		self.name = name
		self.health = health
		self.x = x
		self.y = y
		self.standing = True
		self.left = False
		self.right =False
		print ("Chars Loaded")

	def draw(self, screen):
		if self.standing:
			screen.blit((pygame.image.load(os.path.expanduser("~\\RunBoyDL\\sprites\\char\\char_stand.png")).convert_alpha()),(self.x,self.y))
		elif self.right:
			screen.blit((pygame.image.load(os.path.expanduser("~\\RunBoyDL\\sprites\\char\\char_walk_right.png")).convert_alpha()),(self.x,self.y))
		elif self.left:
			screen.blit((pygame.image.load(os.path.expanduser("~\\RunBoyDL\\sprites\\char\\char_walk_left.png")).convert_alpha()),(self.x,self.y))


class Enemy():
	def __init__ (self, name, health, x, y):
		self.name = name
		self.health = health
		self.x = x
		self.y = y
		self.standing = True
		self.left = False
		self.right =False
		print ("Enemy Loaded")

	def draw(self, screen):
		if self.standing:
			screen.blit((pygame.image.load(os.path.expanduser("~\\RunBoyDL\\sprites\\char\\char_stand.png")).convert_alpha()),(self.x,self.y))
		elif self.right:
			screen.blit((pygame.image.load(os.path.expanduser("~\\RunBoyDL\\sprites\\char\\char_walk_right.png")).convert_alpha()),(self.x,self.y))
		elif self.left:
			screen.blit((pygame.image.load(os.path.expanduser("~\\RunBoyDL\\sprites\\char\\char_walk_left.png")).convert_alpha()),(self.x,self.y))
