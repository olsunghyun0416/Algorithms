# Basic_easy
# N개의 숫자가 주어졌을 때, 중복하여 등장하지 않는 숫자 중 최댓값을 구하는 프로그램을 작성해보세요.

#입력:
# 3
# 1 2 1

#출력: 
# 2

# 입력:
# 4
# 1 2 1 2

#출력: 
# -1
# 
##
##
##



cnt = int(input())
num = list(map(int, input().split()))

def remove_duplicate(ml):
    for i in range(len(ml)):
        seq = ml[i]
        for j in range(i+1, len(ml)):
            if seq == ml[j]:
                print(seq)
                ml[j] = -1
                ml[i] = -1
                
    
    return ml
    
result = remove_duplicate(num)
print(max(result))                


