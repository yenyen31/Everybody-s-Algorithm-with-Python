# 예제 소스 05-1-gcd.py : 최대 공약수를 구하는 알고리즘
# 최대 공약수 구하기
# 입력: a,b
# 출력: a와 b의 최대공약수

def gcd(a, b):
    i = min(a, b)  # 두 수 중에서 최솟값을 구하는 파이썬 함수
    while True:
        if a % i == 0 and b % i == 0:
            return i
        i = i - 1  # i를 1만큼 감소시킴


print(gcd(1, 5))  # 1
print(gcd(3, 6))  # 3
print(gcd(60, 24))  # 12
print(gcd(81, 27))  # 27

# 예제 소스: p05-2-gcd.py : 유클리드 방식을 이용해 최대공약수를 구하는 알고리즘
# 최대 공약수 구하기
# 입력: a,b
# 출력: a와 b의 최대공약수


def gcd(a, b):
    if b == 0:    # 종료 조건
        return a
        return gcd(b, a % b)  # 좀 더 작은 값으로 자기 자신을 호출


print(gcd(1, 5))  # 1
print(gcd(3, 6))  # 3
print(gcd(60, 24))  # 12
print(gcd(81, 27))  # 27


# 연습 문제 5-1
# 0과 1부터 시작해서 바로 앞의 두 수를 더한 값으로 추가하는 방식으로 만든 수열을 피보나치 수열이라고 한다.
# 피보나치 수열이 리스트처럼 0번부터 시작한다고 가정할 때 n번째 피보나치 수열을 구하는 알고리즘을 재귀호출을 이용해 구하기


def fibo(n):
    if n <= 1:
        return n

    return fibo(n-2) + fibo(n-1)


print("n까지의 합:", fibo(10))
