from collections import deque
adj = [[], [2, 5], [1, 3], [2], [7], [1, 6], [5], [4]]
visited = [0] * len(adj)
ans = 0
def dfs(c):
    global ans
    ans += 1
    visited[c] = 1
    for n in adj[c]:
        if not visited[n]:
            dfs(n)

def solution():
    dfs(1)
    return ans
print(solution())