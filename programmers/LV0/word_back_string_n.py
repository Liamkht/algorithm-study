my_string = "ProgrammerS123"
n = 11
def solution(my_string, n):
    answer = ''
    answer += my_string[len(my_string)-n:]
    return answer

print(solution(my_string, n))
print(solution("He110W0r1d", 5))