m = 4
n = 5
h = 2
w = 2
drops = [[0, 0], [3, 1], [1, 3], [2, 4], [1, 1], [2, 2], [2, 3], [0, 4]]
# 각 선인장 후보 위치마다 "몇 번째 비에서 처음 맞는지"를 계산하는 방식이 훨씬 직관적
# 이 경우 될 수 있는 왼쪽 위 후보 => [0, 0], [0, 1], [0, 2], [0, 3]
#                                    [1, 0], [1, 1], [1, 2], [1, 3]
#                                    [2, 0], [2, 1], [2, 2], [2, 3]  
# r == > 0 ~ m - h
# c ==> 0 ~ n - w
#  [0, 0], [0, 1], [1, 0], [1, 1]
def solution(m, n, h, w, drops):
    answer = []
    for row in range(0, m-h+1):
        for col in range(0, n-w+1):
            first_rain = len(drops)
            for time, (x, y) in enumerate(drops):
                if row <= x < row + h and col <= y < col + w:
                    first_rain = time
                    break
            answer.append((first_rain, row, col))

    answer.sort(key=lambda x: (-x[0], x[1], x[2]))

    return [answer[0][1], answer[0][2]]

print(solution(m, n, h, w, drops))

print(solution(3, 3, 1, 1, [[0, 0], [0, 1], [0, 2], [1, 0]]))

print(solution(4, 6, 3, 4, [[1, 2]]))

print(solution(4, 6, 1, 2, [[0, 1], [0, 3], [0, 5], [1, 1], [1, 3], [1, 5], [2, 1], [2, 3], [2, 5], [3, 1], [3, 3], [3, 5]]))

