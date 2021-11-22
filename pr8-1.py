# 일반적인 정렬 알고리즘을 사용해서 리스트 [2, 4, 5, 1, 3]을 정렬

def sel_sort(a):
    n = len(a)
    for i in range(0, n - 1):

        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j

                a[i], a[min_idx] = a[min_idx], a[i]


d = [2, 4, 5, 1, 3]
sel_sort(d)
print(d)
