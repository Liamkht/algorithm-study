# 색  초 노 빨 초 노 빨  초  노
# 1번 2, 3, 5, 7, 8, 10, 12, 13
# 색  초 노 빨 초 노
# 2번 5, 6, 7, 12, 13
signals = [[2, 1, 2], [5, 1, 1]]
def solution(signals):
    current_time = 0
    is_over = False
    while(is_over == False):
        for k in range(len(signals)):
            for j in range(3):
                current_time += signals[k][j]
                signals[k][j] = current_time
            current_time = 0
            first_same = signals[0][1];
            if k == len(signals)-1: # 즉 위에 for문을 다 돈 경우
                for i in range(len(signals)):
                    if first_same == signals[i][1]:
                        is_over = True
                        return -1
    print(signals)


    return current_time

            

print(solution(signals))
