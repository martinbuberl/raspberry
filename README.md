# raspberry

### Hardware

- Raspberry Pi 3 Model B
- SanDisk Extreme Pro Micro SD 32GB

## Setup headless Raspberry Pi

- [Download](https://www.raspberrypi.org/downloads/raspbian/) Raspian Stretch with Desktop *(Version: November 2017)*
- Flash SD card with [Etcher](https://etcher.io/)
- [Enable SSH](https://www.raspberrypi.org/documentation/remote-access/ssh/) by adding an empty file `ssh` onto the SD card's **boot** partition `touch /Volumes/boot/ssh`
- [Configure WiFi](https://raspberrypi.stackexchange.com/a/37921) by adding a file `wpa_supplicant.conf` onto the SD card's **boot** partition `touch /Volumes/boot/wpa_supplicant.conf`:
```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
    ssid="YOUR_WIFI_SSID"
    psk="YOUR_WIFI_PASSWORD"
}
```
- [Get local network IP address](https://raspberrypi.stackexchange.com/q/13936/80323) of Raspberry Pi `ping raspberrypi`
- Connect via SSH `ssh pi@<YOUR_PI_IP_ADDRESS>` (default password for the `pi` user is `raspberry`)
- Run `sudo raspi-config` open **Interfacing Options** and enable **VNC**
- Connect via [VNC](https://www.realvnc.com/en/connect/download/viewer/)
```
- [Upate and upgrade Raspian](https://www.raspberrypi.org/documentation/raspbian/updating.md):
```
sudo apt-get update
sudo apt-get dist-upgrade
sudo apt-get clean
```


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







## Build Tensorflow

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

