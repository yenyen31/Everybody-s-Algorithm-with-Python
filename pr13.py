# 예제 소스 p13-1.py
# 회문 찾기 알고리즘
# 주어진 문장이 회문인지 아닌지 찾기(큐와 스택의 특징을 이용)
# 입력: 문자열 s
# 출력: 회문이면 True, 아니면 False

def palindrome(s):
    # 큐와 스택을 리스트로 정의
    qu = []
    st = []
    # 1단계: 문자열의 알파벳 문자를 각각 큐와 스택에 넣음
    for x in s:
        # 해당 문자가 알파벳이면(공백, 숫자, 특수문자가 아니면)
        # 큐와 스택에 각각 그 문자를 추가
        if x.isalpha():
            qu.append(x.lower())
            st.append(x.lower())
        # 2단계: 큐의 스택에 들어있는 문자를 꺼내면서 비교
    while qu:   # 큐에 문자가 남아있는 동안 반복
        if qu.pop(0) != st.pop():    # 큐와 스택에서 꺼낸 문자가 다르면 회문이 아님
            return False

    return True


print(palindrome("Wow"))
print(palindrome("Madam, I'm Adam."))
print(palindrome("Madam, I'm Adam."))


# 연습문제 13-1.py
# 큐와 스택 이용하지 않고 회문인지 아닌지 판달할 수 있는 방법

def palindrome(s):

    a = []

    for x in s:
        if x.isalpha():
            a.append(x.lower())

    n = len(a)
    for i in range(0, n):
        if a[i] != a[n-1-i]:
            return False

    return True


print(palindrome("Wow"))
print(palindrome("Madam, I'm Adam."))
print(palindrome("Madam, I'm Adam."))
