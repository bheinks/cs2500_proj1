#!/usr/bin/env python3

from sensornetwork import SensorNetwork
from random import uniform
from pprint import pprint

sn = SensorNetwork(50, 50, 5, 300)

#print("Coverage is {:.2f}%".format(sn.coverage(100000)))
pprint(sn.find_intersections())
