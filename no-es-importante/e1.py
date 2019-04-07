import pygame
from pygame.locals import *    # Nuevo en la version 0.03

pygame.init()

ancho = 800
alto = 600
velocidadX = 3
velocidadY = 3
terminado = False

pantalla = pygame.display.set_mode( (ancho, alto) )
pygame.key.set_repeat(1,25)    # Nuevo en la version 0.03

imagenMarciano = pygame.image.load("spaceinvader.png")
rectanguloMarciano = imagenMarciano.get_rect()
rectanguloMarciano.left = 200
rectanguloMarciano.top = 100

imagenNave = pygame.image.load("ufo.png")    # Nuevo en 0.03
rectanguloNave = imagenNave.get_rect()       # Nuevo en 0.03
rectanguloNave.left = ancho/2                # Nuevo en 0.03
rectanguloNave.top = alto-50                 # Nuevo en 0.03


while not terminado:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: terminado = True

    keys = pygame.key.get_pressed()          # Nuevo en 0.03
    if keys[K_LEFT]:                         # Nuevo en 0.03
        print('¡Izquierda!')
        rectanguloNave.left -= 4             # Nuevo en 0.03
    if keys[K_RIGHT]:
        print('Derecha!')                      # Nuevo en 0.03
        rectanguloNave.left += 4             # Nuevo en 0.03

    rectanguloMarciano.left += velocidadX
    rectanguloMarciano.top += velocidadY
    if rectanguloMarciano.left < 0 or rectanguloMarciano.right > ancho:
        velocidadX = -velocidadX
    if rectanguloMarciano.top < 0 or rectanguloMarciano.bottom > alto:
        velocidadY = -velocidadY

    pantalla.fill( (0,0,0) )
    pantalla.blit(imagenMarciano, rectanguloMarciano)
    pantalla.blit(imagenNave, rectanguloNave)    # Nuevo en 0.03
    pygame.display.flip()

pygame.quit()
