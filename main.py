# encoding=utf8
from __future__ import print_function
import pygame
import os
os.environ["SDL_VIDEODRIVER"] = "dummy"

pygame.init()
pygame.joystick.init()

while True:
    for event in pygame.event.get():  # User did something
        print(event.type)
