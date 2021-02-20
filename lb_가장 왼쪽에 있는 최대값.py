# lb_가장 왼쪽에 있는 최대값

# N개의 숫자가 주어졌을 때, 주어진 숫자들 중 최댓값의 위치를 출력합니다. 

# 만약 최댓값이 여러 개라면, 가장 왼쪽에 있는 최댓값의 위치를 출력합니다.

#그 이후에는 위에서 구한 최댓값의 위치보다 더 왼쪽에 있는 숫자들 중 최댓값을 구해 그 위치를 출력합니다. 

# 이 경우에도 최댓값이 여러 개라면, 가장 왼쪽에 있는 최댓값의 위치를 출력합니다.

# 위의 과정을 끊임없이 반복하며, 최종적으로 첫 번째 원소가 뽑히게 되면 이 과정을 종료합니다. 

# 이러한 과정을 거쳐 구해진 최댓값의 위치들을 출력하는 프로그램을 작성해보세요.

# 입력:
# 5
# 3 3 5 4 5

# 출력: 
# 3 1

cnt = int(input())
ml = list(map(int, input().split()))
result = []

def max_index(a, b, ml):
    global result

    this_ml = ml[a:b]
    num = max(this_ml)
    result.append(ml.index(num)+ 1)
    
    if ml.index(num) == 0:
        return 0

    return max_index(0, ml.index(num), this_ml)



max_index(0, len(ml), ml)

for i in range(len(result)):
    print(result[i], end = " ")