# 예제 소스 p02-1-findmax.py
# 최댓값 구하기
# 입력: 숫자가 n개 들어 있는 리스트
# 출력: 숫자 n개 중 최댓값

def find_max(a):
    n = len(a)              # 입력 크기n
    max_v = a[0]            # 리스트의 첫 번째 값을 최댓값으로 기억
    for i in range(1, n):   # 1부터 n-1까지 반복
        if a[i] > max_v:    # 이번 값이 현재까지 기억된 최댓값보다 크면
            max_v = a[i]    # 최댓값을 변경
    return max_v


v = [17, 92, 18, 33, 58, 7, 33, 42]
print(find_max(v))


# 예제 소스 p02-2-findmaxidx.py
# 최댓값의 위치 구하기
# 입력: 숫자가 n개 들어 있는 리스트
# 출력: 숫자 n개 중에서 최댓값이 있는 위치(0부터 n - 1까지의 값)

def find_min_idx(a):
    n = len(a)              # 입력 크기n
    max_idx = 0             # 리스트의 0번 위치를 기억된 최댓값 위치로 기억
    for i in range(1, n):
        if a[i] > a[max_idx]:  # 이번 값이 현재까지 기억된 최댓값보다 크면
            max_idx = i       # 최댓값의 위치를 변경
        return max_idx


v = [17, 92, 18, 33, 58, 7, 33, 42]
print(find_min_idx(v))


# 연습문제 2-1
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
