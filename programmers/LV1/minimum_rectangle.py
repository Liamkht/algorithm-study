def solution(sizes):
    max_width_size, max_height_size = 0, 0

    for width, height in sizes:
        if width < height: # 하나를 기준으로 다 몰자(width를 다 크게 맞추거나 height를 다 크게 맞추거나 )
            width, height = height, width
        max_width_size = max(max_width_size, width)
        max_height_size = max(max_height_size, height)
    return max_width_size * max_height_size

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))