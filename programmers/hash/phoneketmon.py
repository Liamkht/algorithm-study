nums = [3,1,2,3]
def solution(nums):
    dict = {}
    # 종류를 len(nums)/2 개씩 뽑아보고 최대 종류인 애를 리턴
    for num in nums:
        dict[num] = dict.get(num, 0) + 1
    answer = 0
    # 고를 수 있는 마리수 : N/2 ==> len(nums)//2
    # 종류의 가짓수 : 딕셔너리의 키 개수, 즉 len(dict)
    # 만약 len(nums) // 2 == len(dict) 이거 이면 얘가 최대 
    # 만약 고를 수 있는 마리수 < 종류의 가짓수 ==> 이때는 고를 수 있는 마리수 리턴
    # 만약 고를 수 있는 마리수 > 종류의 가짓수 ==> 이때는 종류의 가짓수
    if len(nums)//2 == len(dict):
        answer = len(dict)
    elif len(nums)//2 < len(dict):
        answer = len(nums)//2
    elif len(nums)//2 > len(dict):
        answer = len(dict)

        
    return answer

print(solution(nums))
print(solution([3,3,3,2,2,4]))
print(solution([3,3,3,2,2,2]))