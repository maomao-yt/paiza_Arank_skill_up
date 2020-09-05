N, M = map(int, input().split())
num_list = [int(i) for i in input().split()]


def calc(N, M):

    if 2 not in num_list and 0 not in num_list:
        answer = 1
        return answer
    for i in range(N):  # 要素の拡張
        for j in range(N - i ):  # 同じ要素数で繰り返し
            if 0 in num_list[j:j + i + 1 ]:
                continue
            num = 2**num_list[j:j + i + 1 ].count(2)
            if num >= M:
                answer = (j + i + 1 ) - j
                return answer


ans = calc(N, M)
print(ans)
