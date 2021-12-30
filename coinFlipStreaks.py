import random

numberOfStreaks = 0
experimentCount = 10000

headCount = 0
tailCount = 0
for n in range(experimentCount):    
    if random.randint(0, 1) == 0:
        headCount += 1
        tailCount = 0
    else:
        tailCount += 1
        headCount = 0

    if headCount == 6 or tailCount == 6:
        numberOfStreaks += 1
        headCount = 0
        tailCount = 0

print('Chance of streak: %s%%' % (numberOfStreaks / 100))