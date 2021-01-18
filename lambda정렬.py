# N명의 학생에 대해 키, 몸무게 정보가 주어졌을 때, 다음의 규칙에 따라 정렬

# 학생 수를 입력 받는다
n = int(input())

# info라는 리스트 안에 입력 받은 학생 수만큼 몸무게와 키를 튜플형식으로 변환하여 저장한다
info = [
    tuple(map(int, input().split()))
    for i in range(n)
]

#result라는 변수에 info리스트에 있는 키(x[0])와 몸무게(x[1])를 앞에 
# lambda함수를 사용하고 -를 붙여 내림차순으로 정렬해준다
result = sorted(info, key = lambda x : (-x[0], -x[1]))

for i in range(len(result)):
    print("%d %d %d" %(result[i][0], result[i][1], info.index(result[i])+1))
    # 중복된 키와 몸무게가 있는 경우 앞의 인덱스가 중복해서 출력되기 때문에 
    # 이를 삭제해주어 뒤에는 나중에 입력된 학생의 정보가 나오게 한다 
    info[info.index(result[i])] = 0