N = int(input())
num_list = []
for i in range(N - 1):
    num = list(map(int, input().split()))
    num_list.append(num)

answer = [1]
while True:
    if len(answer) == N:
        break
    for num in num_list:
        if num[0] == answer[-1]:
            answer.append(num[1])
            del num
        elif num[1] == answer[-1]:
            answer.append(num[0])
            del num

for ans in answer:
    print(ans)
