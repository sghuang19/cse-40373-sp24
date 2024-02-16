import time
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

