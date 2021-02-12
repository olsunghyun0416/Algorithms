# 두 개의 단어가 입력으로 주어질 때 
# 두 단어에 속하는 문자들의 순서를 바꾸어 
# 동일한 단어로 만들 수 있는지 여부를 출력하는 코드를 작성해보세요.

# ex)
# aba
# aab       =>     yes

# aaa
# aa        =>     no

str1 = list(input())
str2 = list(input())

str1_dic = {}
str2_dic = {}

for i in str1:
    if i not in str1_dic:
        str1_dic[i] = 1
    else:
        str1_dic[i] += 1

for i in str2:
    if i not in str2_dic:
        str2_dic[i] = 1
    else:
        str2_dic[i] += 1

if str1_dic == str2_dic:
    print("yes")
else:
    print('no')