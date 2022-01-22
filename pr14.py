# 예제 소스 p14-1.py
# 딕셔너리를 이용해 동명이인을 찾는 알고리즘
# 두 번 이상 나온 이름 찾기
# 입력: 이름이 n개 들어 있는 리스트
# 출력: n개의 이름 중 반복되는 이름의 집합

def find_same_name(a):
    # 1단계: 각 이름이 등장한 횟수를 딕셔너리로 만듦
    name_dict = {}
    for name in a:      # 리스트 a에 있는 자료들을 차례로 반복
        if name in name_dict:       # 이름이 name_dict에 있으면
            name_dict[name] += 1        # 등장 횟수를 1 증가
        else:           # 새 이름이면
            name_dict[name] = 1     # 등장 회수를 1로 저장
    # 2단계: 만들어진 딕셔너리에 등장 횟수가 2이상인 것을 결과에 추가
    result = set()          # 결괏값을 저장할 빈 집합
    for name in name_dict:  # 딕서너리  name_dict에 있는 자료들을 차례로 반복
        if name_dict[name] >= 2:
            result.add(name)

    return result


name = ["Tom", "Jerry", "Mike", "Tom"]
print(find_same_name(name))

name = ["Tom", "Jerry", "Mike", "Tom", "Mike"]
print(find_same_name(name2))


# 연습문제 14-1
# 학생 번호와 이름이 주어졌을 때 학생 번호를 입력하면 그 학생 번호에 해당하는 이름을 돌려주고,
# 해당하는 학생 번호가 없으면 물음표를 돌려주기
def find_student_name(S_dict, s_no):

    if s_no in S_dict:
        return S_dict[s_no]
    else:
        return "?"


stu_dict = {
    39: "Justin",
    14: "John",
    67: "Mike",
    105: "Summer"
}

print(find_student_name(stu_dict, 39))
print(find_student_name(stu_dict, 14))
print(find_student_name(stu_dict, 6))
