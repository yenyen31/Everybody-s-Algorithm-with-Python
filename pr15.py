# 예제 소스 15-1.py
# 주어진 친구 관계 그래프에서 모든 친구를 찾는 알고리즘

# 친구 리스트에서 자신의 모든 친구를 찾는 알고리즘
# 입력: 친구 관계 그래프 g, 모든 친구를 찾을 자신 start
# 출력: 모든 친구의 이름

def print_all_friends(g, start):
    qu = []     # 기억 장소 1: 앞으로 처리해야 할 사람들을 큐에 저장
    gone = set()    # 기억 장소 2: 이미 큐에 추가한 사람들을 집합에 기록(중복 방지)

    qu.append(start)    # 자신을 큐에 넣고 시작
    done.add(start)     # 집합에도 추기

    while qu:           # 큐에 처리할 사람이 남아 있는 동안
        p = qu.pop(0)   # 큐에서 처리 대상을 한 명 꺼내
        print(p)        # 이름을 출력하고
        for x in g[p]:  # 그의 친구들 중에
            if x not in done:       # 아직 큐에 추가된 적인 없는 사람을
                qu.append(x)        # 큐에 추가하고
                done.add(x)         # 집합에도 추가


# 친구 관계 리스트
# A와 B가 친구이면
# A의 친구 리스트에도 B가 나오고, B의 친구 리스트에도 A가 나옴
fr_info = {
    'Summer': ['John', "Justin", "Mike"],
    "John": ["Summer", "Justin"],
    "Justin": ["John", "Summer", "Mike", "May"],
    "Mike": ["Summer", "Justin"],
    "May": ["Justin", "Kim"],
    "Kim": ["May"],
    "Tom": ["Jerry"],
    "Jerry": ["Tom"]
}

print_all_friends(fr_info, "Summer")
print()
print_all_friends(fr_info, "Jerry")


# 예제 소스 15-2.py
# 친구 리스트에서 자신이 모든 친구를 찾고 친구들의 친밀도를 계산하는 알고리즘
# 입력: 친구 관계 그래프 g, 모든 친구를 찾을 자신 start
# 출력: 모든 친구의 이름과 자신과의 친밀도

def print_all_friends(g, start):
    qu = []         # 기억장소 1: 앞으로 처리해야 할 (사람 이름, 친밀도) 튜플 큐에 저장
    done = set()    # 기억 장소 2: 이미 큐에 추가한 사람을 집합에 기록(중복 방지)

    qu.append((start, 0))  # (사람 이름, 친밀도) 정보를 하나의 튜플로 묶어 처리
    # 자기 자신의 친밀도: 0
    done.add(start)        # 집합에도 추가

    while qu:           # 큐에 처리할 사람이 남아 있는 동안
        (p, d) = qu.pop(0)  # 큐에서 (사람 이름, 친밀도) 정보를 p와 d로 각각 꺼냄
        print(p, d)         # 사람 이름과 친밀도를 출력
        for x in g[p]:      # 친구들 중에
            if x not in done:  # 아직 큐에 추가된 적이 없는 사람을
                qu.append((x, d + 1))  # 친밀도를 1증가시켜 큐에 추가하고
                done.add(x)            # 집합에도 추가


fr_info = {
    'Summer': ['John', "Justin", "Mike"],
    "John": ["Summer", "Justin"],
    "Justin": ["John", "Summer", "Mike", "May"],
    "Mike": ["Summer", "Justin"],
    "May": ["Justin", "Kim"],
    "Kim": ["May"],
    "Tom": ["Jerry"],
    "Jerry": ["Tom"]

}

print_all_friends(fr_info, "Summer")
print()
print_all_friends(fr_info, "Jerry")


# 연습 문제 15-1.py
# 너비 우선 탐색

# 그래프 탐색: 너비 우선 탐색
# 입력: 그래프 a, 탐색 시작점 start
# 출력: start에서 출발해 연결된 꼭짓점들을 출력

def bfs(g, start):
    qu = []         # 기억 장소1: 앞으로 처리해야 할 꼭짓점을 큐에 저장
    done = set()    # 기억 장소2: 이미 큐에 추가한 꼭짓점들을 집합에 기록(중복 방지)

    qu.append(start)  # 시작점을 큐에 넣고 시작
    done.add(start)  # 집합에도 추가

    while qu:           # 큐에 처리할 꼭짓점이 남아 있으면
        p = qu.pop(0)   # 큐에서 처리 대상을 꺼내어
        print(p)        # 꼭짓점 이름을 출력하고
        for x in g[p]:  # 대상 꼭짓점에 연결된 꼭짓점들 중에
            if x not in done:   # 아직 큐에 추가된 적인 없는 꼭짓접들을
                qu.append(x)    # 큐에 추가하고
                done.add(x)     # 집합에도 추가


# 그래프 정보
g = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1],
    4: [2],
    5: [2]
}

bfs(g, 1)
