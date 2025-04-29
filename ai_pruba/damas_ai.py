#AMARILLOS AI
#VERDE JUEGADOR 



import pygame
import sys
import constantes as cons
from tkinter import font
import copy
pygame.init()
ventana = pygame.display.set_mode((cons.WIDTH , cons.HEIGHT))
pygame.display.set_caption("Damas")

run = True

turno = 2 #turno jugador 
obligado = False
surface = pygame.image.load('ai_pruba\IMG\TABLERO_MADERA.jpeg')
corona_amarilla = pygame.image.load('ai_pruba\IMG\CORONA_AMARILLOO.png')
corona_verde = pygame.image.load('ai_pruba\IMG\CORONA_VERDEE.png')

font = pygame.font.SysFont('arial', 30, bold= True)


FICHA_SELECCIONADA = None
POSIBLE_MOV = []
boton = None

# Matriz para representar el tablero
tablero_matriz = [[0 for _ in range(cons.COL)] for _ in range(cons.ROWS)]

def inicializar_tablero():
    for row in range(cons.COL): #limpia el tablero
        for col in range(cons.ROWS):
            tablero_matriz[row][col] = 0

    for row in range(3):
        for col in range(cons.COL):
            if (row + col) % 2 == 0:
                tablero_matriz[row][col] = 1  # 1 para AI (amarillo)

    for row in range(5, 8):
        for col in range(cons.COL):
            if (row + col) % 2 == 0:
                tablero_matriz[row][col] = 2  # 2 para jugador (verde)

  

def tablero():
    #fondo
    surface = pygame.image.load('ai_pruba\IMG\TABLERO_MADERA.jpeg')
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
    '''
    TURNOS
    '''
        
    if turno == 1:
            
                    #Tablero turno
        turno_ai = pygame.Rect(415, 160, 150, 125)
        pygame.draw.rect(ventana, (142, 81, 26 ), turno_ai)
        title_ai = font.render("TURNO", True, cons.AMARILLO)
        ventana.blit(title_ai,(turno_ai.x + 20, turno_ai.y +10))
        pygame.draw.circle(ventana, cons.AMARILLO, (turno_ai.centerx, turno_ai.y + 90), 18)

        

    
    elif turno == 2:
                #Tablero turno
        turno_jdr = pygame.Rect(415, 160, 150, 125)
        pygame.draw.rect(ventana, (142, 81, 26 ), turno_jdr)            #turno jugador
        title_jdr = font.render("TURNO", True, cons.VERDE)
        ventana.blit(title_jdr,(turno_jdr.x + 20, turno_jdr.y +10))
        pygame.draw.circle(ventana, cons.VERDE, (turno_jdr.centerx, turno_jdr.y +90), 18)     
        
       
     
    
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
    
    boton = pygame.Rect(100, 430 , 200, 55)
    pygame.draw.rect(ventana, cons.CAFE_BOTON , boton)
    title_boton = font.render("Reiniciar", True, cons.BEIGE)
    ventana.blit(title_boton,(boton.x + 30, boton.y +10))
    return boton



#no se spone/actualiza
#   #Tablero turno
 #   turno_jdr = pygame.Rect(415, 250, 150, 125)
  #  pygame.draw.rect(ventana, (142, 81, 26 ), turno_jdr)

def calcular_posmov(row,col,solo_capturas=False):
    POSIBLE_MOV = []
    capturas_posibles = []
    ficha = tablero_matriz [row][col]
    direccion_mov = []

    if ficha == 1: #AI 
        direccion_mov = [(1 , -1), (1, 1)] #se mueve haciaabajo
        jugador_contrario = 2
    elif ficha == 2: #juagadpr
        direccion_mov = [(-1 , -1), (-1, 1)]  #se mueve hacia arriba
        jugador_contrario = 1
    elif ficha == 3: #corona_AI
        direccion_mov = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        jugador_contrario = 2
    elif ficha == 4: #corona_jugdor
        direccion_mov = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        jugador_contrario = 1
    else :
        return POSIBLE_MOV
    

    for cambiar_row,cambiar_col in  direccion_mov:
        hubo_captura = False
        for step in range(1, 8):  # Máximo 7 pasos
            nueva_row = row + cambiar_row * step
            nueva_col = col + cambiar_col * step

            if 0 <= nueva_row < cons.ROWS and 0 <= nueva_col < cons.COL:
                if  tablero_matriz[nueva_row][nueva_col] == 0:
                    POSIBLE_MOV.append((nueva_row, nueva_col))
                    if hubo_captura:
                        capturas_posibles.append((nueva_row, nueva_col))
                elif ficha in (1, 3) and tablero_matriz[nueva_row][nueva_col] in (1, 3):  # Fichas AI
                    break
                elif ficha in (2, 4) and tablero_matriz[nueva_row][nueva_col] in (2, 4):  # Fichas Jugador
                    break
                elif tablero_matriz[nueva_row][nueva_col] == jugador_contrario or tablero_matriz[nueva_row][nueva_col] == jugador_contrario+2:
                    salto_row = nueva_row + cambiar_row
                    salto_col = nueva_col + cambiar_col
                    if 0 <= salto_row < cons.ROWS and 0 <= salto_col < cons.COL:
                            if tablero_matriz[salto_row][salto_col] == 0:
                                POSIBLE_MOV.append((salto_row, salto_col))
                                capturas_posibles.append((salto_row, salto_col))
                                hubo_captura = True
                                solo_capturas = True
                            else: break
                if ficha in (1, 2):
                    break

    if solo_capturas:
        return capturas_posibles 
    else: 
        tiene_que_capturar = False
        for r in range(cons.ROWS):
            for c in range(cons.COL):
                if tablero_matriz[r][c] in (ficha, ficha + 2) and (r != row or c != col):
                    movs = calcular_posmov(r, c, solo_capturas=True)
                    if movs:
                        tiene_que_capturar = True
                        break
            if tiene_que_capturar:
                break

        # Si hay otras fichas que pueden capturar, esta ficha no puede moverse
        if tiene_que_capturar:
            return []
        return POSIBLE_MOV

def mover_fichas(ficha_original,ficha_copia):
    global turno
    ficha_original_row , ficha_original_col = ficha_original
    ficha_copia_row, ficha_copia_col = ficha_copia
    
    ficha = tablero_matriz[ficha_original_row][ficha_original_col]

    # Determinar dirección del movimiento
    direccion_row = 1 if ficha_copia_row > ficha_original_row else -1
    direccion_col = 1 if ficha_copia_col > ficha_original_col else -1

    #quitar ficha contraria
    if abs(ficha_copia_row - ficha_original_row) >= 2:
        current_row, current_col = ficha_original_row + direccion_row, ficha_original_col + direccion_col
         # Recorrer la diagonal hasta llegar al destino
        while (current_row != ficha_copia_row) or (current_col != ficha_copia_col):
            # Si encontramos una ficha contraria, la eliminamos
            if tablero_matriz[current_row][current_col] != 0:
                tablero_matriz[current_row][current_col] = 0
            current_row += direccion_row
            current_col += direccion_col

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

    '''
    TURNOS
    '''
def fichas_turno(ficha, turno):
    if turno == 1:
        return ficha in (1, 3 ) #1 son las fichas 3 fichas coronadas
    elif turno ==2:
        return ficha in (2,4)  #2 son las fichas 4 fichas coronadas
    return False

'''
    TURNOS
    '''

def verificar_ganador(turno):
    #cuanta ficha c/u
    fichas_ai = 0
    fichas_jugador = 0

    for fila in tablero_matriz:
        for ficha in fila:
            if ficha in (1, 3):  # ai
                fichas_ai += 1
            elif ficha in (2, 4):  # jugador
                fichas_jugador += 1

    if fichas_ai == 0:
        return 2  
    elif fichas_jugador == 0:
        return 1  
    else:
        return 0  

'''
TURNOS
'''
def ganador(winner):
    if winner == 1:
        texto = pygame.Rect(100, 20 , 300, 60)
        pygame.draw.rect(ventana, cons.BEIGE, texto)
        title_boton = font.render("Ganaste", True, cons.AMARILLO)
        ventana.blit(title_boton,(texto.x + 35, texto.centery -20)) 
        corona = corona_amarilla
        corona = pygame.transform.scale(corona,  (80, 80))
        corona_rect = corona.get_rect()
        corona_rect.left = texto.left - 100
        corona_rect.centery = texto.centery
        ventana.blit(corona, corona_rect)   
        pygame.display.update()
        pygame.time.delay(4000)

    elif winner == 2:
        texto = pygame.Rect(100, 20 , 300, 60)
        pygame.draw.rect(ventana, cons.BEIGE, texto)
        title_boton = font.render("Ganaste", True, cons.VERDE)
        ventana.blit(title_boton,(texto.x + 40, texto.centery -20)) 
        corona = corona_verde
        corona = pygame.transform.scale(corona,  (80, 80))
        corona_rect = corona.get_rect()
        corona_rect.left = texto.left - 100
        corona_rect.centery = texto.centery
        ventana.blit(corona, corona_rect)   
        pygame.display.update()
        pygame.time.delay(4000)

#movimientos que pude tomar la ia
def sobreponer_mov(tablero, origen , destino):
    tablero_copia = copy.deepcopy( tablero)
    ficha = tablero_copia [origen[0]][origen[1]]

    tablero_copia[origen[0]][origen[1]] = 0
    tablero_copia[destino[0]][destino[1]]  = ficha
    return tablero_copia

#ai mira el tablero
def analizar_tablero(tablero):
    score = 0
    for fila in tablero:
        for ficha in fila:
            if ficha == 1:  # ai ficha normal
                score += 1
            elif ficha == 3:  # ai ficha reina
                score += 2
            elif ficha == 2:  # jdr ficha normal
                score -= 1
            elif ficha == 4:  # jdr ficha reina
                score -= 2
    return score


def analizar_TodosMov(tablero,turno):
    movimientos = []

    for row in range(cons.ROWS):
        for col in range(cons.COL):
            ficha = tablero[row][col]
            if (turno == 1 and ficha in (1, 3)) or (turno == 2 and ficha in (2, 4)):

                mov_posible = calcular_posmov(row, col)
                for mov in mov_posible:
                    
                    tablero_copia = sobreponer_mov(tablero,(row,col),mov)
                    movimientos.append((tablero_copia,(row,col),mov))
    return movimientos


def minimax(tablero, depth, isMaximaxing):
    if depth == 0:
        return analizar_tablero(tablero), tablero

    turno_actual = 1 if isMaximaxing else 2
    movimientos = analizar_TodosMov(tablero, turno_actual)

    #movimientos = analizar_TodosMov(tablero, turno)
    
    if not movimientos:
        return analizar_tablero(tablero), tablero

    mejor_mov = None

    if isMaximaxing:
        maxEval = float('-inf')
        for mov in movimientos:
            evaluacion, _ = minimax(mov[0], depth - 1, False)
            if evaluacion > maxEval:
                maxEval = evaluacion
                mejor_mov = mov
        return maxEval, mejor_mov
    else:
        minEval = float('inf')
        for mov in movimientos:
            evaluacion, _ = minimax(mov[0], depth - 1, True)
            if evaluacion < minEval:
                minEval = evaluacion
                mejor_mov = mov
        return minEval, mejor_mov


inicializar_tablero()


while run:
    print("Valor real de 'turno':", turno)
    print("Turno actual:", "IA (1)" if turno == 1 else "Jugador (2)")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            posicion = pygame.mouse.get_pos()

            # Boton de reinicio
            if boton.collidepoint(posicion):
                inicializar_tablero()
                turno = 2
                FICHA_SELECCIONADA = None
                POSIBLE_MOV = []
                continue

            # permitir  si es turno del jugador
            if turno == 2:
                row, col = obtener_fila_col(posicion)

                if row is not None and col is not None:
                    ficha = tablero_matriz[row][col]

                    if FICHA_SELECCIONADA:
                        if (row, col) in POSIBLE_MOV:
                            score_antes = analizar_tablero(tablero_matriz)
                            mover_fichas(FICHA_SELECCIONADA, (row, col))
                            score_despues = analizar_tablero(tablero_matriz)
                            coronar_fichas()
                            FICHA_SELECCIONADA = None
                            POSIBLE_MOV = []

                            # Verificar ganador después del movimiento del jugador
                            winner = verificar_ganador(turno)
                            if winner != 0:
                                ganador(winner)
                                inicializar_tablero()
                                turno = 2
                                FICHA_SELECCIONADA = None
                                POSIBLE_MOV = []
                                boton = tablero()
                                pygame.display.update()
                                continue

                            if abs(score_despues - score_antes) < 1:
                                turno = 1
                                boton = tablero()
                                pygame.display.update()
                            else:
                                nuevos_movimientos = calcular_posmov(row, col, solo_capturas=True)
                                if nuevos_movimientos:
                                    FICHA_SELECCIONADA = (row, col)
                                    POSIBLE_MOV = nuevos_movimientos
                                    obligado = True
                                else:
                                    turno = 1
                                    obligado = False
                                    boton = tablero()
                                    pygame.display.update()
                        else:
                            if ficha != 0 and fichas_turno(ficha, turno):
                                if not obligado or (obligado and (row, col) == FICHA_SELECCIONADA):
                                    FICHA_SELECCIONADA = (row, col)
                                    POSIBLE_MOV = calcular_posmov(row, col)

                    else:
                        if ficha != 0 and fichas_turno(ficha, turno):
                            FICHA_SELECCIONADA = (row, col)
                            POSIBLE_MOV = calcular_posmov(row, col)

    # turno ia
    if turno == 1:
        boton = tablero()  
        pygame.display.update()
        pygame.time.delay(700)  

        print("IA pensando...")
        _, mejor_movimiento = minimax(tablero_matriz, 3, True)

        if mejor_movimiento:
            _, origen, destino = mejor_movimiento
            ficha = tablero_matriz[origen[0]][origen[1]]

            if fichas_turno(ficha, 1):
                mover_fichas(origen, destino)
                coronar_fichas()

                # Verificar ganador 
                winner = verificar_ganador(turno)
                if winner != 0:
                    ganador(winner)
                    inicializar_tablero()
                    turno = 2
                    FICHA_SELECCIONADA = None
                    POSIBLE_MOV = []
                    boton = tablero()
                    pygame.display.update()
                    continue

                turno = 2
                boton = tablero()
                pygame.display.update()
            else:
                print("⚠️ Movimiento inválido de IA (ficha no es amarilla)")
        else:
            print("⚠️ La IA no encontró ningún movimiento posible")

    boton = tablero()
    pygame.display.update()

'''
falta mostrar si ganaste

while run:
    print("Valor real de 'turno':", turno)
    print("Turno actual:", "IA (1)" if turno == 1 else "Jugador (2)")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            posicion = pygame.mouse.get_pos()

            # Permitir reinicio en cualquier turno
            if boton.collidepoint(posicion):
                inicializar_tablero()
                turno = 2
                FICHA_SELECCIONADA = None
                POSIBLE_MOV = []
                continue

            # SOLO PERMITIR JUGADA DEL JUGADOR EN SU TURNO
            if turno == 2:
                row, col = obtener_fila_col(posicion)

                if row is not None and col is not None:
                    ficha = tablero_matriz[row][col]

                    if FICHA_SELECCIONADA:
                        if (row, col) in POSIBLE_MOV:
                            score_antes = analizar_tablero(tablero_matriz)
                            mover_fichas(FICHA_SELECCIONADA, (row, col))
                            score_despues = analizar_tablero(tablero_matriz)
                            coronar_fichas()
                            FICHA_SELECCIONADA = None
                            POSIBLE_MOV = []

                            winner = verificar_ganador(turno)
                            if winner != 0:
                                ganador(winner)
                                inicializar_tablero()
                                turno = 2
                                continue

                            if abs(score_despues - score_antes) < 1:
                                turno = 1  # Cambia a IA
                                boton = tablero()
                                pygame.display.update()
                            else:
                                nuevos_movimientos = calcular_posmov(row, col, solo_capturas=True)
                                if nuevos_movimientos:
                                    FICHA_SELECCIONADA = (row, col)
                                    POSIBLE_MOV = nuevos_movimientos
                                    obligado = True
                                else:
                                    turno = 1  # Cambia a IA
                                    obligado = False
                                    boton = tablero()
                                    pygame.display.update()

                        else:
                            if ficha != 0 and fichas_turno(ficha, turno):
                                if not obligado or (obligado and (row, col) == FICHA_SELECCIONADA):
                                    FICHA_SELECCIONADA = (row, col)
                                    POSIBLE_MOV = calcular_posmov(row, col)

                    else:
                        if ficha != 0 and fichas_turno(ficha, turno):
                            FICHA_SELECCIONADA = (row, col)
                            POSIBLE_MOV = calcular_posmov(row, col)

    if turno == 1:
        pygame.time.delay(500)  # espera 500 milisegundos = 0.5 segundos

        print("IA pensando...")
        _, mejor_movimiento = minimax(tablero_matriz, 3, True)

        if mejor_movimiento:
            _, origen, destino = mejor_movimiento
            ficha = tablero_matriz[origen[0]][origen[1]]

            print("IA va a mover de:", origen, "con ficha:", ficha)

            if fichas_turno(ficha, 1):
                mover_fichas(origen, destino)
                coronar_fichas()

                winner = verificar_ganador(turno)
                if winner != 0:
                    ganador(winner)
                    inicializar_tablero()
                    turno = 2
                    FICHA_SELECCIONADA = None
                    POSIBLE_MOV = []
                    continue

                turno = 2  # ← Cambiar a turno del jugador
            else:
                print("⚠️ Movimiento inválido de IA (ficha no es amarilla)")
    else:
        print("⚠️ La IA no encontró ningún movimiento posible")

    boton = tablero()
    pygame.display.update()
'''
'''
este jala el ia pero no tablero

while run:
    print("Turno actual:", "IA (1)" if turno == 1 else "Jugador (2)")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

        if turno == 2 and event.type == pygame.MOUSEBUTTONDOWN:
            posicion = pygame.mouse.get_pos()
            row, col = obtener_fila_col(posicion)

            if boton.collidepoint(posicion):
                inicializar_tablero()
                turno = 2
                FICHA_SELECCIONADA = None
                POSIBLE_MOV = []
                continue

            if row is not None and col is not None:
                ficha = tablero_matriz[row][col]

                if FICHA_SELECCIONADA:
                    if (row, col) in POSIBLE_MOV:
                        score_antes = analizar_tablero(tablero_matriz)
                        mover_fichas(FICHA_SELECCIONADA, (row, col))
                        score_despues = analizar_tablero(tablero_matriz)
                        coronar_fichas()
                        FICHA_SELECCIONADA = None
                        POSIBLE_MOV = []

                        winner = verificar_ganador(turno)
                        if winner != 0:
                            ganador(winner)
                            inicializar_tablero()
                            turno = 2
                            continue

                        if abs(score_despues - score_antes) < 1:
                            turno = 1
                        else:
                            nuevos_movimientos = calcular_posmov(row, col, solo_capturas=True)
                            if nuevos_movimientos:
                                FICHA_SELECCIONADA = (row, col)
                                POSIBLE_MOV = nuevos_movimientos
                                obligado = True
                            else:
                                turno = 1
                                obligado = False

                    else:
                        if ficha != 0 and fichas_turno(ficha, turno):
                            if not obligado or (obligado and (row, col) == FICHA_SELECCIONADA):
                                FICHA_SELECCIONADA = (row, col)
                                POSIBLE_MOV = calcular_posmov(row, col)

                else:
                    if ficha != 0 and fichas_turno(ficha, turno):
                        FICHA_SELECCIONADA = (row, col)
                        POSIBLE_MOV = calcular_posmov(row, col)

    # Turno de la IA
    if turno == 1:
        print("IA pensando...")
        _, mejor_movimiento = minimax(tablero_matriz, 3, True)

        if mejor_movimiento:
            _, origen, destino = mejor_movimiento

            if fichas_turno(tablero_matriz[origen[0]][origen[1]], 1):
                mover_fichas(origen, destino)
                coronar_fichas()

                winner = verificar_ganador(turno)
                if winner != 0:
                    ganador(winner)
                    inicializar_tablero()
                    turno = 2
                    FICHA_SELECCIONADA = None
                    POSIBLE_MOV = []
                    continue

                turno = 2
            else:
                print("⚠️ Movimiento inválido de IA (ficha no es amarilla)")
        else:
            print("⚠️ La IA no encontró ningún movimiento posible")

    boton = tablero()
    pygame.display.update()
'''
