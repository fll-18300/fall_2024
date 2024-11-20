################################
# mission_one.py
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

def mission_one(r):
    print("Running Mission 1")
    # Mission Name
    # Authors: Kyle Mortimer 

    r.gyro_drive_straight_distance(200,325)
    r.gyro_tank_turn(200,30)
    r.gyro_drive_straight_distance(200,359)
    r.gyro_tank_turn(200,-115)
    r.gyro_drive_straight_time(200,1251)
    wait(1000)
    r.robot.straight(-150)
    r.gyro_tank_turn(200,33)
    r.gyro_drive_straight_time(200,3192)
    r.robot.straight(-200)