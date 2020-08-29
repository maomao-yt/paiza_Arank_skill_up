Y, X, D = input().split()
Y,X = int(Y),int(X)

d = input()
if D == "N":
    if d == "L":
        X -= 1
    else:
        X += 1

elif D == "W":
    if d == "L":
        Y += 1
    else:
        Y -= 1

elif D == "E":
    if d == "L":
        Y -= 1
    else:
        Y += 1

elif D == "S":
    if d == "L":
        X += 1
    else:
        X -= 1
print(Y, X)
