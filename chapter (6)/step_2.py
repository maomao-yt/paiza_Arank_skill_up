import numpy as np

N = int(input())
num_list = np.array([int(i) for i in input().split()])
n = int(input())

for i in range(n):
    s, e = map(int, input().split())
    num = np.sum(num_list[s:e+1])
    print(num)
