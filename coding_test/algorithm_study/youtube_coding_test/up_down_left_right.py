def solution(n, direction):
    # 동 서 남 북
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    # 초기위치는 (1,1)에서 시작
    si = 1
    sj = 1
    for dir in direction:
        if dir == 'R':
            nx = si + dx[0]
            ny = sj + dy[0]
        elif dir == 'L':
                    nx = si + dx[1]
                    ny = sj + dy[1]
        if dir == 'D':
                    nx = si + dx[2]
                    ny = sj + dy[2]
        if dir == 'U':
                    nx = si + dx[3]
                    ny = sj + dy[3]
        if 0 < nx < n and 0 < ny < n:
            si = nx
            sj = ny
        else:
            continue
    return (nx, ny)
print(solution(5, ['R', 'R', 'R', 'U', 'D', 'D']))