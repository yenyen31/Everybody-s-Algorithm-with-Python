# pr8-1.py 프로그램을 내림차순(큰 수부터 작은 수 수서로 나열하는 방법) 정렬로 바꾸기

def sel_sort(a):
    n = len(a)
    for i in range(0, n - 1):

        min_idx = i
        for j in range(i + 1, n):
            if a[j] > a[min_idx]:
                min_idx = j

        a[i], a[min_idx] = a[min_idx], a[i]


d = [2, 4, 5, 1, 3]
sel_sort(d)
print(d)
