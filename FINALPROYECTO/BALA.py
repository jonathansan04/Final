import pygame
from pygame.sprite import Sprite
from pygame import *
import UTIL

class Bala(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.imagenes = [UTIL.cargar_imagen('Imagenes/rocket.png')
        self.lista = []

        for n in range(3):
            sel.rect = self.imagen.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.lista.append( self.rect)
            y -=40

    def mover( self, velocidad):
            for rectangulo in self.lista:
                         rectangulo.move_ip( 0 , velocidad)
                         

    def pintar (self, pantalla):
                         for rectangulo in self.lista:
                         rectangulo.blit( self.imagen , rectangulo)

     def getRectangulo( self):
                    return self.lista
 
            
