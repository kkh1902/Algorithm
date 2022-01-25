# N개의 수가 주어 졌을 때, 이를 오름차순으로 정렬하는 프로그램 작성
# main
    # 오름차순 정렬
    # 처음 test case 개수 -> for 반복문 testcase만큼하면 되겠지?
    # 빈리스트 초기화하고 리스트에 append한다음 정렬해서 하나씩 출력
    # 출력
        # 하나 씩 , end="" 할필요



N= int(input())
a=[]

for i in range(N):
    a.append(int(input()))

a.sort()

for i in range(N):
    print(a[i])
