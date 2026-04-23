required = [3, 2, 1]
k = 2
def solution(required, k):
    # 가장 큰 놈을 다 없애는 데 걸리는 시간 vs 전체 물량을 k씩 처리하는 시간
    # 둘 중 더 오래 걸리는 쪽이 답!
    total_required = 0
    for x in required:
        total_required += x
    if (((total_required % k))!=0):
        answer = (total_required//k) + 1
    elif (((total_required % k))==0):
        answer = (total_required//k)
    answer = max(answer,max(required))
    return answer
print(solution(required, k))
print(solution([4, 4, 4, 4], 2))
print(solution([1,2,3], 3))
print(solution([3,1,1,1],3))