from sense_hat import SenseHat
# from sense_emu import SenseHat
import numpy as np
from time import time

s = SenseHat()
s.low_light = True

# Define the segment display for the digits
digit = [None for _ in range(10)]

digit[0] = [
    1, 1, 1, 1,
    1, 0, 0, 1,
    1, 0, 0, 1,
    1, 0, 0, 1,
    1, 0, 0, 1,
    1, 0, 0, 1,
    1, 1, 1, 1
]

digit[1] = [
    0, 0, 1, 0,
    0, 1, 1, 0,
    0, 0, 1, 0,
    0, 0, 1, 0,
    0, 0, 1, 0,
    0, 0, 1, 0,
    0, 1, 1, 1
]

digit[2] = [
    1, 1, 1, 1,
    0, 0, 0, 1,
    0, 0, 0, 1,
    1, 1, 1, 1,
    1, 0, 0, 0,
    1, 0, 0, 0,
    1, 1, 1, 1
]

digit[3] = [
    1, 1, 1, 1,
    0, 0, 0, 1,
    0, 0, 0, 1,
    0, 1, 1, 1,
    0, 0, 0, 1,
    0, 0, 0, 1,
    1, 1, 1, 1
]

digit[4] = [
    1, 0, 0, 1,
    1, 0, 0, 1,
    1, 0, 0, 1,
    1, 1, 1, 1,
    0, 0, 0, 1,
    0, 0, 0, 1,
    0, 0, 0, 1
]

digit[5] = [
    1, 1, 1, 1,
    1, 0, 0, 0,
    1, 0, 0, 0,
    1, 1, 1, 1,
    0, 0, 0, 1,
    0, 0, 0, 1,
    1, 1, 1, 1
]

digit[6] = [
    1, 1, 1, 1,
    1, 0, 0, 0,
    1, 0, 0, 0,
    1, 1, 1, 1,
    1, 0, 0, 1,
    1, 0, 0, 1,
    1, 1, 1, 1
]

digit[7] = [
    1, 1, 1, 1,
    0, 0, 0, 1,
    0, 0, 0, 1,
    0, 0, 0, 1,
    0, 0, 0, 1,
    0, 0, 0, 1,
    0, 0, 0, 1
]

digit[8] = [
    1, 1, 1, 1,
    1, 0, 0, 1,
    1, 0, 0, 1,
    1, 1, 1, 1,
    1, 0, 0, 1,
    1, 0, 0, 1,
    1, 1, 1, 1
]

digit[9] = [
    1, 1, 1, 1,
    1, 0, 0, 1,
    1, 0, 0, 1,
    1, 1, 1, 1,
    0, 0, 0, 1,
    0, 0, 0, 1,
    1, 1, 1, 1
]

# Define the colors
N = (0, 0, 0)
P = (255, 105, 180)
B = (0, 0, 255)
G = (0, 255, 0)
R = (255, 0, 0)
W = (255, 255, 255)


# Keeping track of the state
class State:
    mode = 'off'
    unit = 'c'
    temp = s.get_temperature()
    setpoint = 26
    set_mode = False
    polled = time()  # Last time the temperature was polled

    def poll(self):
        """Polls the temperature and updates the state"""
        self.temp = s.get_temperature()
        if self.unit == 'f':
            self.temp = c2f(self.temp)
        if self.temp > self.setpoint:
            self.mode = 'cool'
        elif self.temp < self.setpoint:
            self.mode = 'heat'
        else:
            self.mode = 'off'
        self.polled = time()

    def intensity(self):
        """Returns the intensity in percentage"""
        diff = abs(self.temp - self.setpoint)
        if self.unit == 'f':
            diff = f2c(diff)
        if diff < 0.5:
            return 0
        if diff > 5.5:
            return 100
        return int(18 * diff + 1)

    def listen(self):
        """Listen to the joystick and configure thermostat"""
        events = s.stick.get_events()
        if not events:
            if time() - self.polled > 1:
                self.poll()
            drive()
            return
        for event in events:
            if event.action != 'pressed':
                continue

            if self.set_mode:
                if event.direction == 'up':
                    self.setpoint += 1
                elif event.direction == 'down':
                    self.setpoint -= 1

            if event.direction == 'middle':
                self.set_mode = not self.set_mode
            elif event.direction == 'left':
                self.unit = 'c'
            elif event.direction == 'right':
                self.unit = 'f'
            drive()


state = State()


# Helper functions
def c2f(c):
    return c * 9 / 5 + 32


def f2c(f):
    return (f - 32) * 5 / 9


# Display

def adjust_intensity(color):
    """Adjusts the intensity of a color based on the state"""
    return tuple(int(c * state.intensity() / 100) for c in color)


def get_digits(val):
    val = int(val) if val < 100 else 99
    tens = digit[val // 10]
    ones = digit[val % 10]
    tens = np.array([B if val else N for val in tens]).reshape(7, 4, 3)
    ones = np.array([P if val else N for val in ones]).reshape(7, 4, 3)
    return tens, ones


def drive():
    # Handle the digits
    val = state.setpoint if state.set_mode else state.temp
    val = c2f(val) if state.unit == 'f' else val
    tens, ones = get_digits(val)
    result = np.concatenate((tens, ones), axis=1)

    bottom = [N for _ in range(8)]

    if state.mode != 'off':
        if state.mode == 'heat':
            bottom[0] = adjust_intensity(R)
        if state.mode == 'cool':
            bottom[1] = adjust_intensity(B)

    # TODO: Fan light

    bottom[7] = R  # Power indicator, always on
    bottom = np.array(bottom).reshape(1, 8, 3)

    result = np.concatenate((result, bottom), axis=0).reshape(-1, 3)
    s.set_pixels(result)


if __name__ == '__main__':
    while True:
        state.listen()
