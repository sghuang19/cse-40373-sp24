# FIXME: Threading not supported in emulator
# import threading
import time
# from sense_emu import SenseHat
# from sense_hat import SenseHat

TRAFFIC_SEQUENCE = [
    ('Arrow', 10),
    ('Green', 30),
    ('Yellow', 10),
    ('Red', 0)  # Red is indefinite
]

CROSSWALK_SEQUENCE = [
    ('Green', 20),
    ('Yellow', 10),
    ('Red', 0)  # Red is indefinite
]

COLORS = {
    'Arrow': (144, 238, 144),
    'Green': (0, 255, 0),
    'Yellow': (255, 255, 0),
    'Red': (255, 0, 0),
}


class Display:
    def __init__(self):
        self.pattern = [[(0, 0, 0), ] * 8, ] * 8
        self.s = SenseHat()
        self.s.low_light = True

    def update_region(self, regions, color):
        for x1, y1, x2, y2 in regions:
            for i in range(x1, x2 + 1):
                for j in range(y1, y2 + 1):
                    self.pattern[i][j] = color
        self.refresh()

    def update_pixel(self, x, y, color):
        self.pattern[x][y] = color
        self.refresh()

    def refresh(self):
        self.s.set_pixels([p for row in self.pattern for p in row])


display = Display()


class TrafficLightPair:
    def __init__(self, direction, crosswalk, regions):
        """
        :param regions: A list of the left top and the right bottom
        coordinates of the region
        """

        self.direction = direction
        self.state = 'Red'
        self.crosswalk = crosswalk
        self.regions = regions

    def cycle(self):
        # self.state is always Red when this method is called
        for light, duration in TRAFFIC_SEQUENCE:
            self.state = light
            print(self.direction, "Traffic Lights are now", self.state)
            self.light()
            time.sleep(duration)

    def light(self):
        display.update_region(self.regions, COLORS[self.state])


class CrosswalkPair:
    def __init__(self, direction, regions):
        """
        :param regions: A list of pixel coordinates
        """
        self.direction = direction
        self.state = 'Red'
        self.pressed = False
        self.regions = regions

    def cycle(self):
        for light, duration in CROSSWALK_SEQUENCE:
            self.state = light
            print(self.direction, "Crosswalk Lights are now", self.state)
            self.light()
            time.sleep(duration)
        self.pressed = False

    def press(self):
        print(self.direction, "Crosswalk button pressed")
        self.pressed = True

    def light(self):
        for x, y in self.regions:
            display.update_pixel(x, y, COLORS[self.state])


class Controller:
    def __init__(self, traffic_lights):
        self.traffic_lights = traffic_lights

    def simulate(self):
        while True:
            for light in self.traffic_lights:
                while light.crosswalk.pressed:
                    time.sleep(5)  # Wait for the crosswalk to finish cycling
                light.cycle()
                if light.crosswalk.pressed:
                    # Current light is red, start cycling the crosswalk
                    # FIXME: Threading is not supported in the emulator
                    # threading.Thread(target=light.crosswalk.cycle).start()
                    pass


