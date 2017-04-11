#!/usr/bin/env python3

from sensornetwork import SensorNetwork

# Simulate redundancy algorithms here 

# Example
# SensorNetwork(aoi_size, num_sensors, radius, initial_energy, set_all_active)
sn = SensorNetwork(50, 50, 5, 300, 1000, False)

while len(sn.alive_sensors()) > 0:
    # every call to redundancy algo represents a round
    sn.random_bottom_up()
    print("Coverage is {:.2f}%".format(sn.coverage()))
