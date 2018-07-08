import RPi.GPIO as GPIO
from time import sleep
import time

def SetAngle(angle, pwm, pin):
	#	duty = angle / 18 + 2
	duty = 100
	GPIO.output(pin, True)
	pwm.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(pin, False)
	pwm.ChangeDutyCycle(0)

pin = 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)
pwm=GPIO.PWM(pin, 5000)
pwm.start(0)
SetAngle(180,pwm, pin)

