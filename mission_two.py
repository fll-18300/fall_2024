################################
# mission_two.py
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

def mission_two(r):
    print("Running Mission 2")
    #Wesleys Mission Turn Chicken.
    r.robot.straight(350)
    r.left_attachment_motor.run_angle(300, 90,then=Stop.HOLD, wait=True)
    r.robot.straight(90)
    wait(3000)
    r.robot.straight(-650)