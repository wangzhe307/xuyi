background_img='ground.jpg'
mouse_img='2.png'
import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode((650,433),0,32)

pygame.display.set_caption("hello,world!")

background = pygame.image.load(background_img).convert()
mouse_curser = pygame.image.load(mouse_img).convert_alpha()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    screen.blit(background,(0,0))

    x,y=pygame.mouse.get_pos()
    x-=mouse_curser.get_width()/2
    y-=mouse_curser.get_height()/2

    screen.blit(mouse_curser,(x,y))
    pygame.display.update()

