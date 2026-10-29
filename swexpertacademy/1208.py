import sys
T = 10
for i in range(T):
    N = int(sys.stdin.readline())
    box_height_list = list(map(int, sys.stdin.readline().split()))
    for k in range(N):
        top_height = max(box_height_list)
        low_height = min(box_height_list)
        
        if (top_height - low_height) <= 1:
            break
        top_idx = box_height_list.index(top_height)
        low_idx = box_height_list.index(low_height)

        box_height_list[top_idx] -= 1
        box_height_list[low_idx] += 1
    print("#" + str(i+1), top_height - low_height)
