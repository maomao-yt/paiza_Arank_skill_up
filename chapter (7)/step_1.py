N, M = map(int, input().split())

# 累積和を利用する
def calc(N, M):
    sum = int((M * (M + 1) // 2))
    sub_sum = int((N * (N + 1) // 2))
    if N == 0 and M == 0:
        print(0)
    else:
        print(int(sum) - int(sub_sum)+N)


calc(N, M)
