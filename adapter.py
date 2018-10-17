import pygame, sys
from pygame.locals import *
from disparo import *
from Personaje2.Imagen import *


class PersonajeAbstracto():
    def dispara(self,posx,posy): pass
    def dibujar(self): pass
    

pj = Imagen()
class AdapterPersonaje(PersonajeAbstracto, pygame.sprite.Sprite):

    def __init__(self, Imagen):
        
        self.pj = Imagen
        self.rect = self.pj.imagen.get_rect()
        self.rect.centerx=150
        self.rect.centery=620
        self.listaDisparo=[]

    def disparar(self):
        self.pj.accion()
        
        """self.pj.disparar(posx,posy)
        self.pj.rect.right+=self.pj.velocidad"""

    def dispara (self, posx,posy):
        bomba = Bomba(posx,posy)
        self.listaDisparo.append(bomba)
        
    def dibujar (self,superficie):
        
        superficie.blit(self.pj.imagen,self.rect)

