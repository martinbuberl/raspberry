import io
import picamera
from time import sleep

###########################################
# CONFIGURATION
WIDTH = 640
HEIGHT = 480
FRAMERATE = 24
###########################################

# https://github.com/waveform80/picamera
# https://picamera.readthedocs.io/en/release-1.10/recipes1.html


def main(resolution=(320, 180)):
    print('Initializing camera')
    stream = io.BytesIO()
    with picamera.PiCamera() as camera:
        camera.resolution = (WIDTH, HEIGHT)
        camera.framerate = FRAMERATE
        camera.resolution = resolution
        camera.start_recording(stream, format='h264', quality=23)
        camera.wait_recording(15)
        camera.stop_recording()


if __name__ == '__main__':
    main()
