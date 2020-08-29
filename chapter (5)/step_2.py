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
# 上
y = Y - 1
while True:
    if y == -1:
        break
    if field[y][X] == "*":
        for i in range(abs(Y - y)):
            field[y+i][X] = "*"
        break
    y -= 1

# 下
y = Y + 1
while True:
    if y == H:
        break
    if field[y][X] == "*":
        for i in range(abs(Y - y)):
            field[y-i][X] = "*"
        break
    y += 1


# 左
x = X - 1
while True:
    if x == -1:
        break
    if field[Y][x] == "*":
        for i in range(abs(X - x)):
            field[Y][x+i] = "*"
        break
    x -= 1

# 右
x = X + 1
while True:
    if x == W:
        break
    if field[Y][x] == "*":
        for i in range(abs(X - x)):
            field[Y][x-i] = "*"
        break
    x += 1

for lines in field:
    for char in lines:
        print(char, end="")
    print()  # 改行に対応
