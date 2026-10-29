import sys

def main():
    N, Q = map(int, sys.stdin.readline().split())

    graph = [[0]*(N+1) for i in range(N+1)]
    for i in range(1, N+1):
        row = list(map(int, sys.stdin.readline().split()))
        for j in range(N):
            graph[i][j+1] = row[j]
    INF = float('inf')

    dp = [[[INF] * (N+1) for i in range(N+1)] for j in range(N)]

    for i in range(1, N+1):
        dp[0][i][i] = 0

    for i in range(1, N+1):
        for j in range(1, N+1):
            if graph[i][j] != -1 and i!=j:
                dp[1][i][j] = graph[i][j]

    return True


if __name__ == "__main__":
    main()