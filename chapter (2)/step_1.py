n, m = map(int,input().split())

field =[]
for i in range(n):
    line = input()
    sub_field = []
    for char in line:
        sub_field.append(char)
    field.append(sub_field)
for y in range(n):
    for x in range(m):
        if field[y][x] == "#":
            print(y, x)
