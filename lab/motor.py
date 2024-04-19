from sense_hat import SenseHat
from ULN2003 import ULN2003
import time


def drive(steps: int = 1):
    # TODO: drive the motor throught GPIO
    pass


def control():
    # TODO: control of the motor
    while True:
        for event in sense.stick.get_events():
            print("The joystick was {} {}".format(event.action, event.direction))
            # TODO: drive the motor based on joystick action
            drive()
    pass


if __name__ == "__main__":
    sense = SenseHat()
    sense.show_message("SenseHat started!")

    pins = 26, 19, 13, 6
    Stepper = ULN2003(pins)
    while True:
        Stepper.step(n=100)
        sleep(1)


    # control()

