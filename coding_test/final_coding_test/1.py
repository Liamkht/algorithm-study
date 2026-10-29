from collections import deque
def dfs(c):
    v[c] = 1, ans_dfs.append(c) # 방문노드 추가, 방문 표시

    for n in adj[c]:
        if not v[n]:            # 방문하지 않은 노드인 경우
            dfs(n)

def bfs(s):
    queue = deque()
    queue.append(s) # q에 초기 데이터(들) 삽입
    v[s] = 1, ans_bfs.append(s) # 방문 표시, 방문노드 추가

    while queue:
        c = queue.popleft()
        for n in adj[c]:
            if not v[n]:
                queue.append(n)
                v[n] = 1, ans_bfs.append(n)


N = 5
M = 5
V = 3
adj = [[] for _ in range(N+1)]
adj[5].append(4)
adj[4].append(5)

adj[5].append(2)
adj[2].append(5)

adj[1].append(2)
adj[2].append(1)

adj[3].append(4)
adj[4].append(3)

adj[3].append(1)
adj[1].append(3)
# [1] 오름차순 정렬

for i in range(len(adj)):
    adj[i].sort()
print(adj)


v = [0]*(N+1)
ans_dfs = []
dfs(V)

v = [0] * (N+1)
ans_bfs = [] 
bfs(V)

print(ans_dfs)
print(ans_bfs)