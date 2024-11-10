################################
# mission_six.py
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

def mission_six(r):
    print("Running Mission 6")
    # Mission Name
    # Authors Madeleine, Katherine
    r.robot.straight(375)
    r.robot.turn(13)
    wait(1000)
    r.robot.straight(70)
    wait(1000)
    r.right_attachment_motor.run_time(-100,2500, then=Stop.COAST, wait=False)
    r.robot.turn(55)
    r.robot.straight(-90)
    r.robot.turn(85)
    r.robot.straight(-100)
    r.robot.straight(-400)