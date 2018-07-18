camp
====

Another Raspberry Pi camera webserver.

What it does
============

Hosts a website where you can view your webcam in real time.

Why I wrote it
==============

There are a *lot* of tutorials out there on how to turn your pi into a webcam
server. Most of them involve installing [motion](http://www.lavrsen.dk/foswiki/bin/view/Motion),
which works great in many use cases. However, I wanted something simpler. Namely,
I wanted:

 * Minimal configuration
 * One-way streaming
 * Easily customizable webpage
 * Extensible server

camp does just this. Nothing else. This (hopefully) makes it the simplest
and fastest option out there.

Installation
============

Camp uses [tornado](http://www.tornadoweb.org/en/stable/) to create a
web server. It can interact with the [Pi camera](http://www.adafruit.com/products/1367)
with the aptly named [picamera](http://picamera.readthedocs.org/en/release-1.7/)
module. The command below installs the dependencies.

```
sudo apt-get install python-dev python-pip libjpeg-dev
sudo pip3 install tornado
```

Once the dependencies are installed on your pi, you can run the server.

```
python3 server.py
```

Navigate to http://your.r.pi.ip:8000 and check out your webcam.

####Run on startup

It's nice to have your pi start camp whenever it turns on. Let's make that
happen. Type `sudo nano /etc/rc.local` to open this file for editing, and add
the line `nohup python /home/pi/camp/server.py &` before the last line. Note
that you may need to change the path (`/home/pi/camp/server.py`) to point to
the right file.

####Customization

The website consists of `index.html` and `style.css`. These can be
edited to change the look of camp.

If you want to add in extra functionality, edit `client.js` and `server.py`.
The client should send a request to the server, which will then cause the
server to do something.

If you want to add in extra camera features, opencv comes with a lot of useful
computer vision algorithms. Check out its functionality before writing your
own.
