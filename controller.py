# encoding=utf8
from __future__ import print_function
import time
import os
import sys
import pygame


global JOYSTICK

ANALOG_LX_AXIS = 0 # Left analog stick x-axis to read the left (-1) / right (+1) position
ANALOG_LY_AXIS = 1 # Left analog stick y-axis to read the up (-1) / down (+1) position
ANALOG_RX_AXIS = 2
ANALOG_RY_AXIS = 5
BUTTON_SQUARE = 0
BUTTON_CROSS = 1
BUTTON_CIRCLE = 2
BUTTON_TRIANGLE = 3
BUTTON_L1 = 4
BUTTON_L2 = 6
BUTTON_R1 = 5
BUTTON_R2 = 7

INTERVAL = 0.00 # Time between updates in seconds, smaller responds faster but uses more processor time
TURN_MULTIPLIER = 0.4


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

    try:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.JOYAXISMOTION:
                    x_axis = JOYSTICK.get_axis(ANALOG_LX_AXIS)
                    y_axis = JOYSTICK.get_axis(ANALOG_LY_AXIS)
                    if x_axis != 0 or y_axis != 0:
                        print("Analog stick x={:>6.3f}, y={:>6.3f}".format(x_axis, y_axis))
                elif event.type == pygame.JOYBUTTONDOWN:
                    if JOYSTICK.get_button(BUTTON_SQUARE):
                        print("Square pressed")
                    if JOYSTICK.get_button(BUTTON_CROSS):
                        print("Cross pressed")
                    if JOYSTICK.get_button(BUTTON_CIRCLE):
                        print("Circle pressed")
                    if JOYSTICK.get_button(BUTTON_TRIANGLE):
                        print("Triangle pressed")
                    if JOYSTICK.get_button(BUTTON_L1):
                        print("L1 pressed")
                    if JOYSTICK.get_button(BUTTON_L2):
                        print("L2 pressed")
                    if JOYSTICK.get_button(BUTTON_R1):
                        print("R1 pressed")
                    if JOYSTICK.get_button(BUTTON_R2):
                        print("R2 pressed")
                elif event.type == pygame.JOYBUTTONUP:
                    if JOYSTICK.get_button(BUTTON_R1):
                        print("R1 released")
                    if JOYSTICK.get_button(BUTTON_R2):
                        print("R2 released")

#                if had_event == False:
#                    # Read axis positions (-1 to +1)
#                    if AXIS_UP_DOWN_INVERTED:
#                        up_down = -JOYSTICK.get_axis(AXIS_R2)  # release --> 1     half 0     full press --> -1
#                        throttle = up_down - 1
#                        if throttle < -1.0:
#                            throttle = -1.0
#
#                        if throttle != -1.0:
#                            print("throttle : {0} ".format(throttle))
#                    else:
#                        up_down = JOYSTICK.get_axis(AXIS_R2)
#                    if AXIS_LEFT_RIGHT_INVERTED:
#                        left_right = -JOYSTICK.get_axis(AXIS_LEFT_RIGHT)
#                        #print("left_right : {}".format(left_right))
#                    else:
#                        left_right = JOYSTICK.get_axis(AXIS_LEFT_RIGHT)
#                    # Apply steering speeds
#                    if not JOYSTICK.get_button(BUTTON_FAST_TURN):
#                        left_right *= 1
#
#                    # Determine the drive power levels
#                    if JOYSTICK.get_button(AXIS_L2): # to REVERSE the car
#                        drive_left = throttle
#                        drive_right = throttle
#                    else:                                   # to move FORWARD
#                        drive_left = -throttle
#                        drive_right = -throttle
#
#                    if left_right < -0.05:
#                        # Turning right
#                        drive_left = drive_left * (1.0 - (1.0 * left_right))
#                        drive_right = drive_right - drive_left * TURN_MULTIPLIER
#                    elif left_right > 0.05:
#                        # Turning left
#                        drive_right = drive_right * (1.0 + (1.0 * left_right))
#                        drive_left = drive_left - drive_right * TURN_MULTIPLIER
#
#                    if drive_left != 1.00 or drive_right != 1.00:
#                        print("driveL :{0:.2f} || driveR : {1:.2f} ".format(drive_left, drive_right))
#
#
#                    # Set the motors to the new speeds
#                    #ENA.value = driveLeft
#                    #ENB.value = driveRight

            # Wait for the interval period
            time.sleep(INTERVAL) # default = 0

    except KeyboardInterrupt:
        sys.exit()

controller_init()
controller_events()
