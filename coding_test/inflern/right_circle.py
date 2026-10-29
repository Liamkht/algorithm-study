from collections import deque
def is_correct_parenthesis(string):
    # 그러면 일단 ( 괄호가 들어오면 넣고, ) 괄호가 나오면 빼고 햇을 때 마지막에 다 비어있으면 올바른 괄호
    queue = deque()
    for string_circle in string:
        if string_circle == '(':
            queue.append('(')
        elif string_circle == ')':
            if '(' in queue:
                queue.popleft()
            else:
                return False
    if len(queue) == 0: # 즉 queue의 길이가 0이면 올바른 괄호
        return True
    else:
        return False    


print("정답 = True / 현재 풀이 값 = ", is_correct_parenthesis("(())"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis(")"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())))"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("())()"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())"))