from collections import deque
# return 값 ==> 6
# 최대반복횟수가 k이므로 k보다 작은 동안에 계속 반복
# 종류가 같은 파이프는 항상 같이 열림
# 파이프 종류 1-> A 2->B 3 ->C
# 각 반복별로 음 감염체의 번호들을 기록
# 어떤 파이프를 먼저 열건지도 중요
def solution(n, infection, edges, k):
    answer = 0
    graph = [[] for _ in range(n+1)]
    for x, y, pipe_type in edges:
        graph[x].append((y, pipe_type))
        graph[y].append((x, pipe_type)) 
    print(graph)

    def spread(infected, pipe_type):

        visited = set(infected)
        queue = deque(infected)

        while queue:
            cur = queue.popleft()

            for nxt, t in graph[cur]:
                if t == pipe_type and nxt not in visited:
                    visited.add(nxt)
                    queue.append(nxt)
        return visited

    def dfs(depth, infected, last_type):
        nonlocal answer

        # 지금까지 감염된 개수로 정답 갱신
        answer = max(answer, len(infected))

        # k번 사용했으면 종료
        if depth == k:
            return

        # 다음에 열 파이프 종류
        for pipe_type in [1, 2, 3]:
            if pipe_type == last_type:
                continue
            new_infected = spread(infected, pipe_type)

            dfs(depth + 1, new_infected, pipe_type)

    dfs(0, {infection}, 0)



    return answer

print(solution(n = 10, infection = 1, edges = [[1, 2, 1], [1, 3, 1], [1, 4, 3], [1, 5, 2], [5, 6, 1], [5, 7, 1], [2, 8, 3], [2, 9, 2], [9, 10, 1]], k = 2))