# 1 <= N <= 100,000, 2 <= K <= 100,000  
def solution(N, K):
    # 먼저 k로 나눌 수 있는지 따져보고 나눌 수 없으면 -1
    # 나눌 수 있으면 1이 될 때까지 계속 나누기
    count = 0
    while (N > 1):
        if (N%K == 0):
            N = N // K
        else:
            N = N - 1
        count+=1
    return count
print(solution(25, 3))