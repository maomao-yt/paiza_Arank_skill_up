H, W, sy, sx, N = map(int, input().split())
d = "N"

field = []
for i in range(H):
    sub_field = []
    lines = input()
    for char in lines:
        sub_field.append(char)
    field.append(sub_field)

field[sy][sx] = "*"
for i in range(N):
    m, num = input().split()
    num = int(num)
    if d == "N":
        for j in range(num):
            if m == "L":
                if sx == 0:
                    break
                elif field[sy][sx - 1] == "#":
                    break
                else:
                    sx -= 1
                    d = "W"
                    field[sy][sx] = "*"
            else:
                if sx == W:
                    break
                elif field[sy][sx + 1] == "#":
                    break
                else:
                    sx += 1
                    d = "E"
                    field[sy][sx] = "*"
        else:
            continue
        break
    elif d == "S":
        for j in range(num):
            if m == "L":
                if sx == W:
                    break
                elif field[sy][sx + 1] == "#":
                    break
                else:
                    sx += 1
                    d = "E"
                    field[sy][sx] = "*"
            else:
                if sx == 0:
                    break
                elif field[sy][sx - 1] == "#":
                    break
                else:
                    sx -= 1
                    d = "W"
                    field[sy][sx] = "*"
        else:
            continue
        break
    elif d == "W":
        for j in range(num):
            if m == "L":
                if sy == H:
                    break
                elif field[sy + 1][sx] == "#":
                    break
                else:
                    sy += 1
                    d = "S"
                    field[sy][sx] = "*"
            else:
                if sy == 0:
                    break
                elif field[sy - 1][sx] == "#":
                    break
                else:
                    sy -= 1
                    d = "N"
                    field[sy][sx] = "*"
        else:
            continue
        break
    elif d == "E":
        for j in range(num):
            if m == "L":
                if sy == 0:
                    break
                elif field[sy - 1][sx] == "#":
                    break
                else:
                    sy -= 1
                    d = "N"
                    field[sy][sx] = "*"
            else:
                if sy == H:
                    break
                elif field[sy + 1][sx] == "#":
                    break
                else:
                    sy += 1
                    d = "S"
                    field[sy][sx] = "*"
        else:
            continue
        break
# マップの表示
for lines in field:
    for chars in lines:
        print(chars, end="")
    print()
