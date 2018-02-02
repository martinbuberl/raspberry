# encoding=utf8
from __future__ import print_function
import time
import os
import sys
import pygame


global JOYSTICK

AXIS_R2 = 4 # Joystick axis to read for up / down position
AXIS_L2 = 6
AXIS_UP_DOWN_INVERTED = True # Set this to True if up and down appear to be swapped
AXIS_LEFT_RIGHT = 0 # Joystick axis to read for left / right position
AXIS_LEFT_RIGHT_INVERTED = True # Set this to True if left and right appear to be swapped
BUTTON_FAST_TURN = 9 # Joystick button number for turning fast (R2)
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
        print("Press CTRL+C to quit")
        drive_left = 0.0
        drive_right = 0.0
        up_down = 0.0
        left_right = 0.0

        while True:
            # Get the latest events from the system
            had_event = False
            events = pygame.event.get()
            # Handle each event individually
            for event in events:
                #print("event:{}".format(event.type))

                # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP sJOYHATMOTION
                if event.type == pygame.JOYAXISMOTION:
                    #print("Joystick has been moved")
                    had_event = True
                elif event.type == pygame.JOYBUTTONDOWN:
                    #print("Joystick button pressed")
                    had_event = True

                if had_event:
                    # Read axis positions (-1 to +1)
                    if AXIS_UP_DOWN_INVERTED:
                        up_down = -JOYSTICK.get_axis(AXIS_R2)  # release --> 1     half 0     full press --> -1
                        throttle = up_down - 1
                        if throttle < -1.0:
                            throttle = -1.0

                        if throttle != -1.0:
                            print("throttle : {0} ".format(throttle))
                    else:
                        up_down = JOYSTICK.get_axis(AXIS_R2)
                    if AXIS_LEFT_RIGHT_INVERTED:
                        left_right = -JOYSTICK.get_axis(AXIS_LEFT_RIGHT)
                        #print("left_right : {}".format(left_right))
                    else:
                        left_right = JOYSTICK.get_axis(AXIS_LEFT_RIGHT)
                    # Apply steering speeds
                    if not JOYSTICK.get_button(BUTTON_FAST_TURN):
                        left_right *= 1

                    # Determine the drive power levels
                    if JOYSTICK.get_button(AXIS_L2): # to REVERSE the car
                        drive_left = throttle
                        drive_right = throttle
                    else:                                   # to move FORWARD
                        drive_left = -throttle
                        drive_right = -throttle

                    if left_right < -0.05:
                        # Turning right
                        #IN1.on()
                        #IN2.off()
                        #IN3.off()
                        #IN4.on()

                        drive_left = drive_left * (1.0 - (1.0 * left_right))
                        drive_right = drive_right - drive_left * TURN_MULTIPLIER
                    elif left_right > 0.05:
                        # Turning left

                        #IN1.off()
                        #IN2.on()
                        #IN3.on()
                        #IN4.off()

                        drive_right = drive_right * (1.0 + (1.0 * left_right))
                        drive_left = drive_left - drive_right * TURN_MULTIPLIER
                    print("driveL :{0:.2f} || driveR : {1:.2f} ".format(drive_left, drive_right))


                    # Set the motors to the new speeds
                    #ENA.value = driveLeft
                    #ENB.value = driveRight

            # Wait for the interval period
            time.sleep(INTERVAL) # default = 0

    except KeyboardInterrupt:
        sys.exit()

controller_init()
controller_events()
