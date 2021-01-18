# 지그재그 숫자 채우기
# n * m크기의 직사각형에 숫자를 0부터 순서대로 1씩 증가시키며 
# 왼쪽 위에서부터 시작하여 다음과 같이 지그재그 모양으로 숫자들을 쭉 채우는 코드를 작성

n,m = input().split()

n = int(n)
m = int(m)

# 지그재그로 숫자를 넣어줄 이중 배열을 만들어준다
# ex) n = 4, m = 2
# ㅁ ㅁ
# ㅁ ㅁ
# ㅁ ㅁ
# ㅁ ㅁ
square = [[ 0 for _ in range(m)] for _ in range(n)]

#이중배열을 원하는 순서에 맞게 들어갈 변수를 설정한다
cnt = 0

# m값이 0으로 고정적일 동안 n값은 0부터 m-1까지 cnt를 증가시키면서
# 배열의 값을 채워준다 
for i in range(m):
    if i % 2 == 0:
        for j in range(n):
            square[j][i] = cnt
            cnt += 1
    else:
        for j in range(n-1, -1, -1):
            square[j][i] = cnt
            cnt += 1

# 각 줄에 맞게 출력을 해준다
for i in range(n):
    for j in range(m):
        print(square[i][j], end = " ")
    print(end = '\n')