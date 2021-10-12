# 숫자 n개 중에서 최댓값 찾기

def find_max(i, n):
    if n == 1:
        return i[0]

    max_val = find_max(i, n-1)

    if max_val > i[n-1]:
        return max_val

    else:
        return i[n-1]

    v = [0, 1, 2, 3, 4, 5]
    print(find_max(v, len(v)))
