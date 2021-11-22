# 학생 번호와 이름이 리스트로 주어졌을 때 학생 번호를 입력하면 학생 번호에 해당하는 이름을 순차탐색으로 찾아 돌려주는 함수
# 해당 학생이 없으면 물음표(?)를 돌려줍니다.

def student_num(st_num, st_name, a):
    n = len(st_num)
    for i in range(0, n):
        if a == st_num[i]:
            return st_name[i]
    return "?"


st_num = [39, 14, 67, 105]
st_name = ["Justin", "John", "Mike", "Summer"]
