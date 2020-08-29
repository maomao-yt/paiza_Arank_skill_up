H, W, Y, X = map(int, input().split())

field = []
# 2次元リストマップを作成
for i in range(H):
    sub_field = []
    line = input()
    for char in line:
        sub_field.append(char)
    field.append(sub_field)

field[Y][X] = "*"


# 右上
y = Y - 1
x = X - 1
while True:
    if y == -1 or x == -1:
        break
    if field[y][x] == "*":
        for i in range(abs(Y - y)):
            field[y + i][x + i] = "*"
        break
    y -= 1
    x -= 1

# 左下
y = Y + 1
x = X + 1
while True:
    if y == H or x == W:
        break
    if field[y][x] == "*":
        for i in range(abs(Y - y)):
            field[y - i][x - i] = "*"
        break
    y += 1
    x += 1

# 右上
y = Y - 1
x = X + 1
while True:
    if x == W or y == -1:
        break
    if field[y][x] == "*":
        for i in range(abs(Y - y)):
            field[y + i][x - i] = "*"
        break
    y -= 1
    x += 1

# 左下
y = Y + 1
x = X - 1
while True:
    if y == H or x == -1:
        break
    if field[y][x] == "*":
        for i in range(abs(Y - y)):
            field[y - i][x + i] = "*"
        break
    y += 1
    x -= 1


for lines in field:
    for char in lines:
        print(char, end="")
    print()  # 改行に対応
