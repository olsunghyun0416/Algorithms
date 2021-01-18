word, q = input().split()

#문자열을 바꾸는 형식을 설정할 번호를 입력하고 그 번호를 arr 리스트에 저장한다.
# 1. 가장 앞에 있는 문자를 제외한 나머지 문자를 한 칸씩 앞으로 당기고 가장 앞에 있던 문자를 가장 뒤로 옮깁니다.
# 2. 가장 뒤에 있는 문자를 제외한 나머지 문자를 한 칸씩 뒤로 밀고 가장 뒤에 있던 문자를 가장 앞으로 옮깁니다.
# 3. 문자열을 좌우로 뒤집습니다.
arr = []
for i in range(int(q)):
    num = int(input())
    arr.append(num)

# 1번에 맞는 문자열 이동을 해주는 함수이다
def first(word):
    tmp = word[0]
    word = word[1:] + tmp

    return word

# 2번에 맞는 문자열 이동을 해주는 함수이다
def second(word):
    tmp = word[-1]
    word = tmp + word[0:len(word)-1]

    return word
    
for i in arr:
    if i == 1:
        word = first(word)
        print(word)
    elif i == 2:
        word = second(word)
        print(word)
    else:
        #3번은 따로 함수를 만들지 않고 바로 뒤집어 준다.
        word = word[::-1]
        print(word)