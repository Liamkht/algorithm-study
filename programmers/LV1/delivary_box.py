def solution(n, w, num):
    grid = []
    box = 1
    row = 0

    while box <= n:
        current_row = []
        for i in range(w):
            if box <= n:
                current_row.append(box)
                box += 1

        if row % 2 == 1:
            current_row.reverse()

        grid.append(current_row)
        row += 1      
    target_row, target_col = -1, -1
    for r, row_data in enumerate(grid): # enumerate는 인덱스와 값을 동시에 꺼내줌
        if num in row_data:
            target_row = r
            target_col = row_data.index(num)
            break
    count = 0
    for r in range(target_row, len(grid)):
        if target_col < len(grid[r]):
            count+=1
    return count

print(solution(22, 6, 8))
print(solution(13, 3, 6))

