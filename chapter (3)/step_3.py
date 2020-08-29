H, W, sy, sx, N = map(int, input().split())
d = "N"

field = []
for i in range(H):
    sub_field = []
    lines = input()
    for char in lines:
        sub_field.append(char)
    field.append(sub_field)

for i in range(N):
    m = input()
    if d == "N":
        if m == "L":
            if sx == 0:
                print("Stop")
                break
            elif field[sy][sx - 1] == "#":
                print("Stop")
                break
            else:
                sx -= 1
                d = "W"
                print(sy, sx)
        else:
            if sx == W:
                print("Stop")
                break
            elif field[sy][sx + 1] == "#":
                print("Stop")
                break
            else:
                sx += 1
                d = "E"
                print(sy, sx)
    elif d == "S":
        if m == "L":
            if sx == W:
                print("Stop")
                break
            elif field[sy][sx + 1] == "#":
                print("Stop")
                break
            else:
                sx += 1
                d = "E"
                print(sy, sx)
        else:
            if sx == 0:
                print("Stop")
                break
            elif field[sy][sx - 1] == "#":
                print("Stop")
                break
            else:
                sx -= 1
                d = "W"
                print(sy, sx)
    elif d == "W":
        if m == "L":
            if sy == H:
                print("Stop")
                break
            elif field[sy + 1][sx] == "#":
                print("Stop")
                break
            else:
                sy += 1
                d = "S"
                print(sy, sx)
        else:
            if sy == 0:
                print("Stop")
                break
            elif field[sy - 1][sx] == "#":
                print("Stop")
                break
            else:
                sy -= 1
                d = "N"
                print(sy, sx)
    elif d == "E":
        if m == "L":
            if sy == 0:
                print("Stop")
                break
            elif field[sy - 1][sx] == "#":
                print("Stop")
                break
            else:
                sy -= 1
                d = "N"
                print(sy, sx)
        else:
            if sy == H:
                print("Stop")
                break
            elif field[sy + 1][sx] == "#":
                print("Stop")
                break
            else:
                sy += 1
                d = "S"
                print(sy, sx)
