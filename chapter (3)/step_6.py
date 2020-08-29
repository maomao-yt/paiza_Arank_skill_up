# 次の方角を決める処理
def compass_judge(d, m):
    if (d == "N" and m == "L") or (d == "S" and m == "R"):
        compass = "W"
    elif (d == "N" and m == "R") or (d == "S" and m == "L"):
        compass = "E"
    elif (d == "W" and m == "L") or (d == "E" and m == "R"):
        compass = "S"
    else:
        compass = "N"
    return compass


H, W, sy, sx, N = map(int, input().split())
d = "N"

field = []
for i in range(H):
    sub_field = []
    lines = input()
    for char in lines:
        sub_field.append(char)
    field.append(sub_field)

num_list = []
m_list = []
for i in range(N):
    num, m = input().split()
    num_list.append(int(num))
    m_list.append(m)

for i in range(N + 1):
    # 同じ方角に何マス進むかを決める
    if i == N:
        num = 100 - num_list[i - 1]
    else:
        num, m = num_list[i], m_list[i]
        if i != 0:
            num = num - num_list[i - 1]
    # 方角（d）に向かってnum数進む
    if d == "N":
        for j in range(num):
            if sy == 0:
                print("Stop")
                break
            elif field[sy - 1][sx] == "#":
                print("Stop")
                break
            else:
                sy -= 1
                print(sy, sx)
        else:
            d = compass_judge(d, m)
            continue
        break
    elif d == "S":
        for j in range(num):
            if sy == H - 1:
                print("Stop")
                break
            elif field[sy + 1][sx] == "#":
                print("Stop")
                break
            else:
                sy += 1
                print(sy, sx)
        else:
            d = compass_judge(d, m)
            continue
        break
    elif d == "W":
        for j in range(num):
            if sx == 0:
                print("Stop")
                break
            elif field[sy][sx - 1] == "#":
                print("Stop")
                break
            else:
                sx -= 1
                print(sy, sx)
        else:
            d = compass_judge(d, m)
            continue
        break
    elif d == "E":
        for j in range(num):
            if sx == W - 1:
                print("Stop")
                break
            elif field[sy][sx + 1] == "#":
                print("Stop")
                break
            else:
                sx += 1
                print(sy, sx)
        else:
            d = compass_judge(d, m)
            continue
        break
