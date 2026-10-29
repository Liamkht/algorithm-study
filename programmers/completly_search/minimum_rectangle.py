sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
def solution(sizes):
    for size in sizes: # 일단 제일 큰 애는 가로 혹은 세로가 되야함(가로로 가정)
        if size[0] >= size[1]:
            continue
        else:
            size[0], size[1] = size[1], size[0]
    width_sizes = []
    height_sizes = []
    for size in sizes:
        width_sizes.append(size[0])
        height_sizes.append(size[1])
    answer = max(width_sizes)*max(height_sizes)
    return answer
print(solution(sizes))
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))