from collections import deque

def topological_sort(n, edges):
    graph = [[] for _ in range(n+1)] # 연결 정보 알기위한
    indegree = [0] * (n+1) # 진입 간선의 수를 다 0으로 초기화

    for a, b in edges:
        graph[a].append(b)
        indegree[b]+=1
    queue = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            queue.append(i)
    result = []
    while queue:
        cur = queue.popleft()
        result.append(cur)
        for nxt in graph[cur]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)
    if len(result) != n:
        return -1
    else:
        return result



print(topological_sort(4, [(1,2),(1,3),(2,4),(3,4)]))  # [1, 2, 3, 4]