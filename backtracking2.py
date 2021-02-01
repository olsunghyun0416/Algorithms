# k개 중에 1개를 n번 뽑기
# visitied[] 사용

k, n = tuple(map(int, input().split()))

visited = [
    False for _ in range(k+1)
]

myList = []

def print_num(a):
    for i in range(len(a)):
        if a[i] == True:
            print(i, end=" ")
    print(end="\n")

def choose(cnt, ln):
    if cnt == n:
        print_num(visited)
        return 

    for i in range(ln+1, k+1):
        visited[i] = True
        choose(cnt + 1, ln + 1)
        visited[i] = False


for i in range(1, k+1):
    visited[i] = True
    choose(1, i)
    visited[i] = False

