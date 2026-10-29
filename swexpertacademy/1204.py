import sys
T = int(sys.stdin.readline())
for _ in range(T):
    dict = {}
    Test_case_num = int(sys.stdin.readline())
    scores = list(map(int, sys.stdin.readline().split()))
    for score in scores:
        if score not in dict:
            dict[score] = 1
        else:
            dict[score] += 1
    max_value = 0
    max_frequency_score = 0
    for key, value in dict.items():
        
        if value > max_value: # 이미 나왔던 애보다 큰 값을 만났을 때만
            max_value = value
            max_frequency_score = key
        elif value == max_value: # 이미 나왔던 애랑 그 다음에 나오는 애가 같으면 => 더 score가 높은 애로 선택
            max_frequency_score = max(key, max_frequency_score)

    print("#" + str(Test_case_num) + " " + str(max_frequency_score))






    