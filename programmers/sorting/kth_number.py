array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
def solution(array, commands):
    kth_array = []
    # commands의 i, j , k // i부터 j번째까지 자른 후 정렬해서 k번째 수 찾기
    for command in commands:
        i, j , k = command[0], command[1], command[2]
        sliced = sorted(array[i-1:j]) # sorted()로 원본 훼손 없이 정렬본만 얻기
        kth_array.append(sliced[k-1])
        
    return kth_array
print(solution(array, commands))