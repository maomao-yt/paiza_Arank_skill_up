N = int(input())
num_list = []
for i in range(N - 1):
    num = list(map(int, input().split()))
    num_list.append(num)

apple_num =[]
for i in range(N):
    apple_num.append(int(input()))

answer = [1]
cnt = apple_num[0]
print(cnt)
while True:
    if len(answer) == N:
        break
    for num in num_list:
        if num[0] == answer[-1]:
            answer.append(num[1])
            cnt += apple_num[num[1]-1]
            print(cnt)
            del num
        elif num[1] == answer[-1]:
            answer.append(num[0])
            cnt += apple_num[num[0] - 1]
            print(cnt)
            del num


