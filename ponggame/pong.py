#!/usr/bin/env python3

#import pygame sdl package and system access
import pygame, sys

#initialize pygame
pygame.init()

#Setup the main screen diemnsions 
screen = pygame.display.set_mode((600, 600))
#Title caption
pygame.display.set_caption("Let's Play Pong!")

# game loop logic
while True:
    for event in pygame.event.get(): #checks user actions
        if event.type == pygame.QUIT:
            pygame.quit() #closes game
            sys.exit() #exits program
