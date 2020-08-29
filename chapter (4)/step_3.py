def check(y,x):
    if x != 0 and field[y][x-1] == ".":
        field[y][x - 1] = "*"
        x -= 1
        check(y,x)
    if x != W-1 and field[y][x + 1] == ".":
        field[y][x + 1] = "*"
        x += 1
        check(y, x)
    if y != 0 and field[y-1][x] == ".":
        field[y - 1][x] = "*"
        y -= 1
        check(y, x)
    if y != H-1 and field[y+1][x] == ".":
        field[y + 1][x] = "*"
        y += 1
        check(y, x)


H, W = map(int, input().split())

field = []
for i in range(H):
    sub_field = []
    line = input()
    for char in line:
        sub_field.append(char)
    field.append(sub_field)

grids = []
for y in range(H):
    for x in range(W):
        if field[y][x] == "*":
            grids.append([y, x])

for grid in grids:
    y, x = grid[0], grid[1]
    if field[y][x] == "*":
        check(y,x)

for lines in field:
    for char in lines:
        print(char, end="")
    print()  # 改行に対応
