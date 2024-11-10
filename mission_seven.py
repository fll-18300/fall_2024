################################
# mission_seven.py
################################

import math
import time
from pybricks.ev3devices import *
from pybricks.parameters import *
from pybricks.robotics import *
from pybricks.iodevices import *
from pybricks.tools import wait
from pybricks.hubs import EV3Brick
from robot_18300 import robot_18300
from pybricks.media.ev3dev import Font

def mission_seven(r):  
    print("Running Mission 7")
    # Mission Name: Tape Measure Tool
    # Authors: Kyle 
    r.ev3.screen.clear()
    print("Team 18300 Robot Tape Measure")
    wait(4000)
    # Reset the distance to 0.
    r.robot.reset()
    btns = r.ev3.buttons.pressed()
    r.ev3.screen.set_font(Font(size=16, bold=True))
    while len(btns) == 0:
        r.ev3.screen.clear()
        r.ev3.screen.draw_text(0, 0, "Team 18300")
        r.ev3.screen.draw_text(0, 30, "Push robot to measure!")
        r.ev3.screen.draw_text(0, 60,"dst= " + str(r.robot.distance()))
        r.ev3.screen.draw_text(0, 90, "push btn 2 stop")
        wait(150)
        btns = r.ev3.buttons.pressed()
    # Set the font back
    r.ev3.screen.set_font(Font(size=30, bold=True))
