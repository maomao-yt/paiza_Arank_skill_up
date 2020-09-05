N, M = map(int, input().split())
num_list = [int(i) for i in input().split()]


def calc(N, M):
    sum = 0
    ans = 10 ** 9
    sum += num_list[0]
    l, u = 0, 0
    while True:
        if M <= sum:
            sum -= num_list[l]
            ans = min(ans, u - l + 1)
            l += 1
        else:
            u += 1
            if u == N:
                return ans
            else:
                sum += num_list[u]


ans = calc(N, M)

if ans == 10 ** 9:
    print(-1)
else:
    print(ans)
