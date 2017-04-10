#!/usr/bin/env python3

from sensornetwork import SensorNetwork
from time import sleep

sn = SensorNetwork(50, 100, 5, 300, 1000, True)

## random top down
#rounds = 0
#cov = 100
#while cov > 50:
#    print(len(sn.random_top_down()))
#    cov = sn.coverage()
#    print("Coverage is {:.2f}%".format(cov))
#    rounds += 1
#print(len(sn.random_top_down()))
#print("random top down -", rounds)
#sleep(5)



# random bottom up
print("="*24)
sn.reset(False)
initial = True
#measuring = False
rounds = 0
cov = 0
max_cov = 0
while True:
    if initial and cov > 50:
        rounds = 0
        initial = False

    if not initial and cov <= 50:
        break

    print(len(sn.random_bottom_up()))
    cov = sn.coverage()
    print("Coverage is {:.2f}%".format(cov))
    rounds += 1

#    if cov >= max_cov:
#        max_cov = cov
#    elif cov < max_cov and not measuring:
#        print(max_cov)
#        rounds = 0
#        measuring = True

print("random bottom up -", rounds)
sleep(5)



# all_active
print("="*24)
sn.reset(True)
rounds = 0
cov = 100
while cov > 50:
    print(len(sn.all_active()))
    cov = sn.coverage()
    print("Coverage is {:.2f}%".format(cov))
    rounds += 1
print("all active -", rounds)
sleep(5)



# greedy top down
sn.reset(True)
rounds = 0
cov = 100
sn.init_greedy()
while cov > 50:
    print(len(sn.greedy_top_down()))
    cov = sn.coverage()
    print("Coverage is {:.2f}%".format(cov))
    rounds += 1
print("greedy top down -", rounds)
