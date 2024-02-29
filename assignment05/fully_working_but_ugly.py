from sense_hat import SenseHat
import time
s = SenseHat()
s.low_light = True
green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
orange = (255, 179, 71)
nothing = (0,0,0)
mode_set = False
far_mult = 1
far_add = 0
far_mode = False

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
temperature = round(s.get_temperature())
setpoint = round(s.get_temperature())
print(setpoint)
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
  ON = white
  global H, C, F
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
        for i in range(16):
            N[i] = white if i not in [5, 8, 11] else nothing
    elif position == 'second':
        for i in range(16):
            Y[i] = white if i not in [5, 8, 11] else nothing
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
            
def sleep_and_poll(time_s):
    global temperature, setpoint, far_mode, mode_set, far_mult, far_add
    start_time = time.time()
    while time.time() - start_time < time_s:
        time.sleep(0.01)
        for event in s.stick.get_events():
            if event.action == "pressed":
                if event.direction in ["up"]:
                    mode_set = True
                    print("here")
                    break
                elif event.direction in ["down"]:
                    mode_set = True
                    break
                elif event.direction in ["left"]:
                    setpoint = (setpoint-32)*5/9
                    far_mult = 1
                    far_add = 0
                elif event.direction in ["right"]:
                    far_mult = 9/5
                    far_add = 32
                    if not far_mode:
                      setpoint = round(setpoint * 9/5 + 32)
                      far_mode = True
                      
def poll_temp():
    temperature = round(s.get_temperature())
    temperature = int(temperature * far_mult) + far_add
    if temperature >= 10:
        temp_str = str(temperature)
    else:
        temp_str = '0' + str(temperature)
    print(temperature)
    for i in range(len(temp_str)):
        digit = int(temp_str[i])
        drive_digit(digit, 'first' if i == 0 else 'second')


def drive_setpoint():
    global setpoint
    if setpoint >= 10:
      temp_str = str(setpoint)
    elif setpoint <= 0:
      setpoint = 0
      temp_str = '00'
    else:
      temp_str = '0' + str(setpoint)
    print(setpoint)
    for i in range(len(temp_str)):
        digit = int(temp_str[i])
        drive_digit(digit, 'first' if i == 0 else 'second')
        
def drive_digit(digit, position):
    if digit == '-':
        pass
    elif digit == 0:
        set_num_0(position)
    elif digit == 1:
        set_num_1(position)
    elif digit == 2:
        set_num_2(position)
    elif digit == 3:
        set_num_3(position)
    elif digit == 4:
        set_num_4(position)
    elif digit == 5:
        set_num_5(position)
    elif digit == 6:
        set_num_6(position)
    elif digit == 7:
        set_num_7(position)
    elif digit == 8:
        set_num_8(position)
    elif digit == 9:
        set_num_9(position)
        
def setpoint_mode():
    global setpoint, mode_set, far_mode, setpoint, far_add, far_mult
    drive_setpoint()
    s.set_pixels(drive_neutral())
    while mode_set:
        joystick_input_detected = False
        events = s.stick.get_events()
        if events:
          event = events[0]
          joystick_input_detected = True
        else:
          break
        if event.direction == "up":
            setpoint += 1
            drive_setpoint
            s.set_pixels(drive_neutral())
            mode_set = False
            break
        elif event.direction == "down":
            setpoint -= 1
            drive_setpoint()
            s.set_pixels(drive_neutral())
            mode_set = False
            break
        elif event.direction == "right":
            far_mult = 9/5
            far_add = 32
            if not far_mode:
                setpoint = round(setpoint * 9/5 + 32)
                far_mode = True
        elif event.direction == "left":
            setpoint = (setpoint-32)*5/9
            far_mult = 1
            far_add = 0
          
count = 0

while True:
    s.set_pixels(drive_neutral())
    poll_temp()
    sleep_and_poll(.5)
    if mode_set:
      set_count = count
      while(mode_set):
        setpoint_mode()
        set_count += 1
        if set_count - 70 > count:
          mode_set = False
          break
    if not far_mode:
        temperature_diff = temperature - setpoint
        print(temperature_diff)
        multiplier = min(1.0, max(0.1, abs(temperature_diff) / 5.0))
        intensity = 255 * multiplier
        if temperature_diff > 0.5:
            H = (intensity, 0, 0)  
            C = nothing
            F = (0, intensity, 0)
            s.set_pixels(drive_neutral())

        elif temperature_diff < -0.5:
            H = nothing
            C = (0, 0, intensity)
            F = (0, intensity, 0)
            s.set_pixels(drive_neutral())
        else:
          H = nothing
          C = nothing
          F = nothing
          s.set_pixels(drive_neutral())
    else:
        temperture_diff = int((temperature *9/5) + 32)-setpoint
        
        threshold_fahrenheit = 0.5 * 9/5  
        print(threshold_fahrenheit)
        multiplier = min(1.0, max(0.1, abs(temperature_diff) / threshold_fahrenheit))
        intensity = 255 * multiplier

        if temperature_diff > 1:
            H = (intensity, 0, 0)  
            C = nothing
            F = (0, intensity, 0)
            s.set_pixels(drive_neutral())

        elif temperature_diff < -1:
            H = nothing
            C = (0, 0, intensity)
            F = (0, intensity, 0)
            s.set_pixels(drive_neutral())
        else:
            H = nothing
            C = nothing
            F = nothing
            s.set_pixels(drive_neutral())
        
        pass
      
    count += 1


