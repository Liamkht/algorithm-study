input = [4, 6, 2, 9, 1]
# bubble sort: 앞에서부터 1, 2  2, 3  3, 4 ... 이렇게 비교해 나가기
# idx 0 1 2 3 4
# idx 0부터 3까지
# 0 1 2 3 4         i, j   0 1 / 1 2 / 2 3 / 3 4, 0 1/ 1 2/ 2 3       
# 4 6 2 9 1
#  


def bubble_sort(array):
    # 이 부분을 채워보세요!
    for i in range(len(array)-1): # 0 1 2 3 
        if array[i] > array[i+1]:
            array[i], array[i+1] = array[i+1], array[i]
        


    return array


bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ",bubble_sort([4, 6, 2, 9, 1]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",bubble_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",bubble_sort([100,56,-3,32,44]))