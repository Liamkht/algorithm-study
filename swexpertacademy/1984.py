T = int(input())
for i in range(T):
    result = 0
    count = 0
    test_case = list(map(int, input().split()))
    test_case.sort()
    print(test_case)
    for k in range(1, len(test_case)-1):
        count += 1
        result += test_case[k]
    
    avg_result = result / count
    if avg_result >= int(avg_result) + 0.5:
        avg_result = int(avg_result) + 1
    elif avg_result < int(avg_result) + 0.5:
        avg_result = int(avg_result)
        
    print("#" + str(i+1) + " " + str(avg_result))