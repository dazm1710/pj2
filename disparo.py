"""
@author: David s

"""
import pygame

#heredar el Sprite
class Bomba(pygame.sprite.Sprite):
    
    
    def __init__(self,posX,posY):
        pygame.sprite.Sprite.__init__(self)
        self.imagenA = pygame.image.load('imagenes/b2.png')
        self.imagenB = pygame.image.load('Imagenes/b1.png')
        self.imagenC = pygame.image.load('Imagenes/e1.png')
        self.imagenD = pygame.image.load('Imagenes/e2.png')
        self.imagenE = pygame.image.load('Imagenes/e3.png')
        self.imagenF = pygame.image.load('Imagenes/f.png')
        self.listaImagenes = [self.imagenA,
                              self.imagenB,
                              self.imagenC,
                              self.imagenD,
                              self.imagenE,
                              self.imagenF]
        self.posImagen=0
        
        self.imagenProyectil = self.listaImagenes[self.posImagen]
        self.imagenProyectil = pygame.transform.flip(self.imagenProyectil, True, False)
        self.rect = self.imagenProyectil.get_rect()
        self.tiempoCambio = 1
        self.velocidadDisparo = 2
        self.rect.top=posY
        self.rect.left=posX
        
    #funcion para determinar el desplazamiento del misil
    def trayecto(self):
        if self.rect.left<=500:
            self.rect.left=self.rect.left+self.velocidadDisparo

        if self.rect.top>500:
            if self.rect.left <280:
                self.rect.top=self.rect.top-self.velocidadDisparo

        if self.rect.top<600:
            if self.rect.left >300:
                self.rect.top=self.rect.top+self.velocidadDisparo

    def cambioImg (self):
        if self.rect.top > 450:
            if self.rect.left==200:
                self.posImagen =1
                
        if self.rect.top == 500:
            if self.rect.left == 280:
                self.posImagen =2
                
        if self.rect.top >= 450:
            if self.rect.left > 300:
                self.posImagen =3

        if self.rect.top == 600:
            if self.rect.left > 300:
                self.posImagen =4

        if self.rect.top == 600:
            if self.rect.left > 420:
                self.posImagen = 5
            """self.tiempoCambio +=1
            if self.posImagen > len(self.listaImagenes)-1:
                self.posImagen=0
                """

            
    #funcion para dibujar el misil
    def dibujar(self,superficie):
        self.imagenProyectil = self.listaImagenes[self.posImagen]
        superficie.blit(self.imagenProyectil,self.rect)
