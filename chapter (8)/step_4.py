N, M = map(int, input().split())

field = []
for i in range(N):
    sub_field = []
    for j in range(N):
        sub_field.append(0)
    field.append(sub_field)

# 有向グラフは始まりの頂点の方に「k」を追加（a）
for i in range(M):
    a, b, k = map(int, input().split())
    field[a - 1][b - 1] = k

answer = []
for sub_field in field:
    lists = []
    index = [s for s, x in enumerate(sub_field) if x != 0]
    for num in index:
        lists.append(str(num) + "(" + str(sub_field[num]) + ")")
    answer.append(lists)

for lines in field:
    for char in lines:
        print(char, end="")
    print()  # 改行に対応

for lines in answer:
    for char in lines:
        print(char, end="")
    print()  # 改行に対応
