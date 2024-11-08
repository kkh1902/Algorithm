# 수가 주어지면 각 자리의 수를 내림차순으로 정렬
# main

    # 수가 들어가면 정렬 sort를 써야될 것 같다.
        # sort를 쓰려면 안에 list가 들어 와야한다
        # 그냥 정수를 각각의 수로 리스트를 받을 수 있나?
        # 가능하다  list(map(int, str(n)))
            # 새로운 정렬돤 리스트를 반환하는 함수 sorted 함수
            # 리스트 자체를 정렬시켜버리는 것은 sort 함수(기본 값 오름 차순)
            # sort(reverse=True) 리스트가 내림차순으로 정렬이 됩니다.
            # 정수를 리스트로 바꾸는 게 핵심 -> 해결

n= input()
a = list(map(int,str(n)))
len = len(a)
a.sort(reverse=True)
print(a)

for i in range(len):
    print(a[i], end="")
