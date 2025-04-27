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

#
FICHA_SELECCIONADA = None
POSIBLE_MOV = []

# Matriz para representar el tablero
tablero_matriz = [[0 for _ in range(cons.COL)] for _ in range(cons.ROWS)]

def inicializar_tablero():
    for row in range(3):
        for col in range(cons.COL):
            if (row + col) % 2 == 0:
                tablero_matriz[row][col] = 1  # 1 para AI (amarillo)

    for row in range(5, 8):
        for col in range(cons.COL):
            if (row + col) % 2 == 0:
                tablero_matriz[row][col] = 2  # 2 para jugador (verde)

#AI
#Imagen de corona cuando gana
#win_ai = pygame.image.load('img/corona_amarilla.png')
#titulo de  cuando gana
#title = font.render("DAMAS CHINAS", False, cons.AMARILLO)
#ventana.blit(title, (60, 10))
#PLAYER
#Imagen de corona cuando gana
#win_jugador = pygame.image.load('img/corona_verde.png')
#title = font.render("DAMAS CHINAS", False, cons.VERDE)
#ventana.blit(title, (60, 10))
#titulo de  cuando gana 

def fichas_ai(row,col):
    #Fichas amarillas AI
    for row in range(3):
        for col in range(cons.COL):
            if (row + col) % 2 != 0:
                continue
            else:
                x = cons.BOARD_POSICION[0] + col * cons.CASILLA_SIZE + cons.CASILLA_SIZE // 2
                y = cons.BOARD_POSICION[1] + row * cons.CASILLA_SIZE + cons.CASILLA_SIZE // 2
            
                pygame.draw.circle(ventana, cons.AMARILLO, (x, y), 15)

def fichas_player(row,col):
    # Fichas verdes Jugador
    for row in range(5, 8):
        for col in range(cons.COL):
            if (row + col) % 2 != 0:
                continue
            else:
                x = cons.BOARD_POSICION[0] + col * cons.CASILLA_SIZE + cons.CASILLA_SIZE // 2
                y = cons.BOARD_POSICION[1] + row * cons.CASILLA_SIZE + cons.CASILLA_SIZE // 2
                pygame.draw.circle(ventana, cons.VERDE, (x, y), 15)
    

def tablero():
    #fondo
    surface = pygame.image.load('img/tablero_madera.jpeg')
    ventana.blit(surface, (0,0)) 
    
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

    fichas_ai(row,col)
    '''
    for row in range(3):
        for col in range(cons.COL):
            if (row + col) % 2 != 0:
                continue
            else:
                x = cons.BOARD_POSICION[0] + col * cons.CASILLA_SIZE + cons.CASILLA_SIZE // 2
                y = cons.BOARD_POSICION[1] + row * cons.CASILLA_SIZE + cons.CASILLA_SIZE // 2
            
                pygame.draw.circle(ventana, cons.AMARILLO, (x, y), 15)
'''
    # Fichas verdes Jugador
    fichas_player(row,col)
    '''
    for row in range(5, 8):
        for col in range(cons.COL):
            if (row + col) % 2 != 0:
                continue
            else:
                x = cons.BOARD_POSICION[0] + col * cons.CASILLA_SIZE + cons.CASILLA_SIZE // 2
                y = cons.BOARD_POSICION[1] + row * cons.CASILLA_SIZE + cons.CASILLA_SIZE // 2
                pygame.draw.circle(ventana, cons.VERDE, (x, y), 15)
    '''
    
    #falta moverlo para que aparezca cuando toque cada uno

    #ficha seleccionada

    if FICHA_SELECCIONADA:
        row,col = FICHA_SELECCIONADA
        x = cons.BOARD_POSICION[0] + col * cons.CASILLA_SIZE + cons.CASILLA_SIZE // 2
        y = cons.BOARD_POSICION[1] + row * cons.CASILLA_SIZE + cons.CASILLA_SIZE // 2
        pygame.draw.circle(ventana, cons.BORDE_CIR, (x, y), 25, 3)
    
    #movimientos

    for row,col in POSIBLE_MOV:
        x = cons.BOARD_POSICION[0] + col * cons.CASILLA_SIZE + cons.CASILLA_SIZE // 2
        y = cons.BOARD_POSICION[1] + row * cons.CASILLA_SIZE + cons.CASILLA_SIZE // 2
        pygame.draw.circle(ventana, cons.MOV, (x, y), 10)
    

    #Tablero turno
    turno_ai = pygame.Rect(415, 95, 150, 125)
    pygame.draw.rect(ventana, (142, 81, 26 ), turno_ai)

    #turno ai
    title_ai = font.render("TURNO", True, cons.AMARILLO)
    ventana.blit(title_ai,(turno_ai.x + 20, turno_ai.y +10))
    pygame.draw.circle(ventana, cons.AMARILLO, (turno_ai.centerx, turno_ai.y + 90), 18)

    #Tablero turno
    turno_jdr = pygame.Rect(415, 250, 150, 125)
    pygame.draw.rect(ventana, (142, 81, 26 ), turno_jdr)

     #turno jugador
    title_jdr = font.render("TURNO", True, cons.VERDE)
    ventana.blit(title_jdr,(turno_jdr.x + 20, turno_jdr.y +10))
    pygame.draw.circle(ventana, cons.VERDE, (turno_jdr.centerx, turno_jdr.y + 90), 18)

    boton = pygame.Rect(100, 430 , 200, 55)
    pygame.draw.rect(ventana, (99, 53, 11 ) , boton)
    title_boton = font.render("Reiniciar", True, cons.BEIGE)
    ventana.blit(title_boton,(boton.x + 30, boton.y +10))
    return boton

#no se spone/actualiza
#   #Tablero turno
 #   turno_jdr = pygame.Rect(415, 250, 150, 125)
  #  pygame.draw.rect(ventana, (142, 81, 26 ), turno_jdr)

def calcular_posmov(row,col):
    POSIBLE_MOV = []
    ficha = tablero_matriz [row][col]

    if ficha == 1: #AI
        direccion_mov = [(1 , -1), (1, 1)] 
        jugador_contrario = 2
    elif ficha == 2: #juagadpr
        direccion_mov = [(-1 , -1), (-1, 1)] 
        jugador_contrario = 1
    else :
        return POSIBLE_MOV
    
   
   


 
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

    
    tablero()
    #ventana.blit(title, (125, 50))  
    pygame.display.update()
