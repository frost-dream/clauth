from numba import jit
from time import time
c=int(input())
b=time()
for i in range(100000000*c):
    pass
print("without GPU:", time()-b)
b=time()
@jit(target_backend='cuda')
def a():
    for i in range(100000000*c):
        pass
a()
print("with GPU:", time()-b)
input()
