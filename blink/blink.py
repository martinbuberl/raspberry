import time
import RPi.GPIO as GPIO # pylint: disable=import-error

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

ledPin = 4
GPIO.setup(ledPin, GPIO.OUT)

for i in range(5):
    GPIO.output(ledPin, GPIO.HIGH) # LED on
    time.sleep(0.5)
    GPIO.output(ledPin, GPIO.LOW) # LED off
    time.sleep(0.5)
