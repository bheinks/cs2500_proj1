from sensor import Sensor
from random import uniform

class SensorNetwork:
    def __init__(self, aoi_size, num_sensors, r, e):
        self.sensors = [Sensor(uniform(0, aoi_size), uniform(0, aoi_size), r, e) for i in range(num_sensors)]
