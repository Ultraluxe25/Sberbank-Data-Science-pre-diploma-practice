import numpy as np
from scipy import linalg

n = int(input())
arr = []

for _ in range(n):
    sub_arr = list(map(int, input().split()))
    arr.append(sub_arr)

arr = np.array(arr)    
deter = linalg.det(arr)
print(round(deter))
