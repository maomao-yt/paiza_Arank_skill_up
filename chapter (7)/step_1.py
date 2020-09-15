N, K = map(int, input().split())

# 3つの数値を循環している特性から数列の開始値と終了値から総和の値を推測する
A = [1, 0, -1]


def calc(N, K):
    st = A[N % 3]  # 数列の開始値
    ed = A[K % 3]  # 数列の終了値
    if st == 1:
        if ed == 1:
            return 1
        else:
            return 0
    else:
        if ed == -1:
            return -1
        else:
            return 0


print(calc(N-1, K-1))