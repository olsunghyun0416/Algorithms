# k개 중에 1개를 n번 뽑기

k, n = input().split()

k = int(k)
n = int(n)

myList = []

def choose(cnt):
    if cnt == n:
        for i in range(len(myList)):
            print(myList[i], end = " ")
        print(end = "\n")

        return 
    
    for i in range(cnt+1,k+1):
        if len(myList) > 0 and myList[-1] >= i:
            pass
        else:
            myList.append(i)
            choose(cnt+1)
            myList.pop()
choose(0)
