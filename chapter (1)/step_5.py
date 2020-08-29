H, W = map(int, input().split())
field = []

# 盤面の作成
for i in range(H):
    sub_field = []
    line = input()
    for char in line:
        sub_field.append(char)
    field.append(sub_field)

for y in range(H):
    for x in range(W):
        # 上端の場合
        if y == 0:
            if field[y + 1][x] == "#":
                if x == 0:
                    if field[y][x + 1] == "#":
                        print(y, x)
                        continue
                elif x == W - 1:
                    if field[y][x - 1] == "#":
                        print(y, x)
                        continue
                elif field[y][x + 1] == "#" and field[y][x - 1] == "#":
                    print(y, x)
                    continue
            continue
        # 下端の場合
        elif y == H - 1:
            if field[y - 1][x] == "#":
                if x == 0:
                    if field[y][x + 1] == "#":
                        print(y, x)
                        continue
                elif x == W - 1:
                    if field[y][x - 1] == "#":
                        print(y, x)
                        continue
                elif field[y][x + 1] == "#" and field[y][x - 1] == "#":
                    print(y, x)
                    continue
            continue

        # 左端の場合
        elif x == 0:
            if field[y][x + 1] == "#" and field[y + 1][x] == "#" and field[y - 1][x] == "#":
                print(y, x)
            continue

        # 右端の場合
        elif x == W - 1:
            if field[y][x - 1] == "#" and field[y + 1][x] == "#" and field[y - 1][x] == "#":
                print(y, x)
            continue

        # 上下左右が"#"の場合
        elif field[y + 1][x] == "#" and field[y - 1][x] == "#" and field[y][x + 1] == "#" and field[y][x - 1] == "#":
            print(y, x)
