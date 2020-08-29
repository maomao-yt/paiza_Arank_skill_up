H, W = map(int, input().split())
field = []

# 盤面の作成
for i in range(H):
    sub_field = []
    line = input()
    for char in line:
        sub_field.append(char)
    field.append(sub_field)

# 盤面の上下に"#"があるかチェック（端の場合はどちらかにあればいい）
for y in range(H):
    for x in range(W):
        # 上端の場合
        if y == 0:
            if field[y + 1][x] == "#":
                print(y, x)
            continue
        # 下端の場合
        elif y == H - 1:
            if field[y - 1][x] == "#":
                print(y, x)
            continue

        # 上下が"#"の場合
        elif field[y + 1][x] == "#" and field[y - 1][x] == "#":
            print(y, x)
