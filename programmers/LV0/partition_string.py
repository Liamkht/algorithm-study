str1 = "abc"
str2 = "aabcc"

def solution(str1, str2):
    if str1 in str2:
        answer = 1
    else:
        answer = 0
    return answer 
print(solution(str1, str2))
print(solution("tbt", "tbbttb"))