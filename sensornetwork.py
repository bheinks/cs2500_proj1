from sensor import Sensor
from point import Point
from random import randint

class SensorNetwork:
    def __init__(self, aoi_size, num_sensors, radius, initial_energy):
        self.aoi_size = aoi_size
        self.num_sensors = num_sensors

        # initialize aoi as a two-dimensional list of aoi_size x aoi_size
        self.aoi = [[None for x in range(aoi_size)] for y in range(aoi_size)]        

        while num_sensors > 0:
            # randomly place sensors about aoi
            x, y = randint(1, aoi_size - 1), randint(1, aoi_size - 1)

            # if a sensor isn't already centered here
            if not self.aoi[y][x]:
                self.aoi[y][x] = Sensor(Point(x, y), radius, initial_energy)
                num_sensors -= 1

    def print(self):
        for y in range(self.aoi_size):
            for x in range(self.aoi_size):
                # if sensor found, print center point as 'O'
                if self.aoi[y][x]:
                    print('o ', end='')
                else:
                    print('- ', end='')
            print()
