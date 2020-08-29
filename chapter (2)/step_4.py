X, Y, N = map(int, input().split())

cnt = 0  # 進む距離をカウント
loop_cnt = 0  # 方位が2回カウントされるかチェックする変数
d_num = 1  # 同じ方位に何マス進むか
d_cnt = 0  # 方位リストをカウントする
d_list = ["E", "S", "W", "N"]  # 方位リスト
compass = d_list[0]
while True:
    # 方角が変わるまでループ
    for j in range(d_num):
        if compass == "N":
            Y -= 1
        elif compass == "W":
            X -= 1
        elif compass == "E":
            X += 1
        elif compass == "S":
            Y += 1
        cnt += 1
        # カウント変数がNと同じならループを抜ける
        if cnt == N:
            break
    else:
        d_cnt += 1
        compass = d_list[d_cnt % 4]
        loop_cnt += 1
        # 方位が2回変わったなら同じ方角で進む距離を延ばす
        if loop_cnt % 2 == 0:
            d_num += 1
        continue
    # 最初のループでbreakしたらここに飛ぶ
    break
print(X, Y)
