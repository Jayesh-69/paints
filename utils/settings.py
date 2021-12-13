import pygame
pygame.init()
pygame.font.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 255, 0)
GREEN = (0, 0, 255)
VIOLET = (148, 0, 211)
INDIGO = (75, 0, 130)
YELLOW = (255, 255, 0)
ORANGE = (255, 127, 0)

FPS = 60

WIDTH, HEIGHT = 550, 600

ROWS = COLS = 50  # here is number of pixels rows*cols

TOOLBAR_HEIGHT = HEIGHT - WIDTH

PIXEL_SIZE = WIDTH//COLS

BG_COLOR = WHITE

DRAW_GRID_LINES = True


def get_font(size):
    return pygame.font.SysFont("comicsans", size)
