#!/usr/bin/env python3

from sensornetwork import SensorNetwork
from random import uniform
from pprint import pprint

sn = SensorNetwork(50, 50, 5, 300, 1000, False)

#print(len(sn.find_intersections()))

#for sensor in sn.sensors:
#    print("Coverage is {:.2f}%".format(sn.coverage()))
#    print(sn.is_redundant(sensor))

#print(sum(s.is_active for s in sn.sensors), len(sn.sensors))

init_coverage = sn.coverage()

while sn.coverage()
