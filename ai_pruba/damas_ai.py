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

surface = pygame.image.load('ai_pruba/IMG/TABLERO_MADERA.jpeg')
font = pygame.font.SysFont('arial', 30, bold= True)


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
    surface = pygame.image.load('ai_pruba/IMG/TABLERO_MADERA.jpeg')
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
    for row in range(cons.ROWS):
        for col in range(cons.COL):
            ficha = tablero_matriz[row][col]
            if ficha != 0:
                x = cons.BOARD_POSICION[0] + col * cons.CASILLA_SIZE + cons.CASILLA_SIZE // 2
                y = cons.BOARD_POSICION[1] + row * cons.CASILLA_SIZE + cons.CASILLA_SIZE // 2
                if ficha == 1:
                    color = cons.AMARILLO
                elif ficha == 2:
                    color = cons.VERDE
                elif ficha == 3:
                    color = cons.AMARILLO_NEON
                    pygame.draw.circle(ventana, cons.BEIGE, (x, y), 18)
                    pygame.draw.circle(ventana, cons.NEGRO, (x, y), 16)
                else:
                    color = cons.VERDE_NEON
                    pygame.draw.circle(ventana, cons.BEIGE, (x, y), 18)
                    pygame.draw.circle(ventana, cons.NEGRO, (x, y), 16)
                pygame.draw.circle(ventana, color,(x,y),15)
    #fichas_ai(row,col)
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
    #fichas_player(row,col)
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
    direccion_mov = []

    if ficha == 1: #AI 
        direccion_mov = [(1 , -1), (1, 1)] #se mueve haciaabajo
        jugador_contrario = 2
    elif ficha == 2: #juagadpr
        direccion_mov = [(-1 , -1), (-1, 1)]  #se mueve hacia arriba
        jugador_contrario = 1
    elif ficha == 3: #corona_AI
        for step in range(1, 9):
            direccion_mov.extend([
                (-step, -step),
                (-step, step),
                (step, -step),
                (step, step)
            ])
        jugador_contrario = 2
    elif ficha == 4: #corona_jugdor
        for step in range(1, 9):
            direccion_mov.extend([
                (-step, -step),
                (-step, step),
                (step, -step),
                (step, step)
            ])
        jugador_contrario = 1
    else :
        return POSIBLE_MOV
    

    for cambiar_row,cambiar_col in  direccion_mov:
        nueva_row = row + cambiar_row
        nueva_col = col + cambiar_col
        if 0 <= nueva_row < cons.ROWS and 0 <= nueva_col < cons.COL:
            if tablero_matriz[nueva_row][nueva_col] == 0:
                POSIBLE_MOV.append((nueva_row, nueva_col))
            elif tablero_matriz[nueva_row][nueva_col] == jugador_contrario:
                 salto_row = nueva_row + cambiar_row
                 salto_col = nueva_col + cambiar_col
                 if 0 <= salto_row < cons.ROWS and 0 <= salto_col < cons.COL:
                        if tablero_matriz[salto_row][salto_col] == 0:
                            POSIBLE_MOV.append((salto_row, salto_col))

    return POSIBLE_MOV

def mover_fichas(ficha_original,ficha_copia):
    ficha_original_row , ficha_original_col = ficha_original
    ficha_copia_row, ficha_copia_col = ficha_copia
    

    ficha = tablero_matriz[ficha_original_row][ficha_original_col]

    #quitar ficha contraria
    if abs(ficha_copia_row - ficha_original_row) == 2 and abs(ficha_copia_col - ficha_original_col) == 2:
        fila_comida = (ficha_original_row + ficha_copia_row) // 2
        col_comida = (ficha_original_col + ficha_copia_col) // 2
        tablero_matriz[fila_comida][col_comida] = 0  # Eliminar ficha comida

    tablero_matriz[ficha_copia_row][ficha_copia_col] = ficha
    tablero_matriz[ficha_original_row][ficha_original_col] = 0

def obtener_fila_col(posicion):
    x , y= posicion

    if (x < cons.BOARD_POSICION[0] or x >= cons.BOARD_POSICION[0] + cons.COL * cons.CASILLA_SIZE or
        y < cons.BOARD_POSICION[1] or y >= cons.BOARD_POSICION[1] + cons.ROWS * cons.CASILLA_SIZE):
        return None, None

    #fila y columna posicion
    col = (x - cons.BOARD_POSICION[0]) // cons.CASILLA_SIZE
    row = (y - cons.BOARD_POSICION[1]) // cons.CASILLA_SIZE  
    
    return row,col

def coronar_fichas():
    for col in range(cons.COL):
        # Verificar si fichas del jugador (2) llegaron a la primera fila
        if tablero_matriz[0][col] == 2:
            tablero_matriz[0][col] = 4
        
        # Verificar si fichas de la AI (1) llegaron a la última fila
        if tablero_matriz[cons.ROWS-1][col] == 1:
            tablero_matriz[cons.ROWS-1][col] = 3


inicializar_tablero()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
                posicion = pygame.mouse.get_pos()
                row, col = obtener_fila_col(posicion)

                if row is not None and col is not None:
                    if FICHA_SELECCIONADA:
                        
                        if (row, col) in POSIBLE_MOV:
                            mover_fichas(FICHA_SELECCIONADA, (row, col))
                            coronar_fichas()
                            FICHA_SELECCIONADA = None
                            POSIBLE_MOV = []
                        else:
                            try:
                                if tablero_matriz[row][col] != 0:
                                    FICHA_SELECCIONADA = (row, col)
                                    POSIBLE_MOV = calcular_posmov(row, col)
                            except IndexError:
                                pass

                    else:
                        if tablero_matriz[row][col] != 0:
                            FICHA_SELECCIONADA = (row, col)
                            POSIBLE_MOV = calcular_posmov(row, col)

        
    tablero()
    #ventana.blit(title, (125, 50))  
    pygame.display.update()
