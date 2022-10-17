num = input()

answer = 1

lst = [int(i) for i in num]

for i in lst:
    if i == 0:
        answer += i
    else:
        answer *= i

print(answer)