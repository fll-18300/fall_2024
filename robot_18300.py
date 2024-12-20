################################
# robot_18300.py
################################

# Import the necessary libraries
import sys
import math
import time
from pybricks.ev3devices import *
from pybricks.parameters import *
from pybricks.robotics import *
from pybricks.iodevices import *
from pybricks.tools import wait, StopWatch
from pybricks.hubs import EV3Brick
from pybricks.media.ev3dev import Font

################################
# Define custom_robot Class
################################
class robot_18300:

    def __init__(self):
        
        '''
        This is the construtor for our robot class. 
        This function gets called when a robot object is made from the robot class.
        '''

        # Initialize the brick, motors, sensors
        # Use "try" so there can be an exception if there is an initialization error
        try:
            self.ev3 = EV3Brick()
        except:
            self.ev3.screen.clear()
            self.ev3.light.off()
            self.ev3.light.on(Color.RED)
            self.ev3.screen.draw_text(0,40,"STARTUP ERROR")
            self.ev3.screen.draw_text(0,80,"EV3 FAIL")
            self.ev3.speaker.beep(frequency=2000, duration=1000)
            wait(4000)
            self.ev3.screen.clear()
            sys.exit()
        try:
            self.left_attachment_motor = Motor(Port.A)
        except: 
            self.ev3.screen.clear()
            self.ev3.light.off()
            self.ev3.light.on(Color.RED)
            self.ev3.screen.draw_text(0,40,"STARTUP ERROR")
            self.ev3.screen.draw_text(0,80,"CHECK PORT A")
            self.ev3.speaker.beep(frequency=2000, duration=1000)
            wait(4000)
            self.ev3.screen.clear()
            sys.exit()
        try:
            self.right_attachment_motor = Motor(Port.D)
        except: 
            self.ev3.screen.clear()
            self.ev3.light.off()
            self.ev3.light.on(Color.RED)
            self.ev3.screen.draw_text(0,40,"STARTUP ERROR")
            self.ev3.screen.draw_text(0,80,"CHECK PORT D")
            self.ev3.speaker.beep(frequency=2000, duration=1000)
            wait(4000)
            self.ev3.screen.clear()
            sys.exit()
        try:
            self.left_drive_motor = Motor(Port.B,positive_direction=Direction.COUNTERCLOCKWISE)
        except: 
            self.ev3.screen.clear()
            self.ev3.light.off()
            self.ev3.light.on(Color.RED)
            self.ev3.screen.draw_text(0,40,"STARTUP ERROR")
            self.ev3.screen.draw_text(0,80,"CHECK PORT B")
            self.ev3.speaker.beep(frequency=2000, duration=1000)
            wait(4000)
            self.ev3.screen.clear()
            sys.exit()
        try:
            self.right_drive_motor = Motor(Port.C,positive_direction=Direction.COUNTERCLOCKWISE)
        except: 
            self.ev3.screen.clear()
            self.ev3.light.off()
            self.ev3.light.on(Color.RED)
            self.ev3.screen.draw_text(0,40,"STARTUP ERROR")
            self.ev3.screen.draw_text(0,80,"CHECK PORT C")
            self.ev3.speaker.beep(frequency=2000, duration=1000)
            wait(4000)
            self.ev3.screen.clear()
            sys.exit()
        # keep_trying = 1
        # retry_count = 0
        # while keep_trying == 1:
        #     try:
        #         self.gyro_sensor = GyroSensor(Port.S1)
        #         keep_trying = 0
        #         print("Gyro Init Port 1 Good!")
        #     except:
        #         self.ev3.screen.clear() 
        #         self.ev3.screen.draw_text(0,44,"Gyro Init Port 1 Bad.")
        #         self.ev3.screen.draw_text(0,64,"Retry Attempt # " + str(retry_count + 1))
        #         print("Gyro Init Port 1 Bad. Retry...")
        #         try:
        #             self.analog_sensor = AnalogSensor(Port.S1)
        #             wait(500)
        #             self.gyro_sensor = GyroSensor(Port.S1)
        #             self.ev3.screen.draw_text(0, 22, "Gyro Init Good!")
        #             print("Gyro Init Port 1 Good!")
        #             keep_trying = 0
        #         except:
        #             if retry_count == 1:
        #                 print("Gyro Init Port 1 Bad. Retry limit reached.")
        #                 self.ev3.screen.clear()
        #                 self.ev3.light.off()
        #                 self.ev3.light.on(Color.RED)
        #                 self.ev3.screen.draw_text(0,22,"STARTUP ERROR")
        #                 self.ev3.screen.draw_text(0,44,"CHECK PORT 1")
        #                 self.ev3.screen.draw_text(0,66,"Retry limit reached...")
        #                 self.ev3.speaker.beep(frequency=2000, duration=1000)
        #                 wait(4000)
        #                 self.ev3.screen.clear()
        #                 sys.exit()    
        #             print("Gyro Init Port 1 Bad, Retry again...")
        #             retry_count = retry_count + 1
        keep_trying = 1
        retry_count = 0
        while keep_trying == 1:
            try:
                self.gyro_sensor = GyroSensor(Port.S4, direction=Direction.CLOCKWISE)
                keep_trying = 0
                print("Gyro Init Port 4 Good!")
            except:
                self.ev3.screen.clear() 
                self.ev3.screen.draw_text(0,44,"Gyro Init Port 4 Bad.")
                self.ev3.screen.draw_text(0,64,"Retry Attempt # " + str(retry_count + 1))
                print("Gyro Init Port 4 Bad. Retry...")
                try:
                    self.analog_sensor = AnalogSensor(Port.S4)
                    wait(500)
                    self.gyro_sensor = GyroSensor(Port.S4, direction=Direction.CLOCKWISE)
                    self.ev3.screen.draw_text(0, 22, "Gyro Init Good!")
                    print("Gyro Init Port 4 Good!")
                    keep_trying = 0
                except:
                    if retry_count == 1:
                        print("Gyro Init Port 4 Bad. Retry limit reached.")
                        self.ev3.screen.clear()
                        self.ev3.light.off()
                        self.ev3.light.on(Color.RED)
                        self.ev3.screen.draw_text(0,22,"STARTUP ERROR")
                        self.ev3.screen.draw_text(0,44,"CHECK PORT 4")
                        self.ev3.screen.draw_text(0,66,"Retry limit reached...")
                        self.ev3.speaker.beep(frequency=2000, duration=1000)
                        wait(4000)
                        self.ev3.screen.clear()
                        sys.exit()    
                    print("Gyro Init Port 4 Bad, Retry again...")
                    retry_count = retry_count + 1
        try:
            self.robot = DriveBase(self.left_drive_motor, self.right_drive_motor, wheel_diameter=88, axle_track=115)
            self.robot.settings(straight_speed=400, straight_acceleration=300, turn_rate=200, turn_acceleration=123)
            self.ev3.screen.clear()
            self.ev3.light.off()
            self.ev3.light.on(Color.GREEN)
            self.watch = StopWatch()
            self.ev3.screen.draw_text(10,40,"STARTUP GOOD!")
            self.ev3.screen.set_font(Font(size=30, bold=True))
            wait(1000)
            self.ev3.screen.clear()    
        except:
            self.ev3.screen.clear()
            self.ev3.light.off()
            self.ev3.light.on(Color.RED)
            self.ev3.screen.draw_text(0,40,"STARTUP ERROR")
            self.ev3.screen.draw_text(0,80,"NOT WIRING")
            self.ev3.speaker.beep(frequency=2000, duration=1000)
            #self.ev3.speaker.say("startup error, check wiring")
            wait(4000)
            self.ev3.screen.clear()
            sys.exit()

        # This sets the minimum drive speed to prevent stalling
        self.min_drive_speed = 60.

        # This sets how quickly the robot speeds up and slows down
        # unit(s) of speed (mm/s) per 1 unit of distance (mm)
        self.drive_acceleration = 1.

        # This sets the minimum tank turn speed to prevent stalling
        self.min_tank_turn_speed = 30.

        # This is the radius of the wheels in cms
        # This is so we can convert distance to wheel rotation(s) or the 
        # other way around
        self.wheel_radius = 4.4

        # half of the distace between the wheels(in cms, obvously)
        # We need this in order to convert from degrees we want to spin the bot
        # to how far those wheels have to move.
        self.axle_track = 5.6

        # this is the gain we use when going straight with the gyro sensor
        self.gyro_gain = 3

################################
# Define functions 
################################
    
    # Reset The Gyro
    def calibrate_gyro(self, port_number):
        self.ev3.screen.set_font(Font(size=20))
        retry_calibration = 1
        retry_gyro_reset = 1
        retry_count = 0
        while retry_calibration == 1:
            self.ev3.screen.draw_text(0, 0, "Calibrating The Gyro...")
            self.ev3.screen.draw_text(0, 22, "Do Not Move Robot")
            if port_number == 1:
                while retry_gyro_reset == 1:
                    try:
                        self.analog_sensor = AnalogSensor(Port.S1)
                        wait(500)
                        self.gyro_sensor = GyroSensor(Port.S1)
                        wait(500)
                        retry_gyro_reset = 0
                        print("Gyro 1 Reset Good!")
                        self.ev3.screen.draw_text(0, 44, "Gyro 1 Reset Good!")
                    except: 
                        self.ev3.screen.draw_text(0,66,"Gyro 1 Reset Bad, Retrying")
                        print("Gyro 1 Reset Failed... Retry...")
                        try:
                            self.analog_sensor = AnalogSensor(Port.S1)
                            wait(500)
                            self.gyro_sensor = GyroSensor(Port.S1)
                            wait(500)
                            print("Gyro 1 Reset Good!")
                            retry_gyro_reset = 0
                        except:
                            if retry_count == 1:
                                print("Gyro Cal Port 1 Bad. Retry limit reached.")
                                self.ev3.screen.clear()
                                self.ev3.light.off()
                                self.ev3.light.on(Color.RED)
                                self.ev3.screen.draw_text(0,22,"GYRO CAL ERROR")
                                self.ev3.screen.draw_text(0,44,"CHECK PORT 1")
                                self.ev3.screen.draw_text(0,66,"Retry limit reached...")
                                self.ev3.speaker.beep(frequency=2000, duration=1000)
                                wait(4000)
                                self.ev3.screen.clear()
                                sys.exit()    
                            retry_count = retry_count + 1
                            print("Gyro 1 Reset Failed, Retry again...")
            if port_number == 2:
                while retry_gyro_reset == 1:
                    try:
                        self.analog_sensor = AnalogSensor(Port.S2)
                        wait(500)
                        self.gyro_sensor = GyroSensor(Port.S2)
                        wait(500)
                        retry_gyro_reset = 0
                        print("Gyro 2 Reset Good!")
                        self.ev3.screen.draw_text(0, 44, "Gyro 2 Reset Good!")
                    except: 
                        self.ev3.screen.draw_text(0,66,"Gyro 2 Reset Bad, Retrying")
                        print("Gyro 2 Reset Failed... Retry...")
                        try:
                            self.analog_sensor = AnalogSensor(Port.S2)
                            wait(500)
                            self.gyro_sensor = GyroSensor(Port.S2)
                            wait(500)
                            print("Gyro 2 Reset Good!")
                            retry_gyro_reset = 0
                        except:
                            if retry_count == 1:
                                print("Gyro Cal Port 2 Bad. Retry limit reached.")
                                self.ev3.screen.clear()
                                self.ev3.light.off()
                                self.ev3.light.on(Color.RED)
                                self.ev3.screen.draw_text(0,22,"GYRO CAL ERROR")
                                self.ev3.screen.draw_text(0,44,"CHECK PORT 2")
                                self.ev3.screen.draw_text(0,66,"Retry limit reached...")
                                self.ev3.speaker.beep(frequency=2000, duration=1000)
                                wait(4000)
                                self.ev3.screen.clear()
                                sys.exit()    
                            retry_count = retry_count + 1
                            print("Gyro 2 Reset Failed, Retry again...")
            if port_number == 3:
                while retry_gyro_reset == 1:
                    try:
                        self.analog_sensor = AnalogSensor(Port.S3)
                        wait(500)
                        self.gyro_sensor = GyroSensor(Port.S3)
                        wait(500)
                        retry_gyro_reset = 0
                        print("Gyro 3 Reset Good!")
                        self.ev3.screen.draw_text(0, 44, "Gyro 3 Reset Good!")
                    except: 
                        self.ev3.screen.draw_text(0,66,"Gyro 3 Reset Bad, Retrying")
                        print("Gyro 3 Reset Failed... Retry...")
                        try:
                            self.analog_sensor = AnalogSensor(Port.S3)
                            wait(500)
                            self.gyro_sensor = GyroSensor(Port.S3)
                            wait(500)
                            print("Gyro 3 Reset Good!")
                            retry_gyro_reset = 0
                        except:
                            if retry_count == 1:
                                print("Gyro Cal Port 3 Bad. Retry limit reached.")
                                self.ev3.screen.clear()
                                self.ev3.light.off()
                                self.ev3.light.on(Color.RED)
                                self.ev3.screen.draw_text(0,22,"GYRO CAL ERROR")
                                self.ev3.screen.draw_text(0,44,"CHECK PORT 3")
                                self.ev3.screen.draw_text(0,66,"Retry limit reached...")
                                self.ev3.speaker.beep(frequency=2000, duration=1000)
                                wait(4000)
                                self.ev3.screen.clear()
                                sys.exit()    
                            retry_count = retry_count + 1
                            print("Gyro 3 Reset Failed, Retry again...")
            else:
                while retry_gyro_reset == 1:
                    try:
                        self.analog_sensor = AnalogSensor(Port.S4)
                        wait(500)
                        self.gyro_sensor = GyroSensor(Port.S4, direction=Direction.CLOCKWISE)
                        wait(500)
                        retry_gyro_reset = 0
                        print("Gyro 4 Reset Good!")
                        self.ev3.screen.draw_text(0, 44, "Gyro 4 Reset Good!")
                    except: 
                        self.ev3.screen.draw_text(0,66,"Gyro 4 Reset Bad, Retrying")
                        print("Gyro 4 Reset Failed... Retry...")
                        try:
                            self.analog_sensor = AnalogSensor(Port.S4)
                            wait(500)
                            self.gyro_sensor = GyroSensor(Port.S4, direction=Direction.CLOCKWISE)
                            wait(500)
                            print("Gyro 4 Reset Good!")
                            retry_gyro_reset = 0
                        except:
                            if retry_count == 1:
                                print("Gyro Cal Port 4 Bad. Retry limit reached.")
                                self.ev3.screen.clear()
                                self.ev3.light.off()
                                self.ev3.light.on(Color.RED)
                                self.ev3.screen.draw_text(0,22,"GYRO CAL ERROR")
                                self.ev3.screen.draw_text(0,44,"CHECK PORT 4")
                                self.ev3.screen.draw_text(0,66,"Retry limit reached...")
                                self.ev3.speaker.beep(frequency=2000, duration=1000)
                                wait(4000)
                                self.ev3.screen.clear()
                                sys.exit()    
                            retry_count = retry_count + 1
                            print("Gyro 4 Reset Failed, Retry again...")
            i = 0
            while i <= 10:
                self.ev3.screen.clear()
                self.ev3.screen.draw_text(0, 0, "Checking Gyro For Drift")
                self.ev3.screen.draw_text(0, 22, "DO NOT MOVE!")
                self.ev3.screen.draw_text(0, 44, "Gyro= " + str(self.gyro_sensor.angle()))
                wait(100)
                self.ev3.screen.clear()
                i = i + 1
            if self.gyro_sensor.angle() == 0:
                retry_calibration = 0
                self.ev3.screen.clear()
                self.ev3.screen.draw_text(0, 22, "Gyro")
                self.ev3.screen.draw_text(0, 44, "Calibration")
                self.ev3.screen.draw_text(0, 84, "Complete!")
                wait(200)
                self.ev3.screen.clear()
            else:
                print("Gyro Drift Detected, resetting the Gyro.")                                    
        self.ev3.screen.set_font(Font(size=30, bold=True))

    # gyro tank turn
    def gyro_tank_turn(self,speed, angle):
        ''' Tank turn using the gyro
            angle positive = clockwise
            angle negative = counter-clockwise
        '''
        min_speed = 50
        #Get the current angle
        starting_angle = self.gyro_sensor.angle()
        target_angle = starting_angle - angle
        # Robot must be stopped first
        self.robot.stop()
        # The gyro is mounted upside-down which reverses the gyro measurements 
        if angle >= 0:
        #clockwise
            while self.gyro_sensor.angle() >= target_angle:
                # Ramp the speed based on the perecntage of the turn completed.
                scale = abs((self.gyro_sensor.angle() - starting_angle) / (target_angle - starting_angle))
                unbound_speed = speed * (1 - scale)
                current_speed = max(unbound_speed, self.min_tank_turn_speed)
                self.left_drive_motor.run(current_speed)
                self.right_drive_motor.run(-current_speed)
        else:
        #counter-clockwise
            while self.gyro_sensor.angle() <= target_angle:
                # Ramp the speed based on the perecntage of the turn completed.
                scale = abs((self.gyro_sensor.angle() - starting_angle) / (target_angle - starting_angle))
                unbound_speed = speed * (1 - scale)
                current_speed = max(unbound_speed, self.min_tank_turn_speed)
                self.left_drive_motor.run(-current_speed)
                self.right_drive_motor.run(current_speed)
        self.left_drive_motor.brake()
        self.right_drive_motor.brake()    

    # gyro drive straight
    def gyro_drive_straight_distance(self, max_speed, distance, min_speed=None):
        ''' Drive straight using the gyro.
            Use a proportional feedback loop.
        '''
        # Reset the distance to 0.
        self.robot.reset()
        # Set the min speed
        if min_speed == None: 
            min_speed = max_speed
        current_speed = min_speed

        # Define the feedback loop gain value, "pd."  This determines how much the robot
        # will correct when it drives off course.  
        # This value may need to be adjusted.  Here are some tips:
        # 1) If the value is too large, the robot will over-correct for errors and snake back and forth.  
        # 2) If the value is too small, the robot will not correct enough and will go off course.
        # 3) If the robot spins in circles, try making this value negative (pd=-1)
        pd = -4

        # Get the current gyro angle.  This is the direction the robot should keep driving. 
        starting_angle = self.gyro_sensor.angle()
        # Create a while loop so the robot will drive until it reaches the target distance.  Inside the loop
        # the robot's current direction, "self.gyro_sensor.angle()" is repeatedly checked to see if it has gone off course. 
        # If needed, a course correction is made to turn back to the desired direction (starting_angle)
        while abs(self.robot.distance()) <= distance:
            # Calculate the error (the difference) between where the robot should be pointed and where it is pointed
            # Where the robot should be pointed:     starting_angle
            # Where the robot is currently pointed:  self.gyro_sensor.angle()
            direction_error = starting_angle - self.gyro_sensor.angle()

            # Use the feedback loop gain value, "pd" multiplied by the, "direction_error" to make the robot turn back
            # on course.
            turn = direction_error * pd

            # The robot should drive with the speed passed into this method, "gyro_drive_straight" and turn based on
            # the correction needed to keep going straight.
            self.robot.drive(current_speed,turn)
            if min_speed >= 0:
                # Positive speed, pick the number closer to 0
                current_speed = min((current_speed + abs(self.robot.distance()/10), max_speed))
            else:
                # Negative speed, pick the number closer to 0
                current_speed = max((current_speed - abs(self.robot.distance()/10), max_speed))
        self.robot.stop()

    # gyro drive straight
    def gyro_drive_straight_time(self,max_speed, time, min_speed=None):
        ''' Drive straight using the gyro.
            Use a proportional feedback loop.
        '''
        # Reset the time to 0.
        watch = StopWatch()
        watch.reset()

        # Define the feedback loop gain value, "pd."  This determines how much the robot
        # will correct when it drives off course.  
        # This value may need to be adjusted.  Here are some tips:
        # 1) If the value is too large, the robot will over-correct for errors and snake back and forth.  
        # 2) If the value is too small, the robot will not correct enough and will go off course.
        # 3) If the robot spins in circles, try making this value negative (pd=-1)
        pd = -4

        # Get the current gyro angle.  This is the direction the robot should keep driving. 
        starting_angle = self.gyro_sensor.angle()
        
        if min_speed == None: 
            min_speed = max_speed
        current_speed = min_speed

        # Create a while loop so the robot will drive until it reaches the target distance.  Inside the loop
        # the robot's current direction, "self.gyro_sensor.angle()" is repeatedly checked to see if it has gone off course. 
        # If needed, a course correction is made to turn back to the desired direction (starting_angle)
        while watch.time() <= time:
            # Calculate the error (the difference) between where the robot should be pointed and where it is pointed
            # Where the robot should be pointed:     starting_angle
            # Where the robot is currently pointed:  self.gyro_sensor.angle()
            direction_error = starting_angle - self.gyro_sensor.angle()

            # Use the feedback loop gain value, "pd" multiplied by the, "direction_error" to make the robot turn back
            # on course.
            turn = direction_error * pd

            # The robot should drive with the speed passed into this method, "gyro_drive_straight" and turn based on
            # the correction needed to keep going straight.
            self.robot.drive(current_speed,turn)
            if min_speed >= 0:
                # Positive speed, pick the number closer to 0
                current_speed = min((current_speed + (watch.time() /100), max_speed))
            else:
                # Negative speed, pick the number closer to 0
                current_speed = max((current_speed - (watch.time() /100), max_speed))        
        self.robot.stop()               
