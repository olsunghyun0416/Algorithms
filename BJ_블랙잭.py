# 첫째 줄에 카드의 개수 N(3 ≤ N ≤ 100)과 M(10 ≤ M ≤ 300,000)이 주어진다. 
# 둘째 줄에는 카드에 쓰여 있는 수가 주어지며, 이 값은 100,000을 넘지 않는 양의 정수이다.
# 합이 M을 넘지 않는 카드 3장을 찾을 수 있는 경우만 입력으로 주어진다.
import sys

n,m = input().split()

n = int(n)
m = int(m)

card = input().split()

for i in range(n):
    card[i] = int(card[i])

min = sys.maxsize

for i in range(n-2):
    for j in range(i+1, n-1):
        for z in range(j+1, n):
            sum = card[i] + card[j] + card[z]
            if sum - m == 0:
                min = sum
                break
            else:
                if abs(m - min) > abs(m - sum):
                    min = sum
                
print(min)