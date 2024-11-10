#!/usr/bin/env pybricks-micropython

################################
# main.py
################################

# Import the necessary libraries
import math
import time
from pybricks.ev3devices import *
from pybricks.parameters import *
from pybricks.robotics import *
from pybricks.iodevices import *
from pybricks.tools import wait
from pybricks.hubs import EV3Brick
from robot_18300 import robot_18300
from menu import menu
from pybricks.media.ev3dev import Font

###########
# Startup
###########
# Instantiate the Robot
r = robot_18300()

# Calibrate/Reset the Gyro to prevent drift
# User can skip by pressing the middle button
count = 0
r.ev3.screen.clear()
r.ev3.screen.set_font(Font(size=20))
r.ev3.screen.draw_text(0,44,"Press center button")
r.ev3.screen.draw_text(0,64,"To skip gyro cal")
while count <= 100:
    btns = r.ev3.buttons.pressed()
    if len(btns) == 1: 
        btn = btns[0]
        if btn == Button.CENTER:
            break
    if count == 100:
        r.ev3.screen.clear()
        r.calibrate_gyro(4)
    wait(20)
    count = count + 1
r.ev3.screen.clear()
wait(500)
r.ev3.screen.set_font(Font(size=30, bold=True))

# Program select menu
menu(r)