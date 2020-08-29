X, Y, N = map(int, input().split())
# 初期方向
D = "N"
for i in range(N):
    d = input()
    if D == "N":
        if d == "L":
            X -= 1
            D = "W"
        else:
            X += 1
            D = "E"
    elif D == "W":
        if d == "L":
            Y += 1
            D = "S"
        else:
            Y -= 1
            D = "N"
    elif D == "E":
        if d == "L":
            Y -= 1
            D = "N"
        else:
            Y += 1
            D = "S"
    elif D == "S":
        if d == "L":
            X += 1
            D = "E"
        else:
            X -= 1
            D = "W"
    print(X, Y)