import pygame, sys
from pygame.locals import *
#from Personaje2.Imagen import *
from adapter import *
#from adapterPersonaje import *
#from Clases.jugador import *

#pygame.display.set_mode((ancho,alto))

def controladorJuego():
    pygame.init()
    #colorTexto = (0,212,52)
    fuente = pygame.font.SysFont('Calibri',30)
    #texto = fuente.render("Nota: Presiona barra espaciadora para disparar",0,colorTexto)

    ventana = pygame.display.set_mode((1000,700))
    fondo = pygame.image.load('imagenes/background.jpg')
    fondo = pygame.transform.scale(fondo, (1000,700))
    pygame.display.set_caption("Disparos")
    personajeViejo= Imagen()
    
    persona = AdapterPersonaje(personajeViejo)
    reloj = pygame.time.Clock()
    
    while True:
        reloj.tick(60)
        tiempo = pygame.time.get_ticks()/1000
        ventana.blit(fondo,(0,0))
        
        #ventana.blit(texto,(50,100))
        if len(persona.listaDisparo)>0:
            for x in persona.listaDisparo:
                x.dibujar(ventana)
                x.trayecto()
                x.cambioImg()
                if x.rect.left==600:
                    persona.listaDisparo.remove(x)
                    

        for evento in pygame.event.get():
            x,y = persona.rect.center
            
            persona.disparar()
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
                break
            elif evento.type == pygame.KEYDOWN:
                if evento.key ==K_z:
                    x,y = persona.rect.center
                    persona.dispara(x,y)
                    
        persona.dibujar(ventana)
        pygame.display.update()

controladorJuego()
