# 숫자 n개를 리스트로 입력받아 최솟값을 구하는 프로그램

def find_min_idx(a):
    n = len(a)
    min_idx = a[0]
    for i in range(1, n):
        if a[i] < min_idx:
            min_idx = a[i]

    return min_idx


v = [17, 92, 18, 33, 58, 7, 33, 42]
print(find_min_idx(v))
