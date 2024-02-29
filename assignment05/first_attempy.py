from sense_hat import SenseHat
import time

s = SenseHat()
s.low_light = True

green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
'''
later add code to handle a sigint 
make it exit gracefully after turning off the leds
'''
N = [nothing] * 16
Y = [nothing] * 16
H = nothing
C = nothing
F = nothing
ON = nothing


def turn_off_leds():
    O = nothing
    return [
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
    ]
    
def drive_neutral():
  O = nothing
  return [
      O,     O,     O,     O, O,     O,     O,     O,
      N[1],  N[2],  N[3],  O, Y[1],  Y[2],  Y[3],  O,
      N[4],  N[5],  N[6],  O, Y[4],  Y[5],  Y[6],  O,
      N[7],  N[8],  N[9],  O, Y[7],  Y[8],  Y[9],  O,
      N[10], N[11], N[12], O, Y[10], Y[11], Y[12], O,
      N[13], N[14], N[15], O, Y[13], Y[14], Y[15], O,
      O,     O,     O,     O, O,     O,     O,     O,
      H,     C,     O,     F, O,     O,     O,     ON,
  ]


def set_num_0(position):
    white = (255, 255, 255)
    if position == 'first':
        for i in range(14):
            N[i] = white if i not in [4, 7, 10] else nothing
    elif position == 'second':
        for i in range(14):
            Y[i] = white if i not in [4, 7, 10] else nothing
            
def set_num_1(position):
    white = (255, 255, 255)
    if position == 'first':
        for i in range(16):
            N[i] = white if i in [2, 5, 8, 11, 14] else nothing
    elif position == 'second':
        for i in range(16):
            Y[i] = white if i in [2, 5, 8, 11, 14] else nothing

def set_num_2(position):
    white = (255, 255, 255)
    if position == 'first':
        for i in range(16):
            N[i] = white if i not in [4, 5, 11, 12] else nothing
    elif position == 'second':
        for i in range(16):
            Y[i] = white if i not in [4, 5, 11, 12] else nothing

def set_num_3(position):
    white = (255, 255, 255)
    if position == 'first':
        for i in range(16):
            N[i] = white if i not in [4, 5, 10, 11] else nothing
    elif position == 'second':
        for i in range(16):
            Y[i] = white if i not in [4, 5, 10, 11] else nothing

def set_num_4(position):
    white = (255, 255, 255)
    if position == 'first':
        for i in range(16):
            N[i] = white if i not in [2, 5, 10, 11, 13, 14] else nothing
    elif position == 'second':
        for i in range(16):
            Y[i] = white if i not in [2, 5, 10, 11, 13, 14] else nothing
    
def set_num_5(position):
    white = (255, 255, 255)
    if position == 'first':
        for i in range(16):
            N[i] = white if i not in [5, 6, 10, 11] else nothing
    elif position == 'second':
        for i in range(16):
            Y[i] = white if i not in [5, 6, 10, 11] else nothing

def set_num_6(position):
    white = (255, 255, 255)
    if position == 'first':
        for i in range(16):
            N[i] = white if i not in [2, 3, 5, 6, 11] else nothing
    elif position == 'second':
        for i in range(16):
            Y[i] = white if i not in [2, 3, 5, 6, 11] else nothing
def set_num_7(position):
    white = (255, 255, 255)
    if position == 'first':
        for i in range(16):
            N[i] = white if i in [1, 2, 3, 6, 9, 12, 15] else nothing
    elif position == 'second':
        for i in range(16):
            Y[i] = white if i in [1, 2, 3, 6, 9, 12, 15] else nothing

def set_num_8(position):
    white = (255, 255, 255)
    if position == 'first':
        for i in range(16):
            N[i] = white if i not in [5, 11] else nothing
    elif position == 'second':
        for i in range(16):
            Y[i] = white if i not in [5, 11] else nothing

def set_num_9(position):
    white = (255, 255, 255)
    if position == 'first':
        for i in range(16):
            N[i] = white if i not in [5, 10, 11, 13, 14] else nothing
    elif position == 'second':
        for i in range(16):
            Y[i] = white if i not in [5, 10, 11, 13, 14] else nothing
count = 0


set_num_8('first')
set_num_9('second')

while True: 
  
    s.set_pixels(drive_neutral())
    time.sleep(0.75)
    count += 1
  
    
