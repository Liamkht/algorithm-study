tasks = [[0,3],[2,4],[10,2]]
def solution(tasks):
    current_time = 0
    for start, duration in tasks:
        if current_time>= start:
            current_time += duration
        elif current_time < start:
            current_time = start
            current_time += duration

    return current_time
print(solution(tasks))
print(solution([[0,5],[3,3],[6,4]]))
print(solution([[5,3],[7,4]]))