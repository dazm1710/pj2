import pygame, sys
import Imagen
from Imagen import *
booleano = True
pygame.init()
ventana = pygame.display.set_mode((540,540))
pygame.display.set_caption("Personaje Atacando")
personaje = Imagen()
ventana.fill((0,0,0))

while booleano:
    personaje.dibujar(ventana)
    for event in pygame.event.get():
        personaje.accion()
        if event.type == pygame.QUIT:
            booleano = False
            
    pygame.display.update()
pygame.quit()
sys.exit
