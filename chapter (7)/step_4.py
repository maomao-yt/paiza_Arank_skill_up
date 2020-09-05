N, M = map(int, input().split())


# ユークリッドの互除法
def calc(n, m):
    A = max(n, m)
    B = min(n, m)
    while A % B != 0:
        rest = B
        B = A % B
        A = rest
    return B


ans = calc(N, M)
print(ans)
