# 移動できるかチェック
def check(y, x,cnt,flg):

    if x != 0 and field[y][x - 1] == ".":
        field[y][x - 1] = str(cnt)
        flg = True
    if x != W - 1 and field[y][x + 1] == ".":
        field[y][x + 1] = str(cnt)
        flg = True
    if y != 0 and field[y - 1][x] == ".":
        field[y - 1][x] = str(cnt)
        flg = True
    if y != H - 1 and field[y + 1][x] == ".":
        field[y + 1][x] = str(cnt)
        flg = True
    return flg


H, W = map(int, input().split())

field = []
for i in range(H):
    sub_field = []
    line = input()
    for char in line:
        sub_field.append(char)
    field.append(sub_field)

# ※check関数に入る前にcntとcheck_numの数値は同じにすること（操作回数と2重ループを通る回数は同一のため）
cnt = 0#操作回数
check_num = 0#ループカウント（2重ループを抜けたら1カウントする）
# 陣地を増やせなくなったらループを抜ける
while True:
    flg = False
    for y in range(H):
        for x in range(W):
            # 最初の2重ループの時に通る処理
            if field[y][x] == "*":
                field[y][x] = str(check_num)
                cnt += 1
                flg = check(y, x, cnt,flg)
            #2回目以降の2重ループを通る時の処理
            elif field[y][x] == str(check_num):
                if cnt > check_num:
                    cnt -= 1
                cnt += 1
                flg = check(y, x, cnt,flg)

    check_num += 1
    # 進む場所がなくなったらループを抜ける
    if not flg:
        break
for lines in field:
    for char in lines:
        print(char, end="")
    print()  # 改行に対応
