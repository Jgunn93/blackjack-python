from click import echo
import pygame
import os
from banking_pkg import *
from win_config import *


authorized_user = ""

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    draw_window()

"""     if authorized_user == "":
        print("You must be logged in to play.")
    else:
        print("Logged in as: ", authorized_user)

    menu_input = input()"""