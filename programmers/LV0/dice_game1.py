a = 3
b = 5

def solution(a,b):
    if (a%2 != 0) and (b%2 != 0):
        answer = a*a + b*b
    elif (a%2 == 0) and (b%2 != 0):
        answer = 2*(a+b)
    elif (a%2 != 0) and (b%2 == 0):
        answer = 2*(a+b)
    elif (a%2 == 0) and (b%2 == 0):
        if (a > b):
            answer = a - b
        else:
            answer = b - a
    return answer

print(solution(a, b))
print(solution(6, 1))
print(solution(2, 4))