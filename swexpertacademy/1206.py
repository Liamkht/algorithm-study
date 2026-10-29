import sys
for i in range(10):
    N = int(sys.stdin.readline())
    height_list = list(map(int, sys.stdin.readline().split()))
    
    result = 0
    for j in range(2, (len(height_list)-2)):
        if height_list[j] < max(height_list[j-1], height_list[j+1]):
            continue
        if height_list[j] < max(height_list[j-2], height_list[j+2]):
            continue
        result += (height_list[j]- max(height_list[j-2],height_list[j-1], height_list[j+1], height_list[j+2]))
    print("#" + str(i+1) + " " + str(result))    
    



