import pygame
from pygame import *
class Imagen(pygame.sprite.Sprite):
    def __init__(self):
        
        self.imagen1 = pygame.image.load('imagen 3.png')
        self.imagen2 = pygame.image.load('imagen 2.png')
        self.imagen3 = pygame.image.load('imagen 1.png')
        self.imagen = self.imagen1
        self.imagenes = []
        self.imagenes.append(self.imagen1)
        self.imagenes.append(self.imagen2)
        self.imagenes.append(self.imagen3)
        self.rect = self.imagen1.get_rect()
        self.posX = 10
        self.posY =550
        self.rect.move_ip(self.posX, self.posY)
        self.cte = 0
    def accion(self):
        accion = pygame.key.get_pressed()
        if accion[K_z]:
            self.cte=0
        if self.cte == 0:
            self.imagen = self.imagenes[1]
            self.cte = 1
        elif self.cte == 1:
            self.imagen = self.imagenes[2]
            self.cte=2
        elif self.cte == 2:
            self.cte=3
            self.imagen = self.imagenes[0]
    def dibujar(self, superficie):
        superficie.blit(self.imagen,self.rect)
