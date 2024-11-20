################################
# mission_four.py
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

def mission_four(r):
    print("Running Mission 4")
    # Mission name: Crabby_CRABS >{*-*}<
    # Authors: Lydia 
    r.left_attachment_motor.run_time(-21,2000, then=Stop.COAST, wait=False)
    r.robot.straight(359)
    #robot goes up to the crab mission
    r.left_attachment_motor.stop()
    r.left_attachment_motor.run_time(1000,500, then=Stop.COAST, wait=False)
    wait(300)
    #Robot flicked the mission in half
    r.robot.stop()
    r.gyro_drive_straight_time(230,902)
    #robot pushes into the mission
    #r.robot.straight(203)
    r.robot.stop()
    wait(500)
    r.robot.straight(-207)
    r.right_attachment_motor.run_time(527,1000, then=Stop.COAST, wait=True)
    r.right_attachment_motor.stop()
    r.robot.stop()
    wait(1000)
    #5r.right_attachment_motor.run_time(-12,2000, then=Stop.COAST, wait=False)
    #r.gyro_tank_turn(39,-1)
    r.robot.straight(207)
    #r.gyro_drive_straight_distance(100,207)
    r.robot.stop()
    wait(500)
    #robot stands the mission up
    #r.right_attachment_motor.run_time(-1000,1000, then=Stop.COAST, wait=True)
    r.gyro_drive_straight_distance(100,57)
    #r.robot.straight(57)
    r.right_attachment_motor.run_time(1000,1000, then=Stop.COAST, wait=False)
    wait(100)
    #r.robot.straight(172)
    r.gyro_drive_straight_distance(200,172)
    #robot flicks the mission over to complete it
    #r.right_attachment_motor.run_time(-1560,700, then=Stop.COAST, wait=True)


    
    #wait(100)
    #r.gyro_tank_turn(539,85)
    #r.right_attachment_motor.run_time(-527,1000, then=Stop.COAST, wait=True)
    #r.robot.straight(-528)
    #r.robot.stop()
    #r.left_attachment_motor.run_time(500,500, then=Stop.COAST, wait=False)
    #r.right_attachment_motor.run_time(-500,500, then=Stop.COAST, wait=False)
    #r.robot.straight(287)
    #r.right_attachment_motor.run_time(527,1000, then=Stop.COAST, wait=False)
    #r.robot.stop
    #wait(500)
    #r.left_attachment_motor.run_time(1000,500, then=Stop.COAST, wait=False)
    #Friday stuff \/
    #r.robot.straight(-53)
    #r.gyro_tank_turn(502,-20)
    #r.robot.straight(269)
    #r.gyro_tank_turn(502,-4)
    #r.robot.straight(212)
    #r.gyro_tank_turn(501,-25)
    #hehehe >:) 

    #Mission before adding the new wacky thang \/ 
    #r.left_attachment_motor.run_time(-21,2000, then=Stop.COAST, wait=False)
    #r.robot.straight(359)
    #r.left_attachment_motor.stop()
    #r.left_attachment_motor.run_time(1000,500, then=Stop.COAST, wait=False)
    #wait(300)
    #r.robot.stop()
    #r.robot.straight(203)
    #r.robot.stop()
    #wait(500)
    #r.robot.straight(-207)
    #r.right_attachment_motor.run_time(527,1000, then=Stop.COAST, wait=True)
    #r.robot.stop()
    #r.robot.straight(207)
    #r.robot.stop()
    #r.right_attachment_motor.run_time(-1000,1000, then=Stop.COAST, wait=True)
    #r.robot.straight(57)
    #r.robot.straight(-87)
    #r.right_attachment_motor.run_time(1000,161, then=Stop.COAST, wait=True)
    #r.robot.straight(60)
    #r.right_attachment_motor.run_time(-1560,700, then=Stop.COAST, wait=True)
    #r.robot.straight(-628)
    #hehehe >:)