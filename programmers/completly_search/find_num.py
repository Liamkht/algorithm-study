numbers = "17"
number = 17
def solution(numbers):
    while(i < numbers):
        i = 2
        if i != numbers and numbers % i == 0:
            print("소수 아님")
            break
        i += 1
    answer = 0
    return answer
print(solution(numbers))
print(solution("011")) # 소수 : 2, 3, 5, 7, 11, 13, 17, 19 ...