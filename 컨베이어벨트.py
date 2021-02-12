# t초의 시간이 흐른 뒤 컨베이어 벨트에 놓여있는 숫자들의 상태를 출력하는 프로그램을 작성해보세요.

n ,t = input().split()

n = int(n)
t = int(t)

# 컨에비어 벨트에 숫자를 저장할 이중배열을 만든다
belt = [[0 for i in range(n)]for j in range(2)]

# 두 줄짜리 벨트이기 때문에 2번만 (1 2 3) 이런 형태로 받는다
for i in range(2):
    num = list(map(int, input().split()))
    belt[i] = num

# k가 t초의 시간 만큼 흐른다고 가정했을 때
# 벨트 위 아래로 넘어서 저장되는 숫자는 belt[0][n-1]와 belt[1][n-1]이므로
# 각각의 숫자를 tmp1과 tmp2로 저장한다.]
# i는 위의 벨트와 아래벨트만 움직여 주면 되기 때문에 2번만 돈다
# j는 위의 벨트와 아래벨트 각각 역순으로 움직이며 뒤에 저장될 숫자는 바로 그 앞에 있는 숫자다
for k in range(t):
    tmp1 = belt[0][n-1]
    tmp2 = belt[1][n-1]
    for i in range(2):
        for j in range(n-1, 0, -1):
            belt[i][j] = belt[i][j-1]
        
    # 숫자를 다 옮겨 주면 저장해둔 tmp를 맞은 위치에 저장해준다.
    belt[1][0] = tmp1
    belt[0][0] = tmp2
    
for i in range(2):
    for j in range(n):
        print(belt[i][j], end=" ")
    print(end= '\n')
