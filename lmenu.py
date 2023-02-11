import pygame
import time

once = 1

# LOADING AND STUFF
bg = pygame.image.load("assets/bg.png")
pygame.display.set_caption("LuaDev Engine - Main Menu")

while not exit:
    if once == 1:
    	canvas.blit(pygame.transform.scale(bg, (1280, 720)), (0, 0))
    	pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
    pygame.display.update()