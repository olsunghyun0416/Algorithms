# 1차원 젠가

n = int(input())

# 숫자가 들어온 것을 저장하는 리스트
block = []

# 삭제할 숫자의 범위를 담을 리스트 (ex 2 4, 2 2)
bomb = []

for i in range(n):
    num = int(input())
    block.append(num)

for i in range(2):
    num = list(map(int, input().split()))
    bomb.append(num)

# 숫자를 삭제하는 것은 2번만 시행하므로 i가 두 번 도는 동안
# 삭제하는 범위를 제외한 부분을 슬라이싱하여 block에 저장한다
for i in range(2):
    block = block[0:bomb[i][0]-1] + block[bomb[i][1]:]

print(len(block))
for i in range(len(block)):
    print(block[i])