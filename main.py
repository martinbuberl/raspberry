# encoding=utf8
from __future__ import print_function
import pygame

pygame.init()
pygame.joystick.init()

while not True:
    for event in pygame.event.get():  # User did something
        print(event.type)
