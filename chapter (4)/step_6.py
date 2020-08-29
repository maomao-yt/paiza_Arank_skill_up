# 移動できるかチェック
def check(y, x, flg, p, grid_p1, grid_p2):
    # プレイヤーがAの場合陣地にX、Bの場合陣地にYに置き換える
    if p == "A":
        base = "X"
    else:
        base = "Y"

    if x != 0 and field[y][x - 1] == ".":
        field[y][x - 1] = base
        flg = True
        if p == player[0]:
            grid_p1.append([y, x - 1])
        else:
            grid_p2.append([y, x - 1])

    if x != W - 1 and field[y][x + 1] == ".":
        field[y][x + 1] = base
        flg = True
        if p == player[0]:
            grid_p1.append([y, x + 1])
        else:
            grid_p2.append([y, x + 1])
    if y != 0 and field[y - 1][x] == ".":
        field[y - 1][x] = base
        flg = True
        if p == player[0]:
            grid_p1.append([y - 1, x])
        else:
            grid_p2.append([y - 1, x])
    if y != H - 1 and field[y + 1][x] == ".":
        field[y + 1][x] = base
        flg = True
        if p == player[0]:
            grid_p1.append([y + 1, x])
        else:
            grid_p2.append([y + 1, x])

    return flg, grid_p1, grid_p2


H, W = map(int, input().split())
player = [input()]
if player[0] == "A":
    player.append("B")
else:
    player.append("A")

field = []
for i in range(H):
    sub_field = []
    line = input()
    for char in line:
        sub_field.append(char)
    field.append(sub_field)

check_num = 0  # whileループカウント
flg_count = [0, 0]  # フラグ管理（2つの要素が1になったらループを抜けるようにする）
p = player[0]
grid_p1 = []
grid_p2 = []
check_grid = []
# 陣地を増やせなくなったらループを抜ける
while True:
    flg = False
    if check_num == 0 or check_num == 1:
        for y in range(H):
            for x in range(W):
                if field[y][x] == p:
                    flg, grid_p1, grid_p2 = check(y, x, flg, p, grid_p1, grid_p2)
    # 先行プレイヤーのターン
    elif p ==player[0]:
        while grid_p1:
            y, x = grid_p1.pop()
            check_grid.append([y, x])
        while check_grid:
            y, x = check_grid.pop()
            flg, grid_p1, grid_p2 = check(y, x, flg, p, grid_p1, grid_p2)
    # 後攻プレイヤーのターン
    else:
        while grid_p2:
            y, x = grid_p2.pop()
            check_grid.append([y, x])
        while check_grid:
            y, x = check_grid.pop()
            flg, grid_p1, grid_p2 = check(y, x, flg, p, grid_p1, grid_p2)

    # 陣地を増やせなくなったか確認
    if p == player[0] and flg == False:
        flg_count[0] = 1
    if p == player[1] and flg == False:
        flg_count[1] = 1

    # プレイヤーの交代
    if p == "A":
        p = "B"
    else:
        p = "A"

    check_num += 1
    # 進む場所がなくなったらループを抜ける
    if sum(flg_count) == 2:
        break

for y in range(H):
    for x in range(W):
        if field[y][x] == "X":
            field[y][x] = "A"
        elif field[y][x] == "Y":
            field[y][x] = "B"

a_count = 0
b_count = 0

for y in range(H):
    for x in range(W):
        if field[y][x] == "A":
            a_count += 1
        elif field[y][x] == "B":
            b_count += 1

print(a_count, b_count)
if a_count > b_count:
    print("A")
else:
    print("B")
