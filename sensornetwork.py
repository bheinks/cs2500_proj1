import random

from sensor import Sensor
from pprint import pprint

class SensorNetwork:
    def __init__(self, aoi_size, num_sensors, r, init_e, num_samples, is_active):
        # set of randomly positioned sensors arranged within AoI
        self.sensors = [Sensor(random.uniform(0, 50), random.uniform(0, 50), r, init_e, is_active)
                for i in range(num_sensors)]
        self.redundant_sensors = []
        self.a_sensors = []
        self.init_e = init_e

        # set of randomly selected points in AoI to determine coverage via monte
        # carlo method
        self.mc_points = [(random.uniform(1, aoi_size-1), random.uniform(1, aoi_size-1))
                for i in range(num_samples)]

    # determine coverage using monte carlo points
    def coverage(self):
        points_covered = sum(self.is_covered(x, y) for x, y in self.mc_points)
        return 100 * (points_covered / len(self.mc_points))

    def is_covered(self, x, y, only_active = False):
        for sensor in self.sensors:
            if sensor.is_alive and sensor.is_active and sensor.contains_point(x, y):
                return True
        return False

    # find and return a list of all intersection points between sensors
    def find_intersections(self, sensors):
        intersections = []

        for i, s1 in enumerate(sensors):
            for s2 in sensors[i+1:]:
                i1, i2 = s1.intersects(s2)

                if i1 and i1 not in intersections:
                    intersections.append(i1)
                if i2 and i2 not in intersections:
                    intersections.append(i2)
        
        # filter intersections for only points that are within sensor range
        #return [(x, y) for x, y in intersections if self.is_covered(x, y)]
        return intersections

    def is_redundant(self, sensor):
        # find the intersection points that are covered by this sensor
        #points_covered = [(x, y) for x, y in self.find_intersections()
        #        if sensor.contains_point(x, y)]

        # temporarily disable sensor to determine the difference in coverage
        cov = self.coverage()
        sensor.deactivate()
        
        if self.coverage() == cov:
            return True

        sensor.activate()
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

    def reset(self, is_active):
        for sensor in self.sensors:
            sensor.is_active = is_active
            sensor.e = self.init_e
            sensor.is_alive = True

        self.redundant_sensors = []
        self.a_sensors = []

    def round(self):
        for sensor in self.active_sensors():
            sensor.e -= 1

            if sensor.e == 0:
                sensor.kill()

    def alive_sensors(self):
        return [s for s in self.sensors if s.is_alive]

    def active_sensors(self):
        return [s for s in self.sensors if s.is_active and s.is_alive]

    ###########################
    #                         #
    #  redundancy algorithms  #
    #                         #
    ###########################

    def all_active(self):
        self.round()
        return self.active_sensors()

    def random_bottom_up(self):
        self.round()

        # select a random sensor among those that are alive and not active
        random_set = list(set(self.alive_sensors()) - set(self.active_sensors()))
        
        # if all sensosrs are active, return
        if not random_set:
            return self.active_sensors()

        sensor = random.choice(random_set)

        cov = self.coverage()
        sensor.activate()
        
        if self.coverage() == cov:
            sensor.deactivate()

        #all_intersections = self.find_intersections(self.sensors)
        #active_intersections = self.find_intersections(self.active_sensors())

        #for x, y in list(set(all_intersections) - set(active_intersections)):
        #    if sensor.contains_point(x, y):
        #        sensor.activate()
        #        break

        return self.active_sensors()

    def random_top_down(self):
        self.round()

        active_sensors = self.active_sensors()

        # if all sensors are inactive, return
        if not active_sensors:
            for s in self.redundant_sensors:
                s.activate()

            return self.alive_sensors()

        sensor = random.choice(active_sensors)

        if self.is_redundant(sensor):
            self.redundant_sensors.append(sensor)
            sensor.deactivate()

        return self.active_sensors()

    def init_greedy(self):
        active_sensors = self.active_sensors()
        active_intersections = self.find_intersections(active_sensors)
        self.a_sensors = sorted(active_sensors, key=lambda s: s.points_contained(active_intersections))

    def greedy_top_down(self):
        self.round()

        # sort active sensors by most intersection points

        # filter out sensors we've already determined to not be redundant

        if not self.active_sensors():
            for s in self.redundant_sensors:
                s.activate()

            return self.alive_sensors()

        if not self.a_sensors:
            return self.active_sensors()

        sensor = self.a_sensors.pop()

        if self.is_redundant(sensor):
            self.redundant_sensors.append(sensor)
            sensor.deactivate()

        return self.active_sensors()
