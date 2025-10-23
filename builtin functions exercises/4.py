import math
import time

num = int(input())
msec = int(input())

time.sleep(msec / 1000)
square = math.sqrt(num)

print(f'Square root of {num} after {msec} is {square}')