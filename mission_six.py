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
    r.robot.straight(328)
    r.robot.turn(13)
    wait(1000)
    r.robot.straight(100)
    wait(1000)
    r.right_attachment_motor.run_time(-150,3000, then=Stop.COAST, wait=False)
    # squid part
    r.gyro_tank_turn(200,38)
    r.robot.straight(-90)
    #CRASH
    r.robot.turn(85)
    r.robot.straight(-100)
    r.robot.straight(-400)
    r.robot.straight(512)
    # removing the plant
    #r.robot.straight(50)
    #r.robot.turn(-55)
    #r.robot.straight(260)
    #r.right_attachment_motor.run_time(-11,2500, then=Stop.COAST, wait=False)
    #r.robot.turn(55)
