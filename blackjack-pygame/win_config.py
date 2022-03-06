import pygame
import os
pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE | pygame.HWSURFACE | pygame.DOUBLEBUF)
pygame.display.set_caption("First doge")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

BORDER = pygame.Surface.get_size(WIN)

FPS = 60
VEL = 3

BACKGROUND = pygame.image.load(os.path.join('graphics', 'table_background.jpg'))

def draw_window():
    WIN.blit(BACKGROUND, (0,0))

    pygame.display.update()