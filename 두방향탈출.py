#두 방향 탈출

n ,m = tuple(map(int, input().split()))

matrix = [[0 for _ in range(m)] for _ in range(n)]

visited = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    snake = list(map(int, input().split()))
    matrix[i] = snake

def in_range(x,y):
    if x >= 0 and x < m and y >= 0 and y < n:
        return True

def can_go(x,y):
    return in_range(x, y) and a[x][y] and not visited[x][y]
    
def escape(a, b):
    dxs, dys = [0, 1], [1, 0]

    for dx, dy in zip(dxs, dys):
        new_x, new_y = a+dx, b+dy

        if can_go(new_x, new_y):
            visited[new_x][new_y] = 1
            escape(new_x, new_y)


visited[0][0] = 1
escape(0, 0)

print(visited[n-1][m-1])