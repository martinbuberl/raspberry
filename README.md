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

## Pairing with PS4 Controller

```
sudo pip ds4drv
sudo apt-get install python-pygame
```


- Tp put the controller into pairing mode, press and hold the **Share** button then the **PS** button
- After a few seconds, the light bar will strobe, indicating that the controller is now in pairing mode
- To turn the controller off, hold the **PS** button for 10 seconds
- Tap the **PS** button to wake up the controller, it will automatically re-connect

Read more about it [here](https://github.com/retropie/retropie-setup/wiki/PS4-Controller#general-controller-usage)















- Remote control RC car via Internet or PS4 controller





Check the installed Python versions on your Raspberry Pi:

`python --version` = 2.7.13
`python3 --version` = 3.5.3

Install the matching Python 3 version on your local machine via [pyenv](https://github.com/pyenv/pyenv) on macOS:

```
pyenv install -v 3.5.3
pyenv rehash
```

Note: I had to run `xcode-select --install` because of a `ZipImportError` error before I was able to install 3.5.3 ([see](https://github.com/pyenv/pyenv/issues/454)).

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

