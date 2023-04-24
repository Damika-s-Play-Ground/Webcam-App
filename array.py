import numpy as np
import time

arr = np.random.rand(1, 1000000)

s = time.time()
for i in range(100):
    arr += i
    
print(time.time() - s)
