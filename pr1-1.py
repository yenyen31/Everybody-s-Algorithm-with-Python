# 1부터 n까지 연속한 숫자의 제곱의 합을 구하는 프로그램을 for 반복문으로 만들기

def one(n):
    m = 0
    for i in range(1, n + 1):
        m += i * i

    return m

    print(one(10))
