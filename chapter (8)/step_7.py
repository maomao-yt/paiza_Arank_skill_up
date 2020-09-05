N, M = map(int, input().split())

num_list = []
for i in range(M):
    num = list(map(int, input().split()))
    num_list.append(num)
if N - 1 > M:
    print("NO")
else:
    lists = []
    for i in range(M):
        lists.append(num_list[i][0])
        lists.append(num_list[i][1])
    # 入力した数値を一か所にまとめる
    answer = list(set(lists))
    flg = False
    for i in range(1, N + 1):
        if i not in answer:
            flg = True
            print("NO")
            break
    if not flg:
        print("YES")
