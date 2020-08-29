H, W, sy, sx, m = input().split()

H, W, sy, sx = int(H), int(W), int(sy), int(sx)

field = []
for i in range(H):
    sub_field = []
    lines = input()
    for char in lines:
        sub_field.append(char)
    field.append(sub_field)

if m == "N":
    if sy == 0:
        print("No")
    elif field[sy - 1][sx] == "#":
        print("No")
    else:
        print("Yes")
elif m == "S":
    if sy == H:
        print("No")
    elif field[sy + 1][sx] == "#":
        print("No")
    else:
        print("Yes")
elif m == "W":
    if sx == 0:
        print("No")
    elif field[sy][sx - 1] == "#":
        print("No")
    else:
        print("Yes")
elif m == "E":
    if sx == W:
        print("No")
    elif field[sy][sx + 1] == "#":
        print("No")
    else:
        print("Yes")
