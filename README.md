# alien_invasion
Simple Alien Invasion Game in Python

Instructions
The player controls a ship that appears at the bottom center of the screen.
The player can move the ship right and left using the arrow keys and shoot bullets using the spacebar.

When the game begins

A fleet of aliens fills the top of the screen and moves accross and down the screen

The player must shoot and destroy the aliiens

If a player shoots down all the aliens a new fleet will appear that will move faster

If an alien hits the player's ship or reaches the bottom of the screen the player loses a ship

If the player loses 3 ships the game ends


# Dependencies

# Ubuntu

- replace pip3 with pip if you are using python 2.7

sudo python get-pip.pi

or

pip3 install -U pip3

# Install pip
python3 get-pip.py

verify you have pip by running

pip3 -- version 

# Pygame Library

- download the packages

sudo apt-get install python-pygame

sudo apt-get install python3-dev mercurial
 
- to add sounds you need the following libraries as well

sudo apt-get install libsdl-image1.2-dev libsdl2-dev libsdl-ttf2.0-dev

sudo apt-get install libsdl-mixer1.2-dev libportmidi-dev

sudo apt-get install libswscale-dev libsmpeg-dev libavformat-dev libavcode-dev

sudo apt-get install python-numpy

sudo apt-get install libfreetype6-dev

upgrade matplotlib

sudo pip3 install matplotlib --upgrade

#Installation
pip3 install --user hg+http://bitbucket.org/pygame/pygame

# Secondary installation
If trying the steps above does not work try the following commands

sudo apt-get install python3-pip

pip3 install --upgrade pip

pip3 install pygame
