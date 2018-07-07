#import time
#import pygame
#import RPi.GPIO as GPIO
#from time import sleep


# the data pin of the servo is wired to pin 12
# pin is an integer
def wave_arm(pin):
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(pin, GPIO.OUT)
	pwm=GPIO.PWM(pin, 50)
	pwm.start(0)
	SetAngle(90,pwm,pin)

#	GPIO.cleanup()
	
def SetAngle(angle,pwm,pin):
#	duty = angle / 18 + 2
	duty = 30
	GPIO.output(pin, True)
	pwm.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(pin, False)
	pwm.ChangeDutyCycle(0)
