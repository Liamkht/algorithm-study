# 한 마을에 모험가가 N명 있습니다. 모험가 길드에서는 N명의
# 모험가를 대상으로 '공포도'를 측정햇는데, '공포도'가 
# 높은 모험가는 쉽게 공포를 느껴 위험 상황에서 제대로
# 대처할 능력이 떨어집니다
# 공포도가 x인 모험가는 반드시 x명 이상으로 구성한 모험가 그룹에 참여해야
# 여행을 떠날 수 있도록 규정
# N명의 모험가에 대한 정보가 주어졌을 때, 여행을 떠날 수 있는 그룹 수의 최댓값은?

def solution(n, group):
    # 오름차순으로 정렬한 후에 반복문을 돌리면서 비교하면서 그룹 추가해나가기
    group.sort()
    count = 0 # 현재 그룹에 포함된 모험가의 수
    group_count = 0 # 총 그룹의 수
    """
    for member_scary in group: #앞에서부터 꺼내면서
        if member_scary > count: # 공포도가 현재 그룹에 포함된 모험가수보다 크면 
            count += 1 # 모험가의 수만 증가시킴
        elif member_scary <= count: # 공포도가 현재 그룹에 포함된 모험가수랑 같거나 작으면
            group_count += 1 # 그룹으로 묶임
            count = 1 # 다시 초기화
    # 만약에 공포도
    """
    for member_scary in group:
        count += 1
        if count >= member_scary:
            group_count += 1
            count = 0
    return group_count
print(solution(5, [2, 3, 1, 2, 2]))
