from sympy import Q


N, M = list(map(int, input().split()))
ball = list(map(int, input().split()))

answer = 0

for i in range(len(ball)-1):
    for j in range(i+1, len(ball)):
        if ball[i] == ball[j]:
            pass
        else:
            answer += 1

print(answer)