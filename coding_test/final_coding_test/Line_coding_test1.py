from collections import deque

c = 11
b = 2
#T 0  1  2  3  4  5
#  11 12 14 17 21 26   n  

#T 0  1             2    
#  2 1-1 => b-1 = 1 2-1 => 0, 2-2 => 2 2-3 => 2  
#    1-2 => b+1 = 3 2-1 => 2, 2-2 => 4  2-3 => 6
#    1-3 => b*2 = 4 2-1 => 3, 2-2 => 5, 2-3 => 8
# 아 이거 모든 경우의 수를 다 따져봐야한다 ==> BFS나 DFS
def catch_me(cony_loc, brown_loc):
    time = 0
    queue = deque()
    queue.append((brown_loc, 0))

    visited = [{} for _ in range(200001)]
    while cony_loc <= 200000:
        cony_loc += time

        if time in visited[cony_loc]:
            return time
        
        for i in range(0, len(queue)):
            current_position, current_time = queue.popleft() # brown_loc, 0

            new_time = current_time + 1

            new_position = current_position - 1
            if 0 <= new_position <= 200000:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

            new_position = current_position + 1
            if 0 <= new_position <= 200000:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

            new_position = current_position * 2
            if 0 <= new_position <= 200000:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

        time += 1


print(catch_me(c, b))  # 5가 나와야 합니다!

print("정답 = 3 / 현재 풀이 값 = ", catch_me(10,3))
print("정답 = 8 / 현재 풀이 값 = ", catch_me(51,50))
print("정답 = 28 / 현재 풀이 값 = ", catch_me(550,500))