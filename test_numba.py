from numba import jit
import time

@jit
def withnumba(a,b,c):
    c = 0
    for i in range(0,10000):
        c += a**b**c
    return c

def withoutnumba(a,b,c):
    return a**b**c

start_time = time.time()
withnumba(10000,10000,10000)
print("took " , time.time() - start_time, "seconds")

start_time = time.time()
withoutnumba(1,1,1)
print("Mtook " , time.time() - start_time, "seconds")
