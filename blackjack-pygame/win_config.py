import pygame
import os
pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 1920, 1080
WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE | pygame.HWSURFACE | pygame.DOUBLEBUF)
pygame.display.set_caption("First doge")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

BORDER = pygame.Surface.get_size(WIN)

FPS = 60
VEL = 3

BACKGROUND = pygame.image.load(os.path.join('graphics', 'table_1920_1080.jpg'))

def draw_window():
    WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE | pygame.HWSURFACE | pygame.DOUBLEBUF)
    WIN.blit(BACKGROUND, (0,0))
    pygame.display.flip()
    while True:
        pygame.event.pump()
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            pygame.display.quit()
        elif event.type == pygame.VIDEORESIZE:
            WIN = pygame.display.set_mode(
                event.dict['size'], pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
            WIN.blit(pygame.transform.scale(BACKGROUND, event.dict['size']), (0,0))
            pygame.display.flip()
    # pygame.display.update()