def solution(v):
    x = []
    y = []

    for point in v:
        x.append(point[0])
        y.append(point[1])

    answer = []
    for i in x:
        if x.count(i) == 1:
            answer.append(i)

    for i in y:
        if y.count(i) == 1:
            answer.append(i)
    return answer