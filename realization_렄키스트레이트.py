num = input()

idx = len(num) // 2

left, right = 0, 0

for i in range(idx):
    left += int(num[i])
    right += int(num[i+idx])

if left == right:
    print('LUCKY')
else:
    print('READY')

