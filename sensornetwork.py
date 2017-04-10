from sensor import Sensor
from random import uniform, choice
from pprint import pprint

class SensorNetwork:
    def __init__(self, aoi_size, num_sensors, r, e, num_samples, is_active):
        # set of randomly positioned sensors arranged within AoI
        self.sensors = [Sensor(uniform(0, 50), uniform(0, 50), r, e, is_active)
                for i in range(num_sensors)]

        # set of randomly selected points in AoI to determine coverage via monte
        # carlo method
        self.mc_points = [(uniform(1, aoi_size-1), uniform(1, aoi_size-1))
                for i in range(num_samples)]

    # determine coverage using monte carlo points
    def coverage(self):
        points_covered = sum(self.is_covered(x, y) for x, y in self.mc_points)
        return 100 * (points_covered / len(self.mc_points))

    def is_covered(self, x, y, only_active = False):
        for sensor in self.sensors:
            if sensor.is_alive and sensor.contains_point(x, y):
                return True
        return False

    # find and return a list of all intersection points between sensors
    def find_intersections(self):
        intersections = []

        for i, s1 in enumerate(self.sensors):
            for s2 in self.sensors[i+1:]:
                i1, i2 = s1.intersects2(s2)

                if i1 and i1 not in intersections:
                    intersections.append(i1)
                if i2 and i2 not in intersections:
                    intersections.append(i2)
        
        # filter intersections for only points that are within sensor range
        return [(x, y) for x, y in intersections if self.is_covered(x, y)]

    def is_redundant(self, sensor):
        # find the intersection points that are covered by this sensor
        #points_covered = [(x, y) for x, y in self.find_intersections()
        #        if sensor.contains_point(x, y)]

        # temporarily disable sensor to determine the difference in coverage
        cov = self.coverage()
        sensor.is_alive = False
        
        if self.coverage() == cov:
            return True

        sensor.is_alive = True
        return False

        # if a point is not otherwise covered, sensor is not redundant
        #for s in self.sensors:
        #    if s != sensor:
        #        for x, y in points_covered:
        #            if not s.contains_point(x, y):
        #                break
        #            
        #            self.sensors.remove(sensor)
        #            return True

        #for x, y in points_covered:
        #    if not self.is_covered(x, y):
        #        sensor.is_active = True
        #        return False

    def reset(self):
        for sensor in self.sensors:
            sensor.is_active = True

    def round(self):
        for sensor in self.sensors:
            sensor.e -= 1

            if sensor.e == 0:
                sensor.is_active = False

    def active_sensors(self):
        return [s for s in self.sensors if s.is_active]

    def all_active(self):
        return self.sensors

    def random_bottom_up(self):
        sensor = choice(self.sensors)
        points_covered = [(x, y) for x, y in self.find_intersections()
                if sensor.contains_point(x, y)]

        for x, y in points_covered:
            if not self.is_covered(x, y, True):


    def random_top_down(self):
        return list(filter(lambda s: not self.is_redundant(s), self.sensors))
