H, W, sy, sx, d, m = input().split()

H, W, sy, sx = int(H), int(W), int(sy), int(sx)

field = []
for i in range(H):
    sub_field = []
    lines = input()
    for char in lines:
        sub_field.append(char)
    field.append(sub_field)

if d == "N":
    if m == "L":
        if sx == 0:
            print("No")
        elif field[sy][sx - 1] == "#":
            print("No")
        else:
            print("Yes")
    else:
        if sx == W:
            print("No")
        elif field[sy][sx + 1] == "#":
            print("No")
        else:
            print("Yes")
elif d == "S":
    if m == "L":
        if sx == W:
            print("No")
        elif field[sy][sx + 1] == "#":
            print("No")
        else:
            print("Yes")
    else:
        if sx == 0:
            print("No")
        elif field[sy][sx - 1] == "#":
            print("No")
        else:
            print("Yes")
elif d == "W":
    if m == "L":
        if sy == H:
            print("No")
        elif field[sy + 1][sx] == "#":
            print("No")
        else:
            print("Yes")
    else:
        if sx == 0:
            print("No")
        elif field[sy - 1][sx] == "#":
            print("No")
        else:
            print("Yes")
elif d == "E":
    if m == "L":
        if sy == 0:
            print("No")
        elif field[sy - 1][sx] == "#":
            print("No")
        else:
            print("Yes")
    else:
        if sx == H:
            print("No")
        elif field[sy + 1][sx] == "#":
            print("No")
        else:
            print("Yes")
