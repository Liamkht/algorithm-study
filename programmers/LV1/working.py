def solution(schedules, timelogs, startday): # 금요일부터 시작이면 startday = 5
    # startday부터 시작해서 체킹하다가 주말을 만나면 토, 일 제외 후 다시 체킹
    count = 0
    for i in range(len(timelogs)): # len(timelogs) = 3
        is_give = True
        for j in range(7):
            day = (startday - 1 + j) % 7 + 1 # 얘가 실제 요일
            if (day == 6 or day == 7):
                continue
            else: 
                if timelogs[i][j] > (schedules[i] + 10):   # 각 직원의 timelog(7일에 대한) 희망시각을 비교
                    is_give = False
                    break
                else:
                    continue
        if is_give == True:
            count += 1

    return count

print(solution([700, 800, 1100], [[710, 2359, 1050, 700, 650, 631, 659], [800, 801, 805, 800, 759, 810, 809], [1105, 1001, 1002, 600, 1059, 1001, 1100]], 5))
print(solution([730, 855, 700, 720], [[710, 700, 650, 735, 700, 931, 912], [908, 901, 805, 815, 800, 831, 835], [705, 701, 702, 705, 710, 710, 711], [707, 731, 859, 913, 934, 931, 905]], 1))