"""
Дана квадратная матрица. Найдите определитель данной матрицы.
Сначала вводится размерность n квадратной матрицы, затем n строк матрицы.
Выведите одно целое число — определитель данной матрицы.

Sample Input:
2
4 2
5 3

Sample Output:
2
"""

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
