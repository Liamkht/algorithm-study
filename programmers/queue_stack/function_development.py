progresses = [93,30,55]
speeds = [1, 30, 5]

def solution(progresses, speeds):
    answer = []
    result = []
    for i in range(len(progresses)):
        if (((100-progresses[i]) % speeds[i])!=0):
            day = ((100-progresses[i]) // speeds[i]) + 1
        else:
             day = ((100-progresses[i]) // speeds[i])
        result.append(day)
    current = result[0]
    count = 1

    for j in range(1, len(result)):
        if result[j] <= current:
            count += 1
        else:
            answer.append(count)
            current = result[j]
            count = 1
    answer.append(count)


    return answer

print(solution(progresses, speeds))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))