# 예제 소스 p10-1 : 병합 정렬로 줄 세우는 알고리즘
# 쉽게 설명한 병합 정렬
# 입력: 리스트 a
# 출력: 정렬된 새 리스트

def marge_sort(a):
    n = len(a)
    # 종료 조건: 정렬할 리스트의 자료 개수가 한 개 이하이면 정렬할 필요 없음
    if n <= 1:
        return a
    # 그룹을 나누어 각각 병합 정렬을 호출하는 과정
    mid = n // 2               # 중간을 기분으로 두 그룹으로 나눔
    g1 = merge_sort(a[:mid])   # 재귀 호출로 첫 번째 그룹을 정렬
    g2 = marge_sort(a[mid:])   # 재귀 호출로 두 번째 그룹을 정렬

    # 두 그룹을 하나로 병합
    result = []                # 두 그룹을 합쳐 만들 최종 결과
    while g1 and g2:           # 두 그룹에 모두 자료가 남아 있는 동안 반복
        if g1[0] < g2[0]:      # 두 그룹의 맨 앞 자료 값을 비교
            # g1 값이 더 작으면 그 값을 빼내어 결과로 추가
            result.append(g1.pop(0))
        else:
            # g2 값이 더 작으면 그 값을 빼내어 결과로 추가
            result.append(g1.pop(0))
        # 아직 남아 있는 자료들을 결과에 추가
        # g1과 g2 중 이미 빈 것은 while을 바로 지나감
        while g1:
            result.append(g1.pop(0))
        while g2:
            result.append(g2.pop(0))
        return result


d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
print(marge_sort(d))


# 예제 소스  p10-2 : 일반적인 병합 정렬 알고리즘 : p10-1과 정렬 원리는 같지만. return값이 없고 입력 리스트 안에 자료 순서를 직접 바꿈
# 병합 정렬
# 입력: 리스트 a
# 출력: 없음(입력으로 주어진 a가 정렬됨)

def merge_sort(a):
    n = len(a)
    # 종료조건: 정렬할 리스트의 자료 개수가 한 개 이하이면 정렬할 필요가 없음

    if n <= 1:
        return
    # 그룹을 나누어 각각 병합 정렬을 호출하는 과정
    mid = n // 2   # 중간을 기준으로 두 그룹으로 나눔
    g1 = a[:mid]
    g2 = a[mid:]
    merge_sort(g1)  # 재귀 호출로 첫 번째 그룹을 정렬
    merge_sort(g2)  # 재귀 호출로 두 번째 그룹을 정렬
    # 두 그룹을 하나로 병합

    i1 = 0
    i2 = 0
    ia = 0
    while i1 < len(g1) and i2 < len(g2):
        if g1[i1] < g2[i2]:
            a[ia] = g1[i1]
            i1 += 1
            ia += 1
        else:
            a[ia] = g2[i2]
            i2 += 1
            ia += 1
        # 아직 남아 있는 자료들을 결과에 추가
    while i1 < len(g1):
        a[ia] = g1[i1]
        i1 += 1
        ia += 1

    while i2 < len(g2):
        a[ia] = g2[i2]
        i2 += 1
        ia += 1


d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
merge_sort(d)
print(d)


# 연습문제 10-1 : 프로그램 10-2에서 오름차순 정렬을 내림차순으로 변경

def merge_sort(a):
    n = len(a)
    # 종료조건: 정렬할 리스트의 자료 개수가 한 개 이하이면 정렬할 필요가 없음

    if n <= 1:
        return
    # 그룹을 나누어 각각 병합 정렬을 호출하는 과정
    mid = n // 2   # 중간을 기준으로 두 그룹으로 나눔
    g1 = a[:mid]
    g2 = a[mid:]
    merge_sort(g1)  # 재귀 호출로 첫 번째 그룹을 정렬
    merge_sort(g2)  # 재귀 호출로 두 번째 그룹을 정렬
    # 두 그룹을 하나로 병합

    i1 = 0
    i2 = 0
    ia = 0
    while i1 < len(g1) and i2 < len(g2):
        if g1[i1] > g2[i2]:
            a[ia] = g1[i1]
            i1 += 1
            ia += 1
        else:
            a[ia] = g2[i2]
            i2 += 1
            ia += 1
        # 아직 남아 있는 자료들을 결과에 추가
    while i1 < len(g1):
        a[ia] = g1[i1]
        i1 += 1
        ia += 1

    while i2 < len(g2):
        a[ia] = g2[i2]
        i2 += 1
        ia += 1


d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
merge_sort(d)
print(d)
