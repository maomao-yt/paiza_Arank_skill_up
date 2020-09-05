import numpy as np

N, M = map(int, input().split())
num_list = np.array([int(i) for i in input().split()])

for i in range(M):
    zero_list = np.zeros(N, dtype=np.int32)
    l, u, a = map(int, input().split())
    zero_list[l - 1:u] = a
    num_list += zero_list

for num in num_list:
    print(num)