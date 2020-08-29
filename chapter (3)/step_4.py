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
    m,num = input().split()
    num =int(num)
    if d == "N":
        for j in range(num):
            if m == "L":
                if sx == 0:
                    print(sy, sx)
                    print("Stop")
                    break
                elif field[sy][sx - 1] == "#":
                    print(sy, sx)
                    print("Stop")
                    break
                else:
                    sx -= 1
                    d = "W"

            else:
                if sx == W:
                    print(sy, sx)
                    print("Stop")
                    break
                elif field[sy][sx + 1] == "#":
                    print(sy, sx)
                    print("Stop")
                    break
                else:
                    sx += 1
                    d = "E"
        else:
            print(sy, sx)
            continue
        break
    elif d == "S":
        for j in range(num):
            if m == "L":
                if sx == W:
                    print(sy, sx)
                    print("Stop")
                    break
                elif field[sy][sx + 1] == "#":
                    print(sy, sx)
                    print("Stop")
                    break
                else:
                    sx += 1
                    d = "E"

            else:
                if sx == 0:
                    print(sy, sx)
                    print("Stop")
                    break
                elif field[sy][sx - 1] == "#":
                    print(sy, sx)
                    print("Stop")
                    break
                else:
                    sx -= 1
                    d = "W"
        else:
            print(sy, sx)
            continue
        break
    elif d == "W":
        for j in range(num):
            if m == "L":
                if sy == H:
                    print(sy, sx)
                    print("Stop")
                    break
                elif field[sy + 1][sx] == "#":
                    print(sy, sx)
                    print("Stop")
                    break
                else:
                    sy += 1
                    d = "S"

            else:
                if sy == 0:
                    print(sy, sx)
                    print("Stop")
                    break
                elif field[sy - 1][sx] == "#":
                    print(sy, sx)
                    print("Stop")
                    break
                else:
                    sy -= 1
                    d = "N"
        else:
            print(sy, sx)
            continue
        break
    elif d == "E":
        for j in range(num):
            if m == "L":
                if sy == 0:
                    print(sy, sx)
                    print("Stop")
                    break
                elif field[sy - 1][sx] == "#":
                    print(sy, sx)
                    print("Stop")
                    break
                else:
                    sy -= 1
                    d = "N"

            else:
                if sy == H:
                    print(sy, sx)
                    print("Stop")
                    break
                elif field[sy + 1][sx] == "#":
                    print(sy, sx)
                    print("Stop")
                    break
                else:
                    sy += 1
                    d = "S"

        else:
            print(sy, sx)
            continue
        break
