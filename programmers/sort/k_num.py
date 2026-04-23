array = [1,5,2,6,3,7,4]
commands=[[2,5,3],[4,4,1],[1,7,3]]
def solution(array, commands):
    answer=[]
    for i,j,k in commands:
        slice_array = array[i-1:j]
        slice_array.sort()
        answer.append(slice_array[k-1])
    return answer

print(solution(array, commands))