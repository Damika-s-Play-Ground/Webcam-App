import numpy as np
import time

arr = np.random.rand(1200, 1600)

s = time.time()
for i in range(1, 100):
    arr += i
print(time.time() - s)

arr = np.random.rand(1200, 1600)

s = time.time()
for i in range(1, 100):
    arr = arr + i
print(time.time() - s)


