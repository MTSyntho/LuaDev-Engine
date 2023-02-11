import pygame
import time

pygame.init()
pygame.font.init()

purple = (30,0,30)
white = (255,255,255)
once = 1

# CREATING CANVAS AND PREPARE FADE
canvas = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
# alphaSurf = pygame.Surface((1280,720))
# alphaSurf.fill(purple)
# alphaSurf.set_alpha(0)
# alph = 0

# LOADING
logo = pygame.image.load("assets/logo.png")
pygame.display.set_icon(logo)
title = pygame.image.load("assets/title.png")
splash = pygame.image.load("assets/splash.png")
lemonmilk = pygame.font.SysFont("assets/fonts/LEMONMILK-Regular.ttf", 60)

# TITLE OF CANVAS
pygame.display.set_caption("LuaDev Engine")
exit = False

# PREVENTS EXITING WHEN OPENED
while not exit:
    if once == 1:
        # SPLASH STUFF
        once = 0
        canvas.fill(purple)
        # alph += 0.1
        # alphaSurf.set_alpha(alph)
        # canvas.blit(alphaSurf,(0,0))
        canvas.blit(pygame.transform.scale(splash, (1280, 720)), (0, 0))
        pygame.display.update()
        time.sleep(3)
        canvas.fill(purple)
        import lmenu
        # creatorsplash = lemonmilk.render("BY ITSICECREEPERPE DEV", 1, (255,255,255))
        # canvas.blit(creatorsplash, (350,630))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
    pygame.display.update()