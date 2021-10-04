def find_min_idx(a):
    n = len(a)
    min_idx = a[0]
    for i in range(1, n):
        if a[i] < min_idx:
            min_idx = a[i]

    return min_idx


v = [17, 92, 18, 33, 58, 7, 33, 42]
print(find_min_idx(v))
