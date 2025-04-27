'''
import pygame
import sys

# Inicialización
pygame.init()
WIDTH, HEIGHT = 600, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Damas Chinas")

# Colores
BEIGE = (245, 245, 220)
BLACK = (0, 0, 0)
BABY_YELLOW = (255, 255, 153)
BROWN = (101, 67, 33)
RED = (255, 0, 0)
DARKER_BEIGE = (222, 184, 135)

# Tablero
ROWS, COLS = 8, 8
SQUARE_SIZE = 40
BOARD_TOPLEFT = (50, 50)

# Fuente
font = pygame.font.SysFont('arial', 20)

def draw_board():
    screen.fill(BROWN)

    # Título
    title = font.render("DAMAS CHINAS", True, RED)
    screen.blit(title, (60, 10))

    # Tablero
    for row in range(ROWS):
        for col in range(COLS):
            color = BEIGE if (row + col) % 2 == 0 else DARKER_BEIGE
            rect = pygame.Rect(BOARD_TOPLEFT[0] + col*SQUARE_SIZE, BOARD_TOPLEFT[1] + row*SQUARE_SIZE,
                               SQUARE_SIZE, SQUARE_SIZE)
            pygame.draw.rect(screen, color, rect)

    # Fichas
    for row in range(3):  # Fichas negras
        for col in range(COLS):
            if (row + col) % 2 != 0:
                x = BOARD_TOPLEFT[0] + col*SQUARE_SIZE + SQUARE_SIZE//2
                y = BOARD_TOPLEFT[1] + row*SQUARE_SIZE + SQUARE_SIZE//2
                pygame.draw.circle(screen, BLACK, (x, y), 15)

    for row in range(5, 8):  # Fichas amarillas bebé
        for col in range(COLS):
            if (row + col) % 2 != 0:
                x = BOARD_TOPLEFT[0] + col*SQUARE_SIZE + SQUARE_SIZE//2
                y = BOARD_TOPLEFT[1] + row*SQUARE_SIZE + SQUARE_SIZE//2
                pygame.draw.circle(screen, BABY_YELLOW, (x, y), 15)

    # Panel de turno
    panel = pygame.Rect(400, 100, 160, 150)
    pygame.draw.rect(screen, BEIGE, panel)
    turno_text = font.render("TURNO", True, RED)
    ai_text = font.render("AI:", True, RED)
    player_text = font.render("PLAYER:", True, RED)
    screen.blit(turno_text, (420, 110))
    screen.blit(ai_text, (420, 150))
    screen.blit(player_text, (420, 190))

# Loop principal
running = True
while running:
    draw_board()
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()
'''
import pygame
import sys

# Inicialización
pygame.init()
WIDTH, HEIGHT = 600, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Damas Chinas")

# Colores
BEIGE = (245, 245, 220)
BLACK = (0, 0, 0)
BABY_YELLOW = (255, 255, 153)
BROWN = (101, 67, 33)
RED = (255, 0, 0)
DARKER_BEIGE = (222, 184, 135)

# Tablero
ROWS, COLS = 8, 8
SQUARE_SIZE = 40
BOARD_TOPLEFT = (50, 50)

# Fuente
font = pygame.font.SysFont('arial', 20, bold= True)

def draw_board():
    screen.fill(BROWN)

    # Título
    title = font.render("DAMAS CHINAS", True, RED)
    screen.blit(title, (60, 10))

    # Tablero
    for row in range(ROWS):
        for col in range(COLS):
            if (row + col) % 2 == 0:
                color = BEIGE
            else:
                color = DARKER_BEIGE

            rect = pygame.Rect(
                BOARD_TOPLEFT[0] + col * SQUARE_SIZE,
                BOARD_TOPLEFT[1] + row * SQUARE_SIZE,
                SQUARE_SIZE, SQUARE_SIZE
            )
            pygame.draw.rect(screen, color, rect)

    # Fichas negras
    for row in range(3):
        for col in range(COLS):
            if (row + col) % 2 == 0:
                continue
            else:
                x = BOARD_TOPLEFT[0] + col * SQUARE_SIZE + SQUARE_SIZE // 2
                y = BOARD_TOPLEFT[1] + row * SQUARE_SIZE + SQUARE_SIZE // 2
                pygame.draw.circle(screen, BLACK, (x, y), 15)

    # Fichas amarillas bebé
    for row in range(5, 8):
        for col in range(COLS):
            if (row + col) % 2 == 0:
                continue
            else:
                x = BOARD_TOPLEFT[0] + col * SQUARE_SIZE + SQUARE_SIZE // 2
                y = BOARD_TOPLEFT[1] + row * SQUARE_SIZE + SQUARE_SIZE // 2
                pygame.draw.circle(screen, BABY_YELLOW, (x, y), 15)

    # Panel de turno
    panel = pygame.Rect(400, 100, 160, 150)
    pygame.draw.rect(screen, BEIGE, panel)

    turno_text = font.render("TURNO", True, RED)
    ai_text = font.render("AI:", True, RED)
    player_text = font.render("PLAYER:", True, RED)

    screen.blit(turno_text, (420, 110))
    screen.blit(ai_text, (420, 150))
    screen.blit(player_text, (420, 190))



# Loop principal
running = True
while running:
    draw_board()
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()
