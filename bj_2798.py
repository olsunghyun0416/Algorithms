n, m = map(int, input().split())
card = list(map(int, input().split()))

res = 100000

for i in range(n):
    for j in range(i+1, n):
        for z in range(j+1, n):
            gap = m - (card[i] + card[j] + card[z])
            if card[i] + card[j] + card[z] > m:
                pass
            else:
                if abs(gap) < abs(m - res):
                    res = card[i] + card[j] + card[z]

print(res)