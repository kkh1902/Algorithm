# 회원들 정보를 받아서 나이 순으로 출력하라
# 나이가 같으면 가입한 순으로 한 줄에 한 명 씩 나이와 이름을 공백으로 구분 출력


# main
    # 나이를 정렬 
    # 첫째줄에 testcase개수
    # 2차원 list 로 받는다
    # list의 인덱스[0] 값을 우선순위로 구별한다
        # main 전체다 어떻게 우선순위를 구별할까?
            # if a[0]같으면 조건 걸어보면 우선순위 구할수 있을까?


N = int(input('회원의 수를 입력하세요 : '))
myArr = []
for i in range(N):
    age, name = input('{}번 째 회원의 나이와 이름을 입력하세요 : '.format(i + 1)).split() # 이렇게 input을 받을 수 있는건가?
    myArr.append([int(age), name])
myArr.sort(key = lambda x : x[0])
print(myArr)
for age, name in myArr: print(age, name)
