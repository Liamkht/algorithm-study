T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    houses = []
    for r in range(N):
        row = list(map(int, input().split()))
        for c in range(N):
            if row[c] == 1:
                houses.append(r, c)
    max_houses = 0
    for cx in range(N):
        for cy in range(N):
            dist_counts = [0] * (2 * N)

            for hr, hc in houses:
                dist = abs(hr-cx) + abs(hc-cy)
                dist_counts[dist] += 1

            cnt = 0
            for k in range(1, 2*N + 1):
                if k - 1 < len(dist_counts):
                    cnt += dist_counts[k-1]
                cost = k * k + (k-1) * (k-1)

                if cnt * M >= cost:
                    max_houses = max(max_houses, cnt)
            
            print(f"#{tc} {max_houses}")
