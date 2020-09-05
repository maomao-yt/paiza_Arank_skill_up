N = int(input())
num_list = [int(i) for i in input().split()]

num = 0
for i in range(N):
    num += num_list[i]
    print(num)
