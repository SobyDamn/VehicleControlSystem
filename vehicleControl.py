import RPi.GPIO as GPIO
import time

"""
MOTOR INPUTS
IN1 - GPIO23
IN2 - GPIO24
IN3 - GPIO27
IN4 - GPIO22
"""
GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.OUT) #Set the output pin
GPIO.setup(24,GPIO.OUT) #Set the output pin
GPIO.setup(27,GPIO.OUT) #Set the output pin
GPIO.setup(22,GPIO.OUT) #Set the output pin
m1_pwm1 = GPIO.PWM(23,1000)
m1_pwm2 = GPIO.PWM(24,1000)
m2_pwm1 = GPIO.PWM(27,1000)
m2_pwm2 = GPIO.PWM(22,1000)
m1_pwm1.start(0)
m1_pwm2.start(0)
m2_pwm1.start(0)
m2_pwm2.start(0)
def moveBackward():
    m1_pwm1.ChangeDutyCycle(100)
    m1_pwm2.ChangeDutyCycle(0)
    m2_pwm1.ChangeDutyCycle(100)
    m2_pwm2.ChangeDutyCycle(0)
    #GPIO.output(27,GPIO.HIGH)
    #GPIO.output(22,GPIO.LOW)
    #GPIO.output(23,GPIO.HIGH)
    #GPIO.output(24,GPIO.LOW)

def moveForward():
    m1_pwm1.ChangeDutyCycle(0)
    m1_pwm2.ChangeDutyCycle(100)
    m2_pwm1.ChangeDutyCycle(0)
    m2_pwm2.ChangeDutyCycle(100)

"""
TO turn the vehicle, one vehicle in opposite direction and one in same direction
"""
##Bias to control how much the wheel should move in the direction of the motion while changing direction
bias = 100
def moveRight():
    m1_pwm1.ChangeDutyCycle(0)
    m1_pwm2.ChangeDutyCycle(100)
    m2_pwm1.ChangeDutyCycle(bias)
    m2_pwm2.ChangeDutyCycle(0)
def moveLeft():
    m1_pwm1.ChangeDutyCycle(bias)
    m1_pwm2.ChangeDutyCycle(0)
    m2_pwm1.ChangeDutyCycle(0)
    m2_pwm2.ChangeDutyCycle(100)
def steadyState():
    m1_pwm1.ChangeDutyCycle(0)
    m1_pwm2.ChangeDutyCycle(0)
    m2_pwm1.ChangeDutyCycle(0)
    m2_pwm2.ChangeDutyCycle(0)
    """GPIO.output(23,GPIO.LOW)
    GPIO.output(24,GPIO.LOW)
    GPIO.output(27,GPIO.LOW)
    GPIO.output(22,GPIO.LOW)"""

def cleanUp():
    GPIO.cleanup()
