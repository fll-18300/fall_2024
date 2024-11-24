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
    r.left_attachment_motor.run_time(150,500, then=Stop.HOLD, wait=False)    
    r.right_attachment_motor.run_time(-150 ,500, then=Stop.HOLD, wait=True)
    r.gyro_drive_straight_distance(250,631)
    r.left_attachment_motor.run_time(-100,1000, then=Stop.HOLD, wait=False)    
    r.right_attachment_motor.run_time(100,1000, then=Stop.HOLD, wait=True)
    r.gyro_tank_turn(196,-21 )
    r.robot.drive
    #drive back on an ark
    # Create and define distance, speed, and turn variables
    # to control how fast the robot moves, how sharp it turns, and how far it will go.
    # Reset the robot distance to zero
    speed = -350
    turn = -15
    distance = 501
    r.robot.reset()
    r.left_attachment_motor.run_time(-100,1000, then=Stop.HOLD, wait=False)    
    r.right_attachment_motor.run_time(100,1000, then=Stop.HOLD, wait=False)
    # While the robot.distance() is less than or equal to the variable 'distance' stay in the while loop
    while (abs(r.robot.distance()) <= distance):
        r.robot.drive(speed,turn)
    # r.robot.drive() goes on forever, even after the while loop ends.
    # You need to stop the robot after exiting the while loop
    r.robot.stop()
        #drive back to home with an ark
    # Create and define distance, speed, and turn variables
    # to control how fast the robot moves, how sharp it turns, and how far it will go.
    # Reset the robot distance to zero
    speed = 350
    turn = -90 
    distance = 601
    r.robot.reset()
    r.left_attachment_motor.run_time(-100,1000, then=Stop.HOLD, wait=False)    
    r.right_attachment_motor.run_time(100,1000, then=Stop.HOLD, wait=False)
    # While the robot.distance() is less than or equal to the variable 'distance' stay in the while loop
    while (abs(r.robot.distance()) <= distance):
        r.robot.drive(speed,turn)
    # r.robot.drive() goes on forever, even after the while loop ends.
    # You need to stop the robot after exiting the while loop
    r.robot.stop()
    #r.gyro_drive_straight_distance(-300,620)
    r.left_attachment_motor.stop()
    r.right_attachment_motor.stop()