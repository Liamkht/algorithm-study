from collections import deque
def bfs(si,sj,ei,ej):
    queue = deque()
    queue.append((si,sj))
    v[si][sj] = 1        # 방문 표시
    while queue:
        ci, cj = queue.popleft()
        # 정답 처리가 필요한 경우 이자리에서..
        if (ci,cj) == (ei,ej):
            return v[ei][ej]
        # 네방향, 범위 내, 조건에 맞으면 : board == 1, v == 0
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)): # 방향 상 하 좌 우
            ni = ci + di
            nj = cj + dj
            if 0<=ni<N and 0<=nj<M and board[ni][nj] == 1 and not v[ni][nj]:
                queue.append((ni,nj))
                v[ni][nj] = v[ci][cj] + 1


N = 4
M = 6
board = [[1, 0, 1, 1, 1, 1], [1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 1], [1, 1, 1, 0, 1, 1]]
v = [[0]*M for _ in range(N)]
ans = bfs(0,0,N-1,M-1)
print(ans)
# BFS 풀기