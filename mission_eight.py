################################
# mission_eight.py
################################

import math
import time
from pybricks.ev3devices import *
from pybricks.parameters import *
from pybricks.robotics import *
from pybricks.iodevices import *
from pybricks.tools import DataLog, StopWatch, wait
from pybricks.hubs import EV3Brick
from robot_18300 import robot_18300


def mission_eight(r):
    print("Running Mission 8")
    # Mission Name: Gyro Demonstration
    # Authors: Coach Kevin
    wait(500)
    data = DataLog('time', 'angle')
    watch = StopWatch()
    btns = r.ev3.buttons.pressed()
    while len(btns) == 0:
        r.ev3.screen.clear()
        angle = r.gyro_sensor.angle()*-1
        time = watch.time()
        r.ev3.screen.draw_text(0, 20, "Gyro Angle:")
        r.ev3.screen.draw_text(70, 60, str(angle))
        r.ev3.screen.draw_text(0, 100, "BTN2STOP")
        data.log(time,angle)
        wait(1000)
        btns = r.ev3.buttons.pressed()
    
