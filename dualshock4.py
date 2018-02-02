# encoding=utf8
import time
import os
import sys
import pygame


global joystick

axisR2 = 4 # Joystick axis to read for up / down position
axisL2 = 6
axisUpDownInverted = True               # Set this to True if up and down appear to be swapped
axisLeftRight = 0                       # Joystick axis to read for left / right position
axisLeftRightInverted = True            # Set this to True if left and right appear to be swapped
buttonFastTurn = 9                      # Joystick button number for turning fast (R2)
interval = 0.00 # Time between updates in seconds, smaller responds faster but uses more processor time
TURN_MULTIPLIER = 0.4


def Dualshock4Init():
    global joystick
    # Setup pygame and wait for the joystick to become available
    os.environ["SDL_VIDEODRIVER"] = "dummy" # Removes the need to have a GUI window
    pygame.init()

    print("Waiting for joystick... (press CTRL+C to quit)")

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
                    joystick = pygame.joystick.Joystick(0)
                    break
            except pygame.error:
                # Failed to connect to the joystick, toggle the LED
                pygame.joystick.quit()
                time.sleep(0.1)
        except KeyboardInterrupt:
            # CTRL+C exit, give up
            print("\nUser aborted")
            sys.exit()
    print("Joystick found: {}".format(joystick.get_name()))
    joystick.init()

    axes = joystick.get_numaxes() # Usually axis run in pairs, up/down for one, and left/right for the other
    print("Number of axes: {}".format(axes))
    for i in range( axes ):
        axis = joystick.get_axis( i )
        print("Axis {} value: {:>6.3f}".format(i, axis))
    buttons = joystick.get_numbuttons()
    print("Number of buttons: {}".format(buttons))
    for i in range( buttons ):
        button = joystick.get_button( i )
        print("Button {:>2} value: {}".format(i,button))
    hats = joystick.get_numhats() # Hat switch. All or nothing for direction, not like joysticks. Value comes back in an array.
    print("Number of hats: {}".format(hats))
    for i in range( hats ):
        hat = joystick.get_hat( i )
        print("Hat {} value: {}".format(i, str(hat)))


def RobotControl():
    global joystick

    try:
        print("Press CTRL+C to quit")
        driveLeft = 0.0
        driveRight = 0.0
        #running = True
        #hadEvent = False
        upDown = 0.0
        leftRight = 0.0
        # Loop indefinitely
        while True:
            # Get the latest events from the system
            had_event = False
            events = pygame.event.get()
            # Handle each event individually
            for event in events:
                print("event:{}".format(event.type))

                # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP sJOYHATMOTION
                if event.type == pygame.JOYAXISMOTION:
                    print("Joystick has been moved")
                    had_event = True
                elif event.type == pygame.JOYBUTTONDOWN:
                    print("Joystick button pressed")
                    had_event = True

                if had_event:
                    # Read axis positions (-1 to +1)
                    if axisUpDownInverted:
                        upDown = -joystick.get_axis(axisR2)  # release --> 1     half 0     full press --> -1
                        throttle = upDown - 1
                        if throttle < -1.0:
                            throttle = -1.0
                        print("throttle : {0} ".format(throttle))
                    else:
                        upDown = joystick.get_axis(axisR2)
                    if axisLeftRightInverted:
                        leftRight = -joystick.get_axis(axisLeftRight)
                        print("leftRight : {}".format(leftRight))
                    else:
                        leftRight = joystick.get_axis(axisLeftRight)
                    # Apply steering speeds
                    if not joystick.get_button(buttonFastTurn):
                        leftRight *= 1

                    # Determine the drive power levels
                    if joystick.get_button(axisL2): # to REVERSE the car
                        driveLeft = throttle
                        driveRight = throttle
                    else:                                   # to move FORWARD
                        driveLeft = -throttle
                        driveRight = -throttle

                    if leftRight < -0.05:
                        # Turning right
                        #IN1.on()
                        #IN2.off()
                        #IN3.off()
                        #IN4.on()

                        driveLeft = driveLeft*( 1.0 - (1.0 * leftRight))
                        driveRight = driveRight - driveLeft*TURN_MULTIPLIER
                    elif leftRight > 0.05:
                        # Turning left

                        #IN1.off()
                        #IN2.on()
                        #IN3.on()
                        #IN4.off()

                        driveRight= driveRight*( 1.0 + (1.0 * leftRight))
                        driveLeft= driveLeft - driveRight*TURN_MULTIPLIER
                    print("driveL :{0:.2f} || driveR : {1:.2f} ".format(driveLeft,driveRight))


                    # Set the motors to the new speeds
                    #ENA.value = driveLeft
                    #ENB.value = driveRight

            # Wait for the interval period
            time.sleep(interval) # default = 0

    except KeyboardInterrupt:
        # CTRL+C exit, disable all drives
        print("shutting down...")

Dualshock4Init()
#RobotControl()
