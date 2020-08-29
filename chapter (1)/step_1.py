H, W, N = map(int, input().split())
field = []

# 盤面の作成
for i in range(H):
    sub_field = []
    line = input()
    for char in line:
        sub_field.append(char)
    field.append(sub_field)

# 入力された位置情報を基に盤面の情報を取り出す。
for i in range(N):
    y, x = map(int, input().split())
    print(field[y][x])
