import sys

min = sys.maxsize

num = int(input())
arr = input().split()

for i in range(len(arr)):
    arr[i] = int(arr[i])

for i in range(len(arr)):
    if min > arr[i]:
        min = arr[i]

print(min, end = " ")
print(arr.count(min))