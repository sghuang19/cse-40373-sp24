import digits
import numpy as np

N = (0, 0, 0)
P = (255, 105, 180)
B = (0, 0, 255)

# A global variable to keep the state of the thermostat
state = {'temp': 0, 'setpoint': 0}

def get_digit(val):
    # Take a value from 0 to 99 and return digit matrices
    left = num0
    right = num1
    left = np.where(left == 1, B, N)
    right = np.where(right == 1, P, N)
    return left, right


def drive():
    # TODO: implement this
    bottom_row = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0]])
    left, right = get_digit(state['temp'])
    result = np.concatenate((left, right), axis=1)  # Concatenate two digits
    result = np.concatenate((result, bottom_row), axis=0)  # Concatenate the bottom row
    # TODO: drive the LED
    pass
