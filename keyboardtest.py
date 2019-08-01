#!/usr/bin/env python
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800,480))
pygame.display.set_caption("keyboard test")
pygame.key.set_repeat(500,1000)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if pygame.key.get_pressed()[pygame.K_q]:
            print("q pressed!")
        elif pygame.key.get_pressed()[pygame.K_w]:
            print("w pressed!")
        elif pygame.key.get_pressed()[pygame.K_a]:
            print("a pressed!")
        elif pygame.key.get_pressed()[pygame.K_s]:
            print("s pressed!")
        elif pygame.key.get_pressed()[pygame.K_d]:
            print("d pressed!")

