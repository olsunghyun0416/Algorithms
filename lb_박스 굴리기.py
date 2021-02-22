# lb_박스 굴리기

# 1~100 사이의 숫자로 구성된 n * n 크기의 격자로 이루어져 있는 박스 정보가 주어집니다. 

# 이 박스를 90' 시계방향으로 회전했을 때의 결과를 구하는 프로그램을 작성해보세요

# 입력
# 4
# 1 2 4 3         4 3 3 1
# 3 2 2 3    =>   5 1 2 2
# 3 1 6 2         4 6 2 4
# 4 5 4 4         4 2 3 3

l = int(input())

box = [
    list(map(int, input().split()))
    for _ in range(l)
]

result = []

for i in range(l):
    info = []
    for j in range(l):
        info.append(box[j][i])
    info.reverse()
    result.append(info)


for i in range(l):
    for j in range(l):
        print(result[i][j], end = " ")
    print(end = '\n')

