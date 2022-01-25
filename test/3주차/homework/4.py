# 알파벳 정렬 문제
# 입력
    # 첫째줄에 testcase 개수
    # 둘째줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 하나씩 주어짐 
    # 주어진 문자열의 길이는 50을 넘지 않는다.
# 출력
    # 조건에 따라 정렬 출력
    # 단 같은 단어가 여러 번 입력 된 경우 한번만 출력
# main
    # 조건 (우선순위)
        # 길이가 짧은 것부터
        # 길이가 같으면 사전 순으로
        # 예외 -> 같은거면 한번 만 출력 -> set 함수 집합 한개로 만들어 놓고 시작
            # set을 사용하면 반복은 없어지나 순서가 엉킴
            # 그래서 먼저 set 반복 없애기


N = int(input('단어의 개수를 입력하시오 : '))
myArr = []

for i in range(N):
    word = input('{}번 째 단어를을 입력하세요 : '.format(i + 1)) # 이렇게 input을 받을 수 있는건가?
    myArr.append(word)
myArr.sort(key = lambda x : x) # 사전 순으로 정렬
myArr.sort(key = lambda x : len(x))  # 길이가 짧은 것부터
set(myArr)

for word in myArr: print(word)
