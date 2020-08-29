H, W = map(int, input().split())
field = []

# 盤面の作成
for i in range(H):
    sub_field = []
    line = input()
    for char in line:
        sub_field.append(char)
    field.append(sub_field)

# 盤面の左右に"#"があるかチェック（端の場合はどちらかにあればいい）
for y in range(H):
    for x in range(W):
        # 左端の場合
        if x == 0:
            if field[y][x + 1] == "#":
                print(y, x)
            continue
        # 右端の場合
        elif x == W - 1:
            if field[y][x - 1] == "#":
                print(y, x)
            continue
        # 左右が"#"の場合
        elif field[y][x - 1] == "#" and field[y][x + 1] == "#":
            print(y, x)
