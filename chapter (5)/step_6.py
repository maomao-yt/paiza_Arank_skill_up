H, W= map(int, input().split())

field = []
# 2次元リストマップを作成
for i in range(H):
    sub_field = []
    line = input()
    for char in line:
        sub_field.append(char)
    field.append(sub_field)

Y,X =0,0
for y in range(H):
    for x in range(W):
        if field[y][x] == "!":
            Y,X =y,x

field[Y][X] = "*"
# 上
y = Y - 1
while True:
    if y == -1 or field[y][X] == "#":
        break
    if field[y][X] == "*":
        for i in range(abs(Y - y)):
            field[y + i][X] = "*"
        break
    y -= 1

# 下
y = Y + 1
while True:
    if y == H or field[y][X] == "#":
        break
    if field[y][X] == "*":
        for i in range(abs(Y - y)):
            field[y - i][X] = "*"
        break
    y += 1

# 左
x = X - 1
while True:
    if x == -1 or field[Y][x] == "#":
        break
    if field[Y][x] == "*":
        for i in range(abs(X - x)):
            field[Y][x + i] = "*"
        break
    x -= 1

# 右
x = X + 1
while True:
    if x == W or field[Y][x] == "#":
        break
    if field[Y][x] == "*":
        for i in range(abs(X - x)):
            field[Y][x - i] = "*"
        break
    x += 1

# 右上
y = Y - 1
x = X - 1
while True:
    if y == -1 or x == -1 or field[y][x] == "#":
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
    if y == H or x == W or field[y][x] == "#":
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
    if x == W or y == -1 or field[y][x] == "#":
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
    if y == H or x == -1 or field[y][x] == "#":
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
