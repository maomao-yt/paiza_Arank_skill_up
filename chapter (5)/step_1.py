H, W, Y, X = map(int, input().split())

field = []
# 2次元リストマップを作成
for i in range(H):
    sub_field = []
    for j in range(W):
        sub_field.append(".")
    field.append(sub_field)

field[Y][X] = "!"
# 行を変える
for y in range(H):
    if field[y][X] != "!":
        field[y][X] = "*"

# 列を変える
for x in range(W):
    if field[Y][x] != "!":
        field[Y][x] = "*"

for lines in field:
    for char in lines:
        print(char, end="")
    print()  # 改行に対応
