import time
import sys

indent = 0
increasing = True

try:
    while True:
        print(' ' * indent, end='')
        print('*****')
        time.sleep(0.1)  # Pause for 1/10 of a second.

        if increasing:
            indent = indent + 1
            if indent > 20:
                increasing = False

        elif increasing == False:
            indent = indent - 1
            if indent == 0:
                increasing = True
except KeyboardInterrupt:
    sys.exit()
