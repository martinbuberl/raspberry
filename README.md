# raspberry

### Hardware

- Raspberry Pi 3 Model B
- SanDisk Extreme Pro Micro SD 32GB

## Setup Bluetooth pairing with Playstation 4 Controller

Install [ds4drv](https://github.com/chrippa/ds4drv) - a driver for the PS4's DualShock 4 Wireless Controller.

```
sudo pip ds4drv
sudo apt-get install python-pygame
```

Start the driver

```
sudo ds4drv
```

- To put the controller into pairing mode, press and hold the **Share** button then the **PS** button
- After a few seconds, the light bar will strobe, indicating that the controller is now in pairing mode

You'll see output like this:

```
[info][controller 1] Created devices /dev/input/js0 (joystick) /dev/input/event0 (evdev)
[info][bluetooth] Scanning for devices
[info][bluetooth] Found device 70:20:84:71:FD:DC
[info][controller 1] Connected to Bluetooth Controller (70:20:84:71:FD:DC)
[info][bluetooth] Scanning for devices
[info][controller 1] Battery: Fully charged
[warning][controller 1] Signal strength is low (10 reports/s)
```

You're paired :)

- To turn the controller off, hold the **PS** button for 10 seconds
- Tap the **PS** button to wake up the controller, it will automatically re-connect

Read more about it [here](https://github.com/retropie/retropie-setup/wiki/PS4-Controller#general-controller-usage)

## Start it automatically

Open your `rc.local` file `sudo nano /etc/rc.local` and add the following above the `exit 0` line, so it looks like this:

```
sudo /usr/local/bin/ds4drv &
exit 0
```
https://www.dexterindustries.com/howto/run-a-program-on-your-raspberry-pi-at-startup/
https://www.raspberrypi.org/documentation/linux/usage/rc-local.md
https://github.com/macunixs/dualshock4-pi



## Build Tensorflow

```
pip install numpy
pip install tensorflow
pip install pandas
```





https://github.com/tensorflow/tensorflow/tree/master/tensorflow/contrib/makefile

## Some terminal wisdom

Leave Python shell: `control` + `d`
Leave VIM shell: `esc` and `:wq`

Setup TensorFlow
----------------

https://github.com/samjabrahams/tensorflow-on-raspberry-pi/blob/master/GUIDE.md

sudo apt-get update


Some Pi wisdom
--------------

sudo raspi-config
sudo poweroff
sudo reboot

