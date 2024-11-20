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
    # Authors Me and Me
    r.left_attachment_motor.run_time(-100,2500, then=Stop.HOLD, wait=False)    
    r.right_attachment_motor.run_time(100,2500, then=Stop.HOLD, wait=True)
    r.gyro_drive_straight_distance(200,120)
    r.gyro_tank_turn(125,25)
    r.gyro_drive_straight_distance(225,293)
    #raise the bar
    r.left_attachment_motor.run_time(150,2500, then=Stop.HOLD, wait=False)    
    r.right_attachment_motor.run_time(-150 ,2500, then=Stop.HOLD, wait=True)
    #face the shipwerck
    r.gyro_tank_turn(125,56) 
    #lower the bar
    r.left_attachment_motor.run_time(-100,2500, wait=False)    
    r.right_attachment_motor.run_time(100,2500, wait=True)
    #slowly raise the bar
    r.left_attachment_motor.run_time(10,3500, then=Stop.HOLD, wait=False)    
    r.right_attachment_motor.run_time(-10,3500, then=Stop.HOLD, wait=False)
    #drive to shipwreck 
    r.gyro_drive_straight_distance(81,180)
    #back away from the shipwreck
    r.gyro_drive_straight_distance(-200,50)
    #raise the bar
    r.left_attachment_motor.run_time(100,2500, then=Stop.HOLD, wait=False)    
    r.right_attachment_motor.run_time(-100,2500, then=Stop.HOLD, wait=True)\
    #turn twards coral thing 
    r.gyro_tank_turn(200,-77)
    r.gyro_drive_straight_distance(179,190)
    r.left_attachment_motor.run_time(-150,3500, then=Stop.HOLD, wait=False)    
    r.right_attachment_motor.run_time(150,3500, then=Stop.HOLD, wait=False)
    wait(1000)
    #back away from coral thing
    r.gyro_drive_straight_distance(-179,90)
    r.gyro_tank_turn(200,-16)
    r.gyro_drive_straight_distance(167,159)
    #turn twards the shark
    r.gyro_tank_turn(120,-29)
    r.gyro_drive_straight_distance(99,89)
    r.gyro_drive_straight_distance(-99,249)
    #turn twards the other coral thing
    r.robot.drive(100,-35 )
    wait(1500)
    r.robot.stop()
    r.gyro_drive_straight_distance(167,-100)
    r.gyro_tank_turn(126,91)
    r.gyro_drive_straight_distance(167,232)
    r.left_attachment_motor.stop()
    r.right_attachment_motor.stop()