# encoding=utf8
from __future__ import print_function
import time
import os
import sys
import pygame


global JOYSTICK

AXIS_LSTICK_X = 0 # Left analog stick x-axis => left (-1) to right (+1)
AXIS_LSTICK_Y = 1 # Left analog stick y-axis => up (-1) to down (+1)
AXIS_RSTICK_X = 2 # Right analog stick x-axis => left (-1) to right (+1)
AXIS_RSTICK_Y = 5 # Right analog stick y-axis => up (-1) to down (+1)
AXIS_R2 = 4 # R2 button axis => release (-1) to half (0) to full (+1)
AXIS_L2 = 6 # L2 button axis => release (-1) to half (0) to full (+1)
BUTTON_SQUARE = 0
BUTTON_CROSS = 1
BUTTON_CIRCLE = 2
BUTTON_TRIANGLE = 3
BUTTON_L1 = 4
BUTTON_L2 = 6
BUTTON_R1 = 5
BUTTON_R2 = 7


def controller_init():
    global JOYSTICK

    print("Waiting for controller... (press CTRL+C to quit)")
    os.environ["SDL_VIDEODRIVER"] = "dummy" # Removes the need to have a GUI window
    pygame.init()

    while True:
        try:
            try:
                pygame.joystick.init()
                # Attempt to setup the joystick
                if pygame.joystick.get_count() < 1:
                    # No joystick attached, toggle the LED
                    pygame.joystick.quit()
                    time.sleep(0.1)
                else:
                    # We have a joystick, attempt to initialise it!
                    JOYSTICK = pygame.joystick.Joystick(0)
                    break
            except pygame.error:
                # Failed to connect to the joystick, toggle the LED
                pygame.joystick.quit()
                time.sleep(0.1)
        except KeyboardInterrupt:
            sys.exit()
    print("Controller found: {}".format(JOYSTICK.get_name()))
    JOYSTICK.init()


def controller_events():
    global JOYSTICK

    while True:
        for e in pygame.event.get():
            if e.type == pygame.JOYAXISMOTION:
                axis_lstick_x = JOYSTICK.get_axis(AXIS_LSTICK_X)
                if axis_lstick_x != 0:
                    print("Left stick x-axis={:>6.3f}".format(axis_lstick_x))

                axis_r2 = JOYSTICK.get_axis(AXIS_R2)
                if axis_r2 > -1:
                    print("R2 axis={:>6.3f}".format(axis_r2))

            elif e.type == pygame.JOYBUTTONDOWN and e.button == BUTTON_R2:
                print("R2 pressed")
            elif e.type == pygame.JOYBUTTONUP and e.button == BUTTON_R2:
                print("R2 released")


controller_init()
controller_events()
