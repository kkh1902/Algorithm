
# 입력 
    # 좌표 값 주어짐

# 출력
    # N개의 줄에 점을 정렬한 결과를 출력
    # x좌표가 증가하는 순으로 x좌표가 같으면 
    # y 좌표가 증가하는 순서로 정렬한 다음 출력
    # main
        # 2중 배열 인데 이중배열 우선순위에 따라 출력하라
        # 2 수를 map함수를 써서 input()하기


N = int(input('좌표의 개수를 입력하시오 : '))
myArr = []

for i in range(N):
    myArr.append(input('{}번 째 좌표를 입력하세요 : '.format(i + 1)).split()) # 이렇게 input을 받을 수 있는건가?
    
myArr.sort(key = lambda x : x[0] + x[1]) # 첫번째 좌표 부터 정렬  # 두번째 좌표 정렬

for x, y in myArr: print(x, y)

    
