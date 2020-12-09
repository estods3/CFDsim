import pygame
from pygame.locals import *
import sys, os
import time
import random
from Sample import Vector

##--------------------------------------------------------------------------------------------
## Environment: initializes 'pygame' environment and start, end, and obstacle positions
## controls all redrawing of the pygame interface
##--------------------------------------------------------------------------------------------
BLACK = pygame.Color( 0 ,  0 ,  0 )
WHITE = pygame.Color(255, 255, 255)

class Environment:
    def __init__(self, screenWidth, screenHeight):
        self.mouse = pygame.mouse
        pygame.init()
        self.screenSizeX, self.screenSizeY = screenWidth, screenHeight
        self.screen = pygame.display.set_mode((self.screenSizeX, self.screenSizeY))
        self.screen.fill(WHITE)
        self.fpsClock = pygame.time.Clock()
        self.contour = []

        #self.screen.blit(canvas, (0, 0))

    # Add a contour to run CFD on
    def addContour(self):
        # Check mouse click status
        left_pressed, middle_pressed, right_pressed = self.mouse.get_pressed()

        # Clear current contour and environment
        if left_pressed:
            self.contour = []
            self.clearEnv()

        # Continue to Redraw new Contour
        while left_pressed:
            pygame.draw.circle(self.screen, BLACK, (pygame.mouse.get_pos()),5)
            print(pygame.mouse.get_pos())
            self.contour.append([pygame.mouse.get_pos()])
            pygame.display.update()
            left_pressed, middle_pressed, right_pressed = self.mouse.get_pressed()
            pygame.event.pump() # process event queue

    # clear the environment
    def clearEnv(self):
        self.screen.fill(WHITE)
        pygame.display.update()

    # Check to see if the program was exited
    def checkExited(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
