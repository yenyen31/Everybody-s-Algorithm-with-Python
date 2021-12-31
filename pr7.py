# 예제 소스 p07-1-search.py: 순차탐색으로 특정 값의 위치 찾기
# 리스트에서 특정 숫자의 위치 찾기
# 입력: 리스트 a,찾는 값 x
# 출력: 찾으면 그 값의 위치, 찾기 못하면 -1

def search_list(a, x):
    n = len(a)              # 입력 크기 n
    for i in range(0, n):   # 리스트 a의 모든 값을 차례로
        if x == a[i]:       # x값고 비교하여
            return i        # 같으면 위치를 돌려줍니다.

    return -1               # 끝까지 비교해도 없으면 -1 반환


v = [17, 92, 18, 33, 58, 7, 33, 42]
print(search(v, 18))        # 2(순서상 세 번째지만, 위치 번호는 2)
print(search(v, 33))        # 3(33은 리스트에 두 번 나오지만 처음 나온 위치만 출력)
print(search(v, 900))       # -1(900은 리스트에 없음)

# 연습 문제 7-1
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

# 연습 문제 7-2: 프로그램의 계산 복잡도는?
# O(n)

# 연습 문제 7-3
# 학생 번호와 이름이 리스트로 주어졌을 때 학생 번호를 입력하면 학생 번호에 해당하는 이름을 순차탐색으로 찾아 돌려주는 함수
# 해당 학생이 없으면 물음표(?)를 돌려줍니다.


def student_num(st_num, st_name, a):
    n = len(st_num)
    for i in range(0, n):
        if a == st_num[i]:
            return st_name[i]
    return "?"


st_num = [39, 14, 67, 105]
st_name = ["Justin", "John", "Mike", "Summer"]
