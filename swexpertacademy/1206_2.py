import sys
for t in range(10):
    N = int(sys.stdin.readline())  # 10
    for i in range(N):  # 0 - 9
        count = 0
        height_list = list(map(int, sys.stdin.readline().split())) # 건물의 높이
        for k in range(2, len(height_list)-2): # 즉 2번째 인덱스부터 맨 끝에서 앞으로 두 번째 인덱스까지 2, 9
            if height_list[k] < max(height_list[k-1], height_list[k-2]):
                continue
            if height_list[k] < max(height_list[k+1], height_list[k+2]):
                continue
            count += height_list[k] - max(height_list[k-1], height_list[k-2], height_list[k+1], height_list[k+2]) 
        print("#" + str(t + 1) + " " + str(count))

# 254 - 185 = 69, 227 - 185 = 42