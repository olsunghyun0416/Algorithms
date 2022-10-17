s = input()

cnt0 = 0
cnt1 = 0
s = '2' + s
before = s[0]

for i in s[1:]:
    if before != i and i == "0":
        cnt0 += 1
        before=i
    elif before != i and i == "1":
        cnt1 += 1
        before=i

print(min(cnt0, cnt1))