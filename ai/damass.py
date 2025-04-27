#AMARILLOS AI
#VERDE JUEGADOR 


from tkinter import font
import pygame
import sys
import constantes as cons

pygame.init()
ventana = pygame.display.set_mode((cons.WIDTH , cons.HEIGHT))
pygame.display.set_caption("Damas")

run = True

surface = pygame.image.load('img/tablero_madera.jpeg')
font = pygame.font.SysFont('arial', 30, bold= True)
#AI
#Imagen de corona cuando gana
#win_ai = pygame.image.load('img/corona_amarilla.png')
#titulo de  cuando gana
title = font.render("DAMAS CHINAS", False, cons.AMARILLO)
#ventana.blit(title, (60, 10))
#PLAYER
#Imagen de corona cuando gana
#win_jugador = pygame.image.load('img/corona_verde.png')
#title = font.render("DAMAS CHINAS", False, cons.VERDE)
#ventana.blit(title, (60, 10))
#titulo de  cuando gana 

def tablero():
    
    #fondo
    surface = pygame.image.load('img/tablero_madera.jpeg')
    
    #tablero
    for row in range(cons.ROWS):
        for col in range(cons.COL):
            if (row + col) % 2 == 0:
                color = cons.NEGRO
            else:
                color = cons.BEIGE
            rect = pygame.Rect(
                                cons.BOARD_POSICION[0] + col * cons.CASILLA_SIZE,  #coordenada x
                                cons.BOARD_POSICION[1] + row * cons.CASILLA_SIZE,  #coordenada y
                                cons.CASILLA_SIZE, cons.CASILLA_SIZE               #ancho y alto
                                )
            pygame.draw.rect(ventana, color, rect)

    #Fichas amarillas AI
    for row in range(3):
        for col in range(cons.COL):
            if (row + col) % 2 != 0:
                continue
            else:
                x = cons.BOARD_POSICION[0] + col * cons.CASILLA_SIZE + cons.CASILLA_SIZE // 2
                y = cons.BOARD_POSICION[1] + row * cons.CASILLA_SIZE + cons.CASILLA_SIZE // 2
            
                pygame.draw.circle(ventana, cons.AMARILLO, (x, y), 15)

    # Fichas verdes Jugador
    for row in range(5, 8):
        for col in range(cons.COL):
            if (row + col) % 2 == 0:
                continue
            else:
                x = cons.BOARD_POSICION[0] + col * cons.CASILLA_SIZE + cons.CASILLA_SIZE // 2
                y = cons.BOARD_POSICION[1] + row * cons.CASILLA_SIZE + cons.CASILLA_SIZE // 2
                pygame.draw.circle(ventana, cons.VERDE, (x, y), 15)
    
    #Tablero turno
    pygame.draw.rect(ventana,surface,(450, 100, 160, 150))
    title = font.render("TURNO", False, cons.AMARILLO)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

    ventana.blit(surface,(0,0)) 
    tablero()
    #ventana.blit(title, (125, 50))  
    pygame.display.update()
