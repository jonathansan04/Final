import pygame
from pygame.sprite import Sprite
from pygame import *
import UTIL

class Nave(Sprite):
	def __init__(self):
		Sprite.__init__(self)
		self.imagenes = [UTIL.cargar_imagen('Imagenes/rocket.png'),UTIL.cargar_imagen('Imagenes/rocket.png')]
		self.image = self.imagenes[0]
		self.rect = self.image.get_rect()
		self.rect.move_ip(400, 450)
		self.vida = 100
		self.punt = 0.0
	
                
	def update(self):
		teclas = pygame.key.get_pressed()
		if teclas[K_LEFT] and self.rect.x>=10:
			self.rect.x -= 10
		elif teclas[K_RIGHT] and self.rect.x<=640-self.rect.width:
			self.rect.x += 10
		
