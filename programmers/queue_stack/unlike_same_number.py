arr = [1,1,3,3,0,1,1]

def solution(arr):
    answer = []
    for i in arr:
        # answer이 비어있거나, 마지막 값과 다르면 추가
        if not answer or answer[-1] != i:
            answer.append(i)
    return answer


print(solution(arr))
print(solution([4,4,4,3,3]))

