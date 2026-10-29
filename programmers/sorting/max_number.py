numbers = [6, 10, 2] 
def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x : x*3, reverse=True)
    for i in numbers:
        answer += i

    return answer if int(answer) != 0 else '0'
print(solution(numbers))
print(solution([3, 30, 34, 5, 9]))
