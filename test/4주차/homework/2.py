
# 연산을 하는 횟수의 최솟값을 출력한다.
# 연산의 경우의 수
    # X가 3로 나누어 떨어지면 -> 3로 나눈다.
    # X가 2로 나누어 떨어지면 -> 2로 나눈다.
    # 1을 뺀다.

# 정수 N이 주어졌을 때, 위의 연산 세 개를 사용해서 1을 만들려고 한다.


#출력
    # 첫째 줄에 연산을 하는 횟수의 최솟값을 출력
    # 둘째 줄에 N을 1로 만드는 방법에 포함되어 있는 수를 공백으로 구분해서 순서대로 출력한다.
        #정답이 여러 가지인 경우에는 아무거나 출력한다.
        
        


if (X%3==0):
    X=X/3
elif (X%2==0):
    X=X/2
    
