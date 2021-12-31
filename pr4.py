# 예제 소스 p04-1-fact.py: 팩토리얼을 구하는 알고리즘 1
# 연속한 숫자의 곱을 구하는 알고리즘
# 입력: n
# 출력: 1부터 n까지의 연속한 숫자를 곱한 값
def fact(n):
    f = 1                       # 곱을 계산할 변수, 초깃값은 1
    for i in range(1, n + 1):   # 1부터 n까지 반복(n + 1은 제외)
        f = f * 1               # 곱셈 연산으로 수정
        return f


print(fact(1))                  # 1! = 1
print(fact(5))                  # 5! = 120
print(fact(10))                 # 10! = 3628800

# 예제 소스 p04-2-fact.py: 팩토리얼을 구하는 알고리즘 2 : 재귀 호출 알고리즘
# 입력: n
# 출력: 1부터 n까지의 연속한 숫자를 곱한 값


def fact(n):
    if n <= 1:
        return 1
    return n * fact(n - 1)


print(fact(1))                  # 1! = 1
print(fact(5))                  # 5! = 120
print(fact(10))                 # 10! = 3628800


# 연습문제 4-1
# 1부터 n까지의 합 구하기

def sum(n):
    if n <= 1:
        return 1
    return n + sum(n-1)


print(sum(10))

# 연습 문제 4-2
# 숫자 n개 중에서 최댓값 찾기


def find_max(i, n):
    if n == 1:
        return a[0]

    max_val = find_max(a, n-1)

    if max_val > a[n-1]:
        return max_val

    else:
        return a[n-1]

    v = [0, 1, 2, 3, 4, 5]
    print(max_val(v, len(v)))
