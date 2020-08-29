H, W, N = map(int, input().split())
field = []

# 盤面の作成
for i in range(H):
    sub_field = []
    line = input()
    for char in line:
        sub_field.append(char)
    field.append(sub_field)

# 入力された位置の盤面を"#"に変換。
for i in range(N):
    y, x = map(int, input().split())
    field[y][x] = "#"

# 盤面の出力
for lines in field:
    for char in lines:
        print(char, end="")
    print()  # 改行に対応
