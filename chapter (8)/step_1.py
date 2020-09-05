N,M =map(int,input().split())

field =[]
for i in range(N):
    sub_field = []
    for j in range(N):
        sub_field.append(0)
    field.append(sub_field)

for i in range(M):
    a, b = map(int, input().split())
    field[a-1][b-1] = 1
    field[b-1][a-1] = 1


for lines in field:
    for char in lines:
        print(char, end="")
    print()  # 改行に対応