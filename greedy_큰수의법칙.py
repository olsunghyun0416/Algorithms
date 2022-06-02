# 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙
# 단 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없는 것이 특징

# ex) [2,4,5,4,6], M=8, k=3 -> 6+6+6+5+6+6+6+5 = 46
# ex) [3,4,3,4,3], M=7, k=2 -> 4+4+4+4+4+4+4 = 28

# 입력예시
# 5 8 3
# 2 4 5 4 6

# 출력
# 46

# 내 답안
import time 

l, m, k = map(int, input().split())
lst = list(map(int, input().split()))

start_time = time.time()

index = lst.index(max(lst))

copy_lst = lst.copy()
copy_lst[index] = min(lst)
cnt = 0
result = 0

for i in range(m):
    if cnt == k:
        result += max(copy_lst)
        cnt = 0
    else:
        result += max(lst)
        cnt += 1    

end_time = time.time()

print(result)
print("측정시간1: " , end_time - start_time)

# 예시 답안

l, m, k = map(int, input().split())
lst = list(map(int, input().split()))

start_time = time.time()

lst.sort()
first = lst[l-1]
second = lst[l-2]

cnt = int(m / (k+1)) + k
cnt += m %(k+1)

result = 0
result += cnt * first
result += (m-cnt) * second

end_time = time.time()

print(result)
print("측정시간2: " , end_time - start_time)