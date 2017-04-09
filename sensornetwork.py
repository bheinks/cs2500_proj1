from sensor import Sensor
from random import uniform

class SensorNetwork:
    def __init__(self, aoi_size, num_sensors, r, e):
        self.sensors = [Sensor(uniform(0, aoi_size), uniform(0, aoi_size), r, e) for i in range(num_sensors)]

        # debug list
        #self.sensors = []

        #for y in range(1, 44, 4):
        #    for x in range(1, 24, 4):
        #        self.sensors.append(Sensor(x, y, r, e))

    # determine coverage using monte carlo method (more samples == more accuracy)
    def coverage(self, samples):
        points_covered = 0

        for i in range(samples):
            x, y = uniform(0, 50), uniform(0, 50)

            if self.is_covered(x, y):
                points_covered += 1

        return 100 * (points_covered / samples)

    def is_covered(self, x, y):
        for sensor in self.sensors:
            if sensor.contains_point(x, y):
                return True

        return False

    # find and return a list of all intersection points between sensors
    def find_intersections(self):
        intersections = []

        for i, s1 in enumerate(self.sensors):
            for s2 in self.sensors[i+1:]:
                i1, i2 = s1.intersects(s2)

                if i1 and i1 not in intersections:
                    intersections.append(i1)
                if i2 and i2 not in intersections:
                    intersections.append(i2)
        
        # filter intersections for only points that are within sensor range
        return [(x, y) for x, y in intersections if self.is_covered(x, y)]
