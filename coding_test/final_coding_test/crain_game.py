def solution(board, moves):
    answer = 0
    bucket = []
    for move in moves:
        for row in board:
            last = row[move-1]
            if last == 0:
                continue
            else: # 빈칸이 아닌 인형이 있을 때 
                if len(bucket) == 0: # bucket이 비엇을 때 
                    bucket.append(last)
                    row[move-1] = 0
                    break
                else: # bucket이 안 비엇을 때 
                    if bucket[-1] == last: # 같으면
                        answer += 2
                        bucket.pop()
                        row[move-1] = 0
                        break
                    else: # 다르면
                        bucket.append(last)
                        row[move-1] = 0
                        break
        print(bucket)
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))
# 4 , 3, 1, 1 
# --> 4, 3,  3
# --> 4, 2 , 4  