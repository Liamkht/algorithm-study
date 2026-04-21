# 문자열을 순회하면서 열린 괄호를 만나면 스택에 넣고
# 닫힌 괄호를 만나면 스택에서 제거하면서 
# 최종 문자열 리스트가 비어있으면 올바른 괄호다
# 이런 접근
s = "()()"
def solution(s):
    stack = []
    for x in s:
        if x == "(":
            stack.append(x)
        elif x == ")":
            if not stack: # 닫는 괄호가 먼저 나옴 ==> stack 비어있는데 pop시도 -> False 즉시 리턴
                return False
            stack.pop()
    if not stack: # 올바른 괄호
        return True
    else:  # 열린 괄호가 남음
        return False
print(solution(s))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))