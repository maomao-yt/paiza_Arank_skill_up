H, W, Y, X = map(int, input().split())

field = []
# 2次元リストマップを作成
for i in range(H):
    sub_field = []
    for j in range(W):
        sub_field.append(".")
    field.append(sub_field)

field[Y][X] = "!"

# 右上
y = Y - 1
x = X - 1
while True:
    if y == -1 or x == -1:
        break
    field[y][x] = "*"
    y -= 1
    x -= 1

# 左下
y = Y + 1
x = X + 1
while True:
    if y == H or x == W:
        break
    field[y][x] = "*"
    y += 1
    x += 1


#  左上
y = Y - 1
x = X + 1
while True:
    if y == -1 or x == W:
        break
    field[y][x] = "*"
    y -= 1
    x += 1

# 右下
y = Y + 1
x = X - 1
while True:
    if y == H or x == -1:
        break
    field[y][x] = "*"
    y += 1
    x -= 1


for lines in field:
    for char in lines:
        print(char, end="")
    print()  # 改行に対応
