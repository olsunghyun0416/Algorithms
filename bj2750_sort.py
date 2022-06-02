n = int(input())
lst = []


for i in range(n):
    num = int(input())
    lst.append(num)

for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i] > lst[j]:
            temp = lst[i]
            lst[i] = lst[j]
            lst[j] = temp

print(lst)