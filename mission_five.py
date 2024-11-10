################################
# mission_five.py
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

def mission_five(r):
    print("Running Mission 5")
    # Mission Name push da boat
    # Authors Jackson
    r.gyro_drive_straight_distance(200, 900)
    r.robot.straight(-1000)

    
