N = int(input())
p = list(map(int, input().split()))

p.sort()

cnt = 0
result = 0

for i in p:
    cnt += 1
    if cnt >= i:
        result += 1
        cnt = 0 

print(result)