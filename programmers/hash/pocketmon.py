nums = [3,1,2,3]

def solution(nums):
    dict = {}
    for num in nums:
        dict[num] = 1
    max = len(nums) // 2
    return min(max, len(dict))

print(solution(nums))
print(solution([3,3,3,2,2,4]))
print(solution([3,3,3,2,2,2]))