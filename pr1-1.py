# 숫자 n개를 리스트로 입력받아 최솟값을 구하는 프로그램

def one(n):
    m = 0
    for i in range(1, n + 1):
        m += i * i

    return m

    print(one(10))
