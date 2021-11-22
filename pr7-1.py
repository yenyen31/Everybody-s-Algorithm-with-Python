# 찾는 값이 나오는 모든 위치를 리스트로 돌려주는 탐색 알고리즘
# 찾는 값이 없다면 빈 리스트인 []을 돌려줍니다.

def search(a, x):
    n = len(a)
    list = []
    for i in range(0, n):
        if x == a[i]:
            list.append(i)
    return list


v = [17, 92, 18, 33, 58, 7, 33, 42]
print(search(v, 18))
print(search(v, 33))
print(search(v, 900))
