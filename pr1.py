# 예제 소스 p01-1-sum.py: 1부터 n까지 연속한 숫자의 합을 구하는 알고리즘 1
# 입력: n
# 출력: 1부터 n까지의 숫자를 더한 값

def sum_n(n):
    s = 0                       # 합을 계산할 변수
    for i in range(1, n + 1):   # 1부터 n까지 반복(n + 1은 제외)
        s = s + i

        return s


print(sum_n(10))                # 1부터 10까지의 합
print(sum_n(100))               # 1부터 100까지의 합


# 예제 소스 p01-2-sum.py: 1부터 n까지 연속한 숫자의 합을 구하는 알고리즘 2
# 입력: n
# 출력: 1부터 n까지의 숫자를 더한 값

def sum_n(n):
    return n * (n + 1) // 2


print(sum_n(10))
print(sum_n(100))


# 연습문제 1-1
# 1부터 n까지 연속한 숫자의 제곱의 합을 구하는 프로그램을 for 반복문으로 만들기

def one(n):
    m = 0
    for i in range(1, n + 1):
        m += i * i

    return m

    print(one(10))


# 연습문제 1-2
O(n)

# 연습문제 1-3
O(1)
