#!/usr/bin/env python3

from sensornetwork import SensorNetwork
from random import uniform

sn = SensorNetwork(50, 50, 5, 300)

points_covered = 0

# determine coverage using monte carlo method (more samples == more accuracy)
for i in range(100000):
    x, y = uniform(0, 50), uniform(0, 50)

    for sensor in sn.sensors:
        if sensor.contains_point(x, y):
            points_covered += 1
            break

print("Coverage is {:.2f}%".format(100 * (points_covered / i)))
