# 예제 소스 p03-1-samename.py : 동명이인을 찾는 알고리즘
# 두 번 이상 나온 이름 찾기
# 입력: 이름이 n개 들어 있는 리스트
# 출력: 이름 n개 중 반복되는 이름의 집합

def find_same_name(a):
    n = len(a)
    result = set()
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if a[i] == a[j]:
                result.add(a[i])
    return result


name = ["Tom", "Jerry", "Mike", "Tom"]
print(find_same_name(name))


# 연습문제 3-1
# n명 중 두 명을 뽑아 짝을 짓는다고 할 떄 짝을 지을 수 있는 모든 조합을 출력하는 알고리즘

def bf(a):
    n = len(a)
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            print(a[i], " - ", a[j])


name = ["Tom", "Jerry", "Mike"]
bf(name)

# 연습문제 3-2
# A O(1)
# B O(n)
# C O(n**2)
# D O(n**3)
