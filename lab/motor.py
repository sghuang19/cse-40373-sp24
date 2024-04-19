from ULN2003Pi.ULN2003 import ULN2003
import RPi.GPIO as GPIO
import time

pins = 26, 19, 13, 6
button = 17
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
Stepper = ULN2003(pins)

while True:
    print(GPIO.input(button))
    if GPIO.input(button):
        Stepper.step(n=100)
        time.sleep(0.2)

