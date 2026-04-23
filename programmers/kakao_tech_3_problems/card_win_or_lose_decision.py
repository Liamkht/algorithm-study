a = 5
b = 3
def solution(a, b):
    if a > b:
        answer = "player1"
    elif a < b:
        answer = "player2"
    else:
        answer = "draw"
    return answer

print(solution(a, b))   
print(solution(2, 7))
print(solution(4, 4)) 