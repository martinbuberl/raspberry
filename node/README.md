




# NVM & Node

https://github.com/blobsmith/raspberryTestNode/wiki/Node.js-installation-with-nvm-on-Raspberry-pi

Update Raspian
`sudo apt-get update`
`sudo apt-get upgrade`

Install nvm
Download the last version of nvm from github and put it in the folder .nvm.
`git clone https://github.com/creationix/nvm.git ~/.nvm && cd ~/.nvm && git checkout v0.33.11`

sudo nano ~/.bashrc
You have to add the line `source ~/.nvm/nvm.sh` at the end of this file.

sudo nano ~/.profile
You have to add the line `source ~/.nvm/nvm.sh` at the end of this file.

sudo reboot
