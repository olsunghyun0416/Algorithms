#DFS

n, m = tuple(map(int, input().split()))

visited = [
    False for _ in range(n + 1)
]

#range를 n+1로 설정
matrix = [[0 for i in range(n+1)] for j in range(n+1)]

for i in range(m):
    x, y = tuple(map(int, input().split()))
    matrix[x][y] = 1
    #이 부분
    matrix[y][x] = 1

print(matrix)
my_cnt = 0

def search(num):
    global my_cnt
    global visited

    for i in range(1, n+1):
        if matrix[num][i] and not visited[i]:
            visited[i] = True
            my_cnt += 1
            #print(i, end = " ")
            #print(num)
            search(i)

visited[1] = True
search(1)

print(my_cnt)