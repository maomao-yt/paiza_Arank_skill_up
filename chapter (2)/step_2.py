Y, X, N = map(int, input().split())

for i in range(N):
    compass =input()
    if compass == "N":
        Y -= 1
    elif compass =="W":
        X -= 1
    elif compass == "E":
        X += 1
    elif compass == "S":
        Y += 1
    print(Y, X)
