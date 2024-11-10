################################
# mission_three.py
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

def mission_three(r):
    print("Running Mission 3")
    # Mission Name Sharks forever!
    # Authors
    r.left_attachment_motor.run_time(100,2500, then=Stop.HOLD, wait=False)    
    r.right_attachment_motor.run_time(-100,2500, then=Stop.HOLD, wait=True)
    r.gyro_drive_straight_distance(200,251)
    r.gyro_tank_turn(200,31)
    r.gyro_drive_straight_distance(225,376)
    r.left_attachment_motor.run_time(-100,2500, then=Stop.HOLD, wait=False)    
    r.right_attachment_motor.run_time(100,2500, then=Stop.HOLD, wait=True)
    r.gyro_tank_turn(200,-115)
    r.gyro_drive_straight_time(200,1251)
    wait(1000)
    r.robot.straight(-150)
    r.gyro_tank_turn(200,33)
    r.gyro_drive_straight_time(200,2892)
    r.robot.straight(-200)