import math
N =int(input())

def calc(n):
    if n <= 1:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for i in range(3, math.ceil(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False

    return True

ans =calc(N)
if ans:
    print("YES")
else:
    print("NO")



